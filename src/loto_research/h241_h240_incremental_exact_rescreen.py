"""H241: incremental exact H225 rescreen after H240 separators.

Reconstructs the H235 witness universe (base + all H234 cuts) and appends only
H240 witnesses that were already deduplicated against H234. The H228 quotient
universe and exact shift CSP are unchanged, so totals compare directly to H235.
If H240 contributes zero genuinely new witnesses, H241 is an explicit no-op and
copies the corresponding H235 leaf counts rather than pretending a new screen.
"""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path
import numpy as np
from loto_research.h226_general_coefficient_envelope_prescreen import ODD, expand_witnesses, unique_witness_signature_data
from loto_research.h228_ordered_sector_stabilizer_coefficient_orbits import sector_orbits
from loto_research.h229_quotient_coefficient_envelope_screen import sector_pattern_reps, upper_batch
from loto_research.h230_exact_shift_csp_screen import exact_shift_survivors
from loto_research.h232_chunked_sector_exact_shift_csp import EXPECTED_REPS, EXPECTED_STATES, CHUNKS, ENV_BATCH, bounds

ROOT=Path(__file__).resolve().parents[2]
H234=ROOT/'data'/'derived'/'h234_new_witnesses.json'
H240=ROOT/'data'/'derived'/'h240_new_witnesses.json'
H235=ROOT/'data'/'derived'/'h235_h234_augmented_exact_shift_rescreen.json'
OUTDIR=ROOT/'data'/'derived'/'h241_chunk_shards'
MERGED=ROOT/'data'/'derived'/'h241_h240_incremental_exact_rescreen.json'

def affine_expand(raw):
    aug=[]
    for w in raw:
        assert len(w)==5
        for g in w:
            assert len(g)==4 and len(set(map(int,g)))==4 and all(0<=int(x)<16 for x in g)
        for u in ODD:
            for v in range(16):
                aug.append([[(u*int(x)+v)%16 for x in grp] for grp in w])
    return aug

def witness_universe():
    base,pre_n,h186_n=expand_witnesses()
    a=json.loads(H234.read_text()); b=json.loads(H240.read_text())
    assert a['packet']=='H234' and a['witness_count']==44
    assert b['packet']=='H240' and b['deduplicated_against']=='H234'
    h234=a['witnesses']; h240=b['witnesses']; assert len(h240)==b['witness_count']
    aug234=affine_expand(h234); aug240=affine_expand(h240)
    W=np.concatenate([base,np.asarray(aug234+aug240,dtype=np.int16)],axis=0) if (aug234 or aug240) else base
    return W,pre_n,h186_n,len(aug234),len(aug240),len(h240)

def prior_chunk(si,ci):
    d=json.loads(H235.read_text()); assert d['packet']=='H235'
    ch=d['sectors'][si]['chunks'][ci]; assert (ch['sector_index'],ch['chunk_index'])==(si,ci)
    return ch

def solve_chunk(sector_index,chunk):
    W,pre_n,h186_n,h234_exp,h240_exp,h240_raw=witness_universe()
    if h240_raw==0:
        old=prior_chunk(sector_index,chunk)
        out=dict(old); out['packet']='H241'; out['source_packet']='H235'; out['no_op_no_new_h240_witnesses']=True
        out['h240_raw_new_witnesses']=0; out['h240_affine_expanded_instances']=0
        return out
    orbs=sector_orbits(); orb=orbs[sector_index]; sec=orb[0]; assert sec==EXPECTED_REPS[sector_index]
    A,B,C,D=unique_witness_signature_data(W); top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]
    reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec); assert len(reps)==EXPECTED_STATES[sector_index]
    lo,hi=bounds(len(reps),chunk); local=reps[lo:hi]
    beta,gamma=sec; bi=ODD.index(beta); gi=ODD.index(gamma)
    bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16); need=np.maximum(0,3-bcd).astype(np.uint8)
    env_survivors=exact_states=exact_shift_tuples=0; env_killers=Counter(); csp_killers=Counter(); examples=[]
    for off in range(0,len(local),ENV_BATCH):
        pats=local[off:off+ENV_BATCH]; ub=upper_batch(top,pats); fail=ub<need[:,None]; killed=np.any(fail,axis=0)
        for j,pat in enumerate(pats):
            if bool(killed[j]): env_killers[int(np.flatnonzero(fail[:,j])[0])]+=1; continue
            env_survivors+=1; n,shift_ex,wi=exact_shift_survivors(A,need,pat)
            if n==0:
                if wi is not None: csp_killers[int(wi)]+=1
                continue
            exact_states+=1; exact_shift_tuples+=n
            if len(examples)<40: examples.append({'coefficients':[int(x) for x in pat],'surviving_shift_tuple_count':int(n),'first_shift_examples':shift_ex})
    return {'packet':'H241','source_packet':'H235','sector_index':sector_index,'chunk_index':chunk,'representative':[int(beta),int(gamma)],
        'sector_total_quotient_states':len(reps),'chunk_start':lo,'chunk_stop':hi,'chunk_quotient_states':len(local),
        'ordered_sector_orbit_size':len(orb),'ordered_sector_stabilizer_size':stab_size,'distinct_A_coefficient_actions':coeff_actions,
        'base_expanded_witness_instances':int(len(W)-h234_exp-h240_exp),'h234_raw_witnesses':44,'h234_affine_expanded_instances':h234_exp,
        'h240_raw_new_witnesses':h240_raw,'h240_affine_expanded_instances':h240_exp,'augmented_witness_instances_before_signature_dedupe':int(len(W)),
        'general_signature_unique_witnesses':int(len(A)),'h185_stored':int(pre_n),'h186_witnesses':int(h186_n),'no_op_no_new_h240_witnesses':False,
        'envelope_survivor_states':int(env_survivors),'exact_shift_surviving_coefficient_states':int(exact_states),'exact_surviving_shift_tuples':int(exact_shift_tuples),
        'envelope_first_killer_histogram':{str(k):int(v) for k,v in sorted(env_killers.items())},'csp_terminal_killer_histogram':{str(k):int(v) for k,v in sorted(csp_killers.items())},'first_exact_survivors':examples}

def merge(paths):
    rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:(x['sector_index'],x['chunk_index']))
    assert len(rows)==44 and all(x['packet']=='H241' for x in rows)
    assert [(x['sector_index'],x['chunk_index']) for x in rows]==[(s,c) for s in range(11) for c in range(CHUNKS)]
    sectors=[]
    for s in range(11):
        rr=[x for x in rows if x['sector_index']==s]; assert sum(x['chunk_quotient_states'] for x in rr)==EXPECTED_STATES[s]
        sectors.append({'sector_index':s,'representative':list(EXPECTED_REPS[s]),'quotient_coefficient_states':EXPECTED_STATES[s],
            'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in rr),'exact_shift_surviving_coefficient_states':sum(x['exact_shift_surviving_coefficient_states'] for x in rr),
            'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in rr),'chunks':rr})
    total=sum(x['quotient_coefficient_states'] for x in sectors); assert total==306450
    exstates=sum(x['exact_shift_surviving_coefficient_states'] for x in sectors); no_op=all(x.get('no_op_no_new_h240_witnesses',False) for x in rows)
    return {'packet':'H241','method':'H235_exact_rescreen_plus_genuinely_new_H240_witness_affine_orbits','source_packet':'H235','chunk_shards':44,
        'quotient_coefficient_states_screened':total,'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in sectors),
        'exact_shift_surviving_coefficient_states':exstates,'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in sectors),
        'h240_raw_new_witnesses':rows[0].get('h240_raw_new_witnesses',0),'h240_affine_expanded_instances':rows[0].get('h240_affine_expanded_instances',0),
        'no_op_no_new_h240_witnesses':no_op,'all_general_cyclic_affine_designs_rejected_by_augmented_witnesses':bool(exstates==0),'sectors':sectors,
        'interpretation':'Zero exact survivors closes H225. Positive survivors require another separator packet. no_op=true means H240 added no genuinely new cut and H235 totals are preserved exactly.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sector',type=int); ap.add_argument('--chunk',type=int); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
    if a.sector is not None:
        assert a.chunk is not None and 0<=a.sector<11 and 0<=a.chunk<CHUNKS
        out=solve_chunk(a.sector,a.chunk); OUTDIR.mkdir(parents=True,exist_ok=True); p=OUTDIR/f'sector_{a.sector:02d}_chunk_{a.chunk:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2)); return
    assert a.merge_dir is not None
    out=merge(sorted(a.merge_dir.rglob('sector_*_chunk_*.json'))); MERGED.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
if __name__=='__main__': main()

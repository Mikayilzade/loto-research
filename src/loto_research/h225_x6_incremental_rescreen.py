"""H225-X6: full exact rescreen after H225-X5 separator cuts.

Reconstructs the witness universe from immutable generations rather than from
large prior merged rescreen files: base H226 witnesses + H234 + H225-X1 +
H225-X3 + genuinely new H225-X5 witnesses, each added cut affine-expanded
through the same 128 symmetries. The unchanged H228 quotient universe contains
306,450 coefficient states split into 44 exact chunks.
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
X1=ROOT/'data'/'derived'/'h240_new_witnesses.json'
X3=ROOT/'data'/'derived'/'h225_x3_new_witnesses.json'
X5=ROOT/'data'/'derived'/'h225_x5_new_witnesses.json'
OUTDIR=ROOT/'data'/'derived'/'h225_x6_chunk_shards'
MERGED=ROOT/'data'/'derived'/'h225_x6_incremental_exact_rescreen.json'

def affine_expand(raw):
    aug=[]
    for w in raw:
        assert len(w)==5
        for g in w:
            vals=list(map(int,g)); assert len(vals)==4 and len(set(vals))==4 and all(0<=x<16 for x in vals)
        for u in ODD:
            for v in range(16):
                aug.append([[(u*int(x)+v)%16 for x in grp] for grp in w])
    return aug

def load_packet(path,packet):
    d=json.loads(path.read_text()); assert d['packet']==packet; assert len(d['witnesses'])==int(d['witness_count']); return d

def witness_universe():
    base,pre_n,h186_n=expand_witnesses()
    h234=load_packet(H234,'H234'); x1=load_packet(X1,'H240'); x3=load_packet(X3,'H225-X3'); x5=load_packet(X5,'H225-X5')
    assert h234['witness_count']==44 and x5['witness_count']>0, 'X6 requires genuinely new X5 cuts'
    packs=[h234,x1,x3,x5]; exps=[affine_expand(p['witnesses']) for p in packs]
    extra=[w for block in exps for w in block]
    W=np.concatenate([base,np.asarray(extra,dtype=np.int16)],axis=0)
    return W,pre_n,h186_n,[int(p['witness_count']) for p in packs],[len(x) for x in exps]

def solve_chunk(sector_index,chunk):
    W,pre_n,h186_n,raw_counts,exp_counts=witness_universe(); h234_raw,x1_raw,x3_raw,x5_raw=raw_counts; h234_exp,x1_exp,x3_exp,x5_exp=exp_counts
    orbs=sector_orbits(); orb=orbs[sector_index]; sec=orb[0]; assert sec==EXPECTED_REPS[sector_index]
    A,B,C,D=unique_witness_signature_data(W); top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]
    reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec); assert len(reps)==EXPECTED_STATES[sector_index]
    lo,hi=bounds(len(reps),chunk); local=reps[lo:hi]; beta,gamma=sec; bi=ODD.index(beta); gi=ODD.index(gamma)
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
    return {'packet':'H225-X6','source_packet':'H225-X5','sector_index':sector_index,'chunk_index':chunk,'representative':[int(beta),int(gamma)],
        'sector_total_quotient_states':len(reps),'chunk_start':lo,'chunk_stop':hi,'chunk_quotient_states':len(local),
        'ordered_sector_orbit_size':len(orb),'ordered_sector_stabilizer_size':stab_size,'distinct_A_coefficient_actions':coeff_actions,
        'base_expanded_witness_instances':int(len(W)-sum(exp_counts)),'h234_raw_witnesses':h234_raw,'x1_raw_witnesses':x1_raw,'x3_raw_witnesses':x3_raw,'x5_raw_new_witnesses':x5_raw,
        'h234_affine_expanded_instances':h234_exp,'x1_affine_expanded_instances':x1_exp,'x3_affine_expanded_instances':x3_exp,'x5_affine_expanded_instances':x5_exp,
        'augmented_witness_instances_before_signature_dedupe':int(len(W)),'general_signature_unique_witnesses':int(len(A)),
        'h185_stored':int(pre_n),'h186_witnesses':int(h186_n),'envelope_survivor_states':int(env_survivors),
        'exact_shift_surviving_coefficient_states':int(exact_states),'exact_surviving_shift_tuples':int(exact_shift_tuples),
        'envelope_first_killer_histogram':{str(k):int(v) for k,v in sorted(env_killers.items())},
        'csp_terminal_killer_histogram':{str(k):int(v) for k,v in sorted(csp_killers.items())},'first_exact_survivors':examples}

def merge(paths):
    rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:(x['sector_index'],x['chunk_index']))
    assert len(rows)==44 and all(x['packet']=='H225-X6' for x in rows)
    assert [(x['sector_index'],x['chunk_index']) for x in rows]==[(s,c) for s in range(11) for c in range(CHUNKS)]
    sectors=[]
    for s in range(11):
        rr=[x for x in rows if x['sector_index']==s]; assert sum(x['chunk_quotient_states'] for x in rr)==EXPECTED_STATES[s]
        sectors.append({'sector_index':s,'representative':list(EXPECTED_REPS[s]),'quotient_coefficient_states':EXPECTED_STATES[s],
            'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in rr),
            'exact_shift_surviving_coefficient_states':sum(x['exact_shift_surviving_coefficient_states'] for x in rr),
            'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in rr),'chunks':rr})
    total=sum(x['quotient_coefficient_states'] for x in sectors); assert total==306450; exstates=sum(x['exact_shift_surviving_coefficient_states'] for x in sectors)
    return {'packet':'H225-X6','method':'full_exact_rescreen_after_X5_new_witness_affine_orbits','source_packet':'H225-X5','chunk_shards':44,
        'quotient_coefficient_states_screened':total,'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in sectors),
        'exact_shift_surviving_coefficient_states':exstates,'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in sectors),
        'x5_raw_new_witnesses':rows[0]['x5_raw_new_witnesses'],'x5_affine_expanded_instances':rows[0]['x5_affine_expanded_instances'],
        'all_general_cyclic_affine_designs_rejected_by_augmented_witnesses':bool(exstates==0),'sectors':sectors,
        'interpretation':'Zero exact survivors closes H225. Positive survivors require H225-X7 separators.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sector',type=int); ap.add_argument('--chunk',type=int); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
    if a.sector is not None:
        assert a.chunk is not None and 0<=a.sector<11 and 0<=a.chunk<CHUNKS
        out=solve_chunk(a.sector,a.chunk); OUTDIR.mkdir(parents=True,exist_ok=True); p=OUTDIR/f'sector_{a.sector:02d}_chunk_{a.chunk:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2)); return
    assert a.merge_dir is not None
    out=merge(sorted(a.merge_dir.rglob('sector_*_chunk_*.json'))); MERGED.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
if __name__=='__main__': main()

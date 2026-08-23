"""H235: exact 44-way H232-compatible rescreen after adding H234 counterexamples.

Each of the 44 H234 balanced witnesses is expanded through all 128 affine
x -> u*x+v symmetries (u odd mod 16), appended to the exact H232 witness bank,
and deduplicated by the full general-family incidence signature.  The quotient
coefficient partition and exact legal-shift predicate are unchanged from H232.
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
OUTDIR=ROOT/'data'/'derived'/'h235_chunk_shards'
MERGED=ROOT/'data'/'derived'/'h235_h234_augmented_exact_shift_rescreen.json'


def augmented_witnesses():
    base,pre_n,h186_n=expand_witnesses()
    d=json.loads(H234.read_text())
    assert d.get('packet')=='H234' and d.get('witness_count')==44
    raw=d['witnesses']; assert len(raw)==44
    aug=[]
    for w in raw:
        assert len(w)==5
        for g in w:
            assert len(g)==4 and len(set(g))==4 and all(0<=int(x)<16 for x in g)
        for u in ODD:
            for v in range(16):
                aug.append([[(u*int(x)+v)%16 for x in grp] for grp in w])
    W=np.concatenate([base,np.asarray(aug,dtype=np.int16)],axis=0)
    return W,pre_n,h186_n,len(aug)


def solve_chunk(sector_index:int,chunk:int)->dict:
    orbs=sector_orbits(); orb=orbs[sector_index]; sec=orb[0]
    assert sec==EXPECTED_REPS[sector_index]
    W,pre_n,h186_n,h234_expanded=augmented_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]
    reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec)
    assert len(reps)==EXPECTED_STATES[sector_index]
    lo,hi=bounds(len(reps),chunk); local=reps[lo:hi]
    beta,gamma=sec; bi=ODD.index(beta); gi=ODD.index(gamma)
    bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16)
    need=np.maximum(0,3-bcd).astype(np.uint8)
    env_survivors=exact_states=exact_shift_tuples=0
    env_killers=Counter(); csp_killers=Counter(); examples=[]
    for off in range(0,len(local),ENV_BATCH):
        pats=local[off:off+ENV_BATCH]
        ub=upper_batch(top,pats); fail=ub<need[:,None]; killed=np.any(fail,axis=0)
        for j,pat in enumerate(pats):
            if bool(killed[j]):
                env_killers[int(np.flatnonzero(fail[:,j])[0])]+=1; continue
            env_survivors+=1
            n,shift_ex,wi=exact_shift_survivors(A,need,pat)
            if n==0:
                if wi is not None: csp_killers[int(wi)]+=1
                continue
            exact_states+=1; exact_shift_tuples+=n
            if len(examples)<40:
                examples.append({'coefficients':[int(x) for x in pat],'surviving_shift_tuple_count':int(n),'first_shift_examples':shift_ex})
    return {'packet':'H235','sector_index':sector_index,'chunk_index':chunk,
        'representative':[int(beta),int(gamma)],'sector_total_quotient_states':len(reps),
        'chunk_start':lo,'chunk_stop':hi,'chunk_quotient_states':len(local),
        'ordered_sector_orbit_size':len(orb),'ordered_sector_stabilizer_size':stab_size,
        'distinct_A_coefficient_actions':coeff_actions,'base_expanded_witness_instances':int(len(W)-h234_expanded),
        'h234_raw_witnesses':44,'h234_affine_expanded_instances':int(h234_expanded),
        'augmented_witness_instances_before_signature_dedupe':int(len(W)),
        'general_signature_unique_witnesses':int(len(A)),'h185_stored':int(pre_n),'h186_witnesses':int(h186_n),
        'envelope_survivor_states':int(env_survivors),'exact_shift_surviving_coefficient_states':int(exact_states),
        'exact_surviving_shift_tuples':int(exact_shift_tuples),
        'envelope_first_killer_histogram':{str(k):int(v) for k,v in sorted(env_killers.items())},
        'csp_terminal_killer_histogram':{str(k):int(v) for k,v in sorted(csp_killers.items())},'first_exact_survivors':examples}


def merge(paths:list[Path])->dict:
    rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:(x['sector_index'],x['chunk_index']))
    assert len(rows)==44 and all(x['packet']=='H235' for x in rows)
    assert [(x['sector_index'],x['chunk_index']) for x in rows]==[(s,c) for s in range(11) for c in range(CHUNKS)]
    sectors=[]
    for s in range(11):
        rr=[x for x in rows if x['sector_index']==s]
        assert sum(x['chunk_quotient_states'] for x in rr)==EXPECTED_STATES[s]
        sectors.append({'sector_index':s,'representative':list(EXPECTED_REPS[s]),'quotient_coefficient_states':EXPECTED_STATES[s],
            'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in rr),
            'exact_shift_surviving_coefficient_states':sum(x['exact_shift_surviving_coefficient_states'] for x in rr),
            'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in rr),'chunks':rr})
    total=sum(x['quotient_coefficient_states'] for x in sectors); assert total==306450
    exstates=sum(x['exact_shift_surviving_coefficient_states'] for x in sectors)
    return {'packet':'H235','method':'H232_exact_rescreen_plus_44_H234_witness_affine_orbits','chunk_shards':44,
        'quotient_coefficient_states_screened':total,'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in sectors),
        'exact_shift_surviving_coefficient_states':exstates,'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in sectors),
        'all_general_cyclic_affine_designs_rejected_by_augmented_witnesses':bool(exstates==0),
        'base_expanded_witness_instances':rows[0]['base_expanded_witness_instances'],'h234_raw_witnesses':44,
        'h234_affine_expanded_instances':rows[0]['h234_affine_expanded_instances'],
        'augmented_witness_instances_before_signature_dedupe':rows[0]['augmented_witness_instances_before_signature_dedupe'],
        'general_signature_unique_witnesses':rows[0]['general_signature_unique_witnesses'],'sectors':sectors,
        'interpretation':'Zero exact survivors is an exact finite impossibility certificate for H225 general cyclic-affine family. Positive survivors require another unrestricted separator packet; counts quantify the marginal power of H234 cuts.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sector',type=int); ap.add_argument('--chunk',type=int); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
    if a.sector is not None:
        assert a.chunk is not None and 0<=a.sector<11 and 0<=a.chunk<CHUNKS
        out=solve_chunk(a.sector,a.chunk); OUTDIR.mkdir(parents=True,exist_ok=True)
        p=OUTDIR/f'sector_{a.sector:02d}_chunk_{a.chunk:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2))
    else:
        assert a.merge_dir is not None
        out=merge(sorted(a.merge_dir.rglob('sector_*_chunk_*.json'))); MERGED.parent.mkdir(parents=True,exist_ok=True); MERGED.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
if __name__=='__main__': main()

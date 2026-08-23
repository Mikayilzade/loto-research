"""H232: 44-way chunked exact global-shift CSP for H225/H228 general family.

H231 partitions by 11 sectors but a single hard sector can still consume the full
sector timeout. H232 preserves the exact H230/H231 predicate and further partitions
each sector's deterministic quotient coefficient representative list into four
contiguous chunks. The 44 chunks are disjoint and exhaustive.

Each chunk independently applies the H226 envelope and then H230 exact globally
consistent legal-shift CSP. The merge refuses certification unless every expected
(sector,chunk) pair is present, common witness/schema fields agree, each sector's
four chunk state counts sum to its exact H228 quotient count, and the grand total is
306,450 states.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from collections import Counter
import numpy as np

from loto_research.h226_general_coefficient_envelope_prescreen import (
    ODD, expand_witnesses, unique_witness_signature_data,
)
from loto_research.h228_ordered_sector_stabilizer_coefficient_orbits import sector_orbits
from loto_research.h229_quotient_coefficient_envelope_screen import sector_pattern_reps, upper_batch
from loto_research.h230_exact_shift_csp_screen import exact_shift_survivors

ROOT=Path(__file__).resolve().parents[2]
OUTDIR=ROOT/'data'/'derived'/'h232_chunk_shards'
MERGED=ROOT/'data'/'derived'/'h232_exact_shift_csp_merged.json'
ENV_BATCH=512
CHUNKS=4
EXPECTED_REPS=((1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9))
EXPECTED_STATES=(7806,23052,23052,23052,23052,23052,45760,23052,45760,23052,45760)
assert sum(EXPECTED_STATES)==306450


def bounds(n:int,chunk:int)->tuple[int,int]:
    assert 0<=chunk<CHUNKS
    lo=n*chunk//CHUNKS
    hi=n*(chunk+1)//CHUNKS
    return lo,hi


def solve_chunk(sector_index:int,chunk:int)->dict:
    orbs=sector_orbits(); assert len(orbs)==11
    orb=orbs[sector_index]; sec=orb[0]
    assert sec==EXPECTED_REPS[sector_index]

    W,h185_n,h186_n=expand_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]

    reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec)
    assert len(reps)==EXPECTED_STATES[sector_index]
    lo,hi=bounds(len(reps),chunk)
    local=reps[lo:hi]

    beta,gamma=sec
    bi=ODD.index(beta); gi=ODD.index(gamma)
    bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16)
    need=np.maximum(0,3-bcd).astype(np.uint8)

    env_survivors=0; exact_states=0; exact_shift_tuples=0
    env_killers=Counter(); csp_killers=Counter(); examples=[]
    for off in range(0,len(local),ENV_BATCH):
        pats=local[off:off+ENV_BATCH]
        ub=upper_batch(top,pats)
        fail=ub<need[:,None]
        killed=np.any(fail,axis=0)
        for j,pat in enumerate(pats):
            if bool(killed[j]):
                wi=int(np.flatnonzero(fail[:,j])[0]); env_killers[wi]+=1
                continue
            env_survivors+=1
            n,shift_ex,wi=exact_shift_survivors(A,need,pat)
            if n==0:
                if wi is not None: csp_killers[wi]+=1
                continue
            exact_states+=1; exact_shift_tuples+=n
            if len(examples)<40:
                examples.append({'coefficients':[int(x) for x in pat],
                                 'surviving_shift_tuple_count':n,
                                 'first_shift_examples':shift_ex})

    return {
        'packet':'H232','sector_index':sector_index,'chunk_index':chunk,
        'representative':[int(beta),int(gamma)],
        'sector_total_quotient_states':len(reps),
        'chunk_start':lo,'chunk_stop':hi,'chunk_quotient_states':len(local),
        'ordered_sector_orbit_size':len(orb),
        'ordered_sector_stabilizer_size':stab_size,
        'distinct_A_coefficient_actions':coeff_actions,
        'expanded_witness_instances':int(len(W)),
        'general_signature_unique_witnesses':int(len(A)),
        'h185_stored':int(h185_n),'h186_witnesses':int(h186_n),
        'envelope_survivor_states':int(env_survivors),
        'exact_shift_surviving_coefficient_states':int(exact_states),
        'exact_surviving_shift_tuples':int(exact_shift_tuples),
        'envelope_first_killer_histogram':{str(k):int(v) for k,v in sorted(env_killers.items())},
        'csp_terminal_killer_histogram':{str(k):int(v) for k,v in sorted(csp_killers.items())},
        'first_exact_survivors':examples,
    }


def merge(paths:list[Path])->dict:
    rows=[]
    for p in paths:
        d=json.loads(p.read_text()); assert d['packet']=='H232'; rows.append(d)
    rows=sorted(rows,key=lambda x:(x['sector_index'],x['chunk_index']))
    assert len(rows)==44,len(rows)
    assert [(x['sector_index'],x['chunk_index']) for x in rows]==[(s,c) for s in range(11) for c in range(CHUNKS)]
    common=('expanded_witness_instances','general_signature_unique_witnesses','h185_stored','h186_witnesses')
    for key in common: assert len({x[key] for x in rows})==1,key

    sectors=[]
    for s in range(11):
        rr=[x for x in rows if x['sector_index']==s]
        assert all(tuple(x['representative'])==EXPECTED_REPS[s] for x in rr)
        assert all(x['sector_total_quotient_states']==EXPECTED_STATES[s] for x in rr)
        assert sum(x['chunk_quotient_states'] for x in rr)==EXPECTED_STATES[s]
        for c,x in enumerate(rr):
            lo,hi=bounds(EXPECTED_STATES[s],c)
            assert (x['chunk_start'],x['chunk_stop'])==(lo,hi)
        sectors.append({
            'sector_index':s,'representative':list(EXPECTED_REPS[s]),
            'quotient_coefficient_states':EXPECTED_STATES[s],
            'envelope_survivor_states':sum(x['envelope_survivor_states'] for x in rr),
            'exact_shift_surviving_coefficient_states':sum(x['exact_shift_surviving_coefficient_states'] for x in rr),
            'exact_surviving_shift_tuples':sum(x['exact_surviving_shift_tuples'] for x in rr),
            'chunks':rr,
        })
    total=sum(x['quotient_coefficient_states'] for x in sectors); assert total==306450
    env=sum(x['envelope_survivor_states'] for x in sectors)
    exstates=sum(x['exact_shift_surviving_coefficient_states'] for x in sectors)
    extuples=sum(x['exact_surviving_shift_tuples'] for x in sectors)
    return {
        'packet':'H232','method':'44_way_sector_x4_chunked_exact_global_shift_CSP',
        'chunk_shards':44,'sector_shards':11,
        'quotient_coefficient_states_screened':total,
        'envelope_survivor_states':env,
        'exact_shift_surviving_coefficient_states':exstates,
        'exact_surviving_shift_tuples':extuples,
        'all_general_cyclic_affine_designs_rejected_by_stored_witnesses':bool(exstates==0),
        **{k:rows[0][k] for k in common},
        'sectors':sectors,
        'interpretation':('Zero exact shift-surviving coefficient states across all 44 schema-valid chunks is the finite H225 general cyclic-affine impossibility certificate sought by H230/H231. Positive survivors require unrestricted exact n3<=2 separation.'),
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sector',type=int); ap.add_argument('--chunk',type=int); ap.add_argument('--merge-dir',type=Path); args=ap.parse_args()
    if args.sector is not None:
        assert args.chunk is not None and 0<=args.sector<11 and 0<=args.chunk<CHUNKS
        out=solve_chunk(args.sector,args.chunk); OUTDIR.mkdir(parents=True,exist_ok=True)
        p=OUTDIR/f'sector_{args.sector:02d}_chunk_{args.chunk:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2)); print('RESULT_FILE',p)
    else:
        assert args.merge_dir is not None
        out=merge(sorted(args.merge_dir.rglob('sector_*_chunk_*.json'))); MERGED.parent.mkdir(parents=True,exist_ok=True); MERGED.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2)); print('RESULT_FILE',MERGED)

if __name__=='__main__': main()

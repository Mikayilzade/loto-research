"""H231: sector-sharded exact global-shift CSP for H225/H228 general family.

This is mathematically identical to H230, but one ordered-sector orbit representative
is solved per process. It is designed for 11-way GitHub Actions matrix execution.
Each shard writes a self-contained exact result; the merge step refuses to certify
anything unless all 11 expected sector representatives are present and schema-valid.
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
OUTDIR=ROOT/'data'/'derived'/'h231_sector_shards'
MERGED=ROOT/'data'/'derived'/'h231_exact_shift_csp_merged.json'
ENV_BATCH=512
EXPECTED_REPS=((1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9))


def solve_sector(index:int)->dict:
    orbs=sector_orbits()
    assert len(orbs)==11
    orb=orbs[index]
    sec=orb[0]
    assert sec==EXPECTED_REPS[index],(index,sec)

    W,h185_n,h186_n=expand_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]

    reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec)
    beta,gamma=sec
    bi=ODD.index(beta); gi=ODD.index(gamma)
    bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16)
    need=np.maximum(0,3-bcd).astype(np.uint8)

    env_survivors=0
    exact_states=0
    exact_shift_tuples=0
    env_killers=Counter(); csp_killers=Counter(); examples=[]

    for lo in range(0,len(reps),ENV_BATCH):
        pats=reps[lo:lo+ENV_BATCH]
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
                if wi is not None:csp_killers[wi]+=1
                continue
            exact_states+=1; exact_shift_tuples+=n
            if len(examples)<100:
                examples.append({'coefficients':[int(x) for x in pat],
                                 'surviving_shift_tuple_count':n,
                                 'first_shift_examples':shift_ex})

    return {
        'packet':'H231','sector_index':index,'representative':[beta,gamma],
        'ordered_sector_orbit_size':len(orb),
        'ordered_sector_stabilizer_size':stab_size,
        'distinct_A_coefficient_actions':coeff_actions,
        'quotient_coefficient_states':len(reps),
        'coefficient_orbit_size_histogram':{str(k):int(v) for k,v in orbit_hist.items()},
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
        d=json.loads(p.read_text())
        assert d['packet']=='H231'
        rows.append(d)
    rows=sorted(rows,key=lambda x:x['sector_index'])
    assert len(rows)==11
    assert [tuple(x['representative']) for x in rows]==list(EXPECTED_REPS)
    assert [x['sector_index'] for x in rows]==list(range(11))
    # Common witness/schema fields must agree exactly across independently run shards.
    common=('expanded_witness_instances','general_signature_unique_witnesses','h185_stored','h186_witnesses')
    for key in common:
        assert len({x[key] for x in rows})==1,(key,[x[key] for x in rows])
    total_states=sum(x['quotient_coefficient_states'] for x in rows)
    assert total_states==306450,total_states
    env=sum(x['envelope_survivor_states'] for x in rows)
    exstates=sum(x['exact_shift_surviving_coefficient_states'] for x in rows)
    extuples=sum(x['exact_surviving_shift_tuples'] for x in rows)
    return {
        'packet':'H231','method':'11_way_sector_sharded_exact_global_shift_CSP',
        'sector_shards':11,'quotient_coefficient_states_screened':total_states,
        'envelope_survivor_states':env,
        'exact_shift_surviving_coefficient_states':exstates,
        'exact_surviving_shift_tuples':extuples,
        'all_general_cyclic_affine_designs_rejected_by_stored_witnesses':bool(exstates==0),
        **{k:rows[0][k] for k in common},
        'sectors':rows,
        'interpretation':(
            'Zero exact shift-surviving coefficient states across all 11 schema-valid '
            'shards is the same finite H225 general cyclic-affine impossibility '
            'certificate as H230, with independent sector execution.'
        ),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sector',type=int)
    ap.add_argument('--merge-dir',type=Path)
    args=ap.parse_args()
    if args.sector is not None:
        assert 0<=args.sector<11
        out=solve_sector(args.sector)
        OUTDIR.mkdir(parents=True,exist_ok=True)
        p=OUTDIR/f'sector_{args.sector:02d}.json'
        p.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2))
        print('RESULT_FILE',p)
    else:
        assert args.merge_dir is not None
        paths=sorted(args.merge_dir.rglob('sector_*.json'))
        out=merge(paths)
        MERGED.parent.mkdir(parents=True,exist_ok=True)
        MERGED.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
        print('RESULT_FILE',MERGED)

if __name__=='__main__':main()

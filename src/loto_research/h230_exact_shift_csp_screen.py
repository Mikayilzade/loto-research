"""H230: exact globally-consistent shift CSP screen for H225/H228 general family.

Lottery-only continuation of RI Keno H175.

H229 applies the H226 rowwise optimistic envelope to 306,450 quotient coefficient
states. H230 strengthens this to exact global shift consistency. For each quotient
coefficient-state representative that passes the envelope, enumerate every legal
shift assignment to its three A layers (with distinct shifts for repeated coefficient
blocks) and intersect the exact stored balanced-witness constraints. A shift design
survives iff one and the same legal shift tuple gives total incidence >=3 on every
stored witness signature.

If no shift tuple survives for any of the 306,450 quotient coefficient states, then
every design in the full H225 general cyclic-affine family has an explicit balanced
counterexample (directly for representatives; transported by H228 automorphisms for
orbit mates). That is a finite impossibility certificate for this family.
"""
from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path
from collections import Counter
import numpy as np

from loto_research.h226_general_coefficient_envelope_prescreen import (
    ODD, expand_witnesses, unique_witness_signature_data,
)
from loto_research.h228_ordered_sector_stabilizer_coefficient_orbits import sector_orbits
from loto_research.h229_quotient_coefficient_envelope_screen import (
    sector_pattern_reps, upper_batch,
)

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h230_exact_shift_csp.json'
ENV_BATCH=512
SHIFT_CHUNK=512


def legal_shift_tuples(p:int,q:int,r:int)->np.ndarray:
    """Canonical legal shifts for an unordered 3-multiset of coefficient blocks.

    Identical coefficient blocks represent identical layer families, so ordering
    their shifts is immaterial; use increasing shifts to avoid factorial duplicates.
    Distinct layers are still enforced exactly.
    """
    if p==r:
        z=np.asarray(list(combinations(range(16),3)),dtype=np.int16)
    elif p==q:
        z=np.asarray([(a,b,c) for a,b in combinations(range(16),2) for c in range(16)],dtype=np.int16)
    elif q==r:
        z=np.asarray([(a,b,c) for a in range(16) for b,c in combinations(range(16),2)],dtype=np.int16)
    else:
        z=np.asarray(list(product(range(16),repeat=3)),dtype=np.int16)
    assert len(z) in (560,1920,4096)
    return z


def exact_shift_survivors(A:np.ndarray, need:np.ndarray, pat:tuple[int,int,int], max_store=20):
    """Return count/examples of globally consistent legal shifts passing all rows.

    Filtering is fail-fast but exact. Candidate shift tuples are tested against
    every witness row. We order rows by descending need and then by a deterministic
    hardness proxy (low maximum A incidence first); ordering changes runtime only.
    """
    p,q,r=pat
    shifts=legal_shift_tuples(p,q,r)
    alive=np.ones(len(shifts),dtype=bool)

    # Hard rows first: larger required A contribution, then lower attainable max.
    maxrow=(A[:,p,:].max(axis=1)+A[:,q,:].max(axis=1)+A[:,r,:].max(axis=1)).astype(np.int16)
    order=np.lexsort((maxrow,-need.astype(np.int16)))

    first_killer=None
    for wi in order:
        req=int(need[wi])
        if req<=0:
            continue
        ids=np.flatnonzero(alive)
        if len(ids)==0:
            break
        s=shifts[ids]
        # Exact incidence for this witness and each still-alive legal shift tuple.
        hit=(A[wi,p,s[:,0]].astype(np.int16)
             +A[wi,q,s[:,1]].astype(np.int16)
             +A[wi,r,s[:,2]].astype(np.int16))
        bad=hit<req
        if np.any(bad):
            alive[ids[bad]]=False
            if first_killer is None and not np.any(alive):
                first_killer=int(wi)

    ids=np.flatnonzero(alive)
    ex=shifts[ids[:max_store]].astype(int).tolist()
    return int(len(ids)),ex,first_killer


def run():
    W,h185_n,h186_n=expand_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    rows=len(A)
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]

    sector_results=[]
    total_states=0
    envelope_survivors=0
    exact_design_state_survivors=0
    exact_shift_tuple_survivors=0
    envelope_killers=Counter()
    csp_killers=Counter()

    for orb in sector_orbits():
        sec=orb[0]
        reps,orbit_hist,stab_size,coeff_actions=sector_pattern_reps(sec)
        total_states+=len(reps)
        beta,gamma=sec
        bi=ODD.index(beta); gi=ODD.index(gamma)
        bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16)
        need=np.maximum(0,3-bcd).astype(np.uint8)

        sec_env=0; sec_states=0; sec_shift_tuples=0; examples=[]
        for lo in range(0,len(reps),ENV_BATCH):
            pats=reps[lo:lo+ENV_BATCH]
            ub=upper_batch(top,pats)
            fail=ub<need[:,None]
            killed=np.any(fail,axis=0)
            for j,pat in enumerate(pats):
                if bool(killed[j]):
                    wi=int(np.flatnonzero(fail[:,j])[0]); envelope_killers[wi]+=1
                    continue
                sec_env+=1; envelope_survivors+=1
                n,shift_ex,wi=exact_shift_survivors(A,need,pat)
                if n==0:
                    if wi is not None: csp_killers[wi]+=1
                    continue
                sec_states+=1; sec_shift_tuples+=n
                exact_design_state_survivors+=1
                exact_shift_tuple_survivors+=n
                if len(examples)<50:
                    examples.append({'coefficients':[int(x) for x in pat],
                                     'surviving_shift_tuple_count':n,
                                     'first_shift_examples':shift_ex})

        sector_results.append({
            'representative':[int(beta),int(gamma)],
            'ordered_sector_orbit_size':len(orb),
            'ordered_sector_stabilizer_size':stab_size,
            'distinct_A_coefficient_actions':coeff_actions,
            'quotient_coefficient_states':len(reps),
            'coefficient_orbit_size_histogram':{str(k):int(v) for k,v in orbit_hist.items()},
            'envelope_survivor_states':sec_env,
            'exact_shift_surviving_coefficient_states':sec_states,
            'exact_surviving_shift_tuples':sec_shift_tuples,
            'first_exact_survivors':examples,
        })

    assert total_states==306450,total_states
    out={
        'packet':'H230',
        'method':'H228_quotient_plus_H226_envelope_plus_exact_global_shift_CSP',
        'expanded_witness_instances':int(len(W)),
        'general_signature_unique_witnesses':int(rows),
        'h185_stored':int(h185_n),'h186_witnesses':int(h186_n),
        'ordered_sector_orbits':11,
        'quotient_coefficient_states_screened':int(total_states),
        'envelope_survivor_states':int(envelope_survivors),
        'exact_shift_surviving_coefficient_states':int(exact_design_state_survivors),
        'exact_surviving_shift_tuples':int(exact_shift_tuple_survivors),
        'all_general_cyclic_affine_designs_rejected_by_stored_witnesses':bool(exact_design_state_survivors==0),
        'envelope_first_killer_histogram':{str(k):int(v) for k,v in sorted(envelope_killers.items())},
        'csp_terminal_killer_histogram':{str(k):int(v) for k,v in sorted(csp_killers.items())},
        'sectors':sector_results,
        'interpretation':(
            'Zero exact shift-surviving coefficient states is a finite impossibility '
            'certificate for the full H225 general cyclic-affine family under H228 '
            'symmetry. Positive survivors pass only the stored witness bank and still '
            'require exact unrestricted n3<=2 separation.'
        ),
    }
    return out


def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    slim={k:v for k,v in out.items() if k not in ('sectors','envelope_first_killer_histogram','csp_terminal_killer_histogram')}
    slim['sector_counts']=[{
        'representative':s['representative'],
        'states':s['quotient_coefficient_states'],
        'envelope':s['envelope_survivor_states'],
        'exact_states':s['exact_shift_surviving_coefficient_states'],
        'exact_shift_tuples':s['exact_surviving_shift_tuples'],
    } for s in out['sectors']]
    print(json.dumps(slim,indent=2))
    print('RESULT_FILE',OUT)

if __name__=='__main__':main()

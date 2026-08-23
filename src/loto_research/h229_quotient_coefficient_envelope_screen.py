"""H229: exact H226 envelope screen on H228's 306,450 quotient coefficient states.

Scope: H175 Rhode Island Keno, H225 general cyclic-affine family only.

For each of the 11 true ordered-sector representatives from H228:
1. enumerate exactly one representative of every 3-multiset orbit of the 64 A
   coefficient pairs under that sector's true stabilizer projection;
2. evaluate H226's optimistic but exact necessary-condition envelope over all
   stored balanced witness signatures;
3. reject a quotient state if some witness has best possible legal distinct-shift
   A incidence + fixed B/C/D incidence < 3.

Because the stabilizer is a true automorphism of the whole support/design problem,
checking one coefficient-multiset representative per orbit is WLOG: a killing
balanced witness transports under the inverse automorphism to every orbit mate.
Survivors are NOT validated designs; they still need globally consistent shifts
and exact n3<=2 separation.
"""
from __future__ import annotations

import json
from pathlib import Path
from collections import Counter
import numpy as np

from loto_research.h226_general_coefficient_envelope_prescreen import (
    ODD, COEFFS, expand_witnesses, unique_witness_signature_data, pattern_upper,
)
from loto_research.h228_ordered_sector_stabilizer_coefficient_orbits import (
    G, PATTERNS, coeff_perm, pat_image, sector_image, sector_orbits,
)

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h229_quotient_coefficient_envelope.json'
BATCH=512


def sector_pattern_reps(sec):
    stab=[(p,f) for p,f in G if sector_image(sec,p,f)==sec]
    pms=tuple(sorted(set(coeff_perm(p) for p,f in stab)))
    seen=set(); reps=[]; orbit_hist=Counter()
    for s in PATTERNS:
        if s in seen:
            continue
        orb={pat_image(s,pm) for pm in pms}
        assert all(pat_image(x,pm) in orb for x in orb for pm in pms)
        seen.update(orb)
        reps.append(min(orb)); orbit_hist[len(orb)]+=1
    assert len(seen)==45760
    return reps,dict(sorted(orbit_hist.items())),len(stab),len(pms)


def upper_batch(top, pats):
    """Exact H226 rowwise upper bounds for a batch of coefficient multisets."""
    p=np.asarray([x[0] for x in pats],dtype=np.int16)
    q=np.asarray([x[1] for x in pats],dtype=np.int16)
    r=np.asarray([x[2] for x in pats],dtype=np.int16)
    # Start with all-distinct formula, then overwrite repeated-block cases with
    # sums of the best distinct shifts in that coefficient block.
    ub=top[:,p,0]+top[:,q,0]+top[:,r,0]
    all3=(p==r)
    pq=(p==q)&~all3
    qr=(q==r)&~all3
    if np.any(all3):
        z=p[all3]
        ub[:,all3]=top[:,z,0]+top[:,z,1]+top[:,z,2]
    if np.any(pq):
        z=p[pq]; y=r[pq]
        ub[:,pq]=top[:,z,0]+top[:,z,1]+top[:,y,0]
    if np.any(qr):
        x=p[qr]; z=q[qr]
        ub[:,qr]=top[:,x,0]+top[:,z,0]+top[:,z,1]
    return ub


def run():
    W,h185_n,h186_n=expand_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    rows=len(A)
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]

    orbs=sector_orbits()
    sector_rows=[]
    total_states=0; total_survivors=0

    for orb in orbs:
        sec=orb[0]
        reps,orb_hist,stab_size,coeff_actions=sector_pattern_reps(sec)
        total_states+=len(reps)
        beta,gamma=sec
        bi=ODD.index(beta); gi=ODD.index(gamma)
        bcd=B[:,bi].astype(np.int16)+C[:,gi].astype(np.int16)+D.astype(np.int16)
        need=np.maximum(0,3-bcd).astype(np.uint8)

        survivors=[]
        killer_hist=Counter()
        for lo in range(0,len(reps),BATCH):
            pats=reps[lo:lo+BATCH]
            ub=upper_batch(top,pats)
            fail=(ub < need[:,None])
            killed=np.any(fail,axis=0)
            for j,is_killed in enumerate(killed.tolist()):
                if is_killed:
                    first=int(np.flatnonzero(fail[:,j])[0])
                    killer_hist[first]+=1
                else:
                    survivors.append(list(pats[j]))

        total_survivors+=len(survivors)
        sector_rows.append({
            'representative':[int(beta),int(gamma)],
            'ordered_sector_orbit_size':len(orb),
            'ordered_sector_stabilizer_size':stab_size,
            'distinct_A_coefficient_actions':coeff_actions,
            'quotient_coefficient_states':len(reps),
            'coefficient_orbit_size_histogram':{str(k):int(v) for k,v in orb_hist.items()},
            'envelope_survivor_count':len(survivors),
            'first_survivor_representatives':survivors[:100],
            'killer_witness_histogram':{str(k):int(v) for k,v in sorted(killer_hist.items())},
        })

    assert total_states==306450,total_states
    out={
        'packet':'H229',
        'method':'H228_true_stabilizer_quotient_plus_H226_exact_envelope',
        'expanded_witness_instances':int(len(W)),
        'general_signature_unique_witnesses':int(rows),
        'h185_stored':int(h185_n),
        'h186_witnesses':int(h186_n),
        'ordered_sector_orbits':len(orbs),
        'quotient_coefficient_states_screened':int(total_states),
        'envelope_survivor_count':int(total_survivors),
        'all_coefficient_states_rejected':bool(total_survivors==0),
        'sectors':sector_rows,
        'interpretation':(
            'Zero survivors closes the full H225 general cyclic-affine family by '
            'H226 envelope theorem + H228 true symmetry. Positive survivors remain '
            'necessary-condition survivors only and require exact shift-level search.'
        ),
    }
    return out


def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    slim={k:v for k,v in out.items() if k!='sectors'}
    slim['sector_counts']=[{
        'representative':s['representative'],
        'states':s['quotient_coefficient_states'],
        'survivors':s['envelope_survivor_count']
    } for s in out['sectors']]
    print(json.dumps(slim,indent=2))
    print('RESULT_FILE',OUT)

if __name__=='__main__':
    main()

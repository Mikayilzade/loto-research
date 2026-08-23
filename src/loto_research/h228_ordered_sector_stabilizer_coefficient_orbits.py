"""H228: correct H227 sector action on ordered normalized sectors and quotient A coefficient multisets.

H227 canonicalized (beta,gamma) to beta<=gamma after every group action. That
canonicalization is not itself a well-defined action of S3xS2 on the 36 unordered
representatives because the swap subgroup is not normal in S3. The 11 representative
sector set survives, but orbit sizes/stabilizers must be computed on the 64 ordered
sectors first.

For A, write a*x0+b*x1-x2+c=0. Under a permutation p of groups 0,1,2 the
coefficient triple (a,b,-1) is permuted and renormalized so the new x2 coefficient
is -1. flip(3,4) leaves A coefficient pairs unchanged. We then exactly enumerate
orbits of the 45,760 3-multisets of 64 coefficient pairs under each ordered-sector
stabilizer projection.
"""
from __future__ import annotations
from itertools import combinations_with_replacement, permutations
import json
from pathlib import Path

MOD=16
ODDS=(1,3,5,7,9,11,13,15)
ORDERED=tuple((b,g) for b in ODDS for g in ODDS)
COEFFS=tuple((a,b) for a in ODDS for b in ODDS)
CI={x:i for i,x in enumerate(COEFFS)}
G=tuple((p,f) for p in permutations(range(3)) for f in (False,True))
PATTERNS=tuple(combinations_with_replacement(range(64),3))
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h228_ordered_sector_coefficient_orbits.json'


def inv(x:int)->int:
    for y in ODDS:
        if x*y%MOD==1:return y
    raise ValueError(x)


def norm_projective(t):
    z=inv(t[2]); return (t[0]*z%MOD,t[1]*z%MOD,1)


def sector_image(pair,p,flip):
    q=(pair[0],pair[1],1)
    q=tuple(q[i] for i in p)
    if flip:q=tuple(inv(x) for x in q)
    q=norm_projective(q)
    return q[0],q[1]


def sector_orbits():
    seen=set(); out=[]
    for s in ORDERED:
        if s in seen:continue
        orb={sector_image(s,p,f) for p,f in G}
        assert all(x in ORDERED for x in orb)
        # Full group images from one point are already the complete orbit.
        assert all(sector_image(x,p,f) in orb for x in orb for p,f in G)
        seen.update(orb); out.append(tuple(sorted(orb)))
    assert len(seen)==64 and len(out)==11
    return tuple(out)


def coeff_image(pair,p):
    r=(pair[0],pair[1],15) # -1 mod16
    rp=tuple(r[i] for i in p)
    scale=(-inv(rp[2]))%MOD
    out=(rp[0]*scale%MOD,rp[1]*scale%MOD)
    assert out in CI
    return out


def coeff_perm(p):
    z=tuple(CI[coeff_image(x,p)] for x in COEFFS)
    assert len(set(z))==64
    return z


def pat_image(s,pm):
    return tuple(sorted(pm[i] for i in s))


def multiset_orbit_count(sec):
    stab=[(p,f) for p,f in G if sector_image(sec,p,f)==sec]
    # flip34 may act trivially on A coefficients, so project stabilizer to distinct
    # coefficient permutations before quotienting A multisets.
    pms=tuple(sorted(set(coeff_perm(p) for p,f in stab)))
    seen=set(); reps=[]; hist={}
    for s in PATTERNS:
        if s in seen:continue
        orb={pat_image(s,pm) for pm in pms}
        assert all(pat_image(x,pm) in orb for x in orb for pm in pms)
        seen.update(orb); reps.append(min(orb))
        hist[str(len(orb))]=hist.get(str(len(orb)),0)+1
    assert len(seen)==45760
    return len(stab),len(pms),len(reps),hist


def run():
    orbs=sector_orbits(); rows=[]
    for o in orbs:
        rep=o[0]
        st,proj,n,h=multiset_orbit_count(rep)
        assert st==12//len(o)
        rows.append({'representative':list(rep),'ordered_sector_orbit_size':len(o),
                     'ordered_sector_stabilizer_size':st,'distinct_A_coefficient_actions':proj,
                     'coefficient_multiset_orbits':n,'coefficient_orbit_size_histogram':h,
                     'ordered_sector_orbit':[list(x) for x in o]})
    total=sum(r['coefficient_multiset_orbits'] for r in rows)
    assert total==306450
    return {'packet':'H228','ordered_normalized_sectors':64,'sector_orbits':11,
            'raw_representative_sector_coefficient_patterns':11*45760,
            'exact_stabilizer_quotiented_coefficient_patterns':total,
            'reduction_vs_H227_rep_pattern_workload':(11*45760)/total,
            'rows':rows}


def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()

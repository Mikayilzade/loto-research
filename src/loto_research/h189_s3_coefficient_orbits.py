"""H189 exact S3 + common-unit coefficient orbit quotient for H188.

H188 fixes D=(1,0), B/C shifts zero, and b<=c. This script proves that the
36 remaining coefficient pairs fall into 15 exact symmetry classes once the
full S3 permutation symmetry of supports B,C,D is combined with the H187
common-unit normalization.
"""
from __future__ import annotations

from itertools import combinations_with_replacement, permutations
from math import comb

UNITS=(1,3,5,7,9,11,13,15)


def inv16(a:int)->int:
    for b in UNITS:
        if (a*b)%16==1:
            return b
    raise ValueError(a)


def canonical_pair(b:int,c:int)->tuple[int,int]:
    vals=(b,c,1)
    reps=[]
    for p in permutations(vals):
        r=inv16(p[2])
        x=(p[0]*r)%16
        y=(p[1]*r)%16
        reps.append(tuple(sorted((x,y))))
    return min(reps)


def orbit_map():
    out={}
    for b,c in combinations_with_replacement(UNITS,2):
        k=canonical_pair(b,c)
        out.setdefault(k,[]).append((b,c))
    return out


def main():
    d=orbit_map()
    assert sum(map(len,d.values()))==36
    assert len(d)==15
    reps=sorted(d)
    assert reps==[(1,1),(1,3),(1,5),(1,7),(1,9),(1,11),(1,13),(1,15),
                  (3,5),(3,7),(3,9),(3,13),(3,15),(5,9),(7,9)]
    a_choices=comb(128,3)
    total=a_choices*len(reps)
    assert a_choices==341376
    assert total==5120640
    print('h188_pairs',36)
    print('h189_orbits',len(reps))
    print('canonical_representatives',reps)
    print('A_choices',a_choices)
    print('H189_design_representatives',total)
    for k in reps:
        print(k,'<-',d[k])


if __name__=='__main__':
    main()

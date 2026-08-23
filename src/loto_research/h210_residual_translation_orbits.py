"""H210 exact residual-translation quotient for the H175/H188 restricted family.

After H188 normalization B,C,D all have zero shifts (and D=(1,0)).
There remains a 16-element coordinate-translation symmetry indexed by t mod 16:

  group0 -> group0 - t
  group1 -> group1 - t
  group2 -> group2 - t
  group3 -> group3 + t
  group4 -> group4

For B=(0,3,4), C=(1,3,4), D=(2,3,4), the input translations cancel,
so their zero shifts remain zero. An A=(0,1,2) layer (a,c) transforms as

  (a,c) -> (a, c + (2a-1)t mod 16).

Because every 2a-1 is odd, each nonzero t acts on the 16 shifts for each a
with cycle length 16/gcd(t,16), hence length 2,4,8,or16. Therefore no
nonidentity group element can fix a 3-element A subset. The C16 action on
all C(128,3) A-sets is free, giving exactly C(128,3)/16 = 21,336 A orbits.
Multiplying by H188's 36 ordered B/C coefficient pairs gives 768,096 exact
representatives, a 16x reduction from H188's 12,289,536.
"""
from __future__ import annotations

from collections import Counter
from math import comb, gcd

ODDS=(1,3,5,7,9,11,13,15)
PARAMS=[(a,c) for a in ODDS for c in range(16)]


def translate_layer(p: tuple[int,int], t: int) -> tuple[int,int]:
    a,c=p
    return a,(c+(2*a-1)*t)%16


def cycle_profile(t: int) -> Counter:
    unseen=set(PARAMS)
    out=Counter()
    while unseen:
        start=next(iter(unseen)); q=start; n=0
        while q in unseen:
            unseen.remove(q); n+=1; q=translate_layer(q,t)
        out[n]+=1
    return out


def main():
    profiles={t:dict(sorted(cycle_profile(t).items())) for t in range(16)}
    assert profiles[0]=={1:128}
    for t in range(1,16):
        # all nonidentity cycles have even size, so no invariant 3-subset exists
        assert all(k in (2,4,8,16) for k in profiles[t])
    a_sets=comb(128,3)
    assert a_sets % 16 == 0
    a_orbits=a_sets//16
    h188=a_sets*36
    h210=a_orbits*36
    assert h188==12_289_536
    assert h210==768_096
    print('cycle_profiles',profiles)
    print('A_sets',a_sets)
    print('A_orbits',a_orbits)
    print('H188_representatives',h188)
    print('H210_representatives',h210)
    print('exact_reduction_factor',h188//h210)


if __name__=='__main__':
    main()

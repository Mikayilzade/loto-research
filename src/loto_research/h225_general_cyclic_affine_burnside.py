"""H225 exact Burnside count for the general cyclic-affine H175 family.

After the H225 normalization theorem:
  D=(1,1,0), B=(1,beta,0), C=(1,gamma,0), beta,gamma odd.
Residual stabilizer has (u,t2,t3), size 8*16*16=2048, and acts on an A layer
(a,b,c) by
  (a,b,c) -> (a,b, u*c + (1-a-b)t2
                       - (a(1-beta)+b(1-gamma))t3) mod16.

We need orbits of 3-element A-layer subsets. Burnside avoids enumerating
C(1024,3) subsets. For a permutation with f1 fixed points, f2 2-cycles and
f3 3-cycles, fixed 3-subsets count C(f1,3)+f1*f2+f3.
"""
from __future__ import annotations
from itertools import combinations
from math import comb

MOD=16
ODDS=(1,3,5,7,9,11,13,15)


def cycle123_affine16(u,d):
    perm=[(u*c+d)%16 for c in range(16)]
    seen=[False]*16; f1=f2=f3=0
    for i in range(16):
        if seen[i]: continue
        j=i; n=0
        while not seen[j]:
            seen[j]=True; j=perm[j]; n+=1
        if n==1: f1+=1
        elif n==2: f2+=1
        elif n==3: f3+=1
    return f1,f2,f3

CACHE={(u,d):cycle123_affine16(u,d) for u in ODDS for d in range(16)}


def fixed3(f1,f2,f3):
    return comb(f1,3)+f1*f2+f3


def residual_orbits(beta,gamma):
    total=0
    for u in ODDS:
        for t2 in range(16):
            for t3 in range(16):
                F1=F2=F3=0
                for a in ODDS:
                    for b in ODDS:
                        d=((1-a-b)*t2-(a*(1-beta)+b*(1-gamma))*t3)%16
                        q=CACHE[(u,d)]
                        F1+=q[0]; F2+=q[1]; F3+=q[2]
                total+=fixed3(F1,F2,F3)
    assert total%2048==0
    return total//2048


def fixed_points_affine16(u,d):
    return sum((u*c+d)%16==c for c in range(16))


def swap_coset_fixed3_sum(beta):
    """Burnside numerator for swap(0,1) composed with each residual element.

    Valid only beta=gamma. Diagonal coefficient blocks a=b stay in place.
    Off-diagonal blocks (a,b)<->(b,a) contribute only even cycles; their
    2-cycles are fixed points of the square map on one 16-point block.
    """
    total=0
    for u in ODDS:
        for t2 in range(16):
            for t3 in range(16):
                F1=F2=F3=0
                for a in ODDS:
                    d=((1-2*a)*t2-(2*a*(1-beta))*t3)%16
                    q=CACHE[(u,d)]
                    F1+=q[0]; F2+=q[1]; F3+=q[2]
                for ia,a in enumerate(ODDS):
                    for b in ODDS[ia+1:]:
                        d1=((1-a-b)*t2-(a*(1-beta)+b*(1-beta))*t3)%16
                        d2=((1-b-a)*t2-(b*(1-beta)+a*(1-beta))*t3)%16
                        F2+=fixed_points_affine16((u*u)%16,(u*d1+d2)%16)
                total+=fixed3(F1,F2,F3)
    return total


def full_count():
    # beta<gamma: group0/group1 swap identifies the two ordered BC sectors,
    # so retain one sector and quotient only by its residual stabilizer.
    residual={(be,ga):residual_orbits(be,ga) for be in ODDS for ga in ODDS}
    # Exact symmetry sanity check.
    assert all(residual[(be,ga)]==residual[(ga,be)] for be in ODDS for ga in ODDS)

    diagonal={}
    for be in ODDS:
        sum_g=residual[(be,be)]*2048
        sum_swap=swap_coset_fixed3_sum(be)
        assert (sum_g+sum_swap)%4096==0
        diagonal[be]=(sum_g+sum_swap)//4096

    off=sum(residual[(be,ga)] for be,ga in combinations(ODDS,2))
    diag=sum(diagonal.values())
    total=off+diag
    raw=36*comb(1024,3)
    assert raw==6_423_588_864
    assert off==30_776_576
    assert diag==5_466_528
    assert total==36_243_104
    return residual,diagonal,raw,off,diag,total


def main():
    residual,diagonal,raw,off,diag,total=full_count()
    print('raw_normalized_classes_before_residual_quotient',raw)
    print('off_diagonal_BC_orbits',off)
    print('diagonal_BC_orbits_with_swap',diag)
    print('exact_general_normalized_classes',total)
    print('reduction_factor',raw/total)
    print('diagonal_breakdown',diagonal)
    vals=sorted(set(residual.values()))
    print('residual_orbit_count_values',vals)
    print('VERIFIED')

if __name__=='__main__': main()

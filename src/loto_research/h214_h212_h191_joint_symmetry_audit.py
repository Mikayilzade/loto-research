"""H214 exact joint H212 affine-unit + H191 exceptional-S3 quotient audit.

H212 is globally valid on A.  H191's extra S3 is valid iff all three A layers
have slope 15.  In that exceptional sector each A layer is setwise S3-fixed,
so coordinate permutations act only on the B,C,D support coefficients after
renormalizing D to 1.  The H212 affine-unit action on A commutes with this
coordinate action at the set level, because a=15 layers are equations
x0+x1+x2=c and common unit/translation maps only c.  Therefore the quotient
can safely use 15 B/C coefficient classes for the 9 exceptional H212 A-orbits,
and 36 for all other H212 A-orbits.
"""
from __future__ import annotations

from itertools import combinations_with_replacement, permutations

from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits, LAYERS

UNITS=(1,3,5,7,9,11,13,15)


def inv16(a:int)->int:
    for b in UNITS:
        if (a*b)%16==1:
            return b
    raise ValueError(a)


def canonical_pair(b:int,c:int)->tuple[int,int]:
    vals=(b,c,1)
    out=[]
    for p in permutations(vals):
        r=inv16(p[2])
        out.append(tuple(sorted(((p[0]*r)%16,(p[1]*r)%16))))
    return min(out)


def main():
    reps, sizes, exceptional_from_h212 = enumerate_orbits()
    exceptional=[r for r in reps if all(LAYERS[i][0]==15 for i in r)]
    assert exceptional_from_h212==9
    assert len(exceptional)==9

    coeff_orbits={}
    for b,c in combinations_with_replacement(UNITS,2):
        coeff_orbits.setdefault(canonical_pair(b,c),[]).append((b,c))
    assert len(coeff_orbits)==15

    generic=len(reps)-len(exceptional)
    joint=generic*36+len(exceptional)*15
    assert generic==3983
    assert joint==143523

    print('H212_A_orbits',len(reps))
    print('exceptional_a15_A_orbits',len(exceptional))
    print('generic_A_orbits',generic)
    print('generic_BC_classes',36)
    print('exceptional_S3_BC_classes',len(coeff_orbits))
    print('H214_joint_representatives',joint)
    print('saving_vs_H212',143712-joint)
    print('saving_fraction',(143712-joint)/143712)


if __name__=='__main__':
    main()

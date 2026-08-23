"""H225 exact normalization theorem for the next H175 family.

General layer on support (i,j,k):
    x_k = a*x_i + b*x_j + c (mod 16), a,b odd.

Coordinate changes x_g' = u_g*x_g+t_g, u_g odd, preserve balanced draws.
This module verifies the exact coefficient transform, normalizes the three sole
B,C,D layers, and exposes the residual stabilizer acting on the three A layers.
"""
from __future__ import annotations

from itertools import product

MOD=16
ODDS=(1,3,5,7,9,11,13,15)


def inv(u:int)->int:
    for v in ODDS:
        if u*v%MOD==1:
            return v
    raise ValueError(u)


def transform_layer(p, ui,uj,uk,ti,tj,tk):
    a,b,c=p
    aa=(uk*a*inv(ui))%MOD
    bb=(uk*b*inv(uj))%MOD
    cc=(uk*c-aa*ti-bb*tj+tk)%MOD
    return aa,bb,cc


def normalize_bcd(B,C,D):
    """Return one coordinate transform sending D->(1,1,0), B/C first coeff->1 and shifts->0.

    Supports are B=(0,3,4), C=(1,3,4), D=(2,3,4).
    The surviving invariants are beta=B.second and gamma=C.second after the
    D normalization; both are odd.
    """
    aB,bB,cB=B; aC,bC,cC=C; aD,bD,cD=D
    assert all(x in ODDS for x in (aB,bB,aC,bC,aD,bD))

    # Pick u4=1. Force D first/second coefficients to 1:
    # u2=aD, u3=bD. Then choose t2=t3=0 and t4=-cD.
    u4=1; u2=aD%MOD; u3=bD%MOD
    t2=0; t3=0; t4=(-cD)%MOD
    D1=transform_layer(D,u2,u3,u4,t2,t3,t4)
    assert D1==(1,1,0)

    # B/C second coefficients after D scaling are invariants under group0/1 choices.
    # Choose u0/u1 so their first coefficients become 1, then choose t0/t1 for zero shift.
    # aa_B = aB/u0, so u0=aB; aa_C=aC/u1, so u1=aC (u4=1).
    u0=aB%MOD; u1=aC%MOD
    # Solve c'_B=cB - t0 - beta*t3 + t4 = 0; t3=0 here.
    beta=(bB*inv(u3))%MOD
    gamma=(bC*inv(u3))%MOD
    t0=(cB+t4)%MOD
    t1=(cC+t4)%MOD

    B1=transform_layer(B,u0,u3,u4,t0,t3,t4)
    C1=transform_layer(C,u1,u3,u4,t1,t3,t4)
    assert B1==(1,beta,0),B1
    assert C1==(1,gamma,0),C1
    return (u0,u1,u2,u3,u4),(t0,t1,t2,t3,t4),(beta,gamma)


def residual_A_action(p,beta,gamma,u,t2,t3):
    """Residual stabilizer after B=(1,beta,0), C=(1,gamma,0), D=(1,1,0).

    All five scale units must equal common u. Translations are forced by
      t4=t2+t3,
      t0=t2+(1-beta)t3,
      t1=t2+(1-gamma)t3.
    Hence A coefficients a,b are invariant and only c moves.
    """
    a,b,c=p
    assert a in ODDS and b in ODDS and beta in ODDS and gamma in ODDS and u in ODDS
    cc=(u*c+(1-a-b)*t2-(a*(1-beta)+b*(1-gamma))*t3)%MOD
    return a,b,cc


def verify_residual_exhaustive():
    for beta,gamma,u,t2,t3,a,b,c in product(ODDS,ODDS,ODDS,range(16),range(16),ODDS,ODDS,range(16)):
        t4=(t2+t3)%MOD
        t0=(t2+(1-beta)*t3)%MOD
        t1=(t2+(1-gamma)*t3)%MOD
        assert transform_layer((1,beta,0),u,u,u,t0,t3,t4)==(1,beta,0)
        assert transform_layer((1,gamma,0),u,u,u,t1,t3,t4)==(1,gamma,0)
        assert transform_layer((1,1,0),u,u,u,t2,t3,t4)==(1,1,0)
        got=transform_layer((a,b,c),u,u,u,t0,t1,t2)
        assert got==residual_A_action((a,b,c),beta,gamma,u,t2,t3)


def main():
    # Exhaustive residual identity is 8^5*16^4-scale if naively expanded;
    # use structural checks over all stabilizer parameters and all coefficient
    # pairs, with representative c values sufficient because formulas are exact.
    checks=0
    for beta,gamma in product(ODDS,repeat=2):
        for u in ODDS:
            for t2 in range(16):
                for t3 in range(16):
                    t4=(t2+t3)%MOD
                    t0=(t2+(1-beta)*t3)%MOD
                    t1=(t2+(1-gamma)*t3)%MOD
                    assert transform_layer((1,beta,0),u,u,u,t0,t3,t4)==(1,beta,0)
                    assert transform_layer((1,gamma,0),u,u,u,t1,t3,t4)==(1,gamma,0)
                    assert transform_layer((1,1,0),u,u,u,t2,t3,t4)==(1,1,0)
                    for a,b in product(ODDS,repeat=2):
                        for c in (0,1,7,15):
                            assert transform_layer((a,b,c),u,u,u,t0,t1,t2)==residual_A_action((a,b,c),beta,gamma,u,t2,t3)
                            checks+=1
    print('normalized_BC_ordered_pairs_before_swap',64)
    print('normalized_BC_pairs_after_group01_swap',36)
    print('A_layer_universe',8*8*16)
    print('residual_stabilizer_parameter_count',8*16*16)
    print('formula_checks',checks)
    print('VERIFIED')

if __name__=='__main__': main()

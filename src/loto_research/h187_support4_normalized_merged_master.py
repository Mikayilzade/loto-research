"""H187: merge H185+H186 valid cuts and solve under stronger D=id0 symmetry.

Exact WLOG theorem used here:
- restricted layers: z=a*x+a*y+c mod16, a odd;
- scale groups 0..3 by common odd u and group4 by independent odd w;
- supports ending in group4 get a'=(w/u)*a;
- choose w/u=a_D^{-1}, then translate group4, so the sole (2,3,4)
  layer is exactly id0=(a,c)=(1,0).

This removes the remaining factor 8 in H183's support-D normalization without
excluding any universal n3>=3 design.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, lil_matrix, vstack

from loto_research.h185_h180_affine_orbit_cut_acceleration import (
    ODDS, PARAMS, SUPPORTS, NP, load_bank as load_h185_bank,
)
from loto_research.h186_h185_mass_counterexample_packet import load as load_h186

ORBIT_START=254


def layer_hits(w,support):
    i,j,k=support
    xs=np.asarray(w[i],dtype=int); ys=np.asarray(w[j],dtype=int)
    target=np.zeros(16,dtype=np.int8); target[w[k]]=1
    vals=(PARAMS[:,0,None,None]*xs[None,:,None]
          +PARAMS[:,1,None,None]*ys[None,None,:]
          +PARAMS[:,2,None,None])%16
    return target[vals].sum(axis=(1,2)).astype(np.uint8)


def row(w):
    return np.concatenate([layer_hits(w,s) for s in SUPPORTS])


def orbit(w):
    for u in ODDS:
        for v in range(16):
            yield [[int((int(u)*x+v)%16) for x in grp] for grp in w]


def merged_active_rows():
    """Rebuild H185 base + all orbit-expanded post-H183/H186 valid rows."""
    h185=load_h185_bank()
    h186=load_h186()
    h186_w=[x['witness'] for x in h186['start_witnesses']]
    h186_w += [x['witness'] for x in h186['second_witnesses']]

    out=[]; seen=set()
    def add(w):
        r=row(w); key=bytes(r)
        if key not in seen:
            seen.add(key); out.append(r)

    # Preserve H183 legacy rows directly.
    for w in h185[:ORBIT_START]:
        add(w)

    # H185 post-H183 witnesses were already intended for full common-affine
    # expansion; H186 witnesses receive the same mathematically safe expansion.
    for w in list(h185[ORBIT_START:])+h186_w:
        for wo in orbit(w):
            add(wo)

    return out, len(h185), len(h186_w)


def solve_normalized_master(rows,time_limit=120.0):
    n=4*NP
    base=np.zeros((6,n),dtype=float)
    lb=np.full(6,-np.inf); ub=np.full(6,np.inf)

    for s,required in enumerate((3,1,1,1)):
        base[s,s*NP:(s+1)*NP]=1
        lb[s]=ub[s]=required

    # H187 stronger WLOG normalization: sole support-D layer is exactly id0.
    base[4,3*NP+0]=1
    lb[4]=ub[4]=1

    # H183 swap symmetry: id(B) <= id(C).
    ids=np.arange(NP,dtype=float)
    base[5,NP:2*NP]=ids
    base[5,2*NP:3*NP]=-ids
    ub[5]=0

    R=np.asarray(rows,dtype=float)
    A=vstack([csr_matrix(base),csr_matrix(R)],format='csc')
    lo=np.r_[lb,np.full(len(R),3.0)]
    hi=np.r_[ub,np.full(len(R),np.inf)]

    res=milp(
        np.zeros(n),
        integrality=np.ones(n,dtype=int),
        bounds=Bounds(np.zeros(n),np.ones(n)),
        constraints=LinearConstraint(A,lo,hi),
        options={'time_limit':time_limit,'presolve':True,'mip_rel_gap':0},
    )
    if res.x is None:
        return None,res
    chosen=[np.flatnonzero(res.x[s*NP:(s+1)*NP]>.5).tolist() for s in range(4)]
    return chosen,res


def triples(chosen):
    out=[]
    for s,(i,j,k) in enumerate(SUPPORTS):
        for pid in chosen[s]:
            a,b,c=map(int,PARAMS[pid])
            for x in range(16):
                for y in range(16):
                    out.append((i*16+x,j*16+y,k*16+((a*x+b*y+c)%16)))
    return np.asarray(out,dtype=np.int16)


def exact_separator_le2(chosen,time_limit=60.0):
    """Find a balanced n3<=2 witness exactly; timeout is inconclusive."""
    T=triples(chosen); m=len(T); n=80+m
    A=lil_matrix((5+m+1,n))
    lb=np.full(5+m+1,-np.inf); ub=np.full(5+m+1,np.inf)

    for g in range(5):
        A[g,g*16:(g+1)*16]=1
        lb[g]=ub[g]=4

    for q,(a,b,c) in enumerate(T):
        rr=5+q
        A[rr,int(a)]=1; A[rr,int(b)]=1; A[rr,int(c)]=1
        A[rr,80+q]=-1
        ub[rr]=2

    A[5+m,80:]=1
    ub[5+m]=2

    res=milp(
        np.zeros(n),
        integrality=np.ones(n,dtype=int),
        bounds=Bounds(np.zeros(n),np.ones(n)),
        constraints=LinearConstraint(csr_matrix(A),lb,ub),
        options={'time_limit':time_limit,'presolve':True,'mip_rel_gap':0},
    )
    if res.x is None:
        return None,res
    selected=res.x[:80]>.5
    witness=[[i for i in range(16) if selected[g*16+i]] for g in range(5)]
    exact=int(np.sum(selected[T[:,0]] & selected[T[:,1]] & selected[T[:,2]]))
    return (exact,witness),res


def main():
    rows,h185_n,h186_n=merged_active_rows()
    print('h185_stored',h185_n,'h186_new',h186_n,'merged_active_unique_rows',len(rows))
    chosen,res=solve_normalized_master(rows)
    print('master_status',res.status,res.message)
    if chosen is None:
        # Only solver-certified infeasibility is a proof. Timeout/no incumbent is not.
        return
    print('candidate',chosen)
    print('params',[[PARAMS[i].tolist() for i in ids] for ids in chosen])
    separated,sres=exact_separator_le2(chosen)
    print('separator_status',sres.status,sres.message)
    print('separator_result',separated)


if __name__=='__main__':
    main()

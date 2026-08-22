"""H186: stronger WLOG normalization for H175/H180 restricted diagonal family.

Restricted layers are z=a*x+a*y+c (mod 16), a odd.

H183 normalized the single (2,3,4) layer to c=0. H186 proves a stronger
normalization: scale groups 0..3 by an odd unit u and group 4 by an independent
odd unit w. The three supports ending in group 4 have coefficient
    a'=(w/u)*a,
while the (0,1,2) coefficients are unchanged. Choose w/u=a_D^{-1} to force the
selected (2,3,4) coefficient to 1, then translate group 4 to force c_D=0.
Thus any universal restricted-family design has a representative with the
(2,3,4) layer fixed exactly to candidate id 0 = (a,c)=(1,0).

The script also reproduces the exact n3<=2 separator for H185's recorded
current candidate and can solve the H185 persistent rows with the stronger
normalization when the H185 bank file is present.
"""
from __future__ import annotations

import base64
import json
import zlib
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, lil_matrix, vstack

ODDS=np.array([1,3,5,7,9,11,13,15],dtype=int)
PARAMS=np.array([(a,a,c) for a in ODDS for c in range(16)],dtype=int)
SUPPORTS=[(0,1,2),(0,3,4),(1,3,4),(2,3,4)]
NP=128
ORBIT_START=254
ROOT=Path(__file__).resolve().parents[2]
H185_BANK=ROOT/'data'/'derived'/'h185_h180_witness_bank.zlib.b64'
H185_CURRENT=[[18,54,111],[12],[88],[16]]


def load_h185_bank():
    raw=base64.b64decode(H185_BANK.read_text().strip())
    return json.loads(zlib.decompress(raw).decode())


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


def affine_orbit(w):
    for u in ODDS:
        for v in range(16):
            yield [[int((int(u)*x+v)%16) for x in group] for group in w]


def h185_active_rows(bank):
    out=[]; seen=set()
    def add(w):
        r=row(w); key=bytes(r)
        if key not in seen:
            seen.add(key); out.append(r)
    for w in bank[:ORBIT_START]:
        add(w)
    for w in bank[ORBIT_START:]:
        for wo in affine_orbit(w):
            add(wo)
    return out


def solve_normalized_master(rows,time_limit=30.0):
    """H185 master with stronger exact WLOG D=id0 normalization."""
    n=4*NP
    base=np.zeros((6,n),dtype=float)
    lb=np.full(6,-np.inf); ub=np.full(6,np.inf)

    for s,required in enumerate((3,1,1,1)):
        base[s,s*NP:(s+1)*NP]=1
        lb[s]=ub[s]=required

    # Strong H186 normalization: the sole (2,3,4) layer is exactly id0=(1,0).
    base[4,3*NP+0]=1
    lb[4]=ub[4]=1

    # H183 group-0/group-1 swap symmetry remains: id(B) <= id(C).
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


def exact_score(T,selected):
    return int(np.sum(selected[T[:,0]] & selected[T[:,1]] & selected[T[:,2]]))


def exact_separator_le2(chosen,time_limit=30.0):
    T=triples(chosen)
    m=len(T); n=80+m
    A=lil_matrix((5+m+1,n))
    lb=np.full(5+m+1,-np.inf); ub=np.full(5+m+1,np.inf)

    for g in range(5):
        A[g,g*16:(g+1)*16]=1
        lb[g]=ub[g]=4

    for q,(a,b,c) in enumerate(T):
        r=5+q
        A[r,int(a)]=1; A[r,int(b)]=1; A[r,int(c)]=1
        A[r,80+q]=-1
        ub[r]=2

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
    return (exact_score(T,selected),witness),res


def normalize_current_h185():
    """Concrete H185 D=(3,0) -> D=(1,0); then restore B<=C by swapping 0/1."""
    # 3^{-1}=11 mod16. With zero translations, group4 scale w=11.
    # B (1,12)->(11,4), C (11,8)->(9,8), D (3,0)->(1,0).
    # Swap groups 0/1, hence B/C swap.
    return [[18,54,111],[72],[84],[0]]


def main():
    sep,res=exact_separator_le2(H185_CURRENT)
    print('h185_current_separator_status',res.status,res.message)
    print('h185_current_exact_result',sep)
    print('normalized_equivalent',normalize_current_h185())

    if H185_BANK.exists():
        bank=load_h185_bank()
        rows=h185_active_rows(bank)
        print('h185_bank_witnesses',len(bank),'active_rows',len(rows))
        chosen,mres=solve_normalized_master(rows)
        print('normalized_master_status',mres.status,mres.message)
        print('normalized_master_candidate',chosen)


if __name__=='__main__':
    main()

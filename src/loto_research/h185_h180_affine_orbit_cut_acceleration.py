"""H185 orbit-accelerated continuation for the H175/H180 restricted master.

The merged bank contains 297 exact balanced witnesses. Indices 0..253 are the
H183 base cuts. Indices >=254 are expanded by common affine maps
x -> u*x+v (mod 16), u odd, v=0..15. Every image is itself a balanced draw,
so every generated n3>=3 row is a valid necessary cut.

Expected H185 checkpoint: 4,878 unique active rows and current master ids
[[18,54,111],[12],[88],[16]].
"""
from __future__ import annotations
import argparse, base64, json, random, zlib
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack

ODDS=np.array([1,3,5,7,9,11,13,15],dtype=int)
PARAMS=np.array([(a,a,c) for a in ODDS for c in range(16)],dtype=int)
SUPPORTS=[(0,1,2),(0,3,4),(1,3,4),(2,3,4)]
NP=128
ORBIT_START=254
ROOT=Path(__file__).resolve().parents[2]
BANK=ROOT/'data'/'derived'/'h185_h180_witness_bank.zlib.b64'

def load_bank():
    # The bank is text Base64. Historical commits may omit terminal '=' padding;
    # tolerate that representation while still letting zlib/json validate payload.
    s=''.join(BANK.read_text().split())
    s += '=' * (-len(s) % 4)
    bank=json.loads(zlib.decompress(base64.b64decode(s, validate=True)))
    if len(bank) != 297:
        raise ValueError(f'unexpected H185 witness count: {len(bank)} != 297')
    return bank

def layer_hits(w,support):
    i,j,k=support
    xs=np.asarray(w[i],dtype=int); ys=np.asarray(w[j],dtype=int)
    target=np.zeros(16,dtype=np.int8); target[w[k]]=1
    vals=(PARAMS[:,0,None,None]*xs[None,:,None]+PARAMS[:,1,None,None]*ys[None,None,:]+PARAMS[:,2,None,None])%16
    return target[vals].sum(axis=(1,2)).astype(np.uint8)

def row(w):
    return np.concatenate([layer_hits(w,s) for s in SUPPORTS])

def affine_orbit(w):
    for u in ODDS:
        for v in range(16):
            yield [[int((int(u)*x+v)%16) for x in group] for group in w]

def active_rows(bank):
    out=[]; seen=set()
    def add(w):
        r=row(w); key=bytes(r)
        if key not in seen:
            seen.add(key); out.append(r)
    for w in bank[:ORBIT_START]: add(w)
    for w in bank[ORBIT_START:]:
        for wo in affine_orbit(w): add(wo)
    return out

def solve_master(rows,time_limit=20.0):
    n=4*NP
    base=np.zeros((6,n)); lb=[]; ub=[]
    for s in range(4):
        base[s,s*NP:(s+1)*NP]=1
        req=3 if s==0 else 1
        lb.append(req); ub.append(req)
    for pid,p in enumerate(PARAMS):
        if int(p[2])!=0: base[4,3*NP+pid]=1
    lb.append(0); ub.append(0)
    ids=np.arange(NP,dtype=float)
    base[5,NP:2*NP]=ids; base[5,2*NP:3*NP]=-ids
    lb.append(-np.inf); ub.append(0)
    R=np.asarray(rows,dtype=float)
    A=vstack([csr_matrix(base),csr_matrix(R)],format='csr')
    lo=np.r_[lb,np.full(len(R),3.0)]
    hi=np.r_[ub,np.full(len(R),np.inf)]
    res=milp(np.zeros(n),integrality=np.ones(n,dtype=int),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(A,lo,hi),options={'time_limit':time_limit,'presolve':True,'mip_rel_gap':0})
    if res.x is None: return None,res
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

def score(T,S):
    return int(np.sum(S[T[:,0]] & S[T[:,1]] & S[T[:,2]]))

def local_adversary(T,seed=185999,restarts=60,max_steps=120):
    rng=random.Random(seed); best=10**9; bestS=None
    for _ in range(restarts):
        S=np.zeros(80,dtype=bool)
        for g in range(5): S[rng.sample(range(g*16,(g+1)*16),4)]=True
        q=score(T,S)
        for _ in range(max_steps):
            if q<best: best,bestS=q,S.copy()
            if q<=2: return q,S.copy()
            move=None; newq=q
            for g in range(5):
                chosen=np.flatnonzero(S[g*16:(g+1)*16])+g*16
                free=np.flatnonzero(~S[g*16:(g+1)*16])+g*16
                for old in chosen:
                    S[old]=False
                    for new in free:
                        S[new]=True; t=score(T,S); S[new]=False
                        if t<newq: newq=t; move=(int(old),int(new))
                    S[old]=True
            if move is None: break
            old,new=move; S[old]=False; S[new]=True; q=newq
    return best,bestS

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--attack',action='store_true'); args=ap.parse_args()
    bank=load_bank(); rows=active_rows(bank)
    print('stored_witnesses',len(bank),'active_unique_rows',len(rows))
    chosen,res=solve_master(rows)
    print('master_status',res.status,res.message)
    if chosen is None:
        print('MASTER_INFEASIBLE_RESTRICTED_FAMILY'); return
    print('chosen',chosen)
    print('params',[[PARAMS[i].tolist() for i in ids] for ids in chosen])
    if args.attack:
        T=triples(chosen); q,S=local_adversary(T)
        print('local_score',q)
        if S is not None and q<=2:
            w=[[i for i in range(16) if S[g*16+i]] for g in range(5)]
            print('explicit_counterexample',q,w)

if __name__=='__main__': main()

from __future__ import annotations
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix, csr_matrix

ODDS=np.array([1,3,5,7,9,11,13,15],dtype=int)
PARAMS=np.array([(a,a,c) for a in ODDS for c in range(16)],dtype=int)
SUPPORTS=[(0,1,2),(0,3,4),(1,3,4),(2,3,4)]
CHOSEN=[[3,16,94],[1],[9],[16]]


def build_triples():
    triples=[]
    for s,(i,j,k) in enumerate(SUPPORTS):
        for pid in CHOSEN[s]:
            a,b,c=map(int,PARAMS[pid])
            for x in range(16):
                for y in range(16):
                    z=(a*x+b*y+c)%16
                    triples.append((i*16+x,j*16+y,k*16+z))
    return np.asarray(triples,dtype=np.int16)


def exact_score(triples,selected):
    return int(np.sum(selected[triples[:,0]] & selected[triples[:,1]] & selected[triples[:,2]]))


def solve():
    triples=build_triples(); m=len(triples); n=80+m
    A=lil_matrix((5+m+1,n)); lb=np.full(5+m+1,-np.inf); ub=np.full(5+m+1,np.inf)
    for g in range(5):
        A[g,g*16:(g+1)*16]=1; lb[g]=ub[g]=4
    for q,(a,b,c) in enumerate(triples):
        r=5+q; A[r,int(a)]=1; A[r,int(b)]=1; A[r,int(c)]=1; A[r,80+q]=-1; ub[r]=2
    A[5+m,80:]=1; ub[5+m]=2
    res=milp(np.zeros(n),integrality=np.ones(n,dtype=int),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(csr_matrix(A),lb,ub),options={"time_limit":30.0,"presolve":True,"mip_rel_gap":0})
    if res.x is None:
        print(res.status,res.message); return
    selected=res.x[:80]>0.5
    witness=[[i for i in range(16) if selected[g*16+i]] for g in range(5)]
    print("status",res.status,res.message)
    print("n3",exact_score(triples,selected))
    print("witness",witness)

if __name__=="__main__": solve()

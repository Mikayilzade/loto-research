"""H188 stronger exact canonical master for the H175/H180 restricted family.

Builds on H187's D=id0 theorem and adds exact WLOG constraints:
- B=(0,3,4) shift c_B=0;
- C=(1,3,4) shift c_C=0;
- coefficient a_B <= a_C by swapping groups 0 and 1.

Proof: translate group0 by a_B^{-1}c_B and group1 by a_C^{-1}c_C.
These translations leave D unchanged, preserve B/C coefficients, and only move
A shifts inside A's unrestricted parameter family. Balanced subsets are mapped
bijectively, so universal n3>=3 is invariant.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack

from loto_research.h187_support4_normalized_merged_master import (
    merged_active_rows,
    exact_separator_le2,
)
from loto_research.h185_h180_affine_orbit_cut_acceleration import PARAMS, NP

ZERO_SHIFT_IDS=np.array([0,16,32,48,64,80,96,112],dtype=int)


def solve_h188_master(rows,time_limit=300.0):
    n=4*NP
    constraints=[]; lb=[]; ub=[]

    # cardinalities: A has 3 layers; B,C,D one each.
    for s,required in enumerate((3,1,1,1)):
        r=np.zeros(n,dtype=float)
        r[s*NP:(s+1)*NP]=1
        constraints.append(r); lb.append(required); ub.append(required)

    # H187: D exactly id0=(1,0).
    r=np.zeros(n,dtype=float); r[3*NP+0]=1
    constraints.append(r); lb.append(1); ub.append(1)

    # H188: B and C shifts both zero. Forbid all nonzero-shift ids.
    allowed=set(map(int,ZERO_SHIFT_IDS))
    for s in (1,2):
        r=np.zeros(n,dtype=float)
        for pid in range(NP):
            if pid not in allowed:
                r[s*NP+pid]=1
        constraints.append(r); lb.append(0); ub.append(0)

    # H188 B/C coefficient ordering. With zero shifts, pid=16*k and the pid
    # order equals odd-coefficient order, so sum(pid*B)-sum(pid*C)<=0.
    r=np.zeros(n,dtype=float)
    ids=np.arange(NP,dtype=float)
    r[NP:2*NP]=ids
    r[2*NP:3*NP]=-ids
    constraints.append(r); lb.append(-np.inf); ub.append(0)

    R=np.asarray(rows,dtype=float)
    A=vstack([csr_matrix(np.asarray(constraints)),csr_matrix(R)],format='csc')
    lo=np.r_[np.asarray(lb),np.full(len(R),3.0)]
    hi=np.r_[np.asarray(ub),np.full(len(R),np.inf)]

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


def main():
    rows,h185_n,h186_n=merged_active_rows()
    print('h185_stored',h185_n,'h186_new',h186_n,'merged_active_unique_rows',len(rows))
    print('canonical_representatives',12289536)
    chosen,res=solve_h188_master(rows)
    print('master_status',res.status,res.message)
    if chosen is None:
        # Only status=2 / solver-certified infeasibility closes the family.
        return
    print('candidate',chosen)
    print('params',[[PARAMS[i].tolist() for i in ids] for ids in chosen])
    sep,sres=exact_separator_le2(chosen,time_limit=120.0)
    print('separator_status',sres.status,sres.message)
    print('separator_result',sep)


if __name__=='__main__':
    main()

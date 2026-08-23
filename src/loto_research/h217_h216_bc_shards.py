"""H217: shard H216 exact cut-bank screen by one of 36 ordered B/C pairs.

Scientific predicate is unchanged from H216/H213. Each shard screens all 3,992
H212 A-orbit representatives against the same 4,878 exact H185+H186 necessary
cut rows for one B/C pair. Sharding removes the monolithic completion blocker
without weakening the proof standard.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits
from loto_research.h216_h212_bitset_cut_bank import mask_from_bool

ROOT=Path(__file__).resolve().parents[2]
BC_PAIRS=[(16*i,16*j) for i in range(8) for j in range(i,8)]

def screen_shard(idx:int):
    rows,h185_n,h186_n=merged_active_rows(); R=np.asarray(rows,dtype=np.uint8)
    reps,_,_=enumerate_orbits(); reps_arr=np.asarray(reps,dtype=np.int16)
    assert R.shape==(4878,512) and len(reps)==3992 and len(BC_PAIRS)==36
    A=R[:,reps_arr[:,0]]+R[:,reps_arr[:,1]]+R[:,reps_arr[:,2]]
    masks={k:[mask_from_bool(A[r]>=k) for r in range(len(R))] for k in (1,2,3)}
    b,c=BC_PAIRS[idx]; sm=(1<<len(reps))-1
    bc=R[:,128+b].astype(np.int16)+R[:,256+c].astype(np.int16)+R[:,384].astype(np.int16)
    for ridx,q in enumerate(bc):
        need=3-int(q)
        if need<=0: continue
        if need>3: sm=0; break
        sm &= masks[need][ridx]
        if not sm: break
    survivors=[]
    while sm:
        lsb=sm & -sm; i=lsb.bit_length()-1
        survivors.append([int(x) for x in reps[i]]); sm^=lsb
    return {'packet':'H217','shard':idx,'B':b,'C':c,'D':0,'h185':h185_n,'h186':h186_n,
            'exact_cut_rows':len(R),'A_orbits':len(reps),'survivor_count':len(survivors),'A_survivors':survivors}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('shard',type=int,choices=range(36)); a=ap.parse_args()
    out=screen_shard(a.shard); p=ROOT/'data'/'derived'/'h217_shards'/f'shard_{a.shard:02d}.json'
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='A_survivors'},indent=2)); print('RESULT_FILE',p)
if __name__=='__main__': main()

"""H223: memory-light exact screen of all H212-normalized restricted H175 classes.

Same finite predicate as H219/H222, but avoids materializing the full
4878 x 3992 temporary arithmetic result for every B/C class. Witness rows and
A-incidence are computed once; A candidates are evaluated in bounded blocks.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from loto_research.h187_support4_normalized_merged_master import merged_active_rows
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h223_streaming_survivors.json'
BC_PAIRS=[(16*i,16*j) for i in range(8) for j in range(i,8)]
BLOCK=256

def run():
    rows,h185_n,h186_n=merged_active_rows()
    R=np.asarray(rows,dtype=np.uint8)
    assert R.shape==(4878,512)
    reps,orbit_sizes,exceptional=enumerate_orbits()
    assert len(reps)==3992 and len(BC_PAIRS)==36
    reps_arr=np.asarray(reps,dtype=np.int16)
    # Exact uint8 A incidence, maximum 48; no overflow.
    A=R[:,reps_arr[:,0]]+R[:,reps_arr[:,1]]+R[:,reps_arr[:,2]]
    survivors=[]; counts=[]
    for shard,(b,c) in enumerate(BC_PAIRS):
        bc=R[:,128+b]+R[:,256+c]+R[:,384]
        ids=[]
        for lo in range(0,len(reps),BLOCK):
            hi=min(lo+BLOCK,len(reps))
            # Exact predicate for this bounded candidate block.
            keep=np.all(A[:,lo:hi]+bc[:,None]>=3,axis=0)
            ids.extend((lo+np.flatnonzero(keep)).tolist())
        counts.append(len(ids))
        survivors.extend({'shard':shard,'B':int(b),'C':int(c),'A':[int(x) for x in reps[i]]} for i in ids)
    out={'packet':'H223','method':'streaming_block_exact_cut_bank','block':BLOCK,
         'h185_stored':int(h185_n),'h186_witnesses':int(h186_n),'exact_cut_rows':len(R),
         'A_orbits':len(reps),'bc_classes':len(BC_PAIRS),'normalized_classes_screened':len(reps)*len(BC_PAIRS),
         'orbit_sizes':{str(k):int(v) for k,v in sorted(orbit_sizes.items())},
         'exceptional_a15_A_orbits':int(exceptional),'shard_survivor_counts':counts,
         'survivor_count':len(survivors),'survivors':survivors}
    assert out['normalized_classes_screened']==143712
    assert out['survivor_count']==sum(counts)
    return out

def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='survivors'},indent=2))

if __name__=='__main__': main()

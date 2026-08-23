"""H218: merge all 36 H217 exact B/C shard outputs.

The merger is deliberately strict: it refuses to emit a result unless every
shard 0..35 exists and has the expected exact-cut metadata. The union key is
(B,C,A-representative); thus survivor_count is the exact survivor count of the
H217/H216 necessary-cut screen over all 143,712 H212 classes.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SHARDS=ROOT/'data'/'derived'/'h217_shards'
OUT=ROOT/'data'/'derived'/'h218_h217_merged_survivors.json'


def main():
    rows=[]
    total=0
    for i in range(36):
        p=SHARDS/f'shard_{i:02d}.json'
        if not p.exists():
            raise SystemExit(f'MISSING_SHARD {i}')
        d=json.loads(p.read_text())
        assert d['packet']=='H217' and d['shard']==i
        assert d['exact_cut_rows']==4878 and d['A_orbits']==3992 and d['D']==0
        assert d['survivor_count']==len(d['A_survivors'])
        total += d['survivor_count']
        for a in d['A_survivors']:
            rows.append({'shard':i,'B':d['B'],'C':d['C'],'D':0,'A':a})
    assert total==len(rows)
    out={'packet':'H218','scientific_screen':'H216/H217 exact necessary-cut bank',
         'shards':36,'A_orbits_per_shard':3992,'classes_screened':36*3992,
         'exact_cut_rows':4878,'survivor_count':total,'survivors':rows}
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='survivors'},indent=2))
    print('RESULT_FILE',OUT)

if __name__=='__main__': main()

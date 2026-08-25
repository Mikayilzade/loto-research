"""H225-X20: full 44-way exact rescreen after H225-X19 separator cuts."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import loto_research.h225_x10_incremental_rescreen as base

ROOT=Path(__file__).resolve().parents[2]
X11=ROOT/'data'/'derived'/'h225_x11_new_witnesses.json'
X13=ROOT/'data'/'derived'/'h225_x13_new_witnesses.json'
X15=ROOT/'data'/'derived'/'h225_x15_new_witnesses.json'
X17=ROOT/'data'/'derived'/'h225_x17_new_witnesses.json'
X19=ROOT/'data'/'derived'/'h225_x19_new_witnesses.json'
OUTDIR=ROOT/'data'/'derived'/'h225_x20_chunk_shards'
MERGED=ROOT/'data'/'derived'/'h225_x20_incremental_exact_rescreen.json'
base.PACKETS=base.PACKETS+[(X11,'H225-X11'),(X13,'H225-X13'),(X15,'H225-X15'),(X17,'H225-X17'),(X19,'H225-X19')]

def solve_chunk(sector_index,chunk):
 out=base.solve_chunk(sector_index,chunk)
 out['packet']='H225-X20'; out['source_packet']='H225-X19'
 out['x19_raw_new_witnesses']=out.pop('x9_raw_new_witnesses')
 out['x19_affine_expanded_instances']=out.pop('x9_affine_expanded_instances')
 return out

def merge(paths):
 rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:(x['sector_index'],x['chunk_index']))
 assert len(rows)==44 and all(x['packet']=='H225-X20' for x in rows)
 assert [(x['sector_index'],x['chunk_index']) for x in rows]==[(s,c) for s in range(11) for c in range(base.CHUNKS)]
 sectors=[]
 for s in range(11):
  rr=[x for x in rows if x['sector_index']==s]
  assert sum(int(x['chunk_quotient_states']) for x in rr)==base.EXPECTED_STATES[s]
  sectors.append({'sector_index':s,'representative':list(base.EXPECTED_REPS[s]),'quotient_coefficient_states':base.EXPECTED_STATES[s],
   'envelope_survivor_states':sum(int(x['envelope_survivor_states']) for x in rr),
   'exact_shift_surviving_coefficient_states':sum(int(x['exact_shift_surviving_coefficient_states']) for x in rr),
   'exact_surviving_shift_tuples':sum(int(x['exact_surviving_shift_tuples']) for x in rr),'chunks':rr})
 total=sum(int(x['quotient_coefficient_states']) for x in sectors); assert total==306450
 exstates=sum(int(x['exact_shift_surviving_coefficient_states']) for x in sectors)
 tuples=sum(int(x['exact_surviving_shift_tuples']) for x in sectors)
 return {'packet':'H225-X20','method':'full_exact_rescreen_after_X19_new_witness_affine_orbits','source_packet':'H225-X19','chunk_shards':44,
  'quotient_coefficient_states_screened':total,'envelope_survivor_states':sum(int(x['envelope_survivor_states']) for x in sectors),
  'exact_shift_surviving_coefficient_states':exstates,'exact_surviving_shift_tuples':tuples,
  'x19_raw_new_witnesses':int(rows[0]['x19_raw_new_witnesses']),'x19_affine_expanded_instances':int(rows[0]['x19_affine_expanded_instances']),
  'all_general_cyclic_affine_designs_rejected_by_augmented_witnesses':bool(exstates==0),'sectors':sectors,
  'interpretation':'Zero exact survivors closes H225. Positive survivors require H225-X21 separators.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--sector',type=int); ap.add_argument('--chunk',type=int); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
 if a.sector is not None:
  assert a.chunk is not None and 0<=a.sector<11 and 0<=a.chunk<base.CHUNKS
  out=solve_chunk(a.sector,a.chunk); OUTDIR.mkdir(parents=True,exist_ok=True); (OUTDIR/f'sector_{a.sector:02d}_chunk_{a.chunk:02d}.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k not in ('first_exact_survivors','envelope_first_killer_histogram','csp_terminal_killer_histogram')},indent=2)); return
 assert a.merge_dir is not None; out=merge(sorted(a.merge_dir.rglob('sector_*_chunk_*.json'))); MERGED.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='sectors'},indent=2))
if __name__=='__main__': main()

"""H225-X19: unrestricted exact separators for actual validated H225-X18 survivors."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import loto_research.h225_x17_survivor_separation as base

ROOT=Path(__file__).resolve().parents[2]
X18=ROOT/'data'/'derived'/'h225_x18_incremental_exact_rescreen.json'
OUTDIR=ROOT/'data'/'derived'/'h225_x19_separator_shards'
MERGED=ROOT/'data'/'derived'/'h225_x19_survivor_separation.json'
NEW=ROOT/'data'/'derived'/'h225_x19_new_witnesses.json'
base.X16=X18
base.OUTDIR=OUTDIR
base.MERGED=MERGED
base.NEW=NEW
base.OLD=base.OLD+[(ROOT/'data'/'derived'/'h225_x17_new_witnesses.json','H225-X17')]

def load_x18():
 d=json.loads(X18.read_text())
 assert d['packet']=='H225-X18' and d['chunk_shards']==44 and d['quotient_coefficient_states_screened']==306450 and len(d['sectors'])==11
 assert sum(int(s['quotient_coefficient_states']) for s in d['sectors'])==306450
 assert sum(int(s['exact_shift_surviving_coefficient_states']) for s in d['sectors'])==int(d['exact_shift_surviving_coefficient_states'])
 assert sum(int(s['exact_surviving_shift_tuples']) for s in d['sectors'])==int(d['exact_surviving_shift_tuples'])
 assert int(d['exact_shift_surviving_coefficient_states'])==3300
 assert int(d['exact_surviving_shift_tuples'])==71392
 return d
base.load_x16=load_x18

def relabel_job(out):
 out['packet']='H225-X19'; out['source_packet']='H225-X18'
 if 'x16_chunk_survivor_states' in out: out['x18_chunk_survivor_states']=out.pop('x16_chunk_survivor_states')
 if 'x16_chunk_survivor_shift_tuples' in out: out['x18_chunk_survivor_shift_tuples']=out.pop('x16_chunk_survivor_shift_tuples')
 return out

def solve_job(job,time_limit): return relabel_job(base.solve_job(job,time_limit))

def merge(paths):
 merged,wp=base.merge(paths); x18=load_x18()
 merged['packet']='H225-X19'; merged['source_packet']='H225-X18'
 merged['x18_survivor_states']=int(x18['exact_shift_surviving_coefficient_states'])
 merged['x18_survivor_shift_tuples']=int(x18['exact_surviving_shift_tuples'])
 merged.pop('x16_survivor_states',None); merged.pop('x16_survivor_shift_tuples',None)
 for r in merged['jobs']: relabel_job(r)
 wp['packet']='H225-X19'; wp['deduplicated_against']=['H234','H225-X1','H225-X3','H225-X5','H225-X7','H225-X9','H225-X11','H225-X13','H225-X15','H225-X17']
 return merged,wp

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--job',type=int); ap.add_argument('--time-limit',type=float,default=180.0); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
 if a.job is not None:
  out=solve_job(a.job,a.time_limit); OUTDIR.mkdir(parents=True,exist_ok=True); (OUTDIR/f'job_{a.job:02d}.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='witness'},indent=2)); return
 assert a.merge_dir is not None
 merged,wp=merge(sorted(a.merge_dir.rglob('job_*.json'))); MERGED.write_text(json.dumps(merged,indent=2)+'\n'); NEW.write_text(json.dumps(wp,indent=2)+'\n'); print(json.dumps({k:v for k,v in merged.items() if k!='jobs'},indent=2))
if __name__=='__main__': main()

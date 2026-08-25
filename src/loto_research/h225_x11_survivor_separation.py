"""H225-X11: unrestricted exact separators for actual validated H225-X10 survivors.

This stage intentionally reuses the audited X9 separator implementation while
repointing its globals to X10 and extending the immutable witness history
through X9. Published packets are relabelled H225-X11.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import loto_research.h225_x9_survivor_separation as base

ROOT=Path(__file__).resolve().parents[2]
X10=ROOT/'data'/'derived'/'h225_x10_incremental_exact_rescreen.json'
OUTDIR=ROOT/'data'/'derived'/'h225_x11_separator_shards'
MERGED=ROOT/'data'/'derived'/'h225_x11_survivor_separation.json'
NEW=ROOT/'data'/'derived'/'h225_x11_new_witnesses.json'
base.X8=X10
base.OUTDIR=OUTDIR
base.MERGED=MERGED
base.NEW=NEW
base.OLD=base.OLD+[(ROOT/'data'/'derived'/'h225_x9_new_witnesses.json','H225-X9')]

def load_x10():
 d=json.loads(X10.read_text())
 assert d['packet']=='H225-X10' and d['chunk_shards']==44 and d['quotient_coefficient_states_screened']==306450 and len(d['sectors'])==11
 assert sum(int(s['quotient_coefficient_states']) for s in d['sectors'])==306450
 return d
base.load_x8=load_x10

def relabel_job(out):
 out['packet']='H225-X11'
 out['source_packet']='H225-X10'
 if 'x8_chunk_survivor_states' in out: out['x10_chunk_survivor_states']=out.pop('x8_chunk_survivor_states')
 if 'x8_chunk_survivor_shift_tuples' in out: out['x10_chunk_survivor_shift_tuples']=out.pop('x8_chunk_survivor_shift_tuples')
 return out

def solve_job(job,time_limit): return relabel_job(base.solve_job(job,time_limit))

def merge(paths):
 merged,wp=base.merge(paths)
 x10=load_x10()
 merged['packet']='H225-X11'; merged['source_packet']='H225-X10'
 merged['x10_survivor_states']=int(x10['exact_shift_surviving_coefficient_states'])
 merged['x10_survivor_shift_tuples']=int(x10['exact_surviving_shift_tuples'])
 merged.pop('x8_survivor_states',None); merged.pop('x8_survivor_shift_tuples',None)
 for r in merged['jobs']: relabel_job(r)
 wp['packet']='H225-X11'; wp['deduplicated_against']=['H234','H225-X1','H225-X3','H225-X5','H225-X7','H225-X9']
 return merged,wp

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--job',type=int); ap.add_argument('--time-limit',type=float,default=180.0); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
 if a.job is not None:
  out=solve_job(a.job,a.time_limit); OUTDIR.mkdir(parents=True,exist_ok=True); (OUTDIR/f'job_{a.job:02d}.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='witness'},indent=2)); return
 assert a.merge_dir is not None
 merged,wp=merge(sorted(a.merge_dir.rglob('job_*.json'))); MERGED.write_text(json.dumps(merged,indent=2)+'\n'); NEW.write_text(json.dumps(wp,indent=2)+'\n'); print(json.dumps({k:v for k,v in merged.items() if k!='jobs'},indent=2))
if __name__=='__main__': main()

"""H225-X7: unrestricted exact separators for actual H225-X6 survivors."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from loto_research.h180_h175_master_cutting_plane import exact_separator
from loto_research.h226_general_coefficient_envelope_prescreen import COEFFS
from loto_research.h234_h232_first_survivor_exact_separation import balanced, build_triples, witness_key

ROOT=Path(__file__).resolve().parents[2]
X6=ROOT/'data'/'derived'/'h225_x6_incremental_exact_rescreen.json'
OLD=[
 (ROOT/'data'/'derived'/'h234_new_witnesses.json','H234'),
 (ROOT/'data'/'derived'/'h240_new_witnesses.json','H240'),
 (ROOT/'data'/'derived'/'h225_x3_new_witnesses.json','H225-X3'),
 (ROOT/'data'/'derived'/'h225_x5_new_witnesses.json','H225-X5'),
]
OUTDIR=ROOT/'data'/'derived'/'h225_x7_separator_shards'
MERGED=ROOT/'data'/'derived'/'h225_x7_survivor_separation.json'
NEW=ROOT/'data'/'derived'/'h225_x7_new_witnesses.json'
JOBS=44

def load_x6():
 d=json.loads(X6.read_text()); assert d['packet']=='H225-X6' and d['chunk_shards']==44 and d['quotient_coefficient_states_screened']==306450 and len(d['sectors'])==11
 assert sum(int(s['quotient_coefficient_states']) for s in d['sectors'])==306450
 return d

def solve_job(job,time_limit):
 assert 0<=job<JOBS
 si,ci=divmod(job,4); d=load_x6(); sec=d['sectors'][si]; ch=sec['chunks'][ci]
 assert (int(ch['sector_index']),int(ch['chunk_index']))==(si,ci)
 ns=int(ch['exact_shift_surviving_coefficient_states']); nt=int(ch['exact_surviving_shift_tuples'])
 if ns==0:
  assert nt==0
  return {'packet':'H225-X7','job':job,'sector_index':si,'chunk_index':ci,'skipped_no_survivor':True,'x6_chunk_survivor_states':0,'x6_chunk_survivor_shift_tuples':0,'counterexample_found':False,'conclusive_for_selected_design':True,'n3':None,'witness':None}
 ex=ch['first_exact_survivors']; assert ex
 chosen=ex[0]; coeff=tuple(map(int,chosen['coefficients'])); shifts=tuple(map(int,chosen['first_shift_examples'][0])); beta,gamma=map(int,sec['representative'])
 triples=build_triples(beta,gamma,coeff,shifts); separated,res=exact_separator(triples,time_limit=time_limit)
 out={'packet':'H225-X7','job':job,'sector_index':si,'chunk_index':ci,'skipped_no_survivor':False,'x6_chunk_survivor_states':ns,'x6_chunk_survivor_shift_tuples':nt,'representative':[beta,gamma],'coefficients':list(coeff),'coefficient_pairs':[list(map(int,COEFFS[p])) for p in coeff],'shifts':list(shifts),'triples':int(len(triples)),'separator_status':int(res.status),'separator_message':str(res.message),'counterexample_found':separated is not None,'conclusive_for_selected_design':separated is not None}
 if separated is None: out.update(n3=None,witness=None,interpretation='No feasible incumbent returned within budget: inconclusive, not validation.')
 else:
  score,w=separated; assert score<=2 and balanced(w); out.update(n3=int(score),witness=[[int(x) for x in g] for g in w])
 return out

def old_keys():
 out=set()
 for p,packet in OLD:
  d=json.loads(p.read_text()); assert d['packet']==packet and len(d['witnesses'])==int(d['witness_count']); out.update(witness_key(w) for w in d['witnesses'])
 return out

def merge(paths):
 rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:int(x['job'])); assert len(rows)==JOBS and [int(x['job']) for x in rows]==list(range(JOBS))
 active=[r for r in rows if not r['skipped_no_survivor']]; found=[r for r in active if r['counterexample_found']]
 unique={}
 for r in found: assert int(r['n3'])<=2 and balanced(r['witness']); unique.setdefault(witness_key(r['witness']),r['witness'])
 old=old_keys(); new={k:w for k,w in unique.items() if k not in old}; x6=load_x6()
 merged={'packet':'H225-X7','source_packet':'H225-X6','x6_survivor_states':int(x6['exact_shift_surviving_coefficient_states']),'x6_survivor_shift_tuples':int(x6['exact_surviving_shift_tuples']),'total_chunks':JOBS,'active_survivor_chunks':len(active),'skipped_zero_survivor_chunks':JOBS-len(active),'counterexamples_found':len(found),'inconclusive_active_jobs':len(active)-len(found),'unique_balanced_counterexamples':len(unique),'genuinely_new_witnesses':len(new),'all_selected_active_designs_broken':len(found)==len(active),'jobs':rows}
 wp={'packet':'H225-X7','witness_count':len(new),'witnesses':list(new.values()),'deduplicated_against':['H234','H225-X1','H225-X3','H225-X5'],'validity':'Every stored witness is balanced and returned by unrestricted exact n3<=2 MILP separation.'}
 return merged,wp

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--job',type=int); ap.add_argument('--time-limit',type=float,default=180.0); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
 if a.job is not None:
  out=solve_job(a.job,a.time_limit); OUTDIR.mkdir(parents=True,exist_ok=True); (OUTDIR/f'job_{a.job:02d}.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='witness'},indent=2)); return
 assert a.merge_dir is not None
 merged,wp=merge(sorted(a.merge_dir.rglob('job_*.json'))); MERGED.write_text(json.dumps(merged,indent=2)+'\n'); NEW.write_text(json.dumps(wp,indent=2)+'\n'); print(json.dumps({k:v for k,v in merged.items() if k!='jobs'},indent=2))
if __name__=='__main__': main()

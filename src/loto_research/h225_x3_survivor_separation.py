"""H225-X3: exact separator packet after H225-X2 incremental rescreen.

H225-X2 was completed as 44 exact shards over all 306,450 quotient states.  The
legacy merged JSON was not published reliably, so X3 consumes the compact,
audited 44-row survivor seed reconstructed independently from those shards.
Each row contains one actual shift-level survivor plus the exact per-chunk
survivor counts.  Returned balanced n3<=2 witnesses are deduplicated against
both H234 and H225-X1 before publication.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from loto_research.h180_h175_master_cutting_plane import exact_separator
from loto_research.h226_general_coefficient_envelope_prescreen import COEFFS
from loto_research.h234_h232_first_survivor_exact_separation import build_triples, balanced, witness_key

ROOT=Path(__file__).resolve().parents[2]
X2_SEED=ROOT/'data'/'derived'/'h225_x2_survivor_seed.json'
H234=ROOT/'data'/'derived'/'h234_new_witnesses.json'
X1=ROOT/'data'/'derived'/'h240_new_witnesses.json'
OUTDIR=ROOT/'data'/'derived'/'h225_x3_separator_shards'
MERGED=ROOT/'data'/'derived'/'h225_x3_survivor_separation.json'
NEW=ROOT/'data'/'derived'/'h225_x3_new_witnesses.json'
JOBS=44
EXPECTED_SCHEMA=[
    'sector','chunk','beta','gamma','coeff0','coeff1','coeff2',
    'shift0','shift1','shift2','chunk_survivor_states','chunk_survivor_shift_tuples'
]

def load_x2_seed():
    d=json.loads(X2_SEED.read_text())
    assert d['packet']=='H225-X2-SEED-V1'
    assert d['source_run']==32693907822
    assert d['shards']==44 and d['states']==306450
    assert d['survivor_states']==295293 and d['survivor_shift_tuples']==65921861
    assert d['active_chunks']==44
    assert d['row_schema']==EXPECTED_SCHEMA
    rows=d['seeds']; assert len(rows)==JOBS
    assert [(int(r[0]),int(r[1])) for r in rows]==[(s,c) for s in range(11) for c in range(4)]
    assert sum(int(r[10]) for r in rows)==d['survivor_states']
    assert sum(int(r[11]) for r in rows)==d['survivor_shift_tuples']
    return d

def solve_job(job,time_limit):
    assert 0<=job<JOBS
    si,ci=divmod(job,4); d=load_x2_seed(); row=d['seeds'][job]
    assert (int(row[0]),int(row[1]))==(si,ci)
    beta,gamma=map(int,row[2:4]); coefficients=tuple(map(int,row[4:7])); shifts=tuple(map(int,row[7:10]))
    survivor_states=int(row[10]); survivor_shift_tuples=int(row[11])
    assert survivor_states>0 and survivor_shift_tuples>0
    T=build_triples(beta,gamma,coefficients,shifts)
    separated,res=exact_separator(T,time_limit=time_limit)
    out={'packet':'H225-X3','job':job,'sector_index':si,'chunk_index':ci,'skipped_no_survivor':False,
         'x2_chunk_survivor_states':survivor_states,'x2_chunk_survivor_shift_tuples':survivor_shift_tuples,
         'representative':[beta,gamma],'coefficients':list(coefficients),'coefficient_pairs':[list(map(int,COEFFS[p])) for p in coefficients],
         'shifts':list(shifts),'triples':int(len(T)),'separator_status':int(res.status),'separator_message':str(res.message),
         'counterexample_found':separated is not None,'conclusive_for_selected_design':separated is not None}
    if separated is None:
        out.update(n3=None,witness=None,interpretation='No feasible incumbent returned within budget: inconclusive, not validation.')
    else:
        score,w=separated; assert score<=2 and balanced(w); out.update(n3=int(score),witness=[[int(x) for x in g] for g in w])
    return out

def merge(paths):
    rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:x['job'])
    assert len(rows)==JOBS and [x['job'] for x in rows]==list(range(JOBS))
    active=[r for r in rows if not r['skipped_no_survivor']]; found=[r for r in active if r['counterexample_found']]
    unique={}
    for r in found:
        assert r['n3']<=2 and balanced(r['witness']); unique.setdefault(witness_key(r['witness']),r['witness'])
    old=[]
    for p,packet in ((H234,'H234'),(X1,'H240')):
        d=json.loads(p.read_text()); assert d['packet']==packet; old.extend(d['witnesses'])
    oldkeys={witness_key(w) for w in old}; new={k:w for k,w in unique.items() if k not in oldkeys}
    seed=load_x2_seed()
    merged={'packet':'H225-X3','source_packet':'H225-X2','source_seed_file':str(X2_SEED.relative_to(ROOT)),
            'source_run':seed['source_run'],'source_full_merge_sha256':seed['full_merge_sha256'],
            'x2_survivor_states':seed['survivor_states'],'x2_survivor_shift_tuples':seed['survivor_shift_tuples'],
            'total_chunks':JOBS,'active_survivor_chunks':len(active),'skipped_zero_survivor_chunks':JOBS-len(active),
            'counterexamples_found':len(found),'inconclusive_active_jobs':len(active)-len(found),
            'unique_balanced_counterexamples':len(unique),'genuinely_new_witnesses':len(new),
            'all_selected_active_designs_broken':len(found)==len(active),'jobs':rows}
    wp={'packet':'H225-X3','witness_count':len(new),'witnesses':list(new.values()),
        'deduplicated_against':['H234','H225-X1'],'validity':'Every stored witness is balanced and returned by unrestricted exact n3<=2 MILP separation.'}
    return merged,wp

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--job',type=int); ap.add_argument('--time-limit',type=float,default=180.0); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
    if a.job is not None:
        out=solve_job(a.job,a.time_limit); OUTDIR.mkdir(parents=True,exist_ok=True); p=OUTDIR/f'job_{a.job:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='witness'},indent=2)); return
    assert a.merge_dir is not None
    merged,wp=merge(sorted(a.merge_dir.rglob('job_*.json'))); MERGED.write_text(json.dumps(merged,indent=2)+'\n'); NEW.write_text(json.dumps(wp,indent=2)+'\n'); print(json.dumps({k:v for k,v in merged.items() if k!='jobs'},indent=2))
if __name__=='__main__': main()

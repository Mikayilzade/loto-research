"""H237: unrestricted exact separator for one actual H235 survivor per chunk.

H235 is a complete 44-chunk rescreen after H234. An auxiliary H235-AUDIT
independently verified all 44 chunks and positive survivors in every chunk.
H237 selects one actual shift-level H235 survivor from each chunk and asks the
unrestricted exact n3<=2 separator for a fresh balanced counterexample.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from loto_research.h180_h175_master_cutting_plane import exact_separator
from loto_research.h226_general_coefficient_envelope_prescreen import COEFFS
from loto_research.h234_h232_first_survivor_exact_separation import build_triples, balanced, witness_key
ROOT=Path(__file__).resolve().parents[2]
H235=ROOT/'data'/'derived'/'h235_h234_augmented_exact_shift_rescreen.json'
AUDIT=ROOT/'data'/'derived'/'h236_h235_certificate_audit_summary.json'
OUTDIR=ROOT/'data'/'derived'/'h237_separator_shards'
MERGED=ROOT/'data'/'derived'/'h237_h235_first_survivor_separation.json'
NEW_WITNESSES=ROOT/'data'/'derived'/'h237_new_witnesses.json'
JOBS=44; EXPECTED_STATES=306450; EXPECTED_SURVIVORS=303802; EXPECTED_SHIFT_TUPLES=90425060

def load_h235():
    a=json.loads(AUDIT.read_text())
    assert a['packet']=='H235-AUDIT' and a['audit_target']=='H235' and a['numbered_packet'] is False
    assert a['all_44_chunks_present_and_disjoint'] is True
    assert a['quotient_coefficient_states_verified']==EXPECTED_STATES
    assert a['exact_shift_surviving_coefficient_states']==EXPECTED_SURVIVORS
    assert a['exact_surviving_shift_tuples']==EXPECTED_SHIFT_TUPLES
    d=json.loads(H235.read_text())
    assert d['packet']=='H235' and d['chunk_shards']==44
    assert d['quotient_coefficient_states_screened']==EXPECTED_STATES
    assert d['exact_shift_surviving_coefficient_states']==EXPECTED_SURVIVORS
    assert d['exact_surviving_shift_tuples']==EXPECTED_SHIFT_TUPLES
    return d

def solve_job(job,time_limit):
    assert 0<=job<JOBS
    si,ci=divmod(job,4); d=load_h235(); sec=d['sectors'][si]; ch=sec['chunks'][ci]
    assert (ch['sector_index'],ch['chunk_index'])==(si,ci) and ch['exact_shift_surviving_coefficient_states']>0
    chosen=ch['first_exact_survivors'][0]; coefficients=tuple(map(int,chosen['coefficients']))
    shifts=tuple(map(int,chosen['first_shift_examples'][0])); beta,gamma=map(int,sec['representative'])
    T=build_triples(beta,gamma,coefficients,shifts); separated,res=exact_separator(T,time_limit=time_limit)
    out={'packet':'H237','job':job,'sector_index':si,'chunk_index':ci,'representative':[beta,gamma],
         'coefficients':list(coefficients),'coefficient_pairs':[list(map(int,COEFFS[p])) for p in coefficients],
         'shifts':list(shifts),'triples':int(len(T)),'separator_status':int(res.status),'separator_message':str(res.message),
         'counterexample_found':separated is not None,'conclusive_for_selected_design':separated is not None}
    if separated is None:
        out.update(n3=None,witness=None,interpretation='No feasible incumbent returned within this job: inconclusive, not validation.')
    else:
        score,w=separated; assert score<=2 and balanced(w)
        out.update(n3=int(score),witness=[[int(x) for x in g] for g in w])
    return out

def merge(paths):
    rows=sorted([json.loads(p.read_text()) for p in paths],key=lambda x:x['job'])
    assert len(rows)==JOBS and [x['job'] for x in rows]==list(range(JOBS))
    found=[x for x in rows if x['counterexample_found']]; unique={}
    for r in found:
        assert r['n3']<=2 and balanced(r['witness']); unique.setdefault(witness_key(r['witness']),r['witness'])
    merged={'packet':'H237','method':'44_actual_H235_shift_designs_unrestricted_exact_n3_le_2_separation','source_packet':'H235',
            'selected_actual_designs':JOBS,'counterexamples_found':len(found),'inconclusive_jobs':JOBS-len(found),
            'unique_balanced_counterexamples':len(unique),'all_selected_designs_broken':len(found)==JOBS,
            'source_h235_quotient_states':EXPECTED_STATES,'source_h235_exact_surviving_coefficient_states':EXPECTED_SURVIVORS,
            'source_h235_exact_surviving_shift_tuples':EXPECTED_SHIFT_TUPLES,'jobs':rows,
            'interpretation':'Returned witnesses exactly break selected H235 designs and are reusable cuts; feed new witnesses into another family-wide rescreen.'}
    wp={'packet':'H237','source':'H235 first exact survivor from each of 44 sector×chunk jobs','witness_count':len(unique),
        'witnesses':list(unique.values()),'validity':'Every stored witness is balanced 4+4+4+4+4 and returned by unrestricted exact n3<=2 MILP separation.'}
    return merged,wp

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--job',type=int); ap.add_argument('--time-limit',type=float,default=180.0); ap.add_argument('--merge-dir',type=Path); a=ap.parse_args()
    if a.job is not None:
        out=solve_job(a.job,a.time_limit); OUTDIR.mkdir(parents=True,exist_ok=True); p=OUTDIR/f'job_{a.job:02d}.json'; p.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='witness'},indent=2)); return
    assert a.merge_dir is not None
    merged,wp=merge(sorted(a.merge_dir.rglob('job_*.json'))); MERGED.write_text(json.dumps(merged,indent=2)+'\n'); NEW_WITNESSES.write_text(json.dumps(wp,indent=2)+'\n'); print(json.dumps({k:v for k,v in merged.items() if k!='jobs'},indent=2))
if __name__=='__main__': main()

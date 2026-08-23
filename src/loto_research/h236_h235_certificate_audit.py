"""Auxiliary H235 certificate audit (not a numbered research packet).

Parses the committed H235 merged artifact, independently checks the complete
44-shard / 11-sector partition, and recomputes decisive totals from leaf chunks.
The compact summary is a provenance gate for H237. H236 remains reserved for the
separate RI Lucky 3 Spot research packet.
"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'data'/'derived'/'h235_h234_augmented_exact_shift_rescreen.json'
OUT=ROOT/'data'/'derived'/'h236_h235_certificate_audit_summary.json'
EXPECTED_REPS=((1,1),(1,3),(1,5),(1,7),(1,9),(1,15),(3,5),(3,9),(3,13),(5,9),(7,9))
EXPECTED_STATES=(7806,23052,23052,23052,23052,23052,45760,23052,45760,23052,45760)
EXPECTED_TOTAL=306450

def bounds(n,c): return n*c//4,n*(c+1)//4

def audit():
    d=json.loads(SRC.read_text()); assert d['packet']=='H235' and d['chunk_shards']==44
    sectors=d['sectors']; assert len(sectors)==11
    leaf_states=leaf_env=leaf_exact=leaf_tuples=0; signatures=set(); meta=set(); pairs=[]; ss=[]
    for si,sec in enumerate(sectors):
        assert sec['sector_index']==si and tuple(sec['representative'])==EXPECTED_REPS[si]
        assert sec['quotient_coefficient_states']==EXPECTED_STATES[si] and len(sec['chunks'])==4
        a=b=c=e=0
        for ci,ch in enumerate(sec['chunks']):
            assert ch['packet']=='H235' and (ch['sector_index'],ch['chunk_index'])==(si,ci)
            assert tuple(ch['representative'])==EXPECTED_REPS[si] and ch['sector_total_quotient_states']==EXPECTED_STATES[si]
            lo,hi=bounds(EXPECTED_STATES[si],ci); assert (ch['chunk_start'],ch['chunk_stop'])==(lo,hi)
            assert ch['chunk_quotient_states']==hi-lo; pairs.append((si,ci))
            a+=ch['chunk_quotient_states']; b+=ch['envelope_survivor_states']; c+=ch['exact_shift_surviving_coefficient_states']; e+=ch['exact_surviving_shift_tuples']
            signatures.add(ch['general_signature_unique_witnesses'])
            meta.add((ch['base_expanded_witness_instances'],ch['h234_raw_witnesses'],ch['h234_affine_expanded_instances'],ch['augmented_witness_instances_before_signature_dedupe'],ch['h185_stored'],ch['h186_witnesses']))
        assert a==EXPECTED_STATES[si] and b==sec['envelope_survivor_states'] and c==sec['exact_shift_surviving_coefficient_states'] and e==sec['exact_surviving_shift_tuples']
        leaf_states+=a; leaf_env+=b; leaf_exact+=c; leaf_tuples+=e
        ss.append({'sector_index':si,'representative':list(EXPECTED_REPS[si]),'quotient_states':a,'envelope_survivors':b,'exact_coefficient_survivors':c,'exact_shift_tuple_survivors':e})
    assert pairs==[(s,c) for s in range(11) for c in range(4)] and leaf_states==EXPECTED_TOTAL
    assert (leaf_states,leaf_env,leaf_exact,leaf_tuples)==(d['quotient_coefficient_states_screened'],d['envelope_survivor_states'],d['exact_shift_surviving_coefficient_states'],d['exact_surviving_shift_tuples'])
    assert len(signatures)==1 and len(meta)==1
    assert d['all_general_cyclic_affine_designs_rejected_by_augmented_witnesses']==(leaf_exact==0)
    m=next(iter(meta))
    return {'packet':'H235-AUDIT','audit_target':'H235','audit':'independent_leaf_reaggregation_and_schema_partition_check','numbered_packet':False,
            'all_44_chunks_present_and_disjoint':True,'all_11_sector_totals_verified':True,'quotient_coefficient_states_verified':leaf_states,
            'envelope_survivor_states':leaf_env,'exact_shift_surviving_coefficient_states':leaf_exact,'exact_surviving_shift_tuples':leaf_tuples,
            'h225_general_cyclic_affine_family_closed':leaf_exact==0,'general_signature_unique_witnesses':next(iter(signatures)),
            'base_expanded_witness_instances':m[0],'h234_raw_witnesses':m[1],'h234_affine_expanded_instances':m[2],
            'augmented_witness_instances_before_signature_dedupe':m[3],'pre_h186_bank_size':m[4],'h186_witnesses':m[5],'sectors':ss,
            'interpretation':'Auxiliary independent audit only. Zero exact survivors would certify H225 at H235; positive survivors remain unresolved.'}

def main():
    out=audit(); OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); print('RESULT_FILE',OUT)
if __name__=='__main__': main()

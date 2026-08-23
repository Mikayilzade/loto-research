"""H226 exact coefficient-envelope pre-screen for the H225 general cyclic-affine family.

For A support (0,1,2), a general layer is z=a*x+b*y+c mod16 with odd a,b.
H225 normalization fixes B=(1,beta,0), C=(1,gamma,0), D=(1,1,0), beta<=gamma.

Key theorem: before choosing A shifts, fix only the multiset of three A coefficient
pairs (a,b). For every balanced witness row, maximize A incidence over all legal
*distinct* shifts inside those coefficient blocks. If even this optimistic rowwise
maximum plus fixed B/C/D incidence is <3 on one witness, then every shift realization
of that coefficient multiset is impossible. This rejects whole H225 sectors safely.

Repeated coefficient blocks are handled with top-2/top-3 distinct shifts, so the
bound respects the requirement that the three A layers are distinct.
"""
from __future__ import annotations

import base64, json, zlib
from itertools import combinations_with_replacement
from pathlib import Path
import numpy as np

from loto_research.h183_h180_symmetry_persistent_cuts import load_witness_bank as load_h183_bank
from loto_research.h185_h180_affine_orbit_cut_acceleration import ODDS, load_bank as load_h185_bank
from loto_research.h186_h185_mass_counterexample_packet import load as load_h186

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h226_general_coefficient_envelope.json'
H184_DELTA=ROOT/'data'/'derived'/'h184_h183_new_witnesses.json'
ORBIT_START=254
ODD=tuple(int(x) for x in ODDS)
COEFFS=tuple((a,b) for a in ODD for b in ODD)  # 64 blocks, each 16 shifts
BC_SECTORS=tuple((be,ga) for i,be in enumerate(ODD) for ga in ODD[i:])


_WITNESS_SOURCE='uninitialized'


def _validate_balanced_bank(bank,expected):
    if len(bank)!=expected:
        raise ValueError(f'unexpected witness count {len(bank)} != {expected}')
    for wi,w in enumerate(bank):
        if len(w)!=5:
            raise ValueError(f'witness {wi} has {len(w)} groups')
        for gi,grp in enumerate(w):
            vals=[int(x) for x in grp]
            if len(vals)!=4 or len(set(vals))!=4 or any(x<0 or x>=16 for x in vals):
                raise ValueError(f'witness {wi} group {gi} is not a balanced 4-subset')
    return bank


def _load_pre_h186_bank():
    """Load H185 when intact; otherwise use a named, exact safe recovery subset.

    The historical H185 blob in some research-work commits is corrupted. H232 does
    not require those exact 297 witnesses: any balanced draws are valid necessary
    tests for a universal n3>=3 design. The fallback therefore keeps the intact
    H183 base plus H184 exact delta and lets H186 add its own verified witnesses.
    It never fabricates or relabels H186 witnesses as historical H185 data.
    """
    global _WITNESS_SOURCE
    try:
        bank=_validate_balanced_bank(load_h185_bank(),297)
        _WITNESS_SOURCE='h185_297'
        return bank
    except (ValueError, OSError, json.JSONDecodeError, zlib.error) as exc:
        h183=_validate_balanced_bank(load_h183_bank(),254)
        h184=json.loads(H184_DELTA.read_text())
        if h184.get('packet')!='H184' or h184.get('base_cut_count')!=254 or h184.get('new_cut_count')!=1:
            raise ValueError('invalid H184 recovery delta metadata') from exc
        delta=_validate_balanced_bank(h184.get('witnesses',[]),1)
        bank=h183+delta
        _validate_balanced_bank(bank,255)
        _WITNESS_SOURCE='h183_254_plus_h184_1_recovery'
        return bank


def witness_source():
    return _WITNESS_SOURCE


def expand_witnesses():
    pre= _load_pre_h186_bank(); h186=load_h186()
    h186_w=[x['witness'] for x in h186['start_witnesses']]
    h186_w += [x['witness'] for x in h186['second_witnesses']]
    _validate_balanced_bank(h186_w,189)
    ws=[pre[i] for i in range(ORBIT_START)]
    for w in list(pre[ORBIT_START:])+h186_w:
        for u in ODD:
            for v in range(16):
                ws.append([[(u*int(x)+v)%16 for x in grp] for grp in w])
    return np.asarray(ws,dtype=np.int16),len(pre),len(h186_w)


def support_hits_general(W,i,j,k,a,b,c):
    """Exact incidence for one affine layer across every witness instance."""
    xs=W[:,i,:]; ys=W[:,j,:]; target=W[:,k,:]
    vals=(a*xs[:,:,None]+b*ys[:,None,:]+c)%16
    return (vals[:,:,:,None]==target[:,None,None,:]).sum(axis=(1,2,3)).astype(np.uint8)


def unique_witness_signature_data(W):
    """Deduplicate witnesses by all data needed by H226, not by restricted rows."""
    # A hits: N x 64 x 16.
    N=len(W)
    A=np.empty((N,64,16),dtype=np.uint8)
    for p,(a,b) in enumerate(COEFFS):
        for c in range(16):
            A[:,p,c]=support_hits_general(W,0,1,2,a,b,c)

    # Fixed normalized supports. B beta varies; C gamma varies; D fixed identity.
    B=np.stack([support_hits_general(W,0,3,4,1,be,0) for be in ODD],axis=1)
    C=np.stack([support_hits_general(W,1,3,4,1,ga,0) for ga in ODD],axis=1)
    D=support_hits_general(W,2,3,4,1,1,0)[:,None]

    # Exact dedupe on concatenated signature. This may be >=4878 because general
    # A/B/C incidences distinguish witnesses collapsed by the old diagonal rows.
    sig=np.concatenate([A.reshape(N,-1),B,C,D],axis=1)
    _,idx=np.unique(sig,axis=0,return_index=True)
    idx=np.sort(idx)
    return A[idx],B[idx],C[idx],D[idx,0]


def bytes_mask(cond):
    """Pack a boolean witness vector into bytes; exact and JSON-friendly via base64."""
    return base64.b64encode(np.packbits(cond.astype(np.uint8),bitorder='little').tobytes()).decode()


def pattern_upper(top,p,q,r):
    # top shape rows x 64 x 3, descending distinct-shift incidences.
    if p==r:  # p=p=p
        return top[:,p,0]+top[:,p,1]+top[:,p,2]
    if p==q:  # p=p<r
        return top[:,p,0]+top[:,p,1]+top[:,r,0]
    if q==r:  # p<q=q
        return top[:,p,0]+top[:,q,0]+top[:,q,1]
    return top[:,p,0]+top[:,q,0]+top[:,r,0]


def run():
    W,h185_n,h186_n=expand_witnesses()
    A,B,C,D=unique_witness_signature_data(W)
    rows=len(A)
    # Sort 16 shift incidences and retain exact top three distinct shifts.
    top=np.sort(A,axis=2)[:,:,-3:][:,:,::-1]
    patterns=list(combinations_with_replacement(range(64),3))
    assert len(patterns)==45760

    # For every B/C sector, build three witness masks keyed by required A incidence.
    sector_need=[]
    for be,ga in BC_SECTORS:
        bi=ODD.index(be); gi=ODD.index(ga)
        bcd=B[:,bi]+C[:,gi]+D
        need=np.maximum(0,3-bcd.astype(np.int16)).astype(np.uint8)
        sector_need.append((need>=1,need>=2,need>=3))

    counts=np.zeros(len(BC_SECTORS),dtype=np.int64)
    surviving_examples=[[] for _ in BC_SECTORS]
    pattern_hist={}
    # Cheap exact screen: one vector upper bound per coefficient multiset, then 36 sectors.
    for p,q,r in patterns:
        ub=pattern_upper(top,p,q,r)
        lt1=ub<1; lt2=ub<2; lt3=ub<3
        nsec=0
        for s,(n1,n2,n3) in enumerate(sector_need):
            killed=bool(np.any(lt1 & n1) or np.any(lt2 & n2) or np.any(lt3 & n3))
            if not killed:
                counts[s]+=1; nsec+=1
                if len(surviving_examples[s])<20:
                    surviving_examples[s].append([p,q,r])
        pattern_hist[str(nsec)]=pattern_hist.get(str(nsec),0)+1

    out={
        'packet':'H226',
        'method':'exact_rowwise_distinct_shift_coefficient_envelope',
        'expanded_witness_instances':int(len(W)),
        'general_signature_unique_witnesses':int(rows),
        'h185_stored':int(h185_n),'h186_witnesses':int(h186_n),
        'witness_source':witness_source(),
        'coefficient_blocks':64,'shifts_per_block':16,
        'coefficient_multisets':len(patterns),
        'bc_sectors':len(BC_SECTORS),
        'sector_labels':[[be,ga] for be,ga in BC_SECTORS],
        'surviving_coefficient_multisets_by_sector':[int(x) for x in counts],
        'total_sector_pattern_survivors':int(counts.sum()),
        'pattern_survival_sector_histogram':pattern_hist,
        'first_surviving_patterns_by_sector':surviving_examples,
        'interpretation':'Every rejected coefficient multiset has an explicit stored balanced witness on which even the best legal distinct A shifts cannot reach n3=3. Survivors still require exact shift-level screening and exact n3<=2 separation.',
    }
    return out


def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='first_surviving_patterns_by_sector'},indent=2))
    print('RESULT_FILE',OUT)

if __name__=='__main__': main()

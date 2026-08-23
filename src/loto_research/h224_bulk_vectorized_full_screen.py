"""H224: bulk-vectorized exact H175 restricted-family screen.

Scientific predicate is unchanged from H219/H222/H223. The computational
bottleneck is moved: instead of rebuilding each active witness row separately,
we expand witnesses once and compute the 512 layer-incidence columns in batches.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
import numpy as np

from loto_research.h185_h180_affine_orbit_cut_acceleration import (
    ODDS, PARAMS, SUPPORTS, load_bank as load_h185_bank,
)
from loto_research.h186_h185_mass_counterexample_packet import load as load_h186
from loto_research.h212_h175_affine_unit_orbits import enumerate_orbits

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data' / 'derived' / 'h224_bulk_vectorized_survivors.json'
ORBIT_START = 254
BC_PAIRS = [(16*i,16*j) for i in range(8) for j in range(i,8)]
BATCH = 256


def expand_witnesses():
    h185 = load_h185_bank()
    h186 = load_h186()
    h186_w = [x['witness'] for x in h186['start_witnesses']]
    h186_w += [x['witness'] for x in h186['second_witnesses']]

    ws = [h185[i] for i in range(ORBIT_START)]
    seeds = list(h185[ORBIT_START:]) + h186_w
    for w in seeds:
        for u in ODDS:
            uu = int(u)
            for v in range(16):
                ws.append([[(uu*int(x)+v) % 16 for x in grp] for grp in w])
    W = np.asarray(ws, dtype=np.int16)
    assert W.ndim == 3 and W.shape[1:] == (5,4)
    return W, len(h185), len(h186_w)


def bulk_rows(W: np.ndarray) -> np.ndarray:
    """Compute exact incidence rows in batches, then deduplicate byte-identically."""
    a = PARAMS[:,0].astype(np.int16)
    b = PARAMS[:,1].astype(np.int16)
    c = PARAMS[:,2].astype(np.int16)
    chunks = []
    for lo in range(0, len(W), BATCH):
        wb = W[lo:lo+BATCH]
        parts = []
        for i,j,k in SUPPORTS:
            xs = wb[:,i,:]
            ys = wb[:,j,:]
            target = wb[:,k,:]
            vals = (
                a[None,:,None,None] * xs[:,None,:,None]
                + b[None,:,None,None] * ys[:,None,None,:]
                + c[None,:,None,None]
            ) % 16
            # Each target group has 4 distinct values, so summing equality over
            # target entries exactly counts selected (x,y) pairs hitting group k.
            hits = (vals[...,None] == target[:,None,None,None,:]).sum(axis=(2,3,4))
            parts.append(hits.astype(np.uint8))
        chunks.append(np.concatenate(parts, axis=1))
    all_rows = np.concatenate(chunks, axis=0)
    assert all_rows.shape[1] == 512
    # np.unique(axis=0) is an exact row-set operation; ordering is irrelevant.
    uniq = np.unique(all_rows, axis=0)
    return uniq.astype(np.uint8, copy=False)


def screen(R: np.ndarray) -> dict:
    assert R.shape == (4878,512), R.shape
    reps, orbit_sizes, exceptional = enumerate_orbits()
    assert len(reps) == 3992 and len(BC_PAIRS) == 36
    rr = np.asarray(reps, dtype=np.int16)
    A = R[:,rr[:,0]] + R[:,rr[:,1]] + R[:,rr[:,2]]
    survivors=[]; counts=[]
    for shard,(bb,cc) in enumerate(BC_PAIRS):
        bc = R[:,128+bb] + R[:,256+cc] + R[:,384]
        keep = np.all(A + bc[:,None] >= 3, axis=0)
        ids = np.flatnonzero(keep)
        counts.append(int(len(ids)))
        survivors.extend({
            'shard': shard, 'B': int(bb), 'C': int(cc),
            'A': [int(x) for x in reps[int(q)]]
        } for q in ids)
    return {
        'packet':'H224',
        'method':'bulk_vectorized_rows_plus_exact_full_screen',
        'exact_cut_rows':int(len(R)),
        'A_orbits':len(reps),
        'bc_classes':len(BC_PAIRS),
        'normalized_classes_screened':len(reps)*len(BC_PAIRS),
        'orbit_sizes':{str(k):int(v) for k,v in sorted(orbit_sizes.items())},
        'exceptional_a15_A_orbits':int(exceptional),
        'shard_survivor_counts':counts,
        'survivor_count':len(survivors),
        'survivors':survivors,
    }


def run():
    t0=time.perf_counter()
    W,h185_n,h186_n = expand_witnesses()
    t1=time.perf_counter()
    R = bulk_rows(W)
    t2=time.perf_counter()
    out = screen(R)
    t3=time.perf_counter()
    assert out['normalized_classes_screened'] == 143712
    assert out['survivor_count'] == sum(out['shard_survivor_counts'])
    out.update({
        'h185_stored':int(h185_n), 'h186_witnesses':int(h186_n),
        'expanded_witness_instances':int(len(W)), 'batch':BATCH,
        'seconds_expand':round(t1-t0,6), 'seconds_bulk_rows':round(t2-t1,6),
        'seconds_screen':round(t3-t2,6), 'seconds_total':round(t3-t0,6),
    })
    return out


def main():
    out=run()
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='survivors'},indent=2))
    print('RESULT_FILE', OUT)

if __name__=='__main__':
    main()

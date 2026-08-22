"""Verify H186 exact witness packet and reproduce safe affine-orbit cut counts."""
from __future__ import annotations
import base64, json, zlib
from collections import Counter
from pathlib import Path
import numpy as np
from loto_research.h185_h180_affine_orbit_cut_acceleration import PARAMS, SUPPORTS, ODDS

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'data'/'derived'/'h186_h185_counterexample_packet.zlib.b64'

def load():
    return json.loads(zlib.decompress(base64.b64decode(DATA.read_text().strip())))['h186']

def triples(chosen):
    out=[]
    for s,(i,j,k) in enumerate(SUPPORTS):
        for pid in chosen[s]:
            a,b,c=map(int,PARAMS[pid])
            for x in range(16):
                for y in range(16):
                    out.append((i*16+x,j*16+y,k*16+((a*x+b*y+c)%16)))
    return np.asarray(out,dtype=np.int16)

def score(T,w):
    S=np.zeros(80,dtype=bool)
    for g,grp in enumerate(w):
        for x in grp: S[g*16+x]=True
    return int(np.sum(S[T[:,0]] & S[T[:,1]] & S[T[:,2]]))

def row(w):
    parts=[]
    for i,j,k in SUPPORTS:
        xs=np.asarray(w[i],dtype=int); ys=np.asarray(w[j],dtype=int)
        target=np.zeros(16,dtype=np.int8); target[w[k]]=1
        vals=(PARAMS[:,0,None,None]*xs[None,:,None]+PARAMS[:,1,None,None]*ys[None,None,:]+PARAMS[:,2,None,None])%16
        parts.append(target[vals].sum(axis=(1,2)).astype(np.uint8))
    return np.concatenate(parts)

def orbit(w):
    for u in ODDS:
        for v in range(16):
            yield [[int((int(u)*x+v)%16) for x in grp] for grp in w]

def verify(candidate, items):
    T=triples(candidate); hist=Counter(); seen=set()
    for item in items:
        q=score(T,item['witness'])
        assert q==item['score'] and q<=2
        hist[q]+=1
        for wo in orbit(item['witness']): seen.add(bytes(row(wo)))
    return hist,seen

def main():
    d=load()
    h1,r1=verify(d['start_candidate_ids'],d['start_witnesses'])
    h2,r2=verify(d['second_candidate_ids'],d['second_witnesses'])
    print('packet_A_hist',dict(h1),'rows',len(r1))
    print('packet_B_hist',dict(h2),'union_rows',len(r1|r2))
    assert len(r1)==d['new_only_affine_unique_rows_after_start']==14872
    assert len(r1|r2)==d['new_only_affine_unique_rows_after_second']==18952
    print('VERIFIED')

if __name__=='__main__': main()

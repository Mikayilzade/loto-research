from __future__ import annotations
import itertools, json
from math import comb

MOD=16
ODDS=(1,3,5,7,9,11,13,15)
PARAMS=[(a,c) for a in ODDS for c in range(16)]
PERMS=list(itertools.permutations(range(3)))

def triples(a:int,c:int):
    return frozenset((x,y,(a*x+a*y+c)%MOD) for x in range(MOD) for y in range(MOD))

def main():
    layers={p:triples(*p) for p in PARAMS}
    lookup={s:p for p,s in layers.items()}
    preserved={}
    for perm in PERMS:
        ok=[]
        for p,s in layers.items():
            image=frozenset(tuple(t[i] for i in perm) for t in s)
            if image in lookup:
                ok.append((p,lookup[image]))
        preserved[str(perm)]=ok

    exceptional=[p for p in PARAMS if all(p in dict(preserved[str(perm)]) for perm in PERMS)]
    assert exceptional==[(15,c) for c in range(16)]
    all_a_sets=comb(128,3)
    exceptional_sets=comb(16,3)
    generic_sets=all_a_sets-exceptional_sets
    h188=all_a_sets*36
    safe=generic_sets*36+exceptional_sets*15
    out={
        'preserved_layer_counts':{k:len(v) for k,v in preserved.items()},
        'fully_s3_invariant_layers':exceptional,
        'all_A_sets':all_a_sets,
        'generic_C2_A_sets':generic_sets,
        'exceptional_S3_A_sets':exceptional_sets,
        'h188_representatives':h188,
        'stabilizer_aware_representatives':safe,
        'saving':h188-safe,
        'saving_fraction':(h188-safe)/h188,
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()

"""H190: audit H189's claimed full S3 symmetry of diagonal support A.

A layer is the set of triples (x0,x1,x2) satisfying
    x2 = a*x0 + a*x1 + c (mod 16)
with odd a.  A coordinate permutation is a valid WLOG symmetry for the
restricted diagonal family only if every such layer is mapped back into this
same 128-layer family.
"""
from itertools import permutations
import json
from pathlib import Path

ODDS = (1,3,5,7,9,11,13,15)
MOD = 16
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h190_a_support_s3_symmetry_audit.json"

def layer(a,c):
    return frozenset((x,y,(a*x+a*y+c)%MOD) for x in range(MOD) for y in range(MOD))

def main():
    layers={(a,c):layer(a,c) for a in ODDS for c in range(MOD)}
    reverse={s:p for p,s in layers.items()}
    rows=[]
    for perm in permutations(range(3)):
        preserved=[]
        for par,s in layers.items():
            image=frozenset(tuple(t[i] for i in perm) for t in s)
            if image in reverse:
                preserved.append((par,reverse[image]))
        rows.append({
            "permutation": list(perm),
            "diagonal_layers_preserved": len(preserved),
            "preserved_a": sorted({p[0][0] for p in preserved}),
            "is_global_symmetry": len(preserved)==len(layers),
        })
    payload={
        "family_size":len(layers),
        "result":rows,
        "global_symmetry_permutations":[r["permutation"] for r in rows if r["is_global_symmetry"]],
        "conclusion":"Only identity and swap of the two A inputs preserve the full restricted diagonal A family. Full S3 is not a WLOG symmetry.",
    }
    OUT.write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps(payload,indent=2))

if __name__=="__main__":
    main()

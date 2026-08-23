# H228 append — 2026-08-23

- Scope: H175 Rhode Island Keno / H225 general cyclic-affine family only.
- Audited H227's cross-sector quotient. Found a rigor issue: canonicalizing beta/gamma to an unordered pair after every S3xS2 image is not itself a valid 12-element group action because the swap subgroup is not normal in S3.
- Corrected method: act on all 64 ordered normalized sectors first. Exact ordered orbit count remains 11, with the same representative labels, so H227's 11-sector WLOG existence-search reduction survives.
- Correct ordered sector orbit sizes: `1,6,6,3,3,3,12,6,12,6,6`; stabilizers: `12,2,2,4,4,4,1,2,1,2,2`.
- Derived exact induced action on the 64 A coefficient pairs `(a,b)` from permutations of `(a,b,-1)` and quotient all 45,760 3-multisets under each true sector stabilizer.
- Exact total coefficient-multiset quotient states across the 11 representative sectors: **306,450**, versus 503,360 raw representative-sector patterns and 1,647,360 original 36-sector patterns.
- Safe workload reductions: **1.64255x** beyond H227 and **5.37562x** versus H226 raw sector-pattern workload.
- This is WLOG pruning, not a universal construction/impossibility proof. H226 envelope + shift-level exact separation remain required.
- Status: **NO SUCCESS; NOT EXHAUSTED**.

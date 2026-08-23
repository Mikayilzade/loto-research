# H211 — H175 combined residual-translation + stabilizer quotient

Status: **validated exact reduction; no terminal success**.

## Question
Can H210's exact residual `C16` translation quotient be safely combined with H191's exceptional S3 stabilizer saving for the restricted H175 diagonal family?

## Inputs
- H188 normalized family: `12,289,536` representatives.
- H210 residual translation action is free on every 3-element A-layer subset, giving `21,336` A-orbits and `768,096` total representatives before H191's exceptional stabilizer saving.
- H191 proved that only layers with coefficient `a=15` are fully S3-compatible. A 3-element A subset wholly inside those 16 layers can use 15 B/C coefficient classes instead of 36.

## Exact combination
H210 translations preserve the coefficient `a`; on the `a=15` sector they act on shifts by

`c -> c + (2*15-1)t = c + 13t (mod 16)`.

Since 13 is invertible modulo 16, this is an ordinary cyclic translation action on the 16 shifts. As in H210, no nonidentity element can fix a 3-element subset, so the action is free on `C(16,3)=560` exceptional A subsets.

Thus:
- exceptional translation orbits: `560 / 16 = 35`;
- generic A subsets: `C(128,3)-C(16,3)=340,816`;
- generic translation orbits: `340,816 / 16 = 21,301`.

Apply H191's B/C class counts inside these disjoint sectors:

`21,301 * 36 + 35 * 15 = 767,361`.

## Result
The exact safe restricted-family search checkpoint improves from H210's `768,096` to **767,361** representatives, an additional 735-class reduction. Relative to H188 this is a reduction factor of about 16.016x.

This does **not** prove universal `n3>=3`, nor impossibility of the restricted family. The next high-value step remains direct enumeration/canonicalization of these 767,361 classes against the accumulated exact balanced witness bank, followed by exact separation only for survivors.

Reproducer: `src/loto_research/h211_combined_translation_stabilizer_quotient.py`.

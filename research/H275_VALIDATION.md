# H275 VALIDATION — Singapore TOTO cascade/full-cover bound

Validated: 2026-08-25
Status: **PASS — arithmetic and structural rejection gates verified**

## Independent checks
1. Main-space size: `C(49,6) = 13,983,816`.
2. Ordinary entry cost checked against current Singapore Pools how-to-play / bet-type pages: SGD 1.
3. Exact fixed-tier full-cover counts recomputed combinatorially:
   - G5: `C(6,4)C(42,2) = 12,915`;
   - G6: `C(6,3)C(42,2) = 17,220`;
   - G7: `C(6,3)C(42,3) = 229,600`.
4. Fixed-tier gross recomputed: `12,915×50 + 17,220×25 + 229,600×10 = SGD 3,372,250`.
5. Cost = SGD 13,983,816; fixed-tier return = **24.11537737624694%**; deficit = **SGD 10,611,566**.
6. Structural cascade gate checked: every purchased six-number line is itself a legal Group-1 draw outcome, so no nonempty portfolio can guarantee `no Group 1` for every draw.
7. Full-cover gate checked: complete `C(49,6)` ownership contains the winning six-number selection for every possible draw and therefore necessarily creates a Group-1 winning share, preventing the no-G1 cascade trigger.
8. Duplicate-stress gate checked from current rules: Groups 1–4 are shared by winning shares; no useful hard external-share cap/reservation was established. Strict guarantee therefore cannot rely on a positive share of those pools.

## Source consistency
- Singapore Pools current rules index lists TOTO rules.
- GRA search lists TOTO Game Rules effective 11 Aug 2026.
- Singapore Pools current FAQ describes cascade after the configured no-winner sequence and payment to the next winning prize group.
- 20 Aug 2026 official result shows Group 1 unwon and SGD 2,953,462 snowballed, confirming live operation of the mechanism.

## Validation conclusion
H275 does **not** prove that every possible TOTO betting strategy is unprofitable. It rigorously closes the specific strict-guarantee lane tested here: forcing cascade via a nonempty portfolio and/or taking over the complete six-number space while relying on cascade/shared-pool value.

Files validated:
- `src/loto_research/h275_singapore_toto_cascade_bound.py`
- `data/derived/h275_singapore_toto_cascade_bound.json`
- `research/h275_singapore_toto_cascade_bound.md`

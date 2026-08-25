# H264 validation — Uganda LOTTO fixed-tier / roll-down screen

Validated 2026-08-25 against the current published Uganda National Lottery LOTTO rules v1.6 and an independent exact combinatorial recomputation.

## Rule gates
- Game matrix: 6/52 plus bonus; UGX 1,000 per entry.
- Participant daily LOTTO wager cap: UGX 500,000.
- Divisions 1–6: pari-mutuel.
- Division 7 Match 3: fixed UGX 10,000 per winning entry.
- Division 8 Match 2 + Bonus: fixed UGX 4,000 per winning entry.
- Rule 6.5.3: if Division 6 has no winner, its accumulated fund rolls to Division 1 of the next draw, not fixed Division 7.
- Rules 7.2 and 7.3: special Division-1 roll-down explicitly excludes fixed payout divisions.

Primary official source:
https://www.nationallottery.go.ug/assets/documents/LOTTO_RULES_AND_REGULATIONS.pdf

## Exact arithmetic gates
- `C(52,6) = 20,358,520` one-copy full-cover entries.
- Full-cover cost = UGX 20,358,520,000.
- Match-3 count for every draw = `C(6,3) C(45,3) = 283,800`.
- Match-2+Bonus count for every draw = `C(6,2) C(45,3) = 212,850`.
- Fixed Match-3 gross = UGX 2,838,000,000.
- Fixed Match-2+Bonus gross = UGX 851,400,000.
- Total fixed-tier gross = UGX 3,689,400,000.
- Fixed-tier return ratio = **0.1812214247401088 = 18.1221424740%**.

## Conclusion
The candidate fails the targeted mechanism structurally, before any coverage optimization: accumulated jackpot/pari-mutuel money is prohibited from entering the fixed payout divisions under the current special roll-down rules. The two fixed tiers alone return only 18.1221% under exact one-copy full coverage.

Status: **CLOSED / REJECTED for fixed-per-winning-selection external subsidy under current v1.6 rules.**

Reopen only on a material official rule/promotion change that routes deterministic external funds into Divisions 7 or 8.

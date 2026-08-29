# H351 VALIDATION

Independent arithmetic checks:

- `C(44,6)=7,059,052`; at $2, exact cover cost = **$14,118,104**.
- Hypergeometric partition `sum_k C(6,k)C(38,6-k)` = **7,059,052**, so no state-count gap.
- Match-5 count 228; Match-4 10,545; Match-3 168,720.
- Fixed lower payout = `228*5000 + 10545*200 + 168720*4 = $3,923,880`.
- Advertised $28.6m jackpot with no external duplicate gives nominal gross **$32,523,880 > cost**.
- Stronger-than-real stress jackpot grants the portfolio its entire purchase cost back into the jackpot: `$28,600,000 + $14,118,104 = $42,718,104`.
- With four external jackpot duplicates, five winning jackpot tickets share that amount. Gross upper bound = `$3,923,880 + $42,718,104/5 = $12,467,500.80`, below cost by **$1,650,603.20**.
- Current rules explicitly permit jackpot sharing among multiple winning ticket holders and no checked rule hard-caps external duplicate count below four.

Validation result: **CLOSED AS STRICT GUARANTEE**.

Arithmetic inconclusive: **0**.  
Closure-relevant inconclusive: **0**.

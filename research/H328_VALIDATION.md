# H328 VALIDATION

Date: 2026-08-28

Independent arithmetic validation for `h328_botb_carnival_pass_gate`.

Inputs copied from the checked live BOTB Carnival page:
- N = 999,999 maximum ticket identifiers;
- instant prizes won = 4,761;
- instant prizes left = 195,204;
- paid ticket price = £1.29;
- separate end prize = £2,000.

Recomputed totals:
- prize-bearing support represented by snapshot = `4,761 + 195,204 = 199,965`;
- zero-instant support = `999,999 - 199,965 = 800,034`;
- full paid acquisition = `999,999 × 1.29 = £1,289,998.71`.

Subsidy stress validation:
- actual documented Ultimate-plan Instant Win allocation in the secondary product-design record = 15;
- H328 intentionally strengthens this to 209 tickets by pretending every monthly Ultimate entry can be redirected into the same Instant Wins pool;
- `800,034 >= 209`, therefore an allocation of 209 entirely zero-instant IDs exists;
- BOTB's own current help/content states Instant Win IDs are randomly generated after checkout, so the player cannot target prize IDs;
- separate end draw retains legal external winners because 209 << 999,999.

Zero-inconclusive condition:
The closure proof does not require knowing which exact zero IDs remain unsold, the value of individual instant prizes, or the precise current Pass checkout price. It only needs the finite support count and post-checkout random allocation. Under the deliberately stronger 209-entry grant, a complete zero-instant allocation remains legal. Thus there is no unresolved branch needed for the H328 conclusion.

Validated result: **strict guaranteed withdrawable-cash floor = £0; H328 CLOSED for the checked Carnival × documented Pass route.**

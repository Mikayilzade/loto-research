# H197 — Rhode Island first-deposit-match Keno bound

Updated: 2026-08-23
Status: **NO SUCCESS**
Scope: LOTTERY ONLY

## Target
Test the currently advertised Rhode Island Lottery **50% First-Time Deposit Match** as a deterministic lottery-specific subsidy, especially against the open Rhode Island Keno coverage branch.

## Fresh official evidence
- The current Rhode Island Lottery homepage still advertises **First Deposit match** in August 2026.
- The official promotion rules state the offer began 2025-03-10 and continues until an end date is posted with advance notice.
- Eligible first-time Plus-member deposits receive **50% iLottery Bonus Money up to $50**; a $100 initial deposit therefore maximizes the bonus at $50.
- Bonus Money may be played on **online Keno or eInstants**, cannot itself be withdrawn, and expires after seven days.
- Current iLottery Terms (updated 2026-07-14) state that player deposits generally **may not be withdrawn**; only iLottery winnings may be withdrawn. They also state promotional offers are discretionary and may be cancelled without notice.

Official sources:
- Current homepage: https://www.rilot.com/en-us/home.html
- First-Time Deposit Match rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/First-Time-Deposit_Match-RULES-MAR2025.pdf
- Current iLottery Terms / registration page: https://www.rilot.com/en-us/registration.html

## Exact H173 subsidy bound
The already-validated H173 3-spot cover costs **$4,560** at $1 per wager.

With a true pre-draw 2x entitlement, its worst-case gross is **109.6491%**, approximately **$5,000**. Without that doubler, the ordinary Keno floor is exactly half, approximately **$2,500 = 54.82456%** of face spend.

The first-deposit promotion can contribute at most **$50** of Bonus Money regardless of how much cash is deposited. Thus the minimum external cash needed to fund the ordinary $4,560 H173 basket is at least:

`4560 - 50 = $4,510`.

Worst-case withdrawable lottery winnings remain about **$2,500**, so the guaranteed cash result is at most:

`2500 - 4510 = -$2,010`.

Equivalently, the promotion offsets only **1.0965%** of H173 face cost, while ordinary H173 needs about **45.1754%** external subsidy to reach break-even without the 2x multiplier.

Therefore the current first-deposit match is nowhere near strong enough to replace the missing deterministic 2x Keno overlay.

## Why the headline 50% match is not a 1.5x cash bankroll
The $100 deposited principal is not freely recoverable cash: current Terms say player deposits may not be withdrawn, while Bonus Money also cannot be withdrawn. Both must be converted through lottery play before winnings become withdrawable. So treating `$100 deposit + $50 bonus` as a risk-free $150 cash bankroll would be incorrect.

Even conditional on the bonus already being credited, the H173 arithmetic above remains strongly negative without a separate prize doubler.

## Guarantee gate
Before bonus credit, the current general Terms also make promotional entitlement discretionary/cancellable. That independently prevents treating the advertised match itself as an unconditional pre-deposit guarantee. This is secondary to the stronger arithmetic closure: even granting the full $50 bonus, it does not make ordinary H173 profitable.

## Result
**ЕЩЁ НЕ УСПЕХ.** Current RI 50% First-Time Deposit Match is a real Keno-eligible subsidy, but its hard $50 cap leaves ordinary H173 at roughly **-$2,010 guaranteed cash**; it cannot substitute for the unresolved pre-draw 2x doubler.
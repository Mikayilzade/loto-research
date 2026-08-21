# H157 — BCLC Keno Value Bundle deterministic subsidy threshold

Updated: 2026-08-21
Status: **MECHANISM VALIDATED / NO CURRENT QUALIFYING BUNDLE FOUND / NOT SUCCESS**

## Question
H156 showed that random Doubler/Tripler messages do not create a strict player-owned cover subsidy. BCLC's current Keno game conditions contain a different mechanism: **Keno Value Bundles**, where a player purchases `X` advance draws and receives `Y` free draws. Because the free draws are attached to the purchaser's own ticket, this solves the Nth-ticket/random-ownership problem if a sufficiently generous bundle is active.

Primary sources:
- BCLC current Keno game conditions (July 2025 revision, current in 2026): https://corporate.bclc.com/content/dam/bclccorporate/documents/terms-and-conditions/rules-and-regulations/lotto/keno-keno-bonus-game-conditions.pdf
- Current BCLC Keno play/paytable: https://www.playnow.com/keno/learn/
- Current 2026 retail promotion: Keno Doubler, July 27–September 7, 2026: https://www.bclcretailerhub.com/content/dam/retailerhub/promotions/2026/Keno_Doubler_Jul_2026_RIS.pdf

## Official mechanism
The BCLC game conditions expressly define Keno Value Bundles as the opportunity to purchase `X` advance-buy draws and receive `Y` free draws, with `X` and `Y` determined by BCLC during temporary promotion periods. The same conditions distinguish this from the free Doubler/Tripler, which is randomly assigned.

Therefore a Value Bundle is structurally superior for strict coverage: the subsidy is deterministic **after the bundle terms are announced** and belongs to the player's ticket.

## Exact deterministic coverage math
For an 80-number Keno draw with 20 drawn numbers, buy every `k`-subset once for one draw. For a realized draw, the number of purchased tickets matching exactly `j` numbers is

`C(20,j) * C(60,k-j)`.

Using the current BCLC fixed Keno paytable, the exact full-cover ratios are:

| Spot | Full-cover tickets | Guaranteed gross / draw | Base cover ratio | Free/paid ratio needed to exceed 100% |
|---:|---:|---:|---:|---:|
| 1 | 80 | 40 | 50.0000% | >100.0000% |
| 2 | 3,160 | 1,900 | **60.1266%** | **>66.3158%** |
| 3 | 82,160 | 51,300 | **62.4391%** | **>60.1559%** |
| 4 | 1,581,580 | 920,550 | 58.2045% | >71.8082% |
| 5 | 24,040,016 | 16,148,100 | **67.1718%** | **>48.8721%** |
| 6 | 300,500,200 | 186,541,050 | 62.0768% | >61.0907% |
| 7 | 3,176,716,400 | 2,035,566,900 | 64.0777% | >56.0605% |
| 8 | 28,987,537,150 | 17,210,941,950 | 59.3736% | >68.4250% |
| 9 | 231,900,297,200 | 140,397,957,800 | 60.5424% | >65.1736% |
| 10 | 1,646,492,110,120 | 1,051,062,624,842 | 63.8365% | >56.6502% |

For a bundle with `X` paid and `Y` free draws, assuming the same complete cover is valid for all included draws,

`R_bundle = r * (X + Y) / X = r * (1 + Y/X)`.

Strict pre-tax overlay requires `Y/X > 1/r - 1`.

## Executable-sized candidates
### Pick 2
Base cover: 3,160 tickets, gross 1,900 per draw, `r=0.6012658228`.

- `buy 2 get 1`: `R=0.9018987342` — negative.
- `buy 3 get 2`: `R=1.0021097046` — **+0.21097% conditional overlay**.
- `buy 1 get 1`: `R=1.2025316456` — **+20.2532% conditional overlay**.

Thus a future BCLC Value Bundle of at least **2 free per 3 paid** already crosses break-even for Pick 2, before tax/friction.

### Pick 3
Base cover: 82,160 tickets, gross 51,300 per draw, `r=0.6243914314`.

- `buy 2 get 1`: `R=0.9365871470` — negative.
- `buy 3 get 2`: `R=1.0406523856` — **+4.0652% conditional overlay**.
- `buy 1 get 1`: `R=1.2487828627` — **+24.8783% conditional overlay**.

Pick 3 needs `Y/X > 60.1559%`.

### Pick 5 false lead — liability cap
Pick 5 has the best uncapped ratio, 67.1718%, so `buy 2 get 1` appears to give `100.7576%`. But full-cover guaranteed gross is CAD 16,148,100 per draw, far above the BCLC maximum combined Keno liability stated on the current PlayNow Keno rules page (CAD 2 million per draw). Therefore the uncapped Pick-5 full-cover overlay is **not a valid strict theorem**. The liability cap can reduce the payout enough to destroy it.

This makes Pick 2 / Pick 3 much cleaner monitoring targets because their full-cover gross is far below the cap.

## Current 2026 promotion state
The current publicly posted BCLC retail Keno promotion for July 27–September 7, 2026 is **Keno Doubler**. Tickets are randomly selected for a Doubler message, and replay does not guarantee another Doubler. This is already closed by H156 as a strict guarantee.

No current 2026 BCLC Value Bundle with a published `X:Y` schedule was found in this packet. The game rules preserve the mechanism for temporary promotions, so it becomes a high-value recurring monitor rather than a current executable strategy.

## Exact trigger for future monitoring
Immediately reopen H157 if BCLC publishes a deterministic Value Bundle satisfying any of:

- Pick 2: `Y/X > 0.6631578947` (integer example: buy 3, get 2 free);
- Pick 3: `Y/X > 0.6015594542` (buy 3, get 2 free works);
- any other spot: compare the announced `Y/X` to the table above, then apply liability caps and transaction limits.

Before declaring SUCCESS, still verify:
1. identical player-selected numbers persist across the free draws;
2. complete covering ticket volume can actually be issued before the first included draw closes;
3. no per-player/per-draw wager or prize-liability reduction applies to the selected low spot;
4. cancellation/invalid-ticket branches cannot strand paid consideration;
5. tax, travel/geographic eligibility and execution costs leave a strictly positive net floor.

## Result
**No current SUCCESS.** H157 establishes a genuinely player-owned deterministic subsidy class and an exact alert threshold. A future BCLC `buy 3 get 2 free` (or stronger) Keno Value Bundle would make Pick 2 and Pick 3 immediate strict-cover candidates; the currently active 2026 promotion is random Doubler instead.
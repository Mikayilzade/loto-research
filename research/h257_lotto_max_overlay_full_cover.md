# H257 — LOTTO MAX 2026 MAXPLUS/MAXMILLIONS full-cover guarantee screen

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED for strict guaranteed profit**

## Question

Can the redesigned 2026 Canadian LOTTO MAX create a guaranteed-profit full-cover opportunity when externally accumulated money is distributed through the Main Jackpot, MAXPLUS and MAXMILLIONS exact-match draws?

This is structurally different from ordinary jackpot-only coverage because every MAXPLUS/MAXMILLIONS series is another 7-number draw over the same 1–52 outcome space. A complete 7/52 cover therefore necessarily contains every such drawn series.

## Current official rules

The current LOTTO MAX Game Conditions are effective April 10, 2026. They state:
- each C$6 play contains four selections of seven numbers from 1–52;
- the Main Draw is seven main numbers plus one bonus number;
- C$2.88 of every C$6 play is allocated to prize funding;
- 4/7 pays a fixed C$20, 3/7+Bonus pays a fixed C$20, and 3/7 pays a Free Play;
- the Main Jackpot and upper main tiers are shared among winning selections;
- the number of MAXPLUS draws is tied to C$1m jackpot tranches (with discretion for additional series), and each MAXPLUS prize is at least C$100,000;
- when the jackpot would otherwise reach at least C$50m, ILC publicly announces a number of MAXMILLIONS draws, each nominally C$1m;
- a MAXPLUS or MAXMILLIONS prize is divided by the number of times the drawn seven-number series appears on winning tickets.

Primary source:
- WCLC / ILC `LOTTO MAX Game Conditions`, effective 2026-04-10: https://www.wclc.com/lotto-max-3.0-game-conditions.htm

Current-state check at this packet: the next Ontario draw shown for Tuesday 2026-08-25 is only C$10m plus 10 × C$100,000 MAXPLUS prizes, so there is no current MAXMILLIONS accumulation to exploit.

## Idealized complete-cover lower bound on cost

The exact 7-number outcome space is:

`C(52,7) = 133,784,560` selections.

To avoid overstating execution cost, give the strategy the impossible-best packing assumption that all four selection slots in every C$6 play can be used perfectly with no duplicates or regional selection constraints. Then the absolute minimum number of plays is:

`133,784,560 / 4 = 33,446,140 plays`

and the idealized minimum cost is:

`33,446,140 × C$6 = C$200,676,840`.

Any real constraint that prevents perfect four-slot packing only increases cost, so this is player-favorable.

## Deterministic fixed-cash floor

For one copy of every 7-subset and any realized Main Draw, the exact counts are outcome-independent.

For 4/7 (four main numbers and three undrawn non-bonus numbers):

`C(7,4) × C(44,3) = 463,540` winning selections.

For 3/7+Bonus:

`C(7,3) × C(44,3) = 463,540` winning selections.

Both fixed categories pay C$20, so the strict immediate cash floor is:

`(463,540 + 463,540) × C$20 = C$18,541,600`.

That is only **9.2395%** of the already-idealized minimum full-cover cost, leaving a fixed-floor deficit of **C$182,135,240**.

The 3/7 Free Play is not credited as immediate guaranteed cash because a future free play retains a legal zero-cash outcome.

## Why MAXPLUS/MAXMILLIONS do not create a guarantee

Full coverage does solve one problem: for every announced MAXPLUS or MAXMILLIONS series, our portfolio necessarily includes at least one matching 7-number selection.

But the official rule then divides that nominal prize by the number of times the same series appears on winning tickets. The same sharing structure applies to the Main Jackpot and upper pari-mutuel main categories.

Published rules provide no useful hard pre-draw upper bound on the number of external matching selections for any particular seven-number series. Therefore, for a strict all-outcome proof, an arbitrary number of outside duplicates remains a legal market branch. Our share of each Main Jackpot/MAXPLUS/MAXMILLIONS/upper-tier pool can consequently be driven arbitrarily close to zero.

Thus externally accumulated headline prizes cannot be assigned any positive deterministic lower-bound contribution without an independently enforceable cap on outside duplicates.

This remains true even if the announced number of MAXMILLIONS becomes extremely large: every one of those prizes is individually shareable, so a finite advertised overlay does not repair the missing worst-case sharing bound.

## Current-state rejection

The next 2026-08-25 draw is only C$10m with ten C$100k MAXPLUS prizes. It is nowhere near an exceptional MAXMILLIONS state, but the rejection is stronger than a current-state EV calculation: **the guarantee class fails structurally for any finite headline overlay under the present sharing rule unless a useful external-duplicate cap is established.**

## Reopen conditions

Reopen LOTTO MAX full-cover overlay only if at least one materially new condition becomes true:
1. MAXPLUS/MAXMILLIONS change from shared prizes to fixed per-winning-selection payouts;
2. a binding pre-draw cap on total external selections/duplicates becomes available and is low enough for a positive worst-case floor;
3. all eligible selections can be reserved/monopolized before cutoff at a known bounded cost;
4. a new non-shareable externally funded fixed payout is attached to player-controlled 7-number identifiers and exceeds the exact acquisition deficit.

## Conclusion

**NOT A SUCCESS.** LOTTO MAX 2026 has genuine external overlay mechanics and complete coverage would hit every MAXPLUS/MAXMILLIONS series, but sharing destroys the strict floor. The only non-shareable immediate-cash categories guarantee C$18.5416m against an idealized minimum C$200.67684m acquisition cost.

Reproduction:
- `src/loto_research/h257_lotto_max_overlay_full_cover.py`
- `data/derived/h257_lotto_max_overlay_full_cover.json`

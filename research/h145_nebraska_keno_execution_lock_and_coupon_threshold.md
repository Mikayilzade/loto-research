# H145 — Nebraska Keno execution lock + coupon threshold

Updated: 2026-08-21
Status: **EXECUTION ARCHITECTURE MATERIALLY STRENGTHENED / LIVE NUMERIC SPECIAL STILL REQUIRED / NO SUCCESS**

## New result
H144 established Nebraska municipal Keno as a promising dynamic-paytable class. H145 resolves a major execution concern and lowers the required special-paytable threshold when a player-owned free-play credit exists.

Current Big Red / La Vista FAQ states:
- Play+ account funds can be transferred out;
- after purchase, a ticket can be voided before the game starts, with funds returning to the account balance;
- saved/practice tickets can be prepared in advance;
- current Monthly Keno Specials and community paybooks are viewable inside the Big Red Keno app;
- actual play remains location-bound.

Primary/current pages:
- https://www.lavistakeno.com/frequentlyaskedquestions
- https://nebraskagamingcommission.org/gaming-laws/county-city-lottery-regulations

Nebraska regulations additionally require the payout schedule to be known before number selection and require accepted wagers to be represented by an outside ticket / transaction record. Outside tickets identify the applicable paytable. These rules create a stronger pre-draw execution lock than the Kentucky H136-H140 deposit-bonus route.

## Execution sequence now supported
A viable Nebraska candidate can use:

`observe posted paytable -> build full cover -> submit/accept all tickets -> verify every outside ticket/paytable -> if any required leg is missing, void before game start -> otherwise let game close`.

Because Play+ funds are withdrawable and pre-start voids return the stake to account balance, external principal need not be irreversibly trapped before complete coverage is verified. This materially removes the H136-style precommitment blocker.

## Coupon-adjusted Pick-1 theorem
For an 80-number / 20-draw Pick-1 game, cover all 80 numbers at stake `w` each.

- face cost `S = 80w`
- exactly 20 winners
- if gross payout multiple is `p`, deterministic gross `G = 20pw`
- base cover ratio `r = p/4`

If a player already owns usable free-play credit `F`, external cash needed is `S-F` and pre-tax deterministic profit is:

`P = 20pw - (80w - F)`.

Break-even condition:

`p > 4 - F/(20w)`.

For Quarter-Madness-scale `w = $0.25`, full face cover is $20. A $5 player-owned coupon would reduce external cash to $15, so:

- `p=3.00` -> gross $15 -> exactly break-even before tax/costs;
- `p=3.25` -> gross $16.25 -> +$1.25 pre-tax;
- `p=3.50` -> gross $17.50 -> +$2.50;
- `p=3.75` -> gross $18.75 -> +$3.75;
- `p=4.00` -> gross $20 -> +$5.00.

Thus with a genuinely pre-owned $5 coupon, the direct special-paytable trigger falls from `>4.00x` to **`>3.00x`** on a $20 cover, subject to coupon applicability and paytable/aggregate limits.

## Current promotion check
La Vista's public Events page shows a historical/current-site promotion wording: buy a burger and collect $5 in Keno Cash. The opened page, however, currently specifies **Wednesdays in July** (July 1, 8, 15, 22, 29), so this specific coupon is **not treated as live on 2026-08-21**. Search snippets showing other month text are inconsistent and are not accepted as authoritative.

Therefore no current coupon is credited in the terminal theorem.

## Kearney-specific current evidence
Current June 2026 local reporting states Big Red Keno has used a **Kearney-specific pay table since the beginning of April 2026**, rather than a statewide table, and displayed the paybook to the City Council. This confirms that live community-specific numeric schedules genuinely exist in 2026.

Source:
- https://kgfw.com/2026/06/24/410592/

The exact numeric Kearney paytable is still not exposed in reliable web text. Big Red's own FAQ says the current community paybook and Monthly Keno Specials are inside the app under Official Rules / Monthly Keno Specials.

## Result
- Withdrawable funding architecture: **VALIDATED current**.
- Pre-start ticket void with stake return: **VALIDATED current**.
- Posted/identified paytable before draw: **VALIDATED regulatory requirement**.
- Community-specific 2026 paytables: **VALIDATED current**.
- Coupon-adjusted threshold theorem: **VALIDATED**; $5 on a $20 cover reduces Pick-1 trigger from >4.00x to >3.00x.
- Current qualifying $5 coupon: **NOT VALIDATED**; July offer expired / page inconsistent.
- Exact live special Pick-1 `p>3.00` or direct `p>4.00`: **NOT YET CAPTURED**.
- Terminal SUCCESS: **NO**.

## Next action
1. Capture current Big Red app Monthly Keno Specials / Official Rules numeric schedules for Kearney, Omaha, Lincoln, Fremont, Norfolk, Blair, Beatrice, Valley and La Vista.
2. Prioritize any Pick-1 schedule `p>3.00` if a usable pre-owned free-play coupon is simultaneously live; `p>4.00` is direct overlay without coupon.
3. Verify per-game aggregate payout limit and per-ticket limits before execution.
4. Search current Nebraska free-play coupons that are unconditional or acquired independently of extra economic cost.
5. For any candidate, test the complete sequence including void-before-start and Play+ withdrawal before classifying SUCCESS.

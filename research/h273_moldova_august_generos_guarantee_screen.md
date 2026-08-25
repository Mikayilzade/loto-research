# H273 — Moldova AUGUST GENEROS 2026 strict-guarantee screen

Date checked: 2026-08-25
Status: **CLOSED / REJECTED for strict deterministic-profit construction**

## Why this was worth checking

The active `AUGUST GENEROS 2026` campaign on 7777.md is run by NGM Company together with the National Lottery of Moldova and is funded from the organizer's own revenue without an extra participation fee. That makes it a real external-subsidy candidate rather than an ordinary negative-EV draw.

Official campaign page:
- https://7777.md/pages/?pr=1539

The rules state that every **MDL 100 of eligible real-money turnover creates one participation** in the applicable Special Prize draw. The special-prize periods are:
- 1–6 Aug: 7 × MDL 100,000 cash = **MDL 700,000**;
- 7–16 Aug: 7 trips with a **MDL 60,000 cash substitute** each = **MDL 420,000** cash-equivalent;
- 17–30 Aug: one Mercedes-Benz CLE 200 Coupé with a **MDL 1,000,000 cash substitute**.

So the campaign exposes **MDL 2,120,000** of stated special-prize cash/cash-substitute liabilities across the three registration periods, funded externally to the qualifying wager itself.

## Exact current-period blocker

For the currently active 17–30 Aug registration window there is one Special Prize winner, selected randomly from eligible participations. Participations are assigned automatically from turnover; the rules do not provide player-selectable or player-reservable identifiers.

Let our finite portfolio create `N >= 1` eligible participations. If there exists even **one external eligible participation**, selecting that external participation is a legal draw outcome. In that outcome our special-prize receipt is **MDL 0**.

Therefore, for every finite `N`:

`worst_case_special_prize(N, external_entries >= 1) = 0`.

Buying more entries can raise probability but cannot produce the strict everywhere-positive floor required by this project. The important difference from H262's terminal Gold Ball theorem is that there is no hard issuance cap or reservation mechanism allowing us to certify ownership of the complete eligible identifier set before draw cutoff.

## Tournament branch

The same campaign also advertises a **MDL 500,000** electronic-ticket tournament paid to the top 1,000 ranks. Points equal real-money stake value on specified electronic tickets.

This also fails as a strict guarantee. The published rules give no hard cap on participant count or obtainable points. For any finite score `S` that we choose, a legal configuration exists with 1,000 external participants each scoring more than `S`, leaving us outside all paid places. Hence the pre-draw deterministic tournament floor is also zero.

Moreover, tournament awards are **bonus funds rather than cash** and carry wagering conditions of **x10 in E-BILETE or x5 in SPORT**, so even a known paid rank could not be valued at face cash for a strict-profit proof.

## Calendar / gift branch

The campaign's summer bonus calendar does not repair the guarantee:
- offers/missions can depend on deposit, turnover or other announced conditions;
- FREEBET gifts are random among MDL 20 / 50 / 100 / 7,777 on days when the offer is activated;
- the bonus wheel is periodic and random;
- free-spin package size and unit value are random;
- bonus funds are not directly cash-redeemable and are subject to use/wagering conditions.

The organizer also retains rule-defined rights to modify the campaign in exceptional circumstances. None of these features supplies a fixed, precommitted, monopolizable cash subsidy to every qualifying portfolio.

## Reproducible formal screen

`src/loto_research/h273_moldova_august_generos_guarantee_screen.py` encodes two adversarial certificates:
1. one external current-period raffle participation is enough to make our special-prize floor zero, no matter whether we own 1 entry or millions;
2. for any finite tournament score, 1,000 legal external scores above it make the tournament bonus floor zero.

Derived result:
- `data/derived/h273_moldova_august_generos_guarantee_screen.json`

## Conclusion

This campaign is useful evidence that **real sponsor/organizer-funded external money exists**, but the allocation mechanism is open and adversarially shareable. It is therefore **not a strict guaranteed-profit construction**.

Reopen only if a future promotion adds at least one of:
- a hard, known cap on eligible promotional identifiers plus a way to reserve/own all of them;
- a fixed bonus paid to every qualifying entry rather than a random winner;
- a bounded leaderboard/turnover pool whose complete takeover cost can be proven below a guaranteed cash-equivalent liability.

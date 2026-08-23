# H204 — Rhode Island app-generated QR retail execution gate

Updated: 2026-08-23
Status: **NO SUCCESS**
Scope: LOTTERY ONLY.

## Target
Test a new primary-source execution route for H173/H175: whether the current Rhode Island Lottery mobile app can pre-build draw-game wagers into a QR code that a retailer terminal or self-service vending machine scans, potentially reducing the same-draw manual-entry bottleneck for the 4,336/4,560-play Keno portfolio.

## Fresh official evidence

The current Rhode Island Lottery Retailer News and Announcements page states that players can use the RI Lottery App to make their **wager selections** and generate a **QR code** to scan at retail for purchase of a draw-game ticket. It further states that this QR code can be scanned using either a retailer terminal or a self-service vending machine.

Official source: https://www.rilot.com/en-us/retailers-corner/retailer-news.html

This is materially stronger than the generic post-purchase QR evidence rejected in H203. Here, the QR is explicitly a **pre-purchase wager-selection transfer mechanism**.

## What H204 establishes

1. A current official RI mechanism exists for moving user-entered draw-game selections from the app to a retail terminal/SSVM through one QR scan.
2. Therefore the H173/H175 execution analysis should no longer assume every arbitrary selection must necessarily be keyed manually at the terminal.
3. This route is directly relevant to Keno only if the app's draw-game QR builder includes Keno and preserves multiple user-specified Keno selections in one generated code/order.

## What remains unproved

The official page does **not** state:
- the maximum number of wager selections encoded in one QR code;
- whether one QR may contain multiple independently specified Keno plays;
- whether Keno is included in this exact retail-QR workflow rather than only other draw games;
- whether a scan can commit all encoded plays to the same Keno draw;
- per-transaction, per-ticket, terminal, self-service-vending, or pre-draw throughput limits;
- whether arbitrary 4,336/4,560-play portfolios can be split across enough QR payloads and accepted before cutoff without discretionary rejection.

Hence this does **not** yet prove executable acquisition of the full H173/H175 portfolio.

## Consequence

H203's conclusion is refined, not overturned: generic post-purchase ticket QR codes remain irrelevant, but there is now official proof of a distinct **pre-purchase app-generated wager QR** channel. This is the best current execution lead and deserves direct capacity testing/document recovery.

## Non-repeat rule
Do not again treat all RI QR evidence as post-purchase only. Distinguish:
- ticket-validation/second-chance QR: post-purchase identifier;
- app wager-builder QR: pre-purchase selection-transfer mechanism.

Do not infer bulk capacity from the latter without an explicit selection-count or payload-capacity source.

## Next actions
1. Recover RI mobile-app help/FAQ/screenshots/manual text for Keno QR play-building and determine whether Keno supports multiple panels/selections per QR.
2. Recover terminal/SSVM documentation for QR transaction capacity, ticket-line limits and same-draw processing.
3. If a finite per-QR capacity is found, compute exact minimum QR scans/terminals/participants required for H175 (4,336) and H173 (4,560).
4. Continue exact H188/H191 mathematical pruning in parallel.

## Result
**ЕЩЁ НЕ УСПЕХ.** A real pre-purchase QR wager-transfer mechanism is now officially proven, but its Keno multi-selection capacity is still unknown, so full 4,336/4,560-play same-draw execution is not yet guaranteed.

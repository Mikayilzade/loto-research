# H208 — Rhode Island retail/SSVM strict Keno execution failure

Updated: 2026-08-23
Scope: LOTTERY ONLY
Status: **NO SUCCESS; CURRENT RETAIL/SSVM CHANNEL NOT A STRICT GUARANTEE**

## Target
Continue H207's H173/H175 execution gate after online/iLottery was closed as a strict-guarantee channel. Test whether physical Rhode Island Lottery retailer terminals or self-service vending machines (SSVMs) can force complete same-draw acquisition of the prescribed Keno portfolio.

## Required portfolio
The two live conditional constructions require complete ownership of every prescribed $1 3-spot wager for one target Keno draw:

- H175 hybrid: 4,336 distinct wagers;
- H173 cover: 4,560 distinct wagers.

Current RI rules cap an ordinary Keno Ticket at $150. Even under the most favorable possible interpretation that a physical ticket may aggregate many independent $1 selections, this implies a hard lower bound of:

- `ceil(4336/150) = 29` separately issued tickets for H175;
- `ceil(4560/150) = 31` separately issued tickets for H173.

This lower bound does not assume anything about actual board capacity; actual ticket count may be much larger.

## Primary-source execution evidence
1. RI Lottery's current retailer news confirms that draw-game selections made in the RI Lottery App can generate a QR code which is scanned at either a retailer terminal or an SSVM. Thus physical terminal/SSVM purchase is a real execution path.
2. RI Lottery's current retailer FAQ expressly addresses Lottery terminal jams causing ticket misprints. The prescribed procedure is to reprint, call the IGT hotline, and for Keno/Bingo/Wild Money misprints the ticket **should be voided prior to the draw**. Credit for a damaged/misprinted ticket is stated to be **at the discretion of the Rhode Island Lottery**.
3. Current official Keno rules state that Keno draws occur every four minutes and that a Keno ticket can only be cancelled from the same terminal before the draw. This makes correction of a failed/misprinted component time-sensitive for a same-draw portfolio.
4. RI promotional rules for terminal/SSVM ticket issuance independently acknowledge technical-error branches: incomplete/failed/delayed computer transmissions, hardware/software/network failures, and Lottery rights to modify/suspend/cancel promotions. These terms are promotion-specific, so they are supporting evidence rather than the core generic Keno rule.

## Exact strict-guarantee consequence
H173/H175 are deterministic payoff theorems only after **all** prescribed wagers for the same draw have been successfully issued. The current physical execution path requires at least 29/31 separately issued tickets under the most favorable ticket-packing assumption.

The Lottery's own retailer FAQ establishes an allowed operational branch where a terminal jams/misprints a required Keno ticket, after which reprint/void/correction must occur before the draw and any credit is discretionary. No current rule recovered in H208 gives the player an irrevocable right to force successful reissuance of every required wager before the four-minute target draw closes, nor an atomic all-or-none transaction covering all 4,336/4,560 wagers.

Therefore the branch

`one required physical issuance fails or is misprinted and is not successfully reissued before the target draw`

cannot be excluded under current published rules. In that branch, the prescribed portfolio is incomplete and the H173/H175 worst-case return theorem no longer applies.

## What this closes / does not close
**Closed:** current ordinary retailer-terminal/SSVM issuance as the sole execution basis for a *strict deterministic guarantee* of H173/H175.

**Not closed:**
- practical or positive-EV execution using many terminals/retailers;
- a future operator-approved bulk/atomic syndicate facility;
- a pre-issued coupon/promotion that itself locks the entire required portfolio;
- the H175 combinatorial mathematics;
- recovery of current Kick Back with Keno rules, which could create a smaller or differently executable deterministic overlay.

## Sources
- RI Lottery current Keno rules / 2026 Rules and Regulations: Keno ticket cap, four-minute draws, cancellation-before-draw rule.
- RI Lottery Retailer News: app-generated QR code can be scanned at retailer terminal or SSVM.
- RI Lottery Retailer FAQ: terminal jam/misprint procedure; Keno misprints voided before draw; credit discretionary.
- RI Lottery 2025 Be a Millionaire Day rules: terminal/SSVM promotion and explicit technical-failure disclaimer (supporting control).

## Verdict
**ЕЩЁ НЕ УСПЕХ.** Current RI retail/SSVM execution does not supply a strict all-branches guarantee that all 4,336/4,560 same-draw Keno wagers will be successfully issued before cutoff.
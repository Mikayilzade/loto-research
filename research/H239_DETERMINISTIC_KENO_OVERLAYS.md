# H239 — Deterministic Keno overlays

Date: 2026-08-24
Status: NOT SUCCESS, but mechanism class confirmed

## Question
Do real lottery promotions exist where an overlay is known before purchase and applies deterministically to all qualifying Keno tickets, rather than being assigned randomly after/at purchase?

## Evidence

### 1. Ohio KENO Double BOOSTER — deterministic time-window overlay (historical)
Official Ohio Lottery promotion rules for September 2025 state that **all BOOSTERS are doubled** on KENO tickets purchased with BOOSTER during the promotional hours. The published mapping was 1X→2X, 2X→4X, 3X→6X, 4X→8X, 5X→10X, 10X→20X. The qualifying condition was deterministic: ticket purchased at an Ohio Lottery KENO retailer during the published Tuesday 4–5 p.m. windows and BOOSTER added.

This proves that a true pre-announced all-qualifying-ticket Keno multiplier overlay exists in practice.

Important limitation: BOOSTER itself costs an extra dollar per dollar wagered, so this is not a free 2X floor relative to base-ticket cost.

### 2. Georgia KENO Bonus Hours — deterministic +30% payout (2026, expired)
Georgia Lottery's 2026 KENO Bonus Hours page states that winning KENO tickets purchased during listed offer periods received a **30% higher payout than the standard payout**. Retail and online purchases were both eligible. The offer periods ran between June 15 and July 15, 2026.

This is a deterministic, pre-announced payout overlay with no random ticket-tag gate. It is expired as of 2026-08-24.

### 3. North Carolina Keno Bonus Hours — deterministic +50% conditional on Multiplier purchase (2026, expired)
NC Lottery announced every Friday in June and July 2026, 4–6 p.m., participating-location Keno wins received **50% more prize money** when the player added the Multiplier. Multi-draw tickets bought during the qualifying window remained eligible for later draws.

The window was deterministic, but adding Multiplier doubles the base ticket cost. The promotion is expired as of 2026-08-24.

### 4. Missouri Club Keno Bonus Hours — deterministic increased-prize structure
Missouri Lottery retailer materials document Bonus Hours in which qualifying 10-draw Club Keno tickets purchased during published Friday windows receive increased cash prizes; historical/current materials describe increases of up to 50% on eligible base prizes. The qualification is based on purchase time and ticket structure, not a random tag.

The Missouri retailer promotional-materials page was still listing Club Keno Bonus Hours as a current promotion in August 2026, but the exact August/September 2026 qualifying dates and legal rules were not located in this run, so current executability is not yet established.

### 5. BCLC Keno Doubler — rejected as deterministic
BCLC's Feb 9–Apr 10, 2026 Keno Doubler randomly printed a `$$KENO DOUBLER$$` message on tickets. A replay did not guarantee another Doubler message. This is the same random-ticket-tag failure mode as H237/H238 and cannot guarantee universal 2X qualification over a finite full-coverage set.

## Implication for the full 3-spot coverage thesis
A key blocker in H236 was not the existence of deterministic promotions in principle. H239 resolves that: deterministic pre-announced Keno overlays **do exist**.

The unresolved gate is stronger:

1. the overlay must be active/current (or announced future);
2. it must apply to every ticket in the required coverage set;
3. its guaranteed payout uplift must be large enough after any add-on cost;
4. transaction/play limits must allow the needed coverage to be entered in time;
5. liability caps and promotional exclusions must not destroy the guarantee.

The located 2026 Georgia and North Carolina windows are already expired. Ohio's 2025 all-BOOSTER-doubled promotion proves the mechanism but BOOSTER doubles wager cost. BCLC is random. Missouri requires a separate exact-current-rules check.

## Verdict
NOT SUCCESS. H239 confirms the target mechanism is real, but no currently executable promotion found in this run yet supplies a guaranteed sufficiently large, all-ticket uplift for the 82,160-combination 3-spot coverage construction.

## Sources
- Ohio Lottery KENO Double BOOSTER rules, Sep 2025: https://www.ohiolottery.com/getattachment/be2303f8-361b-4beb-aca7-2b9790a8e8fb/Ohio-Lottery-KENO-Double-Booster_SepPromo_20250819.pdf
- Ohio Lottery KENO rules/current game page: https://www.ohiolottery.com/games/keno/
- Georgia Lottery KENO Bonus Hours June/July 2026: https://www.galottery.com/en-us/promotions/2026/June/KenoBonusHoursJuneJuly.html
- NC Lottery Keno Bonus Hours, 2026-06-05: https://nclottery.com/NewsBlogDetails/2026/6/5/Enjoy-a-bonus-month-of-Keno-Bonus-Hours-
- Missouri Lottery retailer promotional materials: https://retailer.molottery.com/displaytopic.do?topic=promotional-materials
- BCLC Keno Doubler retailer info, 2026: https://www.bclcretailerhub.com/content/dam/retailerhub/promotions/2026/Keno_Doubler_HN_Feb_2026_RIS.pdf

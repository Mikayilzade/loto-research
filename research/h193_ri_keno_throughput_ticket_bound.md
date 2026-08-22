# H193 — Rhode Island Keno throughput / ticket-bound screen

Updated: 2026-08-22
Status: **NO SUCCESS; EXECUTION GATE NARROWED**
Scope: LOTTERY ONLY.

## Target
Resolve one of H192's live execution unknowns for the H173/H175 Rhode Island doubled 3-spot coverage: whether 4,336 or 4,560 distinct $1 Keno plays can be submitted into one draw.

## Official rule evidence recovered
The Rhode Island Lottery's indexed official Keno rules state:

- Keno wagers for a single draw may be $1, $2, $5 or $10.
- A player may wager for up to 15 consecutive draws.
- Maximum price for an ordinary Keno Ticket is **$150**.
- Maximum rises to $300 with Keno Plus and $450 when Keno Plus + Overtime is involved.
- Keno draws take place every **4 minutes**.

The current 2026 official rules search result additionally confirms Registered Ticketless Play exists; the current RI site confirms iKeno/online Keno remains offered. The live homepage also continues to advertise the unresolved `Kick Back with Keno Promotion`, but its exact rules were not recoverable in this packet.

Primary official/current sources:
- RI Lottery current homepage: https://www.rilot.com/en-us/home.html
- RI Lottery official indexed rules (2025 text, same Keno ticket cap/draw cadence): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2025.pdf
- RI Lottery 2026 rules indexed by search (URL later returns 404 but indexed text contains the current Registered Ticketless Play wording): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf

## Exact execution arithmetic
For a coverage composed of distinct $1 wagers all targeting the same draw, the $150 maximum ticket-price rule implies a hard lower bound on the number of ordinary tickets/registered ticketless purchase objects if the cap applies per object:

- H175 target: `ceil(4,336 / 150) = 29` tickets.
- H173 target: `ceil(4,560 / 150) = 31` tickets.

If a ticket/object can contain 150 independently specified 3-spot wagers for the same draw, these are the theoretical minimum counts. If the UI/terminal permits fewer separately specified plays per ticket, the actual transaction count is higher.

Because draws are four minutes apart, a same-draw strategy must complete all required submissions before sales close for the chosen draw. The public rule text does **not** publish:

- a maximum number of independently specified Keno plays per Ticket beyond the dollar-price cap;
- a maximum number of Ticketless Plays/cart lines per checkout;
- a transaction-rate guarantee;
- a cutoff interval before each four-minute draw;
- an API/bulk-upload facility;
- a guarantee that 29/31 max-value distinct-number tickets can be issued atomically before one target draw.

## Consequence
This materially sharpens, but does not resolve, the execution gate.

The earlier question was vaguely whether thousands of individual plays could be entered in four minutes. Under the published $150 ticket cap, the absolute best-case packaging requirement is only 29 ordinary tickets for the 4,336 design (31 for 4,560), so execution is **not disproved by the ticket-value cap alone**. Conversely, no public evidence proves that one ticket can carry 150 arbitrary distinct 3-spot selections or that 29/31 such objects can be completed before the same draw.

Therefore throughput remains **INCONCLUSIVE**, not rejected and not validated.

## Promotion recovery note
Fresh search again confirms the current official homepage advertises `Kick Back with Keno Promotion`, but no exact rules/landing PDF was indexed under that phrase. Do not infer a multiplier, free wager, cash-back percentage or deterministic entitlement from the title alone.

## Next action
1. Recover the exact `Kick Back with Keno Promotion` rules/landing payload through site assets, promotion indexes, or current RI contact/public materials.
2. Recover the live Keno UI's actual QTY/cart constraints and whether multiple arbitrary selections are grouped in one Registered Ticketless Play.
3. Seek authoritative cutoff/terminal throughput language or empirical UI evidence sufficient to certify 29 (H175) / 31 (H173) max-value same-draw purchase objects.
4. Keep H175 mathematical universal `n3>=3` gate open independently.

## Result
**ЕЩЁ НЕ УСПЕХ.** Official rules reduce the H175 same-draw execution requirement to a best-case minimum of 29 $150 tickets, but public evidence still does not prove that 4,336 distinct 3-spot plays can be committed before one four-minute draw.
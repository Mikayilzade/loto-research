# H130 — New Jersey Fast Play Progressive finite-grid interpretation / jackpot threshold screen

Updated: 2026-08-20
Status: **FINITE-GRID TAKEOVER REJECTED / HIGH-JACKPOT +EV THRESHOLD QUANTIFIED / NO GUARANTEE**

## Question
NJ Fast Play Progressive publishes a `jackpot grid size of 500,000 tickets` with one jackpot winner. Could this be a finite-deck buy-the-pot mechanism where purchasing a complete or remaining grid guarantees the jackpot?

## Primary-rule finding: the grid is probabilistic, not depleting inventory
The official game pages state both:
- `Fast Play prizes instantly replenish after every purchase`;
- `each ticket sold has the same great odds of winning`;
- jackpot grid size 500,000 with one jackpot winner;
- non-jackpot grid size 150,000 with fixed prize frequencies.

That combination rules out the key deterministic takeover premise. A purchase does **not** remove a unique hidden jackpot position from a finite unsold deck. The prize distribution replenishes, so buying 500,000 tickets does not force possession of the jackpot ticket. The 500,000 figure is an odds grid / probability denominator.

Primary sources:
- Fast Play hub/rules: https://www.njlottery.com/en-us/drawgames/fastplay.html
- $10 U.S. Soccer: https://www.njlottery.com/en-us/drawgames/fastplay/187.html
- $20 Max Win: https://www.njlottery.com/en-us/drawgames/fastplay/180.html
- $30 Jersey Jackpot: https://www.njlottery.com/en-us/drawgames/fastplay/160.html
- $5 Perfectly Pear: https://www.njlottery.com/en-us/drawgames/fastplay/182.html
- $1 Jersey Jackpot: https://www.njlottery.com/en-us/drawgames/fastplay/161.html

## Jackpot sharing across price points
All Fast Play Progressive games feed one common progressive jackpot. Official rules state:
- $30: 100% jackpot + $25,000;
- $20: 100%;
- $10: 100%;
- $5: 50%;
- $2: 20%;
- $1: 10%.

This creates a genuine jackpot-state EV effect, but not deterministic coverage.

## Exact EV threshold method
For a game with ticket price `p`, jackpot share `s`, jackpot-hit probability `1/500000`, jackpot-hit fixed bonus `b`, and exact non-jackpot-grid average face value `f`, nominal EV is:

`EV(J) = f + (s*J + b)/500000`.

Nominal break-even jackpot:

`J* = ((p-f)*500000 - b)/s`.

Free-ticket prizes are valued at face value in this deliberately favorable screen. Taxes, travel, retailer execution, and time are omitted, so the calculated thresholds are lower bounds for real break-even.

## Sampled active-game thresholds
| Game | Price | Exact fixed-grid avg | Fixed gross | Jackpot share | Nominal J* |
|---|---:|---:|---:|---:|---:|
| $10 U.S. Soccer | $10 | $6.103333 | 61.0333% | 100% | **$1,948,333** |
| $20 Max Win | $20 | $12.406667 | 62.0333% | 100% | **$3,796,667** |
| $30 Jersey Jackpot | $30 | $18.840000 | 62.8000% | 100% + $25k | **$5,555,000** |
| $5 Perfectly Pear | $5 | $2.893333 | 57.8667% | 50% | **$2,106,667** |
| $1 Jersey Jackpot | $1 | $0.537500 | 53.7500% | 10% | **$2,312,500** |

Historical/current-scale control: NJ Lottery reported a 100%-jackpot Fast Play win of **$160,474** on July 29, 2026, and the official home page showed **$459,619** on July 26, 2026 before that later win. Both are far below even the lowest sampled nominal threshold (~$1.95m).

Sources:
- July 30, 2026 winner release: https://www.njlottery.com/en-us/newsandevents/newsinput/2026/press-releases/FP_RetailWin_073026.html
- official homepage indexed July 26 state: NJ Lottery home page, estimated progressive jackpot $459,619.

## Deterministic guarantee result
Because the prize grids replenish after every purchase, there is always a lawful outcome in which an arbitrarily large finite purchase misses the jackpot. Therefore:

**No finite number of purchases creates a strict jackpot-possession guarantee.**

Even if the progressive jackpot someday exceeds a nominal +EV threshold, the mechanism would be a positive-EV state only, not terminal guaranteed profit. A guarantee would require an external refund/subsidy or another contract that covers every losing branch.

## Result
H130 closes the apparent `500,000-ticket grid takeover` loophole. NJ Fast Play Progressive remains worth monitoring only as a rare high-jackpot **+EV** class if the common jackpot rises above the exact game-specific threshold, but it cannot be converted into a buy-all deterministic guarantee under the published replenishing rules.

No terminal SUCCESS.

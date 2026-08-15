# H008 — EuroMillions cross-jurisdiction valuation

Updated: 2026-08-15
Status: **material jurisdictional EV differences validated; standalone guaranteed-profit arbitrage rejected**

## Question
Can the same common EuroMillions draw be bought in a jurisdiction whose ticket price, tax treatment, local add-on or claim rules create a guaranteed arbitrage relative to another jurisdiction?

This packet focuses on official operator/tax sources for Spain, France, Ireland and the UK.

## Common game anchor
The common EuroMillions main game is 5 numbers from 50 plus 2 Lucky Stars from 12. The jackpot is shared across participating countries. Spain, France and Ireland currently list a simple line at **€2.50**. The UK lists **£2.50** per play.

Official sources:
- Spain SELAE: https://www.loteriasyapuestas.es/es/centro-de-ayuda/como-se-juega/jugar-a-euromillones
- France FDJ: https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/comment-jouer
- Ireland National Lottery: https://www.lottery.ie/draw-games/euromillions
- UK National Lottery: https://www.national-lottery.co.uk/games/euromillions

Therefore there is **no main-game acquisition-price arbitrage among the three euro-priced jurisdictions** before promotions/access costs. The UK price is denominated in GBP and requires an FX comparison, so it is not a fixed same-currency price identity.

## National bundled add-ons differ
The same €2.50/£2.50 purchase is not economically identical because each jurisdiction can attach a national raffle.

### Spain — El Millón
SELAE states that each EuroMillions bet at the same price also enters El Millón; one €1m code prize is awarded in Spain. The official page gives an illustrative probability around 1 in 5m when there are 5m bets.

Source:
https://www.loteriasyapuestas.es/es/centro-de-ayuda/como-se-juega/jugar-a-euromillones

### France — My Million
FDJ states that every €2.50 EuroMillions grid automatically receives a My Million code and one French code wins **€1m** at each draw.

Sources:
- https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/comment-jouer
- https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/resultats/mardi-02-juin-2026

### Ireland — Ireland Only Raffle
The Irish National Lottery states that every line receives an Ireland Only Raffle code and **10 Irish players win €5,000 each** per draw. Special announced draws can add an extra prize.

Sources:
- https://www.lottery.ie/game-information/euromillions
- https://www.lottery.ie/game-information/euromillions/euromillions-ireland-only-raffle

### UK — Millionaire Maker
The UK National Lottery includes a national Millionaire Maker prize with EuroMillions; its game page lists a guaranteed **£1m** prize category alongside the £2.50 play price.

Source:
https://www.national-lottery.co.uk/games/euromillions

These add-ons can change EV materially, but all are random. They do not create a deterministic cash floor.

## Tax difference is economically large
### Spain
SELAE currently states:
- prize <= €40,000: exempt;
- on a prize above €40,000, the portion above €40,000 is withheld at **20%**;
- El Millón uses a proportionally smaller €24,000 exemption.

Source:
https://www.loteriasyapuestas.es/es/centro-de-ayuda/premios/como-tributan-los-premios-de-selae

For a single main-game prize J > €40,000, operator-level Spanish net is:

`net_ES(J) = 40,000 + 0.8 * (J - 40,000)`.

Illustrative sole-jackpot net amounts:
- €17m gross -> **€13.608m net**;
- €100m gross -> **€80.008m net**;
- €250m gross -> **€200.008m net**.

At the €250m cap the Spanish special tax alone removes **€49.992m** versus a jurisdiction in which the initial lottery prize is not taxed.

### France
FDJ states that gambling/lottery winnings are not subject to French income tax as gambling income.

Source:
https://www.fdj.fr/mag/questions/gains-imposables-etat

### Ireland
Irish Revenue explicitly lists lottery wins among gains exempt from CGT and also lists lottery/game-with-prizes winnings as exempt receipts for CAT in the cited contexts. This confirms a materially more favorable direct lottery-win tax treatment than Spain at operator/player-prize level, although individual cross-border tax residency still requires separate analysis.

Sources:
- https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx
- https://www.revenue.ie/en/gains-gifts-and-inheritance/cat-exemptions/certain-receipts/index.aspx

### UK
The National Lottery states that there is no tax on the initial lottery win; later investment income is separately taxable.

Source:
https://www.national-lottery.co.uk/life-changing/winner-euromillions-davies-hairdresser

## Cross-jurisdiction dominance result
For the **common main-game component only**, a €2.50 French ticket and a €2.50 Spanish ticket buy the same 5+2 draw probability, but a sufficiently large Spanish prize is reduced by the special lottery tax while the French initial lottery win is not taxed as gambling income.

Thus, conditional on lawful equal access and ignoring the jurisdiction-specific add-on, France **strictly dominates Spain on net payout for main-game prizes above €40,000 at the same posted €2.50 price**.

This is a real valuation difference, not a number-prediction effect.

However it is not automatically executable for an Azerbaijan-based player. Account eligibility, physical-location requirements, KYC, claim rules, travel/agent costs and the player's own tax residence can alter the final result. No cross-border execution assumption is promoted without verifying those constraints.

## Why H008 does NOT satisfy terminal guaranteed profit
Let a jurisdiction j sell a positive-cost EuroMillions line with total cash return `R_j(omega)` across main game plus local random add-ons for draw outcome omega.

Every surveyed jurisdiction still has legal joint outcomes in which:
- the main line wins no main-game prize; and
- the national random code/add-on does not win.

Therefore for a single positive-cost line there exists omega with `R_j(omega)=0 < cost_j`.

Buying the same line in multiple jurisdictions does not remove this: there are joint draw/code outcomes where none of the main lines or national raffle codes win. It can diversify and alter EV, but cannot guarantee positive net cash profit.

Complete main-game coverage was already tested under H002b/H012 and also fails the terminal guarantee route because of cost, sharing and the terminal-cap rolldown incompatibility.

### H008 terminal theorem
Cross-jurisdiction price/tax/add-on differences can change **expected value and conditional net payout**, but if every available jurisdiction retains at least one all-loss outcome and no deterministic subsidy exceeds total acquisition cost, jurisdiction shopping alone cannot produce an all-outcome positive-profit guarantee.

Status:
- **material jurisdictional valuation difference: VALIDATED**;
- **France-vs-Spain common-main-game tax dominance above €40k: VALIDATED subject to lawful access/personal-tax caveat**;
- **standalone guaranteed-profit arbitrage: REJECTED**.

## Future use
H008 should return only as an overlay when another structural state is already near/beyond break-even. Then choose the jurisdiction by:
1. effective line price after FX/fees;
2. local raffle expected value;
3. operator withholding / personal tax;
4. claim/access costs;
5. sharing and payout rules.

It is no longer a primary terminal-guarantee branch by itself.

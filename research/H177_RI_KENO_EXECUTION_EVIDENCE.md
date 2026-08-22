# H177 — Rhode Island Keno execution evidence

Date: 2026-08-22
Status: NOT SUCCESS

## Question
Can the conditional 3-spot covering construction be executed in Rhode Island Keno under the required Keno Plus / same-draw assumptions?

## New official evidence

1. Current RI Lottery Keno page exposes an online purchase flow with: number selection, amount per game, consecutive games, Keno Plus option, Keno Overtime option, and Buy Now. This confirms online Keno purchase and that Keno Plus is selectable in the current interface.
2. RI Lottery's 2024 winner report states a $2 seven-spot Keno Plus wager won a $9,000 base prize and was tripled to $27,000 when the 3X multiplier was drawn. Thus Keno Plus is a random multiplier, not a pre-lockable 2X selection.
3. RI Lottery's 2022 winner report explicitly says a player doubled the wager to add Keno Plus; a $52,500 base 8-spot prize became $105,000 when 2X came up. This confirms the Plus option costs the base wager again and 2X is an outcome of the multiplier draw.
4. RI Lottery's 2020 report gives another example: $1 six-spot + Keno Plus, with 10X producing $12,000 from a $1,200 standard prize. It also documents an iKeno player accidentally placing the same $1 six-spot wager twice; both copies won in the same draw. This is evidence that duplicate same-draw online wagers have existed, but it does not prove current bulk capacity or thousands of plays in one draw.
5. The current RI Lottery winners page (updated 2026-08-03) includes an iLottery Keno win dated 2026-01-28, corroborating that online Keno remains operational in 2026.

## Consequence for the prior 2X conditional thesis

The critical assumption "buy Keno Plus while locking multiplier = 2X" is falsified by official evidence. The player can buy Keno Plus, but the multiplier is drawn. Therefore any EV/guarantee calculation conditioned on knowing 2X before ticket purchase is not an executable strategy unless a separate promotion or mechanism explicitly preassigns/doubles eligible tickets before the draw.

A historical 2025 Lucky 3 Spot Keno promotion did pre-mark eligible 3-spot tickets for doubled prizes, but it was restricted to one venue and a two-hour promotional period on 2025-06-18. It proves that preassigned 2X-style promotions can exist, not that one is active now.

## Remaining gates

- Obtain the current official 3-spot prize table and recompute unconditional Keno Plus EV using the actual multiplier distribution/cost.
- Establish current transaction/ticket/play limits and whether ~4,336 distinct 3-spot wagers can be submitted before one draw closes.
- Continue the combinatorial search for a valid construction with the required n3>=3 property below 4,336/4,560, independently of the failed affine design.
- Search current/future promotions for a genuine preassigned doubler/overlay that changes the economics before purchase.

## Verdict

NOT SUCCESS. H177 closes one important ambiguity: ordinary Keno Plus does **not** let the player lock 2X before purchase. The current conditional-profit construction therefore cannot yet be treated as executable. Same-draw duplicate online wagering is historically evidenced, but bulk same-draw capacity remains unproven.

## Sources

- Rhode Island Lottery current Keno page: https://www.rilot.com/en-us/keno.html
- RI Lottery news, 2024-10-25: https://www.rilot.com/en-us/player-zone/news/news-input/2024/2MillionInstantTicketWinner.html
- RI Lottery news, 2022-09-01: https://www.rilot.com/en-us/player-zone/news/news-input/2022/105000KenoPlusWinner.html
- RI Lottery news, 2020-06-18: https://www.rilot.com/en-us/player-zone/news/news-input/2020/KenoPlayersWinningatRetailandOnline.html
- RI Lottery Keno winners, updated 2026-08-03: https://www.rilot.com/en-us/winners/winners-keno.html
- Lucky 3 Spot Keno promotion rules (2025): https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf

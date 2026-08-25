# H267 VALIDATION — Lucky Lotteries full-buyout bound

Date: 2026-08-25
Result: **VALIDATED / REJECTED FOR STRICT GUARANTEED PROFIT**

## Rule gates
- Rules document states it is in force from **18 May 2025**.
- Super Jackpot pool = **270,000** unique sequential identifiers.
- Mega Jackpot pool = **200,000** unique sequential identifiers.
- Duplicate generated identifiers are cancelled/refunded/replaced.
- Draw occurs after all available numbers are sold.
- Jackpot Number is drawn after the cash-prize Winning Numbers.
- Jackpot Prize is paid **iff** the Jackpot Number is one of those Winning Numbers.
- Therefore a legal no-jackpot branch remains even under perfect ownership of the whole ticket pool.
- Free-ticket consolation prizes have a rules-defined cash equivalent excluding commission.

## Independent arithmetic
### Super Jackpot
Cash prize schedule sum:
`100000 + 10000 + 5000 + 2*500 + 10*200 + 20*100 + 100*50 + 600*25 + 750*15 + 2480*10 = 176050`.

Free-ticket-equivalent entry count on the no-jackpot branch:
`2*25 + 2*15 + 4*10 + 20*5 + 40*3 + 200*2 + 1200 + 1500 + 4960 + 10 = 8410`.

Guaranteed no-jackpot gross:
`176050 + 2*1000 + 8410*2 = 194870`.

Full retail buyout:
`270000 * 2.20 = 594000`.

Return:
`194870 / 594000 = 0.32806397306397306` = **32.8063973064%**.

Commission-free subscription-only check:
`194870 / (270000*2) = 0.3608703703703704` = **36.0870370370%**, consistent with the published 36.0870% Prize Fund after rounding.

### Mega Jackpot
Cash prize schedule sum:
`200000 + 20000 + 5000 + 5*1000 + 10*500 + 25*100 + 75*75 + 600*40 + 700*20 + 2800*12 = 314725`.

Free-ticket-equivalent entry count on the no-jackpot branch:
`2*25 + 2*15 + 10*10 + 20*5 + 50*3 + 150*2 + 1200 + 1400 + 5600 + 10 = 8940`.

Guaranteed no-jackpot gross:
`314725 + 2*1000 + 8940*5 = 361425`.

Full retail buyout:
`200000 * 5.50 = 1100000`.

Return:
`361425 / 1100000 = 0.3285681818181818` = **32.8568181818%**.

Commission-free subscription-only check:
`361425 / (200000*5) = 0.361425` = **36.1425%**, exactly the published Mega Jackpot Prize Fund percentage.

## Closure statement
The full-buyout hypothesis is deliberately stronger than real execution. Yet even under perfect ownership, a legal no-jackpot outcome exists and returns only ~32.8% of retail acquisition cost. Hence Lucky Lotteries cannot support an everywhere-positive guaranteed-profit takeover under the checked rules.

Source rules: https://support.ozlotteries.com/hc/en-us/article_attachments/14948080526607
Current gameplay summary: https://help.thelott.com/hc/en-us/articles/4416872034073-How-do-I-play-the-Lucky-Lotteries-raffle-style-game

# H068 — CBAR investment-coin mandatory buyback / secondary-market arbitrage

Updated: 2026-08-18
Status: **PROMISING MECHANISM / CURRENT MARKET SCREEN NEGATIVE / NOT SUCCESS**

## Question
Can an authentic Central Bank of Azerbaijan investment gold coin be acquired on the secondary market below a legally/contractually constrained same-day bank buyback amount, creating a deterministic cash spread after all costs?

This is a new deterministic-redemption class rather than a lottery-number strategy. It is relevant because the project completion criterion allows any reproducible executable guaranteed positive net-profit mechanism among the registered lottery/lottery-adjacent alternatives.

## 1. Official buyback mechanism — validated
CBAR's official `Bullion coin sales agents` page states that appointed sales agents must:
- repurchase CBAR investment coins from the public;
- organize examination/authentication of the coins;
- pay citizens the value of repurchased coins **on the same day**;
- set retail sale price at the gold rate plus no more than 10%;
- set repurchase price at the gold rate minus no more than 3%.

The appointed agents shown are Bank of Baku and TuranBank.

Primary source:
- https://www.cbar.az/page-838/bullion-coin-sales-agents

This is materially stronger than ordinary resale liquidity: there is an official repurchase channel and an explicit pricing band tied to the official gold rate.

## 2. Eligible coin anchor
CBAR's catalogue includes the Heydar Aliyev 100-year investment series. The 1 troy ounce coin is:
- gold Au 999.9;
- weight: 1 troy ounce;
- nominal: 100 AZN;
- issue year: 2023.

Primary source:
- https://www.cbar.az/page-840/investment-coins

The catalogue/current pricing page also exposes repurchase-price documents for 1 oz, 1/2 oz, 1/4 oz and 1/10 oz investment coins.

## 3. Repurchase-price reference data
One indexed official repurchase table parsed by the research tool reports, for 2026-07-16:
- 1 oz: **6,651.28 AZN**;
- 1/2 oz: **3,325.64 AZN**;
- 1/4 oz: **1,662.82 AZN**;
- 1/10 oz: **665.13 AZN**.

The same official document states condition gates including intact design/surface, undamaged packaging/certificate where applicable, and full weight/metal content.

Important cache note: the CBAR catalogue page currently labels newer pricing documents, while indexed PDF/screenshot layers returned inconsistent historical dates. Therefore these exact amounts are reference observations, **not a locked 2026-08-18 executable quote**. For execution the same-day agent quote must be used.

A separate official CBAR rate observation on 2026-07-31 gives XAU = **6,937.8275 AZN per troy ounce**. Under the published maximum 3% repurchase haircut, the rule-implied minimum at that observation is:

`1 oz floor = 6,937.8275 * 0.97 = 6,729.692675 AZN`.

For 1/10 oz:

`0.1 oz floor = 672.9692675 AZN`.

Source:
- https://www.cbar.az/currency/rates

Again: these are historical/reference calculations, not today's locked price.

## 4. Current secondary-market screen
Two recent indexed Azerbaijan marketplace asks were checked against the official mechanism.

### 1 oz CBAR coin
Lalafo listing:
- describes a Heydar Aliyev investment gold coin;
- 31.1 g / ~1 oz;
- 999.99 gold;
- ask: **9,950 AZN**.

Source:
- https://lalafo.az/

This is far above the ~6.65–6.73k official reference repurchase range. No arbitrage.

### 1/10 oz CBAR coin
Tap.az listing:
- Heydar Aliyev 100-year gold monetary sign;
- 3.11 g = 1/10 oz;
- 999.9 gold;
- ask: **880 AZN**.

Source:
- https://tap.az/

This is above the ~665–673 AZN official reference repurchase range. No arbitrage.

Derived screen:
- `data/derived/h068_coin_buyback_market_screen.csv`

## 5. Necessary condition for an executable sure spread
Let:
- `B` = same-day bank repurchase quote after authentication;
- `P` = seller acquisition price;
- `C` = transport/authentication/payment/other transaction costs;
- `T` = tax attributable to the transaction;
- `M` = required safety margin for price movement before settlement.

A candidate is worth executing only if:

`B - P - C - T - M > 0`

and, for strict project SUCCESS, every irreversible step must occur only after authenticity/condition/eligibility are locked.

### Strong execution pattern
The ideal transaction would be:
1. seller and buyer attend an appointed agent;
2. bank authenticates the exact coin and gives the applicable repurchase quote;
3. buyer only then pays the seller an agreed `P < B - all costs`;
4. title/possession transfers;
5. buyer immediately tenders the same authenticated coin for same-day bank repurchase.

The public material proves bank examination and same-day repurchase, but it does **not** yet prove that the agent will support a pre-payment authentication/conditional transfer workflow. That is the main execution-lock question.

## 6. Tax gate
A current State Tax Service Q&A dated 2026-06-02 says ongoing gold-sale activity is entrepreneurship and cannot use the simplified-tax regime for this activity; under an income-tax regime, profit after documented related expenses is taxable, with possible microenterprise relief only if its conditions are met.

Primary source:
- https://www.taxes.gov.az/

This does not establish the exact treatment of a one-off personal disposal. A repeated arbitrage strategy therefore requires transaction-specific tax treatment before terminal SUCCESS.

## 7. Result
### Validated
- official mandatory/agent repurchase mechanism exists;
- agent organizes authentication;
- repurchase is same-day;
- repurchase price is constrained to official gold rate minus at most 3%;
- current sampled marketplace asks exist for the same CBAR series.

### Failed in current live screen
The sampled 1 oz and 1/10 oz asks are well **above** official reference buyback levels. There is no positive spread in the observed listings.

### Remaining terminal gates
H068 can become a strict guaranteed-profit strategy only after all of these are simultaneously locked:
1. a live authentic eligible coin offered below the same-day repurchase quote by enough margin;
2. exact same-day agent buyback quote;
3. condition/authenticity confirmation before irreversible seller payment, or another enforceable seller-condition mechanism;
4. complete fees/transport/payment costs;
5. transaction-specific tax treatment;
6. immediate same-day repurchase execution.

## Reopen rule
Do not repeat generic gold searches. Reopen H068 only when either:
- a live CBAR investment coin ask falls below the contemporaneous Bank of Baku/TuranBank buyback quote by a material all-in margin; or
- an appointed agent confirms a workflow allowing authentication/quote before irreversible purchase.

## Current conclusion
**Mechanism class validated; current market screen negative; NOT SUCCESS.**

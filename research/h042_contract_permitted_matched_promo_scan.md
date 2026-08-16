# H042 — contract-permitted matched-promotion scan

Updated: 2026-08-16
Status: **mechanism strengthened; no current executable terminal guarantee found**

## Question
H041 proved that an already-earned stake-not-returned free-bet token can be converted into an outcome-independent positive cash floor after an opposing lay is fully matched. The remaining bottleneck is contractual/acquisition risk: can we find a current promotion whose terms permit the hedge and whose reward is deterministic for an eligible user?

This packet screens exchange-centric operators because they are the most plausible place for a promotion and the hedge to coexist without a generic anti-arbitrage clause.

## 1. Betfair — negative contractual control
Current Betfair standard promotion terms explicitly cover the case where promotion play creates guaranteed wins/profits with no or minimal risk and reserve remedies including invalidation/withholding. Therefore Betfair remains unsuitable for a strict contractual guarantee even when the mechanical hedge is perfect.

Sources:
- https://www.betfair.com/en/aboutUs/Terms.and.Conditions/
- https://support.betfair.com/app/answers/detail/6244-sportsbook-free-bet-faq/

Conclusion: **REJECTED for strict promotion-backed guarantee**.

## 2. Matchbook — important positive contract signal, but no current token source
Matchbook's current Standard Promotional Terms state that an unrestricted Free Bet may be played on an exchange bet; the stake is not returned; free bets cannot be cashed out/edited; and API users are excluded from promotions. In the retrieved standard terms, no generic clause equivalent to Betfair's explicit “guaranteed/minimal-risk profit” prohibition was found.

This is materially stronger than H041's Sky/Betfair examples: the issuer is itself an exchange and its promotion framework explicitly contemplates exchange free bets.

A 2026 PredictStreet/Matchbook offer (“Bet £20, Get £26 in Free Bets”) provides an informative specific-term control. It expressly prohibited trading the **qualifying** selection and “manipulative trading strategies,” and excluded signups from matched-betting affiliates. However its free-bet section did not separately state that a later cash opposing position to a credited free-bet token was prohibited. The offer expired **2026-07-30**, before this screen, so it is not executable now.

Sources:
- https://www.matchbook.com/page/rules_and_regulations/standard-promo-terms-and-conditions
- https://welcome.matchbook.com/WC2026

Conclusion: **PROMISING CONTRACT ARCHITECTURE, but no current deterministic executable token source verified**.

## 3. BETDAQ — current commission subsidies do not create a standalone surebet
BETDAQ currently advertises a new-customer **0% exchange commission for 100 days** promotion running through **2026-12-31** for UK/Irish customers. It also advertises DAQBACK, refunding first-month exchange commission as withdrawable cash up to the stated cap.

These are real deterministic cost subsidies, but they refund/remove commission rather than adding outcome-independent external value.

Let `G` be pre-commission trading profit in an outcome, `C >= 0` commission that would otherwise be paid, and `r in [0,1]` the refunded fraction. Then:

`P = G - (1-r)C <= G`.

Therefore if the underlying fully hedged position has `G <= 0`, a commission-only rebate cannot make that outcome strictly positive. At `r=1` it can at best recover the zero-commission result `P=G`. A genuine pre-commission price arbitrage is still required.

Implemented:
- `src/loto_research/commission_subsidy.py`
- `tests/test_commission_subsidy.py`

Sources:
- https://promotions.betdaq.com/
- https://promotions.betdaq.com/daqback/

Conclusion: **VALID cost reducer / H020 overlay; REJECTED as standalone guaranteed-profit source**.

## 4. BetConnect — hedge venue explicitly friendly to matched betting, but geography and acquisition remain
Current BetConnect support describes the service as an exchange-like back/lay marketplace and explicitly says its 0% lay commission is attractive to matched bettors. Its current signup guidance requires UK/Northern Ireland residence and a UK/NI bank account. Current general bonus-abuse terms focus on multiple accounts/bad-faith claiming; no current public deterministic free-bet acquisition offer was found in this screen.

Older operator-authored matched-betting material is unusually explicit that the service is built to lay bookmaker qualifying bets and convert free bets; this is useful mechanism validation but is not a current promotion guarantee.

Sources:
- https://support.betconnect.com/hc/en-gb/articles/10859349411869-Is-BetConnect-an-exchange
- https://support.betconnect.com/hc/en-gb/articles/10858475095709-I-want-to-join-BetConnect-How-do-I-sign-up
- https://info.betconnect.com/terms-conditions/

Conclusion: **VALID hedge venue class; no current deterministic reward source and not executable from Azerbaijan under stated signup requirements**.

## New theorem / strategic narrowing
H041's problem decomposes into three independent gates:

1. **Acquisition gate** — the promo reward must be deterministic after actions we can hedge without violating terms.
2. **Conversion gate** — the credited value must be convertible into an outcome-independent cash floor via a fully matched opposing market.
3. **Contract gate** — neither the qualifying hedge nor conversion hedge may trigger a no-risk/arbitrage/clawback clause.

H041 already validates gate 2. H042 shows that gate 3 is not universally impossible: exchange-centric contracts can be materially friendlier than sportsbook promo contracts. The unresolved gate is now primarily **current deterministic acquisition**.

## Data
- `data/derived/h042_contract_gate_screen.csv`

## Current conclusion
- Contract-permitted matched betting: **real mechanism class**.
- Current BETDAQ 0%-commission/commission-refund promotions: **real but insufficient alone**.
- Current BetConnect: **useful hedge venue, geography-gated, no deterministic public bonus found**.
- Matchbook exchange-free-bet framework: **best contractual lead**, but the concrete 2026 token offer recovered here is expired and had qualifying-trade restrictions.
- Strict guaranteed positive net profit executable now: **NOT FOUND**.

## Next highest-value branch
Search for a **current deterministic free-bet/credit issuer whose specific and incorporated general terms do not forbid external hedging**, especially offers where:
- qualifying action is tiny or itself hedgeable without violating terms;
- reward is fixed rather than random;
- reward winnings are withdrawable;
- no matched-betting affiliate / no-risk / arbitrage / irregular-play exclusion applies;
- geography is actually executable for the target user, or the result is explicitly classified as jurisdiction-limited rather than SUCCESS.

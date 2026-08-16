# H043 — acquisition-first free-bet / credit screen

Updated: 2026-08-16
Status: **mechanism class survives, but no current Azerbaijan-executable terminal candidate found**

## Goal
Start from the missing H041/H042 gate: find a deterministic source of promotional betting value that can be converted into an all-outcome cash floor without violating incorporated terms.

Required gates for terminal SUCCESS:
1. **Acquisition** — promo/token is deterministically earned under known actions, not awarded randomly/targeted after the fact.
2. **Conversion** — token can be paired with compatible opposing liquidity so minimum cash after settlement exceeds acquisition + hedge costs.
3. **Contract** — neither the specific offer nor incorporated general terms can claw back the value for guaranteed/minimal-risk/arbitrage play.
4. **Jurisdiction/execution** — the user can lawfully open/use the required accounts from Azerbaijan and obtain/withdraw winnings.
5. **Irrevocability** — all hedge legs are accepted/matched before exposure begins; void/settlement mismatch is controlled.

H041 already proves the conversion algebra for stake-not-returned free bets. This packet screens acquisition/contract/jurisdiction.

## Current operator screen

### 1. Spreadex — strongest structural lead, but jurisdiction-failed
Current indexed promotion pages include account-targeted **free fixed-odds reward bets**. One page explicitly describes the reward as risk-free and requiring **no qualifying bets**. Another generic fixed-odds free-bet page says the token can be split and, for some versions, cash-out is allowed if cash-out value exceeds the free-bet stake.

Relevant pages:
- https://www.spreadex.com/sports/free-fixed-odds-bet-reward/
- https://www.spreadex.com/sports/fixed-odds-free-bet-offer/
- https://www.spreadex.com/sports/free-bet-on-deposit/

This is important because it demonstrates a real acquisition class with zero incremental wagering requirement once the token is actually allocated to an account. The retrieved promo terms contain generic anti-abuse/collusion discretion, but no explicit Betfair/Betway-style sentence banning an external hedge merely because it produces low or guaranteed risk.

However Spreadex's current Restricted Territories page states fixed-odds services are licensed for **UK, Ireland and Denmark** and are restricted for people living outside those territories:
- https://www.spreadex.com/sports/terms-agreements/restricted-territories/

Therefore an Azerbaijan resident cannot use this as the project's current executable terminal strategy.

Also, these reward pages are account-targeted: the value/expiry appears in `My Promotions`. That means public existence of the reward is not deterministic proof that a newly opened eligible account will receive it.

**Result:** architecture-promising / jurisdiction + allocation gate failed for current user.

### 2. Matchbook — permissive token mechanics, but current acquisition offers stale/expired or non-deterministic
Matchbook standard promotional terms allow a free bet to be used on an exchange market, with stake-not-returned mechanics:
- https://www.matchbook.com/page/rules_and_regulations/standard-promo-terms-and-conditions

The specific `CHAMPIONS` offer is indexed as running through **2026-08-31**, but qualifying requires a £20 bet on a team to win the **2025/26 Premier League**. By 2026-08-16 that competition is already settled, so the qualifying market is no longer a live executable acquisition route. The offer also excludes same-selection back/lay volume and manipulative trading strategies from qualification.

Source:
- https://www.matchbook.com/page/rules_and_regulations/podcast-offer-terms-conditions/

PredictStreet/Matchbook pages still display World Cup welcome offers such as Bet £20/Get £26 or Bet £30/Get £66, but H042 recovered the specific WC2026 terms with an end date of **2026-07-30**. The current front-end page is therefore treated as stale until specific live terms prove otherwise.

**Result:** contract architecture remains interesting; no current deterministic acquisition source established.

### 3. bet365 — acquisition exists, contract gate fails
A current Bulgaria-localized welcome bonus offers a 100% matched bonus up to €200 after qualifying deposit/rollover, but bet365 general terms explicitly identify arbitrage / betting all possible outcomes to guarantee profit as grounds for account action. Offer terms also contain guaranteed-profit clawback language for enhanced payments/free bets in promotion contexts.

Sources:
- https://www.bet365.com/promos/en-bg/home/open-account-global-offer
- https://help.bet365.com/s/en-gb/terms-and-conditions

Even if jurisdiction were otherwise workable, this cannot support strict terminal guarantee under the project standard.

**Result:** contract gate failed.

### 4. Betway — contract gate fails explicitly
Current 2026 promo terms say combinations of free-bet and cash wagers on the same event that create equal/zero-margin or hedge positions are irregular gaming and may lead to withheld withdrawals/confiscation.

Source:
- https://betway.com/terms-and-conditions/en?promoid=1113840

**Result:** contract gate failed.

### 5. Rivalry — contract gate fails explicitly
Current promotional terms classify betting all likely outcomes, equal/zero-margin betting, and hedge betting intended to guarantee promotional profit as irregular betting.

Source:
- https://www.rivalry.com/terms/promo-terms

**Result:** contract gate failed.

### 6. Winz — Azerbaijan explicitly excluded
Current sports welcome promotion terms explicitly list **Azerbaijan** among excluded countries.

Source:
- https://www.winz1.me/promotions/welcome-sports

**Result:** jurisdiction gate failed.

## H043 acquisition theorem / classification
A no-deposit or no-qualifying-bet free token is not itself terminal SUCCESS. It advances the search because its acquisition cost can be zero, but strict guaranteed cash still needs conversion + contract + jurisdiction gates.

For a stake-not-returned free bet of face `F`, backed at decimal odds `O` and externally laid at odds `L` with commission `c`, the H041 equalized conversion produces positive cash only after the lay is irrevocably matched. If `F` was acquired at zero incremental cost, any strictly positive converted floor is mechanically a profit. Therefore the remaining difficulty is overwhelmingly **contract + executable acquisition**, not mathematics.

This packet identifies a particularly strong future trigger:

> **Zero-cost allocated token + external hedge explicitly permitted (or operator-issued exchange token with normal opposing trading permitted) + Azerbaijan-accessible accounts + matched liquidity = immediate H041 terminal candidate.**

## Current conclusion
- Deterministic zero-incremental-cost token class: **exists in real operator promotions**.
- Contract-permitted conversion architecture: **exists as a class (H042)**.
- Same offer satisfying acquisition + contract + Azerbaijan jurisdiction simultaneously: **NOT FOUND on 2026-08-16**.
- Terminal SUCCESS: **NO**.

## Next research priority
1. Search operators/exchanges actually accepting Azerbaijan residents for **allocated/free-token** offers without anti-hedge clauses.
2. Search issuer-side exchange promotions where token use on exchange markets and ordinary opposing trading are explicitly permitted; distinguish self-matching/collusion from independent-counterparty hedging.
3. Search deterministic withdrawable **cash** rebates rather than free bets, because cash collapses the conversion gate.
4. If none exists, return to H020 live post-fill cross-venue arbitrage when raw order books become accessible.

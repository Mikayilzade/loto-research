# STATUS

Updated: 2026-08-17
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H052 upfront insured-interest candidate isolated**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H052 — newest packet
File:
- `research/h052_upfront_insured_interest.md`

## New strongest current guarantee candidate
Two current Azerbaijan bank products explicitly combine **interest paid in advance** with deposit-insurance claims:

### Expressbank — Əlavə fürsət
- AZN;
- minimum 500 AZN;
- 12/18/24 months;
- interest paid **in advance**;
- current official indexed rate around 9.5% (official page has recently shown 9.5–10% depending crawl date);
- product page states the deposit amount is insured by the Deposit Insurance Fund.

### VTB Azerbaijan — Avans
- AZN;
- minimum 500 AZN;
- 12–36 months;
- interest received immediately after deposit registration;
- current table: 1y 9.25%, 1.5y 9.5%, 2y 8.75%, 3y 7.75%.

## Why H052 is materially stronger than H051
For principal `P`, separately vested upfront cash reward `R`, minimum recoverable principal `C`, and unavoidable costs `F`, strict floor is:

`G = R + C - P - F`.

If prepaid interest is irrevocably paid and **the full original principal remains the protected insured balance** (`C=P`), then any `R>F` creates a deterministic positive floor. At the minimum 500-AZN size, 9.5% is 47.50 AZN gross upfront reward.

This eliminates H051's immediate-failure problem **only if** insolvency cannot claw back/set off the prepaid interest or reduce insured principal by the unearned prepaid amount.

## Current blocker — narrow contract/accounting question
Current public product pages prove upfront payment + advertised insurance, but do not expose enough product-specific liquidation wording to prove whether:
1. full principal `P` remains the insured deposit balance after the upfront interest is credited;
2. upfront interest is separately vested and withdrawable;
3. an insurance event cannot trigger recoupment/setoff/principal reduction equal to prepaid unearned interest.

The current Azerbaijan Deposit Insurance Law pays 100% of insured deposit balance up to 100,000 AZN and separately limits interest compensation to interest accrued by the insurance-event date. Expressbank's current general conditions defer early-interest recalculation to the individual product agreement. Older/general Azerbaijan prepaid-interest forms show that voluntary early termination can recoup prepaid interest from principal, which prevents assuming the favorable insolvency treatment without the current contract.

**H052 status: PROMISING / INCONCLUSIVE — not SUCCESS yet.**

# H051 — prior packet
File:
- `research/h051_regulated_deposit_fixed_reward_screen.md`

Ordinary insured deposits strongly protect principal but fail strict guaranteed-profit status because an immediate insurance event can make accrued interest arbitrarily close to zero.

# H050 / H049
- Bitget Cash Plus: principal protection but dynamic APR; no locked positive minimum before commitment.
- Historical USDGO make-whole + retained yield: valid mathematical construction, but current fixed retail overlap not proven.

# Strongest non-terminal positive-EV lottery result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain materially below modeled break-even participation. Strong +EV overlay remains, but recipient selection is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 live two-sided arbitrage: mechanism validated; non-terminal without vested subsidy.
- H019 capped fixed-prize saturation: valid in principle; sampled instances fail full-cap cash-floor economics.
- H007 high-frequency RNG: data-gated; trustworthy ordered bulk history missing.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# General terminal gates now established
Any SUCCESS must prove all of:
1. contract permission / irrevocability;
2. complete execution/fill;
3. settlement isomorphism for cross-product hedges where relevant;
4. strictly positive void/cancellation floor;
5. commissions, taxes, funding/FX, limits and withdrawals included;
6. promotion/rebate entitlement survives every allowed branch;
7. principal redemption/make-whole and a strictly positive reward must be simultaneously eligible and fixed before capital is committed;
8. for principal-protected yield products, dynamic APR or vague `up to` yield is insufficient; capture a locked positive minimum payout;
9. for insured deposits, principal protection plus post-opening accrued interest is insufficient unless the minimum protected reward is already strictly positive even for an immediate insurance event;
10. for **prepaid-interest deposits**, prove that the prepaid reward remains separately vested and does not reduce/offset insured principal under bank insolvency or forced liquidation.

# Next priorities
1. **H052 decisive contract test:** recover the current Expressbank `Əlavə fürsət` and VTB `Avans` individual deposit agreement / standard information form; isolate prepaid-interest treatment under insurance event, insolvency, forced liquidation, setoff and early termination.
2. If full insured principal survives the prepaid reward, immediately bound tax, account/card, cash-out/transfer and funding costs and test the 500-AZN minimum as a candidate terminal SUCCESS.
3. Search additional current Azerbaijan prepaid-interest deposits for a contract whose insolvency accounting is public and explicit.
4. Capture live subscription/order terms for any principal-guaranteed structured product with locked non-reducible minimum return.
5. H020 live arbitrage only if paired with a vested subsidy.
6. H037 broaden controls / recalculate after autumn-2026 rule change.
7. H019 only if capped-entry economics materially improve.
8. H006/H007 after reliable histories/machine metadata become obtainable.
9. H010/H014 if new authoritative data routes appear.
10. Before EXHAUSTED: additional deterministic action/rebate scans, Bayesian hidden-state inference and causal implementation tests.

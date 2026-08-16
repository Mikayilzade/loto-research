# STATUS

Updated: 2026-08-17
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H052 narrowed to VTB Avans product-specific Application-Agreement**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H052 — newest packet
File:
- `research/h052_upfront_insured_interest.md`

## Current candidate
Two current Azerbaijan bank products explicitly combine **interest paid in advance** with deposit-insurance claims:

### Expressbank — Əlavə fürsət
- AZN;
- minimum 500 AZN;
- 12/18/24 months;
- interest paid **in advance**;
- current rate table 9.50% / 9.00% / 9.00%;
- official page says the deposit amount is insured by the Deposit Insurance Fund.

### VTB Azerbaijan — Avans
- AZN;
- minimum 500 AZN;
- 12–36 months;
- interest available immediately after registration;
- current page observed 2026-08-17: **9.25% / 9.50% / 8.75% / 7.75%** for 12/18/24/36 months;
- product remains listed on VTB's current retail-deposit page.

## NEW — current VTB general agreement recovered
VTB's official documents page publishes the latest retail `Bank Xidmətlərinin Göstərilməsi haqqında Müqavilənin Ümumi Şərtləri`, effective **06.01.2025**.

Deposit clauses materially narrow the H052 uncertainty:
- 6.1: important product conditions live in the individual `Ərizə-Razılaşma`;
- 6.11–6.13: customer-requested early withdrawal / early interest treatment;
- **6.14:** when the early-payment/early-withdrawal case occurs, previously paid interest is deducted from principal;
- 6.21: on insurance event, matured depositor obligations to the bank are deducted from protected deposit compensation.

Crucially, the recovered recoupment clause is textually tied to **customer-requested early withdrawal**. The public general deposit section does **not** state that bank insolvency / Deposit Insurance statutory maturity automatically triggers the same prepaid-interest recoupment.

The Deposit Insurance Law separately deems unexpired deposits **matured** when compensation is announced. Therefore statutory forced maturity is not textually identical to the customer `vaxtından əvvəl` withdrawal branch in VTB 6.11–6.14.

## H052 status after this run
This materially strengthens VTB Avans relative to the prior checkpoint, but it is still **not SUCCESS** because clause 6.1 makes the product-specific `Avans` Application-Agreement decisive and that document was not publicly recovered.

Remaining possible disqualifiers in the missing Application-Agreement:
- lien/block over principal equal to prepaid interest;
- automatic recoupment on any termination/maturity event;
- explicit treatment of statutory forced maturity as recoupment-triggering;
- separate due obligation for unearned prepaid interest.

If none exists, then within the insurance limit the candidate can potentially satisfy `C=P`, leaving upfront reward `R` as a strictly positive floor after bounded costs. At the 500-AZN minimum and current 12-month 9.25% VTB rate, gross upfront interest is about **46.25 AZN** before tax/costs.

Current H052 state: **PROMISING / INCONCLUSIVE — decisive gap now mostly the Avans `Ərizə-Razılaşma` or explicit VTB/ADIF interpretation.**

# H051 — prior packet
Ordinary insured deposits protect principal strongly but fail strict guaranteed-profit status because an immediate insurance event can leave accrued interest arbitrarily close to zero.

# H050 / H049
- Bitget Cash Plus: principal protection but dynamic APR; no locked positive minimum before commitment.
- Historical USDGO make-whole + retained yield: valid construction historically, but current fixed retail overlap not proven.

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
10. for **prepaid-interest deposits**, prove that the prepaid reward remains separately vested and does not reduce/offset insured principal under bank insolvency or forced liquidation;
11. where prepaid interest is secured by a principal lien/block, prove the lien cannot become an offsettable due obligation on the insurance-event branch.

# Next priorities
1. **H052 decisive VTB document:** recover current `Avans` `Ərizə-Razılaşma` / individual deposit agreement. This is now the highest-value single missing document.
2. Recover current Expressbank `Əlavə fürsət` individual agreement / standard terms and compare forced-maturity accounting.
3. Search authoritative VTB/ADIF interpretation of prepaid interest when an insurance event occurs before original contractual maturity.
4. If a product explicitly preserves full insured principal after prepaid reward, immediately bound tax, account/card, cash-out/transfer and funding costs at minimum size and test terminal SUCCESS.
5. Search additional current Azerbaijan prepaid-interest products only where product-specific terms are public enough to resolve the same branch.
6. H020 live arbitrage only if paired with a vested subsidy.
7. H037 broaden controls / recalculate after autumn-2026 rule change.
8. H019 only if capped-entry economics materially improve.
9. H006/H007 after reliable histories/machine metadata become obtainable.
10. H010/H014 if new authoritative data routes appear.
11. Before EXHAUSTED: additional deterministic action/rebate scans, Bayesian hidden-state inference and causal implementation tests.

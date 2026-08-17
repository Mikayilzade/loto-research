# H053 — deterministic bank cashback / welcome-subsidy screen

Updated: 2026-08-17
Status: **ACTIVE CURRENT SUBSIDIES FOUND; standalone guaranteed cash-profit not proven**

## Question
Can a current Azerbaijan bank promotion create a deterministic positive cash floor that survives all allowed branches, without relying on lottery luck, resale value, or an unsafe refund loop?

The relevant structure is:

`net = vested_cash_subsidy + guaranteed_recovery_of_qualifying_spend - qualifying_spend - unavoidable_fees`.

For terminal SUCCESS, the qualifying spend itself must either be recoverable as cash/principal or be an already-unavoidable expense explicitly accepted as baseline. A discount/cashback on discretionary consumption is economically useful but is not standalone net cash profit from zero.

## Current live screens

### ABB — 3% cashback on foreign payments
Official ABB help-center page, current on 2026-08-17:
- campaign runs **7 August–7 September 2026**;
- customer must order/own ABB shares and hold a TamKart Mastercard;
- 3% cashback on payments abroad and foreign websites;
- campaign cashback cap **50 AZN**;
- cashback is additional to the ordinary cashback package.

Primary source:
- https://destek.abb-bank.az/en/articles/100-3percent-cashback-on-payments-abroad

This is a real deterministic percentage subsidy conditional on qualifying settled purchases, but it does not by itself return the purchase principal. ABB-share acquisition/ownership is also an eligibility condition with its own market/execution cost. Therefore the promotion is not a standalone guaranteed-profit construction.

### Yelo — Welcome cashback package
Current Yelo cashback page states:
- first-time Yelo card customers receive the **Welcome** cashback package free for 30 days;
- cashback applies to eligible retail purchases and is calculated in AZN equivalent;
- current published categories include material percentages such as supermarkets, hotels, cinemas, ADY, AzParking and others depending on package.

Primary source:
- https://yelo.az/az/individuals/cashback/

Again, this is a deterministic subsidy on eligible consumption, not a principal-returning leg. It can reduce an expenditure the customer would have made anyway, but it cannot certify positive standalone cash profit without a separately guaranteed conversion/recovery mechanism.

### Kapital Bank / BirKart — 30 AZN gift after 100 AZN cashless turnover
A currently indexed official Kapital Bank campaign page states:
- **30 AZN** is credited to the card balance after one-time or cumulative **100 AZN cashless turnover** within the first 30 days after card receipt;
- campaign page says valid until **31 August** and online card orders only;
- benefit can be received once;
- card has a monthly service fee unless the relevant turnover waiver is met.

Primary source:
- https://www.kapitalbank.az/en/kampaniyalar/birkart-sifarisi-30-azn-cashback-qazandirir-4

Caution: the indexed page does not display an explicit year in the visible campaign text and currently redirects when opened, so this is not promoted to a verified 2026 executable offer without a fresh date-bearing source.

Even if current, a 30-AZN subsidy after 100-AZN discretionary retail spend is not standalone guaranteed cash profit because the 100 AZN purchase principal is consumed. If the same 100 AZN replaces an unavoidable expense, it can be a conditional savings edge, not a zero-capital arbitrage proof.

## General theorem for retail-spend cashback
Let:
- `S > 0` = qualifying retail spend;
- `B > 0` = deterministic cashback/bonus;
- `V_min` = guaranteed cash-recoverable value of the acquired good/service across all allowed outcomes;
- `F` = unavoidable fees/costs.

Then the strict cash floor is:

`G = B + V_min - S - F`.

For ordinary consumption, `V_min` is not contractually equal to `S`; frequently it is 0 in strict cash terms. Therefore cashback percentage `<100%` cannot establish a standalone positive cash floor.

A true terminal candidate requires one of:
1. `V_min = S` by contract/law (principal-returning or fully refundable with bonus explicitly surviving refund);
2. `B > S + F` even with `V_min=0`;
3. an already-unavoidable spend baseline, in which case the result is guaranteed incremental savings rather than standalone cash arbitrage.

## Refund-loop control
A refund/reversal cannot be assumed to preserve cashback. Current Azerbaijan campaign rules commonly exclude or reverse benefits on returned transactions; for example recent Birbank and ABB campaigns explicitly state reversal/clawback treatment. Therefore `buy -> receive cashback -> refund purchase` is not accepted as a guaranteed mechanism unless the exact current contract expressly preserves the benefit after refund.

## Result
Current Azerbaijan banking promotions do contain deterministic, non-lottery subsidies, but the live examples found in this packet are tied to real consumption or eligibility costs. None yet supplies a contractually guaranteed `principal return + vested cash bonus` pair.

Status: **NO SUCCESS**.

## Next high-value branch
Search current offers where the qualifying action preserves principal by construction, especially:
- cash deposit / account funding bonuses with withdrawable principal;
- salary-transfer/account-switch cash incentives with no minimum unrecoverable spend;
- broker/bank cash bonuses for holding cash or government-backed assets where principal floor is contractual;
- fee rebates that exceed an otherwise fully reversible/returnable principal leg and explicitly survive cancellation.

Do not use merchandise resale value as a guarantee and do not assume refunds preserve cashback.
# H096 — Azerbaijan employment / self-employment / liberated-territory subsidy screen

Updated: 2026-08-19
Status: **VALIDATED CURRENT SUBSIDY CLASSES / NO STANDALONE GUARANTEED-PROFIT CONSTRUCTION FOUND**

## Goal
Continue the deterministic-subsidy search after H094/H095. Screen current Azerbaijan programs where a participant receives cash reimbursement, wage co-financing, social-insurance reimbursement, utility support, or in-kind assets, and test whether any mechanism by itself creates a strictly positive worst-case net cash/asset floor after mandatory costs.

The terminal standard remains stricter than positive EV: the subsidy/entitlement must be lockable before irreversible cost and must leave strictly positive net value under every compliant execution branch.

## 1. Liberated territories — mandatory social-insurance reimbursement
Current official Economy Ministry / State Tax Service material confirms:
- employer-paid compulsory state social-insurance contributions in liberated territories are subsidized **80% during 2026–2028** (then 60%, then 40%);
- qualifying self-employed / individual entrepreneurs pay their own compulsory state social-insurance contribution and receive a **100% subsidy through 2032**;
- some sectors/contractors are excluded.

Primary sources:
- https://economy.gov.az/az/page/qarabag-azerbaycandir
- https://www.taxes.gov.az/az/post/2271

### Guarantee test
Let `C_ss > 0` be a legally required social-insurance payment and `r` the reimbursement rate.

Standalone incremental cash after the reimbursement is:

`net = -C_ss + r*C_ss = -(1-r) * C_ss`.

Therefore:
- self-employed 100% subsidy: `net = 0` before registration/admin/compliance costs;
- employer 80% subsidy in 2026–2028: `net = -0.20*C_ss` before other payroll costs.

The program can improve the economics of a real business but **cannot by itself create positive cash from the reimbursed contribution**.

Status: **REJECTED as standalone guaranteed-profit subsidy; retain only as overlay on independently profitable activity**.

## 2. Liberated territories — utility support
The official Economy Ministry page confirms qualifying production residents can receive **20% financial assistance** on paid electricity, gas, water and wastewater utility charges through 2032.

Primary source:
- https://economy.gov.az/az/page/qarabag-azerbaycandir

### Guarantee test
For qualifying utility spend `U > 0`:

`net direct subsidy cycle = -U + 0.20U = -0.80U`.

No standalone positive floor exists without productive output whose value exceeds the remaining 80% + all other costs.

Status: **REJECTED standalone / VALIDATED cost-reduction overlay**.

## 3. Social workplaces — 50% wage + payroll co-financing
Current State Employment Agency guidance states:
- private/non-municipal employers active for the required period may apply;
- approved social jobs are financed for a defined period (current registry/FAQ: employment contract at least 6 months; financing for half of contract duration, capped at 12 months);
- the Agency finances **50% of the salary and specified payroll deductions**, subject to the national-average-wage cap;
- applications are analyzed and can be approved or refused.

Primary sources:
- https://dma.gov.az/fealiyyet/funksional-istiqametler/sosial-terefdaslarla-is/emekhaqqinin-maliyyelesidirlmesi
- https://dma.gov.az/reyestrler/birge-maliyyelesme-reyestr?hl=az
- https://dma.gov.az/fealiyyet/sual-cavab?hl=az

### Guarantee test
If the gross eligible payroll cost is `W`, the direct program component is approximately:

`net before employee output = -W + 0.5W = -0.5W` (subject to caps and excluded extras).

The employee may create value, but that is ordinary business execution risk. There is no guaranteed positive floor from the subsidy alone. Entry is also approval-dependent rather than an automatic entitlement.

Status: **REJECTED standalone / VALIDATED labor-cost overlay**.

## 4. 2026 pilot for beneficiaries of the Employment Support Project
A January 28, 2026 official Ministry announcement describes a pilot for beneficiaries who hire workers into small businesses created under the Employment Support Project:
- first 3 months: **100% of wages plus related employer/employee tax/social deductions** paid by the project;
- next 3 months: **50%**;
- cooperation agreements are signed with participants.

Primary source:
- https://sosial.gov.az/az/media/xeberler/mesgulluga-destek-layihesi-istirakcilarina-ve-hessas-qruplar-ucun-is-yerlerinin-yaradilmasina-daha-bir-destek-8930

### Guarantee test
For the first three months the reimbursed payroll itself can reach a zero direct employer cost (`-W + W = 0`), not a positive cash payment above payroll. The next three months are negative before worker output. Profit therefore requires productive business output, and eligibility is restricted to project beneficiaries plus program procedures.

Status: **REJECTED standalone / PROMISING overlay for an already profitable eligible microbusiness**.

## 5. Self-employment program — in-kind assets transfer after one compliant year
Current Ministry / State Employment Agency pages confirm:
- eligible applicants are unemployed persons, plus certain land-share holders without other employment;
- applicants pass suitability review, training/business-plan stages and evaluation;
- material/equipment/property is provided **in kind for one year under contract**;
- activity is monitored;
- if activity remains compliant with the approved business plan through the contract period, the supplied property is transferred into the participant's ownership;
- unjustified non-use can require return of the property or its market value.

Primary sources:
- https://sosial.gov.az/az/fealiyyet/fealiyyet-istiqametleri/mesgulluq-xidmetleri/ozunumesgulluq/ozunumesgulluq-proqrami
- https://dma.gov.az/fealiyyet/funksional-istiqametler/issiz-ve-isaxtaranlarla-is/ozunemes
- https://www.dma.gov.az/fealiyyet/funksional-istiqametler/ozunumesgulluq

### Why this is structurally stronger than a simple reimbursement
Unlike a 20%/50% cost rebate, the program can transfer a positive-value productive asset without a stated participant purchase price. In principle this can create a positive balance-sheet subsidy after one compliant year.

However a strict guaranteed-profit theorem is **not** yet available because:
1. entry is not unconditional — suitability, training/business-plan assessment and program allocation precede asset delivery;
2. the participant must actually run the approved activity for one year and pass monitoring;
3. operating, registration, premises, consumables, maintenance and time costs depend on the selected package;
4. the one-year residual market value / liquidation value of the supplied assets is not fixed by the program;
5. premature non-use can trigger return of property or market value.

A future executable proof would need an **already-approved participant + signed contract + exact asset package + locked one-year minimum compliant operating cost + conservative realizable asset value after ownership transfer** with `asset_floor + business_cash_floor > all costs`.

Status: **MECHANISM VALIDATED / STRONG LEAD / APPROVAL + ONE-YEAR EXECUTION-GATED / NOT SUCCESS**.

## Necessary-condition summary
| Mechanism | Direct support rate | Standalone deterministic floor from subsidy alone |
|---|---:|---:|
| Self-employed social insurance, liberated territories | 100% of qualifying contribution | 0 before admin costs |
| Employer social insurance, liberated territories (2026–2028) | 80% | negative 20% of contribution |
| Utility support, liberated territories | 20% | negative 80% of utility cost |
| Social-workplace payroll co-financing | 50% subject to cap | negative 50% of eligible payroll before output |
| Employment Support pilot, first 3 months | 100% payroll + specified deductions | 0 before non-payroll costs / output |
| Self-employment assets | in-kind property after compliant year | potentially positive asset transfer, but no fixed liquidation floor and approval/execution conditions remain |

## Strategic conclusion
H096 closes several tempting reimbursement loops by the same necessary condition: a reimbursement at or below the qualifying cost does not create positive standalone cash. The **self-employment asset-transfer program is the only materially stronger lead in this packet**, because it can confer positive-value property without an explicit matching purchase payment, but strict SUCCESS would require a specific approved contract/package and one-year cost/value floor.

Next subsidy search should prioritize mechanisms that pay **more than the participant's unavoidable incremental cost**, or grant a transferable/cash-redeemable asset with a legally fixed floor after approval.

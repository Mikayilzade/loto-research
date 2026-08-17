# H056 — Azerbaijan-compatible fixed-cash referral / funding rewards

Updated: 2026-08-17
Status: **MECHANISM VALIDATED; STRONG CURRENT LEAD; NOT TERMINAL SUCCESS**

## Goal
Continue H055 with the missing geography gate: find a current regulated provider that explicitly onboards Azerbaijan residents and pays a **fixed cash** reward rather than shares, points, lottery credit, or variable yield.

## Strongest current lead — Interactive Brokers Refer-a-Friend
Primary current sources:
- IBKR available countries: https://www.interactivebrokers.com/en/accounts/open-account-country-list.php
- Current referral page: https://www.interactivebrokers.com/en/trading/referral-member-to-member.php
- Current program agreement dated 2 July 2026: https://ndcdyn.interactivebrokers.com/aces/Agreement/AgreementVersion/4841

### Geography gate — PASSED at platform level
IBKR's current Available Countries and Territories page explicitly lists **Azerbaijan**.

The current referral-program exclusions list residents of mainland China, Spain, Portugal, Japan, Denmark, Israel and Poland. Azerbaijan is not in that named exclusion list. The agreement still preserves a residual exclusion where local law/regulation prohibits participation.

Therefore H055's prior problem — no proven Azerbaijan-accessible fixed-cash mechanism — is materially narrowed for IBKR.

### Fixed-cash leg — VALIDATED
Current public program terms state that the **Referring Client receives a flat USD 200 payment per eligible referral**.

Conditions for the USD 200 referrer payment:
- referred person opens via the unique referral link;
- referred person deposits at least **USD 10,000 within 30 days**;
- referred person maintains at least USD 10,000 for **one year**;
- referrer is an eligible IBKR individual/joint client;
- current public referral page says referrer must have account NLV at least **USD 2,000** and have placed at least one securities trade;
- no payment when referrer and referred client are family members or live at the same exact physical address;
- referrer cannot refer their own account and must not assist/control the referred account after referral.

This is structurally stronger than H054's referred-client stock award because the referrer's reward is a **fixed cash amount**, not market-valued shares.

## Guarantee accounting
For the referrer, define:
- `B = 200 USD` fixed contractual payment if all program conditions are satisfied;
- `F = all marginal costs`, including required qualifying trade, funding/withdrawal/FX, tax, and any account-maintenance costs;
- `G = B - F` because the referred client's USD 10,000 is not the referrer's capital and the referrer's own NLV requirement is an eligibility condition rather than a consumed stake.

If `F < 200` and entitlement were irrevocably fixed once the referral conditions are met, this would be a positive deterministic cash reward.

## Why this is NOT terminal SUCCESS
The current agreement contains several branches incompatible with the project's strict all-outcome guarantee standard:

1. **Program amendment / termination discretion** — IBKR may change the terms in its sole discretion and may close the program to new participants.
2. **Eligibility discretion** — account eligibility is determined by IBKR under policies that may vary over time and jurisdiction.
3. **Anti-abuse discretion** — accounts established to improperly exploit, abuse, or undermine the program are ineligible, as determined by IBKR.
4. **Independent-person dependency** — the referred client must independently open, fund, and maintain the account; the referrer is contractually prohibited from controlling or assisting that account after referral.
5. **Residual local-law gate** — rewards are not paid where IBKR confirms local law/regulation prohibits participation. Azerbaijan is available for account opening and is not named in the referral exclusion list, but the terms do not provide an unconditional positive eligibility warranty for every Azerbaijan resident.
6. **Tax / all-in cost floor not yet proved** — participants bear tax obligations; strict net-profit proof needs Azerbaijan-specific treatment and exact funding/trading/withdrawal costs.

Thus this is a **conditional fixed-cash earning opportunity**, not a proof of guaranteed profit across every allowed contractual branch.

## Other H056 controls
### Payoneer
Current 2026 Prestige Club pages show real cashback credited to Payoneer balances and qualifying flows can include withdrawals to local bank. However participation is invitation-only, targets are communicated privately, and reward amount/category is not publicly fixed. A historical 2025 Payoneer campaign explicitly included Azerbaijan and paid USD 300 after USD 25,000 eligible outgoing volume, validating geography/mechanism historically, but it expired 25 Aug 2025.

Current sources:
- https://pages.payoneer.com/prestigeclub/
Historical explicit-Azerbaijan control:
- https://pages.payoneer.com/unlock-global-growth/

Result: **current mechanism real, but no public deterministic fixed floor available to arbitrary Azerbaijan resident**.

### Freedom24
Current 2026 WELCOME promotion offers gift shares for funding tiers, and the official account-opening flow asks for tax residency/proof of address. The reward is explicitly market-valued stock and can fluctuate; this remains H054-style variable reward, not fixed cash.

Sources:
- https://lp.freedom24.com/en/welcome
- https://freedom24.com/faq/13096-how-to-open-an-account-as-an-individual

Result: **REJECTED for strict fixed-cash H056 filter**.

### Interactive Brokers referred-client award
The referred client receives IBKR shares ($1 in shares per $300 net deposit under the 2 Jul 2026 agreement, max $1,000) with one-year transfer restriction. That leg remains variable market value and is not the H056 cash candidate.

## Strategic conclusion
H056 produced the strongest geography-compatible fixed-cash lead so far:

**IBKR Azerbaijan-compatible platform + USD 200 referrer payment = validated current fixed-cash mechanism.**

It still fails terminal SUCCESS because the cash entitlement is not contractually irrevocable across all permitted amendment/eligibility/anti-abuse/local-law branches and depends on an independent referred person's one-year behavior.

## Next higher-value branches
1. Search for a similar Azerbaijan-accessible referral/account-switch reward where entitlement becomes **irrevocably vested immediately after deterministic actions**, without a one-year third-party dependency or broad anti-abuse cancellation discretion.
2. Check regulated cross-border payment providers for fixed cash paid after ordinary incoming/outgoing business volume where Azerbaijan is explicitly eligible and the amount/threshold are public.
3. Revisit H052 only if the missing product-specific Avans / Əlavə fürsət agreement becomes obtainable through a genuinely new source.
4. H020 remains a separate post-fill surebet mechanism when raw executable books become accessible.

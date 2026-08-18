# H069 — damaged AZN face-redemption arbitrage

Updated: 2026-08-18
Status: **VALIDATED MECHANISM / NO LIVE DISCOUNTED EXECUTABLE INSTANCE FOUND**

## Hypothesis
Acquire an authentic damaged Azerbaijan-manat banknote at a price materially below face value, then redeem it at the Central Bank for full nominal value.

This is a different mechanism from ordinary collectible-banknote trading. The edge, if present, comes from a statutory redemption floor rather than prediction or resale demand.

## Primary official rules
Central Bank of Azerbaijan rules on currencies unfit for circulation establish:
- damaged national banknotes may be presented to banks or the Central Bank for replacement;
- authenticity is checked from security features;
- a non-counterfeit paper banknote retaining at least 60% of its surface in one intact part is payable at nominal value;
- alternatively, parts belonging to the same banknote that preserve 100% of the original surface are payable;
- the Central Bank performs national-currency replacement free of charge;
- payable banknotes are replaced without quantity limit;
- when authenticity / surface entitlement requires expert examination, the Central Bank decides entitlement and pays the holder if positive;
- notes suspected of deliberate unlawful damage may be referred to law enforcement.

Official sources:
- https://www.cbar.az/law-261/regulations-on-signs-of-currencies-unfit-for-circulation-their-replacement-and-expertise?language=az
- https://www.cbar.az/page-841/replacement-of-currencies
- https://cbar.az/page-73/questions-and-answers

The current consumer-facing CBAR page adds a practical criterion: an intact/continuous preserved portion of at least 60% plus at least one full serial number is redeemable; non-contiguous pieces require stronger serial-number evidence.

## Deterministic arithmetic
For one banknote with nominal value `F`, acquisition price `P`, and all-in execution cost `C`:

`net = F - P - C`

A strict positive nominal-cash floor exists only if all of the following are locked before irreversible payment:

`P + C < F`

and
1. note is authentic;
2. note meets the CBAR redemption-area/serial requirements;
3. note has not been unlawfully altered in a way that creates confiscation/referral risk;
4. the redemption entitlement is verified with sufficient certainty before seller payment;
5. no seller/title/fraud dispute can reverse possession or payment economics.

Examples before costs:
- authentic redeemable 100-AZN note bought for 90 AZN => 10 AZN gross spread;
- authentic redeemable 200-AZN note bought for 170 AZN => 30 AZN gross spread.

These examples are arithmetic thresholds, **not live offers**.

## Execution-lock problem
The key weakness is adverse selection: a seller willing to dispose of a damaged note below face may know or suspect that it is counterfeit, below the surface threshold, already problematic, or otherwise not redeemable.

Therefore an ordinary marketplace purchase before CBAR/bank verification does **not** satisfy the project's guarantee standard.

The strongest possible execution structure would be one of:
- conditional sale inside/adjacent to a CBAR service office, with payment to seller only after successful replacement;
- seller presents the note for replacement first and assigns/sells the resulting cash claim/value at a contractual discount (unlikely economically);
- a bank/CBAR employee confirms immediate eligibility while seller remains owner, followed by simultaneous purchase and exchange;
- enforceable refund/escrow if redemption is refused.

Current official material confirms the redemption right but does not provide a public pre-purchase anonymous eligibility checker or binding reservation/quote mechanism.

## Fresh secondary-market screen — 2026-08-18
Searches across indexed Azerbaijan classifieds for terms equivalent to damaged/torn/unfit manat did not return a live damaged-current-AZN note offered below face.

The indexed `əskinas`/banknote category is dominated by collectible old notes, foreign notes and numismatic listings. One current category page and individual listing were inspected; prices reflect collector value, not damaged-face arbitrage.

Representative indexed market source:
- https://tap.az/elanlar/hobbi-ve-asude/kolleksiyalar?q%5Bkeywords%5D=%C9%99skinaslar

No candidate is therefore executable in this run.

## Tax / legal classification
No tax advantage is assumed. If repeated acquisition/redemption becomes systematic entrepreneurial activity, ordinary tax/business-registration obligations may apply. This packet does not claim a tax exemption.

The strategy also explicitly excludes deliberately damaging valid banknotes; CBAR rules allow referral when unlawful intentional damage is suspected. Only already-damaged notes acquired lawfully are in scope.

## Terminal test result
**Not SUCCESS.**

The deterministic redemption mechanism is real and stronger than many resale-price arbitrages because the face-value payer is the currency issuer and CBAR replacement is free/unlimited for qualifying notes. But no live discounted candidate and no pre-payment verification lock were found.

## Reopen gate
Do not repeat broad damaged-banknote searches. Reopen H069 only when at least one genuinely new item exists:
1. live authentic-looking current AZN note offered sufficiently below face;
2. bank/CBAR confirmation that eligibility can be determined before irreversible purchase;
3. workable escrow/conditional-sale structure at the redemption point;
4. a specialist market/source where damaged AZN is routinely sold at discounts.

At that point compute: `face - purchase - transport - verification/exchange fees - tax/transaction costs`, and require strictly positive worst-case cash after the redemption gate is locked.

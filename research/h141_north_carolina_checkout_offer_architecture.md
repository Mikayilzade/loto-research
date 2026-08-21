# H141 — North Carolina checkout-level Lottery Offer architecture

Updated: 2026-08-21
Scope: LOTTERY ONLY
Status: **CHECKOUT-LEVEL SUBSIDY ARCHITECTURE VALIDATED / CURRENT SUITABLE >BREAK-EVEN OFFER NOT FOUND / NO SUCCESS**

## Objective
Follow H140's highest-priority branch: find a state lottery where a deterministic subsidy/discount is applied at the same checkout where the complete draw-game basket is assembled, so the player can verify the subsidy before external cash is committed.

North Carolina is the strongest architecture match found in this packet.

## 1. Official NCEL terms explicitly support checkout-level Lottery Offers
Current North Carolina Education Lottery Online Play Terms define a distinct `Lottery Offers` class for lottery purchases. The terms state that offers may apply to a single game **or to the whole shopping cart** and include Discount Offers, Credit Offers, Free Lottery Game Offers, and Free Game Bonuses.

Most importantly, the current terms say:

- when a player qualifies for a **Discount Offer, the ticket is immediately discounted**;
- Lottery Offers can depend on number of tickets, number of draws, minimum purchase, subscriptions, or add-ons;
- promo codes may entitle a player to discounts/free games/bonus money upon a specified action;
- draw-game purchases are accepted through the Online Play checkout system.

Official source:
- https://nclottery.com/Terms

This is materially better than the Kentucky H136-H140 ordering. A true purchase-level Discount Offer can in principle be visible/applied before checkout completion, so if the discount is absent the player can decline to commit external cash.

## 2. 2026 transaction-level precedent: promo code entered in Shopping Cart
NCEL's 2026 `M4LDEAL26` promotion is an official concrete example of this architecture. The published steps were:

1. choose Millionaire for Life;
2. choose Buy Now;
3. **on the Shopping Cart page enter promo code `M4LDEAL26`**;
4. complete the $10 purchase;
5. receive a free $5 Millionaire for Life ticket.

The promotion permitted repeated qualification via separate qualifying transactions during its June 1–July 1, 2026 window.

Official source:
- https://nclottery.com/PromotionsSpecialty

This offer is expired and Millionaire for Life does not provide the compact non-shareable deterministic coverage needed for terminal SUCCESS. Its value here is architectural evidence: NCEL can place a deterministic lottery-specific promo directly in the purchase cart, before checkout completion.

## 3. Current Welcome Offer is not enough for NC Pick 3
NCEL currently advertises a new-player Welcome Offer with a 100% first-deposit match up to $50 plus free Digital Instant games. The deposit-match Bonus can be used on draw games including Pick 3.

Official sources:
- https://nclottery.com/promo/digital-instants-welcome
- https://nclottery.com/PromotionsSpecialty

However, this is still a **deposit Bonus**, not a purchase-level Discount Offer. Current NCEL terms also make promotions discretionary and deposited funds nonrecoverable by chargeback/reversal; only winnings are withdrawable in the ordinary flow. So the H140 ordering problem remains for this offer.

Even before execution/legal gates, North Carolina Pick 3 has a weaker deterministic cover ratio than Kentucky:

### Exact full cover
Current official Pick 3 table:
- 1,000 ordered outcomes;
- $0.50 Exact per outcome;
- $250 Exact payout on a $0.50 play.

Therefore:
- face coverage = 1,000 × $0.50 = **$500**;
- guaranteed gross = **$250**;
- deterministic ratio `r = 0.50`.

### Pair full cover
Current official Pick 3 table:
- 100 ordered front-pair (or back-pair) outcomes;
- $0.50 each;
- winning Pair pays $25.

Therefore:
- face coverage = 100 × $0.50 = **$50**;
- guaranteed gross = **$25**;
- deterministic ratio `r = 0.50`.

Official current payout source:
- https://nclottery.com/Pick3-Draw?dn=13708

## 4. Exact subsidy threshold
For deterministic cover ratio `r`, external cash `D`, and usable subsidy `B`:

`profit = r(D+B) - D`.

Positive floor requires:

`B/D > 1/r - 1`.

For NC Pick 3, `r=0.50`, so:

`B/D > 1.00`.

Thus the subsidy must be **strictly greater than 100% of external cash**. A 100% deposit match merely reaches pre-tax break-even under perfect execution:

- deposit $25 + $25 Bonus -> $50 Pair cover -> guaranteed $25 gross -> **$0 pre-tax**;
- deposit $250 + $250 Bonus -> $500 Exact cover -> guaranteed $250 gross -> **$0 pre-tax**.

Any tax/friction makes it negative. Therefore the current NC 100% Welcome Offer cannot produce a guaranteed positive Pick 3 floor even if every execution problem were solved.

## 5. Why checkout-level offers still matter
The H140 target class remains valid, and North Carolina gives the cleanest official implementation found so far:

`assemble basket -> apply Lottery Offer/Discount in cart -> verify discounted price -> complete checkout`.

Unlike a nonwithdrawable deposit match, a purchase-level discount can theoretically solve the dangerous pre-commitment ordering. For a game with `r>0.50`, a sufficiently large discount may cross break-even.

Equivalent discount condition in terms of face price discount fraction `q`:

`r / (1-q) > 1`  ->  `q > 1-r`.

Examples:
- `r=.50` requires discount **>50% of face price**;
- `r=.60` requires **>40%**;
- `r=2/3` requires **>33.33%**;
- `r=.75` requires **>25%**.

This makes current/future `buy X get Y free`, cart coupons, and whole-cart Discount Offers materially more promising when paired with a compact fixed-prize game above 60% deterministic coverage.

## 6. Current campaign screen
Fresh August 2026 official/search-index screen found:
- current NCEL Welcome Offer: 100% deposit match up to $50 + 25 free Digital Instant games;
- NCEL terms still support whole-cart immediate Discount Offers;
- no current public August 2026 purchase-level Discount Offer was found that applies to Pick 3 or another compact fixed-prize draw game at a rate above its exact break-even threshold;
- historical/current-site 2026 `M4LDEAL26` proves checkout promo-code execution but expired July 1 and targeted a progressive/shareable game.

Therefore this packet does **not** claim current executable arbitrage.

## 7. Result
- **Checkout-level deterministic Lottery Offer architecture: VALIDATED.**
- **Promo code in shopping cart before purchase: VALIDATED by official 2026 NCEL campaign.**
- **Current NC Pick 3 deterministic cover ratio: 50%.**
- **Current 100% Welcome deposit match: only theoretical break-even on Pick 3 before tax and still subject to deposit/promo execution gates.**
- **Current >break-even checkout discount for compact fixed-prize coverage: NOT FOUND.**
- Terminal state: **NO SUCCESS; NOT EXHAUSTED**.

## Next action
1. Monitor/search NCEL and other state lotteries specifically for purchase-level `Discount Offer` / BOGO / cart promo applying to Pick 3/4 or other compact fixed-prize games.
2. Highest-value numerical target is a compact non-shareable game with deterministic ratio `r>0.60`; then only a checkout discount above `1-r` of face price is needed.
3. Search for current checkout BOGO that allows player-chosen free numbers and repeated transactions; pair with exact cover theorem.
4. Do not reopen NC 100% deposit-match + Pick 3 unless subsidy exceeds 100% or a higher-r eligible compact game is identified.

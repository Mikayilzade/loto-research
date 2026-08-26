# H283 execution verification — 2026-08-26

Branch: `research-work`
State: **ARITHMETIC VALID; EXECUTION GATE STILL OPEN**

## Scope

Follow-up on H283 Pennsylvania iLottery Refer-A-Friend + PICK 3 Front Pair cover. H225-X* was checked first and remains CLOSED / EXHAUSTED at X20; no H225-X21/X22 work is warranted.

## Official evidence matrix

### A. Online PICK 3 and Front Pair are real/current — VERIFIED

Current PA iLottery Help explicitly says PICK 3 can be played online at palottery.com and lists FRONT PAIR as a supported play type. The current PA iLottery PICK 3 page exposes BUY NOW and a $0.50 starting price.

Sources:
- https://help.pailottery.com/hc/en-us/articles/8063702035092-How-do-you-play-PICK-3
- https://www.pailottery.com/?more_info=pick-3

### B. One online purchase may contain multiple plays and player-selected numbers — VERIFIED GENERALLY

Current binding PA iLottery Terms, section 10, state that a purchase has a Game, a **number of Plays**, a purchase price of the Play(s), and the **numbers or selections chosen on any Play**. The same section says initiating a purchase authorizes deduction of the cost of **that purchase**, and completed purchases are final.

This materially supports a multi-selection purchase as one purchase object, but does not state the PICK 3 per-purchase play maximum.

Source:
- https://www.pailottery.com/signup/terms-and-conditions/

### C. Online PICK 3 wagering at the $100+ scale is officially contemplated — VERIFIED, BUT NOT A SINGLE-TRANSACTION PROOF

An official PA iLottery promotion rule for online draw-game wagering explicitly created a PICK 3 / PICK 3 with Wild Ball tier for **$100.00 or more** wagered online. This eliminates the weaker concern that $100 of online PICK 3 wagering is inherently unsupported.

However, the promotion measured wagering over its entry period; it does **not** prove that $100 can be submitted as one PICK 3 purchase or that it can contain 100 distinct Front Pair plays.

Source:
- https://www.pailottery.com/p/DCNYRE/

### D. Retail PICK 3 permits a $100 single ticket and supports carting — VERIFIED RETAIL-ONLY

Current 2026 retailer terminal documentation states:
- FRONT PAIR is supported;
- ADD TO CART and BUY NOW are available;
- maximum value of a single PICK 3 ticket is **$100**.

This is strong compatibility evidence for the target cover but cannot be silently transferred to the online channel.

Sources:
- https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/QRG/WAVE-X_Terminal-Operations-Guide_2-2-2026.pdf
- https://www.palottery.pa.gov/PaLotteryWebSite/media/Retailer-Documents/QRG/WAVE-8_Terminal-Operations-Guide_1-16-2026.pdf

### E. Online limits can be game-specific — VERIFIED

PA iLottery Help explicitly limits online Powerball / Mega Millions to five plays for up to 26 draws. Therefore absence of a published PICK 3 cap is not proof that 100 plays are allowed.

Source:
- https://help.pailottery.com/hc/en-us/articles/8063697229972-Can-I-purchase-Powerball-and-Mega-Millions-tickets-online

### F. No Kentucky/NH-style general number-rejection clause found in current PA iLottery Terms — VERIFIED NEGATIVE CHECK, NOT A WARRANTY

Fresh text search of current PA iLottery Terms found no general clause reserving a right to reject an otherwise valid purchase merely because of the chosen number(s). The explicit refusal language located concerns geolocation / invalid eligibility conditions. The Terms do allow player-set spend limits and impose account/fraud restrictions.

This improves H283 relative to H279/H280, but absence of a clause is not proof that every syntactically valid 100-play PICK 3 request is operationally accepted.

Source:
- https://www.pailottery.com/signup/terms-and-conditions/

### G. Referral bonus and cash conversion route — VERIFIED CURRENTLY

Current Refer A Friend terms give the referred new player **$100 Bonus Money** after registration through the referral link and first deposit of at least $10 using code FRIEND. Current Bonus Policy explicitly allows Bonus Money wagering on Draw Games and states Draw Game prizes won with Bonus Money are paid in cash regardless of remaining play-through on that Bonus Money.

Sources:
- https://www.pailottery.com/p/refer-a-friend/
- https://www.pailottery.com/p/bonus-policy/

## Exact arithmetic remains unchanged

Target cover: one $1 FRONT PAIR play on each ordered pair `00` through `99` for the same PICK 3 drawing.

- number of outcomes / plays: 100;
- cover spend: $100;
- each legal draw has exactly one matching Front Pair;
- fixed $1 Front Pair prize: $50;
- guaranteed cash gross after a complete accepted cover: $50;
- qualifying external cash deposit: $10;
- conditional guaranteed cash profit vs external deposit: **+$40**.

The $0.50 version costs $50 and returns $25 for every draw, leaving +$15 versus the same $10 external deposit if the complete cover is accepted.

## Stronger execution conclusion from this pass

H283 is now supported by four independent official facts that were previously only partially linked:
1. PICK 3 with Front Pair is explicitly sold online;
2. binding iLottery Terms model one purchase as containing a number of Plays and player-selected numbers/selections;
3. official PA rules have explicitly contemplated $100+ online PICK 3 wagering;
4. retail PICK 3 permits a $100 single ticket.

This substantially narrows the uncertainty, but it still does not meet the rigorous SUCCESS standard. No public official source located in this pass proves **all** of the following:

1. one online PICK 3 purchase may contain at least **100 distinct Front Pair plays for the same drawing**;
2. all 100 selections are committed as a single all-or-none completed purchase rather than through sequential partial acceptance;
3. there is no online-specific line/cart/liability control capable of stopping the set after only a strict subset has been accepted.

A strict subset of `00`-`99` has a legal draw outcome paying zero, so partial acceptance destroys the guarantee. The remaining gap is therefore operational and binary, not mathematical.

## Practical evidence needed to close H283

Any one authoritative item that simultaneously establishes the 100-play same-draw purchase and its completion semantics would be enough to re-evaluate for SUCCESS, for example:
- current PA iLottery PICK 3 Buy Now UI/manual showing a 100-play cart/purchase;
- official Help article stating the PICK 3 online per-transaction play limit is at least 100;
- written PA iLottery support confirmation that 100 distinct Front Pair selections can be submitted and accepted in one checkout and that a failed checkout does not partially purchase a subset.

Until then the correct state is **PROMISING CONDITIONAL SUCCESS LEAD / EXECUTION GATE OPEN**, not SUCCESS.

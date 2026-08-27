# H321 VALIDATION — Diamond Winners electronic free-entry cap bound

Validated: 2026-08-28
Conclusion: **CLOSED / CAP-BLOCKED**

## Independent checks

1. The live competition page advertises a £100 cash prize, £10 nominal entry, and a 100% off code that makes the entry free.
2. The same page publishes a hard 1,000-entry competition cap and **maximum 1 entry per person**.
3. The live snapshot used for the exact bound showed **178 / 1,000** entries already present.
4. Governing Terms clause 4.1(a) selects the Main-draw winner from valid Entrants; clause 4.1(c) describes auto-draw selection from valid entries.
5. Terms clause 3.6 permits only one account per person, so the per-person cap cannot be multiplied by opening extra accounts.
6. Even if one of the 178 observed entries is credited to the target player, at least `178 - 1 = 177` valid entries remain external.
7. Hence a legal state exists in which an external valid entry wins the £100 prize.
8. In that state the target player's withdrawable-cash return from the competition is £0.
9. Therefore the strict all-outcomes cash floor is **£0**; a zero acquisition cost does not convert the promotion into a guaranteed positive-cash strategy.

Arithmetic cross-check:

- maximum advertised identifier share: `1 / 1000 = 0.001 = 0.1%`;
- minimum external observed entries under the player-favourable one-owned-entry assumption: `177`;
- strict guaranteed cash floor: `£0`.

The Python model asserts these values and the derived JSON records the same terminal result.

Sources checked:

- https://diamondwinners.co.uk/product/100-cash-facebook-vip-group-exclusive-3/
- https://diamondwinners.co.uk/terms-conditions/

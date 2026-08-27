# H309 — Salexmo postal-bundle finite-pool takeover screen

Checked: 2026-08-27
State: **CLOSED / TAKEOVER-BLOCKED**

## Why this packet matters

H302/H308 showed that UK postal free-entry routes usually fail because postage is not actually cheap enough or because receipt/reservation is not guaranteed. H309 checks a stronger variant: Salexmo explicitly grants multiple competition tickets for one postal entry on some live draws. This can make the effective postal cost per ticket materially lower than the website ticket price.

The important discovery is that one currently advertised future draw crosses the pure arithmetic threshold under impossible-perfect ownership.

## Governing current facts

Royal Mail currently prices a Second Class letter/postcard up to 100g at **£0.91**.
Source: https://www.royalmail.com/sending/uk/2nd-class

Salexmo terms shown on the competition pages state that:
- each free entry must be posted separately;
- proof of posting does not guarantee entry;
- if the entry cap is reached before the postal entry is received, it is not entered;
- ticket numbers are allocated after order/entry processing;
- each competition can impose a maximum per user.

Sources used:
- https://salexmo.co.uk/competition/ps2000-cash-prize-for-just-2p-a-ticket-4926
- https://salexmo.co.uk/competition/ps900-cash-main-prize-plus-ps90-cash-instant-wins-2926
- https://salexmo.co.uk/competition/super-low-odds-ps10000-prize-pot-with-a-ps2000-cash-end-prize-17926
- https://salexmo.co.uk/competition/ps12500-instant-win-prize-pot-plus-a-ps500-cash-end-prize-7926

## Exact screen

Using £0.91 per separately posted free-entry card:

| Draw | N | Max/user | Postal tickets/card | Advertised cash liabilities | Hypothetical postal full-pool cost | Liability / cost |
|---|---:|---:|---:|---:|---:|---:|
| £2,000 cash — 4 Sep | 200,000 | 50,000 | 43 | £2,000 | £4,233.32 | 47.2442% |
| £900 + 10×£90 — 2 Sep | 40,000 | 10,000 | 10 | £1,800 | £3,640.00 | 49.4505% |
| £10,000 instant pot + £2,000 end — 17 Sep | 12,000 | 2,500 | 1 | £12,000 | **£10,920.00** | **109.8901%** |
| £12,500 instant pot + £500 end — 7 Sep | 866,666 | 150,000 | 29 | £13,000 | £27,196.26 | 47.8007% |

The 17 September competition is therefore a genuine arithmetic near-success. Under the deliberately impossible assumption that one player could acquire every one of the 12,000 identifiers via valid £0.91 postal entries, all £10,000 of instant-win liabilities plus the £2,000 end prize would be controlled. Gross £12,000 minus £10,920 postage = **£1,080 deterministic positive margin**, before the cost of postcards/materials.

This is materially different from the earlier postal screens because the prize liabilities exceed the postal acquisition cost.

## Why it is still not a rigorous SUCCESS

The actual current rules destroy full ownership in several independent ways.

1. **Per-user cap:** the 17 Sep draw permits only 2,500 entries per user out of 12,000, so one eligible player can control at most **20.8333%** of the finite pool.
2. **Existing external inventory:** at the checked snapshot, 728/12,000 entries were already sold. Even if the cap vanished, those identifiers are outside a new entrant's control.
3. **Postal non-atomicity:** proof of posting is not proof of receipt/entry.
4. **Race against cap:** postal entries received after the finite cap is filled are excluded.
5. **Random allocation:** identifiers are not preselected/reserved by the postal sender before processing.

Because at least one external eligible identifier remains, there is a legal main-draw outcome in which an external ticket wins the £2,000 end prize. Because the player cannot own every published instant identifier either, the total-liability takeover theorem cannot be executed. The strict guaranteed-profit floor is therefore not established.

## Conclusion

**NO SUCCESS. H309 CLOSED / TAKEOVER-BLOCKED.**

The useful new theorem is narrower and actionable for future search: a postal/free-entry route can genuinely cross 100% if the prize pool is sufficiently dense. The 17 Sep Salexmo economics prove that arithmetic is no longer the universal blocker. Future search should prioritize a finite pool with all of the following simultaneously:

- deterministic liabilities > exact cheapest full-acquisition cost;
- per-player cap >= full pool (or otherwise enough to force every winning identifier);
- zero external tickets already allocated at acquisition start;
- electronic/atomic reservation or another rule that guarantees acceptance of the complete required inventory.

Reproducible arithmetic: `src/loto_research/h309_salexmo_postal_bundle_screen.py` and `data/derived/h309_salexmo_postal_bundle_screen.json`.

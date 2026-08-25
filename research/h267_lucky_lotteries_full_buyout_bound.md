# H267 — Lucky Lotteries finite-pool full-buyout bound

Date: 2026-08-25
Disposition: **CLOSED / REJECTED** for strict guaranteed-profit takeover.

## Why this candidate mattered
Lucky Lotteries Super Jackpot and Mega Jackpot are unusually close to the target mechanism:

- each draw has a finite sequential ticket pool;
- duplicate generated identifiers are cancelled/refunded/replaced, so identifiers are unique within the draw;
- the draw occurs only after all available numbers have been sold;
- thousands of fixed cash/consolation prizes are guaranteed;
- an accumulated jackpot can inject external reserve money.

The current The Lott help material also says entries may be requested in random or sequential order and that the draw closes once all tickets are sold. This makes the products materially more interesting than ordinary open combination lotteries.

## Authoritative rules checked
Tattersall's **Rules of Authorised Lotteries**, Schedule F, rules in force for draws/entries conducted on and after **18 May 2025**:

- https://support.ozlotteries.com/hc/en-us/article_attachments/14948080526607
- current gameplay summary: https://help.thelott.com/hc/en-us/articles/4416872034073-How-do-I-play-the-Lucky-Lotteries-raffle-style-game

Relevant rule facts:

1. Super Jackpot ticket pool: identifiers `000001..270000`; Mega Jackpot: `000001..200000`.
2. Duplicate generated identifiers are cancelled and refunded/replaced.
3. A draw occurs once all available numbers are sold.
4. Cash-prize Winning Numbers are drawn first; a separate Jackpot Number is then drawn.
5. **The Jackpot Prize is paid only if the Jackpot Number is also one of the cash-prize Winning Numbers.**
6. If it is not, the jackpot rolls forward and the Jackpot Number instead receives the specified free-ticket consolation.
7. The rules explicitly permit cash equivalent for the `$2 Free Ticket` / `$5 Free Ticket`, excluding commission.

The last point lets the bound value every free-ticket consolation as immediate cash-equivalent subscription value, which is favourable to the player.

## Exact impossible-perfect full-buyout test
To avoid execution ambiguity, H267 grants the player the stronger impossible assumption that they own **every unique identifier** in the draw from inception.

### Super Jackpot

- 270,000 identifiers.
- Retail price used: A$2.20 per entry (A$2 subscription + A$0.20 commission), consistent with published The Lott material.
- Full retail buyout: **A$594,000**.
- All fixed cash-prize levels: **A$176,050**.
- Two guaranteed A$1,000 first-prize-neighbour consolation awards: **A$2,000**.
- Rules-defined free-ticket-equivalent units on the legal no-jackpot branch: **8,410 x A$2 = A$16,820**.
- Guaranteed gross in that legal branch: **A$194,870**.
- Retail-cost floor return: **32.8063973%**.
- Deficit: **A$399,130**.

Even if all retailer commission were magically removed and the buyer paid only subscription value, the floor is only **36.0870%**, exactly matching the rules' Super Jackpot Prize Fund percentage.

### Mega Jackpot

- 200,000 identifiers.
- Retail price used: A$5.50 per entry (A$5 subscription + A$0.50 commission).
- Full retail buyout: **A$1,100,000**.
- All fixed cash-prize levels: **A$314,725**.
- Two guaranteed A$1,000 first-prize-neighbour consolation awards: **A$2,000**.
- Rules-defined free-ticket-equivalent units on the legal no-jackpot branch: **8,940 x A$5 = A$44,700**.
- Guaranteed gross in that legal branch: **A$361,425**.
- Retail-cost floor return: **32.8568182%**.
- Deficit: **A$738,575**.

Again, with commission unrealistically removed, the floor is **36.1425%**, exactly the Mega Jackpot Prize Fund percentage.

## Structural blocker stronger than the economics
Owning the complete ticket pool guarantees ownership of every cash-prize winning identifier and of the Jackpot Number identifier, but it **does not force the jackpot event**. The jackpot event is a relation between two random draw stages: the separate Jackpot Number must coincide with one of the previously selected cash-prize Winning Numbers.

A legal outcome always exists where that coincidence does not occur. On that outcome the accumulated jackpot remains unpaid and rolls to the next draw. Therefore even an impossible perfect takeover cannot turn the accumulated jackpot into a deterministic external subsidy.

This is stronger than an execution objection: even if exact complete acquisition were operationally possible, the strict worst-case gross is still only about 32.8% of retail cost.

## Conclusion
**H267 CLOSED / REJECTED.** Lucky Lotteries validate several attractive takeover ingredients (finite unique identifiers, sellout before draw, sequential issuance, external jackpot reserve) but fail the decisive guarantee condition because complete ownership does not force the jackpot-trigger relation.

Reopen only if the rules change so that complete ownership itself guarantees payment of the accumulated jackpot, or a deterministic external subsidy is paid independently of the jackpot-number/cash-winner coincidence.

## Reproducibility

- `src/loto_research/h267_lucky_lotteries_full_buyout_bound.py`
- `data/derived/h267_lucky_lotteries_full_buyout_bound.json`
- `research/H267_VALIDATION.md`

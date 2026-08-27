# H322 — SOBO Instant Win Frenzy: first-ticket-free + random-allocation cap bound

Date checked: 2026-08-28
State: **CLOSED / CAP-AND-RANDOM-ALLOCATION-BLOCKED**

## Why this was worth checking

This live competition combines several features that are individually useful for a guaranteed-profit search:

- a finite pool of **500,000** identifiers;
- the **first ticket free** for every account;
- electronic ticket holding for 10 minutes during checkout;
- instant prizes plus five advertised £1,000 cash prizes;
- a near-zero-sold snapshot (1 / 500,000 sold when checked).

The competition page also exposes a `Manual` ticket UI, so H322 explicitly checked whether that meant prize-bearing identifiers could be selected rather than merely ticket quantity/manual entry mode.

## Governing facts

Live competition page:
https://sobocompetitions.com/competitions/instant-win-29p

At the checked snapshot it stated:

- 500,000 total tickets;
- 499,999 remaining / 1 sold;
- £0.29 per ticket;
- first ticket free;
- maximum 2,000 tickets per person;
- tickets held for 10 minutes during checkout;
- 50,000 advertised instant-credit prizes and five £1,000 cash prizes.

The governing August-2026 Competition Rules and Terms are decisive:

- https://sobocompetitions.com/competition-rules
- https://sobocompetitions.com/terms

They state that ticket numbers are allocated **at random from the remaining pool**, the entrant **cannot choose a number**, and instant-win assignments are hidden before purchase. Thus the `Manual` UI is not evidence of selectable identifier ownership.

The free route is also only one entry per person per competition and is subject to the same per-person cap:
https://sobocompetitions.com/free-entry

## Exact worst-case bound

Give the player an intentionally favourable interpretation: assume every one of the 50,000 advertised instant-credit prizes and all five £1,000 cash prizes occupy distinct identifiers.

Then the maximum number of prize-bearing identifiers is

`50,000 + 5 = 50,005`.

Therefore at least

`500,000 - 50,005 = 449,995`

identifiers have no instant prize under this player-favourable model.

The real maximum one player can hold is only 2,000. Since

`449,995 >= 2,000`,

there is a legal random allocation in which **all 2,000 allowed tickets held by the player fall in the zero-instant residual set**. The one free ticket changes acquisition cost but does not remove that legal zero-instant allocation.

The separate/main draw does not create a positive floor either. The player cannot reserve the full finite pool, and the competition remains open to external valid entrants, so a legal external-winner state remains.

Hence the strict withdrawable-cash floor is:

**£0**.

This conclusion does not require estimating EV, sell-through, or the value of site credit.

## Reusable gate

For a finite instant-win pool with hidden/random identifier allocation, if the number of legal zero-cash identifiers is at least the maximum number of entries one player can hold, then a one-player strict positive cash floor is impossible:

`zero_cash_identifiers >= player_cap  =>  worst_case_cash_floor = 0`.

A free first ticket or small deterministic discount cannot change that unless it also changes which identifiers can be controlled.

## Files

- `src/loto_research/h322_sobo_first_ticket_free_cap_bound.py`
- `data/derived/h322_sobo_first_ticket_free_cap_bound.json`
- `research/H322_VALIDATION.md`
- `research/H322_STATUS.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H322_APPEND.md`

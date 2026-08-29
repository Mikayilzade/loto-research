# H350 — Irish Lotto Plus Raffle additive-subsidy / ownership bound

Date: 2026-08-29  
Status: **CLOSED AS STRICT GUARANTEE**

## Why this packet

H349 found a rare isolated >100% special-event full-cover result, but external top-tier duplicates destroyed the guarantee. H350 therefore tests a different live mechanism: an additive fixed raffle attached to each paid Lotto Plus play, with a finite four-digit identifier universe and a periodic €1m pool.

This is not a repeat of H251/H252. Those packets tested the 6/45-era Lotto Plus number-cover economics and cap sharing. H350 isolates the **raffle identifier subsidy and its ownership/dilution structure** under current 6/47 Issue 8 rules.

## Binding mechanics

Current Lotto Plus Game Rules (Issue 8, October 2024) state:

- Lotto Plus Raffle Entry Numbers are issued sequentially from `0000` to `9999`;
- each Lotto Plus Play receives one raffle entry number;
- Lotto Plus costs €1 per Play, with a minimum of two Plays;
- a raffle entry matching the winning four-digit number receives a fixed €500;
- the €1m Million Euro Raffle, when conducted, is additional to the usual €500 and is either:
  1. divided equally between all Ticket Owners bearing the winning raffle number, or
  2. awarded to one Ticket Owner selected from all tickets bearing that number.

Official sources:
- https://www.lottery.ie/game-information/lotto-plus/million-euro-raffle
- https://cdn1.lottery.ie/uploads/Issue_8_PLI_RULES_LOTTO_PLUS_Lotto_Plus_Million_Euro_Raffle_OCT_2024_29_10_af83876177.pdf

## Exact ordinary-raffle bound

Let `N` be the number of Lotto Plus plays owned and let the 10,000 possible raffle codes be the outcome classes. No matter how the `N` entries are distributed, at least one code has multiplicity at most

`floor(N / 10,000)`.

Therefore even granting impossible-perfect balancing, the minimum ordinary raffle gross over all possible winning codes is at most

`€500 × floor(N / 10,000)`.

The incremental Lotto Plus cost is `€1 × N`, so

`net <= 500*floor(N/10000) - N`.

Write `N = 10,000q + r`, `0 <= r < 10,000`. Then

`net <= 500q - 10,000q - r = -9,500q - r < 0`

for every `N > 0`.

A complete 10,000-code cycle costs **€10,000** in Plus add-ons and guarantees at most **€500** ordinary raffle gross: only **5%** return on the add-on, deficit **€9,500**. The required base Lotto purchase is deliberately omitted; including it only worsens the result.

The executable checker also scanned every `N=1..2,000,000`; nonnegative cases: **0**.

## Million Euro Raffle rescue screen

The periodic €1m pool is economically large enough to matter, but it is not a non-dilutable owned-code subsidy.

Under the current rules the pool may be split across all Ticket Owners with the winning code, or a single owner may be selected from all matching tickets. Public issuance remains open; no binding pre-draw rule was found that lets one player monopolize every occurrence of every code or hard-caps external matching tickets.

Thus a legal external matching ticket gives:
- **single-owner mode:** a legal branch where the external ticket owner receives the whole €1m, so our special bonus is €0;
- **shared mode:** external owners dilute our share, with no binding external-count cap sufficient for a strict positive floor.

The rules independently reserve power to restrict/prohibit participation deemed to interfere with other players' reasonable access, so a market-takeover assumption cannot be promoted to an execution guarantee.

## Validation / closure

- Identifier universe: **10,000** exactly.
- Ordinary complete-cycle incremental cost: **€10,000**.
- Ordinary complete-cycle guaranteed-gross upper bound: **€500**.
- Ordinary additive return ceiling: **5%**.
- Symbolic all-`N>0` proof: complete.
- Implementation scan `N=1..2,000,000`: **0 nonnegative cases**.
- Arithmetic inconclusive: **0**.
- Closure-relevant inconclusive: **0** for the claimed strict-guarantee rejection.

**Result: NOT SUCCESS.** The fixed €500 raffle cannot finance its own Lotto Plus add-on even under impossible-perfect code balancing, while the €1m event has an external-owner/dilution zero-floor branch. Reopen only if rules create a non-dilutable special payment to every matching entry or a binding mechanism that guarantees monopoly of every eligible occurrence.

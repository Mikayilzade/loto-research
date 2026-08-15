# H030 — Virginia Cash 5 with EZ Match

Updated: 2026-08-16
Status: **current full-space guaranteed-profit route rejected; EZ Match paid add-on rejected as guarantee amplifier**

## Current operator facts
Primary source: https://www.valottery.com/data/draw-games/cash5

Current Virginia Lottery page states:
- choose 5 numbers from 1–45;
- each Cash 5 play costs $1;
- jackpot starts at $200,000 and grows until won;
- current checkpoint advertised jackpot: **$210,000** (page snapshot August 15, 2026);
- fixed lower tiers: 4 matches $200, 3 matches $5, 2 matches $1;
- jackpot odds 1 in 1,221,759;
- jackpot is divided equally among multiple winning plays;
- EZ Match costs an extra $1 per play and pays instant fixed prizes up to $500.

## 1. Exact full-space Cash 5 coverage
Combination space:

`C(45,5) = 1,221,759` plays.

At $1 each, full-space cost is **$1,221,759**.

For any realized winning 5-set, exact match counts among the complete portfolio are:
- 5 matches: `1`;
- 4 matches: `C(5,4)C(40,1)=200`;
- 3 matches: `C(5,3)C(40,2)=7,800`;
- 2 matches: `C(5,2)C(40,3)=98,800`.

Deterministic fixed-tier cash excluding jackpot:

`200*$200 + 7,800*$5 + 98,800*$1 = $177,800`.

Therefore a **sole-winner** jackpot must exceed:

`$1,221,759 - $177,800 = $1,043,959`

just to reach pre-tax/pre-execution break-even.

At the checkpoint jackpot of $210,000, even granting our portfolio the entire jackpot gives:

`($177,800 + $210,000) / $1,221,759 = 31.740%` gross return.

## 2. Strict guarantee failure from jackpot sharing
The official rule explicitly states that the jackpot is divided equally among multiple winning plays.

Full-space coverage guarantees that our portfolio holds one winning 5/5 line, but it does **not** prevent external players from holding the same line. There is no useful pre-draw hard cap on the number of external jackpot-winning plays available from the current public rules.

Therefore even a future advertised jackpot above the $1.043959m sole-winner break-even threshold would not by itself establish an all-outcome profit guarantee. External jackpot sharing can reduce our realized jackpot share.

Status: **REJECTED as strict guaranteed-profit full-space route under current public rules.**

## 3. EZ Match add-on
Official current EZ Match prize/odds rows:
- $500 @ 1/84,000;
- $250 @ 1/42,000;
- $100 @ 1/12,000;
- $50 @ 1/4,200;
- $20 @ 1/1,680;
- $15 @ 1/1,050;
- $10 @ 1/112;
- $5 @ 1/280;
- $4 @ 1/76;
- $3 @ 1/14;
- $2 @ 1/9.

Summing published prize × probability gives approximate gross EV:

`$0.654615706` per $1 EZ Match add-on, or **65.4616%**.

The add-on therefore has negative expected value by a wide margin. Since it is a separately paid random wager, mixing it into Cash 5 portfolios cannot create a strict all-outcome positive guarantee under additive pricing: such a guarantee would imply positive expected profit, contradicting the non-positive expectation of its constituents.

Multi-Draw and Repeat simply replicate paid plays. The official page also notes EZ Match applies only once to a Multi-Draw ticket/subscription, so there is no repeated-free-EZ-Match loophole.

## Conclusion
H030 closes the current Virginia Cash 5 + EZ Match route:
- current full-space state is massively below break-even even under sole-jackpot assumption;
- future jackpot-only positive EV is not a strict guarantee because of external jackpot sharing;
- EZ Match is ~65.46% gross EV and cannot rescue the guarantee.

Reopen only if a future rule/promotion creates a deterministic external subsidy or a useful hard bound on jackpot sharing that can be locked before purchase.
# H268 — New Zealand Powerball terminal / Must Be Won duplicate bound

Date: 2026-08-25
Status: **REJECTED for strict guaranteed-profit takeover**

## Why this candidate was worth testing

New Zealand Powerball has a genuine terminal mechanism. Under Lotto Rules 2025, if a jackpot may no longer roll over (or on a specified Powerball date) and there is no Division 1 winning selection, the Division 1 allocation is added to the next-lowest Powerball division with one or more winners. This is exactly the kind of externally accumulated forced-distribution mechanism prioritised by `STATUS.md`.

Current rules before 13 September 2026 use 6-of-40 Lotto plus one Powerball from 1..10. A standard Lotto selection costs NZ$0.70 and a Powerball selection NZ$0.80, so one paired line costs NZ$1.50. The enacted 2026 amendment, effective 13 September 2026, expands Powerball to 1..14, lowers the Powerball minimum prize-pool percentage from 60% to 55%, adds fixed Division 8 = NZ$12, and raises fixed Division 7 from NZ$15 to NZ$20.

Primary legal sources:
- Lotto Rules 2025, rules 10, 25, 29, 30, 32–34: https://www.legislation.govt.nz/regulation/public/2025/0174/latest/whole.html
- Lotto Amendment Rules 2026, effective 2026-09-13: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/51/en/latest/whole.html

Useful official background: Lotto NZ has historically described Powerball terminal jackpots as Must Be Won draws; if Division 1 is absent, the jackpot rolls to the next winning Powerball division. Lotto NZ's 2023 ministerial briefing records a NZ$50m threshold at that time; the March 2026 announced matrix change raises the marketed maximum to NZ$60m from the September 2026 changeover.

## Structural blocker: coverage cannot force the rolldown branch

Let a purchased Powerball line be `(S,p)`, where `S` is one 6-number subset of 1..40 and `p` one Powerball number.

Every such purchased line is itself a legal draw outcome: the six drawn Lotto numbers can equal `S` and the Powerball can equal `p`. Therefore **any non-empty player portfolio has at least one legal draw state in which that portfolio creates a Powerball Division 1 winner**.

Consequences:
1. no non-empty portfolio can guarantee the `no Division 1 winner` condition in every draw state;
2. complete outcome coverage is even stronger in the wrong direction: it guarantees that the player has a Division 1 winner, so the terminal rolldown branch cannot occur;
3. a takeover construction must therefore survive the ordinary/shared Division 1 branch as well, not merely the advertised Must Be Won rolldown.

That already closes the idea of *forcing* the rolldown by coverage. H268 then stress-tests whether complete coverage could still guarantee profit via the Division 1 jackpot itself.

## Exact current-matrix complete cover

Current pre-2026-09-13 matrix:
- `C(40,6) = 3,838,380` main Lotto combinations;
- 10 Powerball values;
- paired outcome space = **38,383,800 lines**;
- NZ$1.50 per paired line;
- exact one-copy full-cover cost = **NZ$57,575,700**.

For any realised draw, this portfolio has:
- 10 Standard-Lotto Division 1 entries (the winning six repeated once for each Powerball value);
- exactly 1 Powerball Division 1 entry;
- deterministic lower-tier winning-entry counts.

Powerball Division 7 fixed cash count is
`C(6,3) * C(33,3) = 109,120`, hence NZ$1,636,800 at NZ$15 each.

Standard Lotto Division 7 produces 1,091,200 winning selections across the ten copies, with rules-defined value NZ$3,055,360, but it is paid as future bonus selections. H268 deliberately assigns those future selections **zero strict cash floor**, because all of them can legally lose in the next draw.

## Legal duplicate counterexample

The key adversarial external market state is simple and finite: after fixing a realised draw, suppose external players hold `m` additional copies of exactly that realised Division 1 paired line.

This is not speculative game manipulation; it is simply a legal ticket population that a guarantee has to survive. Those entries:
- dilute our Standard Lotto Division 1 share from `10/(10+m)`;
- dilute our Powerball Division 1 share from `1/(1+m)`;
- still increase current-draw turnover, which H268 credits into lower pari-mutuel pools using the player-favourable minimum prize-pool rules minus the maximum legally permitted reserve set-asides.

So the stress model does **not** pretend the extra ticket turnover vanishes. It gives the portfolio the lower-tier pool growth while applying the actual sharing dilution.

At a NZ$50,000,000 carried/terminal jackpot stress level, scanning `m=0..200,000` gives the minimum at:
- external exact Division-1 duplicates: **18,968**;
- portfolio gross cash floor in this legal state: **NZ$10,281,979.96**;
- acquisition cost: **NZ$57,575,700**;
- deficit: **NZ$47,293,720.04**;
- gross/cost: **17.8582%**.

Even an artificial current-matrix sensitivity with NZ$60,000,000 jackpot remains crushed:
- minimum at `m = 19,884`;
- gross **NZ$10,282,494.71**;
- deficit **NZ$47,293,205.29**;
- gross/cost **17.8591%**.

This is enough to reject strict guaranteed profit: one legal external-ticket configuration below cost is sufficient.

## Enacted 13 September 2026 matrix

The enacted amendment changes Powerball from 10 to 14 values while price remains unchanged and the minimum Powerball prize pool becomes 55% of turnover. It also adds fixed D8 and increases fixed D7.

Exact cover:
- `C(40,6) * 14 = 53,737,320` paired lines;
- cost = **NZ$80,605,980**.

Fixed Powerball counts for every realised draw:
- D7: 109,120 entries × NZ$20 = **NZ$2,182,400**;
- D8: `C(6,2)*C(33,3)=81,840` entries × NZ$12 = **NZ$982,080**.

Using a NZ$60m jackpot stress and the same legal exact-D1 duplicate family:
- minimum within `m=0..200,000` occurs at **23,175** external D1 duplicates;
- gross = **NZ$15,122,347.33**;
- full-cover cost = **NZ$80,605,980**;
- deficit = **NZ$65,483,632.67**;
- gross/cost = **18.7608%**.

Thus the September 2026 matrix change does not rescue the takeover mechanism.

## Conclusion

H268 is closed for the target mechanism.

The useful lesson is stronger than a simple EV rejection: **a Must Be Won rolldown is not automatically monopolizable by outcome coverage.** When every purchased outcome is itself a possible top-prize outcome, any non-empty portfolio preserves a legal branch where it creates Division 1 and prevents rolldown. If the top prize is shareable and external duplicates are not hard-capped/reservable, a finite external duplicate population can destroy the cash floor even when a no-external full cover would appear profitable.

Reopen this family only if one of these structural gates changes:
- eligible top-prize identifiers become uniquely reservable/hard-capped before cutoff;
- the terminal jackpot is paid per winning selection rather than shared;
- the forced-distribution condition can be guaranteed independently of the player's own purchased outcomes;
- or an external deterministic subsidy is large enough to survive a rigorous external-duplicate minimisation.

Reproducible files:
- `src/loto_research/h268_nz_powerball_terminal_duplicate_bound.py`
- `data/derived/h268_nz_powerball_terminal_duplicate_bound.json`

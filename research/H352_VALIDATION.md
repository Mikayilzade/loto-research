# H352 independent validation

Validated 2026-08-29.

1. H225-X* remains terminal: H225-X20 exact closure certificate is unchanged at 0 coefficient survivors / 0 legal shift tuples.
2. Current Enable game rules were checked directly. They describe the weekly guaranteed winner as a random selection from unique eligible tickets, not a player-controlled monopoly of six-digit Game Numbers.
3. Current Super Draw rules were checked directly. Each weekly ticket produces one entry, entries may originate on multiple participating lottery sites, there is no per-person entry limit, and one RNG winner is selected from all eligible entries.
4. Because external eligible entries already exist, simultaneous legal branches exist where the target player receives neither the weekly guaranteed prize nor the Super Draw prize.
5. Jackpot full-cover concession was deliberately favorable: grant £25,000 guaranteed once N reaches the entire 10^6 six-digit universe. At £1/ticket the resulting net is still at most -£975,000.
6. Boundary evaluation: N=1 -> -£1; N=267 -> -£267; N=999999 -> -£999999; N=1000000 -> -£975000; N=1000001 -> -£975001; N=2000000 -> -£1975000.

Arithmetic inconclusive: 0.
Closure-relevant inconclusive: 0.
Conclusion: H352 CLOSED / NO SUCCESS.

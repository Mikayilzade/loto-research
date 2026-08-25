# H225-X15 / H225-X16 validation

Authoritative workflow run: `32805383127` (`H225 X15-X16 exact continuation`), conclusion `success`.

## H225-X15 exact separator
Merged artifact: `9548040849`, digest `sha256:af5872c71b5c5c4ac39d7168b89fb4370a9507b5a9a537e4fe4a5aff65126678`.

Independent checks on the downloaded merged packet:
- packet/source: `H225-X15` / `H225-X14`;
- exactly 44 ordered jobs (`0..43`);
- 44 active survivor chunks;
- 44/44 exact counterexamples found;
- `inconclusive_active_jobs = 0`;
- `all_selected_active_designs_broken = true`;
- 44 unique balanced counterexamples;
- 44 genuinely new witnesses;
- witness packet contains exactly 44 witnesses and is deduplicated against H234 and H225-X1/X3/X5/X7/X9/X11/X13;
- authoritative X14 source totals asserted as 76,196 coefficient survivors / 3,807,980 legal shift tuples.

## H225-X16 full exact rescreen
Merged artifact: `9548762247`, digest `sha256:16e55597261a820cd00561541cba10e5c1feeee3885b0a81b7520846be1f9d13`.

Independent checks on the downloaded merged packet:
- packet/source: `H225-X16` / `H225-X15`;
- exactly 44 unique `(sector, chunk)` shards in canonical 11×4 order;
- exactly 11 sectors;
- sector quotient-state counts sum to exactly **306,450** and match the top-level screened total;
- sector survivor-state counts sum exactly to **48,387**;
- sector legal-shift-tuple counts sum exactly to **2,116,464**;
- X15 witness payload contains 44 raw new witnesses / 5,632 affine-expanded instances;
- closure flag is false.

Reduction from X14 to X16:
- coefficient survivors removed: **27,809** (76,196 → 48,387);
- legal shift tuples removed: **1,691,516** (3,807,980 → 2,116,464).

## Conclusion
H225 is **not closed** at X16 because exact survivors remain positive. The mandatory next generation is H225-X17 exact separation over actual X16 survivors, followed by H225-X18 full rescreen if X17 yields genuinely new cuts. Closure may be claimed only if a full rescreen returns zero exact survivors after the 44-shard / 11-sector / 306,450-state consistency checks.

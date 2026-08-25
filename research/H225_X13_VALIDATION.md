# H225-X13 exact separator validation

Validated from workflow run `32801267776`, merged artifact `9546611965`, digest `sha256:d605873ab023f4fbbdc6b4b1c66cde7870f7242c679b4b41e84ac8dc40203315`.

## Strict gate checks

- packet: `H225-X13`
- source packet: `H225-X12`
- source run: `32796246076`
- source X12 survivors: **110,487 coefficient states / 6,180,594 legal shift tuples**
- total jobs/chunks: **44**, ordered IDs exactly `0..43`
- active survivor chunks: **44**
- counterexamples found: **44/44**
- inconclusive active jobs: **0**
- unique balanced counterexamples: **44**
- genuinely new witnesses after history deduplication: **44**
- `all_selected_active_designs_broken == true`
- witness packet count: **44**

The witness packet declares deduplication against `H234`, `H225-X1`, `H225-X3`, `H225-X5`, `H225-X7`, `H225-X9`, and `H225-X11`, and records every stored witness as balanced and returned by unrestricted exact `n3<=2` MILP separation.

## Interpretation

**H225-X13 passes the separator gate rigorously.** This is not closure of H225: the next required step is H225-X14 full incremental rescreen over the unchanged 306,450-state quotient universe.

At validation time the workflow had produced all 44 X13 shard artifacts plus the merged X13 artifact. No X14 shard artifact had yet been published, so no X14 survivor claim is made here.

## Next strict gate

Accept H225-X14 only after all of the following are independently verified:
1. 44 unique chunk shards;
2. 11 sectors;
3. sector coefficient-state counts sum exactly **306,450** and match the top-level total;
4. survivor-state and legal-shift-tuple sector sums match their top-level totals;
5. zero exact survivor states => rigorous H225 closure; any positive survivor count => H225 remains open and X15/X16 must consume the actual validated X14 packet.

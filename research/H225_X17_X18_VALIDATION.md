# H225-X17 / H225-X18 validation certificate

Validated 2026-08-25 against authoritative GitHub Actions run `32809156175` (`success`).

## H225-X17
Merged artifact `9549487377`, digest `sha256:0279a59e00f7111475fa1b5d9242bc4c0fbc138c065afbea8376e5e83d41d230`.

Independent checks:
- exactly 44 ordered jobs (`0..43`);
- 44 active survivor chunks;
- 44 exact counterexamples found;
- **0 inconclusive active jobs**;
- `all_selected_active_designs_broken = true`;
- 44 unique/genuinely new balanced witnesses;
- witness packet deduplicated through H225-X17 predecessor history ending at H225-X15.

## H225-X18
Merged artifact `9550091411`, digest `sha256:147b9b9a5e7ee1dc43ed9c37db84cd85edc7caaee7acbbe381923e4214207892`.

Independent checks on the merged JSON:
- packet `H225-X18`, source `H225-X17`;
- exactly 44 canonical `(sector, chunk)` shards = 11 sectors × 4 chunks;
- exactly **306,450** quotient coefficient states screened;
- sector quotient-state sums equal the top-level total;
- sector survivor-state sums equal **3,300**;
- sector legal-shift-tuple sums equal **71,392**;
- X17 supplied 44 raw new witnesses / 5,632 affine instances;
- closure flag is false because exact survivors remain positive.

## Consequence
H225 is **not closed** at X18. The exact-family cutting-plane lane must continue from the actual X18 survivor packet. H225-X19/X20 is therefore the next generation; zero X20 survivors would close H225, while positive survivors require a subsequent generation.

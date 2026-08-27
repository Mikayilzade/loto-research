# H324 independent validation

Date: 2026-08-28

Validated independently from the research narrative.

## Arithmetic assertions

Free £10k / 40-winner draw:
- published pool = 300,000;
- max per person = 49;
- checked entries = 2,367;
- minimum external already-entered IDs, even granting all 49 to us: `2367 - 49 = 2318`;
- `2318 >= 40`, therefore a legal all-external 40-winner set exists;
- strict player cash floor = £0.

£1,000 LOW ODDS:
- `149 * 9.99 = 1488.51`;
- `1000 / 1488.51 = 0.6718127523 < 1`;
- cap `5 < 149` independently prevents one-player full takeover.

£10,000 for 2p:
- `1,189,995 * 0.02 = 23,799.90`;
- `10,000 / 23,799.90 = 0.4201698326 < 1`;
- cap `50,000 < 1,189,995`.

£20,000 for 2p:
- `1,749,999 * 0.02 = 34,999.98`;
- `20,000 / 34,999.98 = 0.5714288980 < 1`;
- cap `50,000 < 1,749,999`.

## Logical validation

For any finite draw selecting `k` winning entries, if at least `k` external valid entries remain possible, there exists a legal outcome selecting only external winners. Hence no strictly positive one-player cash floor follows from that draw alone. H324 applies this directly to the current 40-winner free giveaway and the single-winner paid pools.

No SUCCESS claim is warranted. H324 is a terminal rejection for the checked constructions only.

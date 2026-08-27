# H314 — WinWink £50k COIN FLIP finite instant-win cap bound

Status: **CLOSED / ZERO STRICT CASH FLOOR**
Snapshot: 2026-08-27

## Why this was worth testing

The live WinWink `£50k COIN FLIP!` is unusually transparent for an instant-win product:

- finite ticket universe: **142,857**;
- exactly **71,428** instant-win positions are cryptographically committed before sales;
- ticket price: **£1**;
- player cap: **21,429 tickets**;
- the operator publishes the SHA-256 commitment and says winning positions are sealed before sales and revealed only after entry;
- the live page states `1 in 2 win a prize` and lists cash/credit tiers.

This makes it a useful candidate for a strict worst-case finite-pool analysis rather than an EV estimate.

Operator source checked 2026-08-27:
- https://winwink.co.uk/competitions/50k-coin-flip

## Fresh live snapshot used

The operator page showed:

- sold tickets: **1,615 / 142,857**;
- instant wins remaining: **70,598 / 71,428**;
- max entries per person: **21,429**;
- postal entries already closed; online entry remained open.

Therefore:

- instant-winning positions already consumed = `71,428 - 70,598 = 830`;
- sold non-winning positions = `1,615 - 830 = 785`;
- total non-winning positions in the committed universe = `142,857 - 71,428 = 71,429`;
- remaining non-winning positions = `71,429 - 785 = 70,644`.

The consistency check is exact:

`70,598 remaining winners + 70,644 remaining non-winners = 141,242 remaining tickets`.

## Strict cap theorem

The player may control at most **21,429** tickets, while **70,644** non-winning positions remain.

Hence:

`70,644 >= 21,429`.

Because the winning positions are sealed/unreadable before purchase rather than player-selectable, there exists a legal allocation in which **all 21,429 tickets permitted to one player occupy non-winning positions**.

That legal outcome yields:

- maximum attempted spend: **£21,429**;
- instant-win cash received: **£0**;
- strict guaranteed cash floor: **£0**.

This is enough to reject the product as a guaranteed-profit construction. A displayed 50% hit-rate and a large advertised instant prize pool do not help a worst-case portfolio when the allowed player cap is smaller than the remaining losing inventory.

## Stronger reusable rule

For a finite precommitted instant-win pool with:

- `N` currently available identifiers;
- `W` currently available winning identifiers;
- `L = N-W` currently available losing identifiers;
- player acquisition cap `C`;
- winning IDs hidden/unselectable before irreversible purchase;

if `L >= C`, then the strict instant-win cash floor of every allowed one-player portfolio is zero. No prize-value arithmetic is needed.

H314 is a clean live witness of this rule:

- `L = 70,644`;
- `C = 21,429`;
- margin `L-C = 49,215`.

## Conclusion

**H314 CLOSED / CAP-BLOCKED.**

Do not reopen this exact draw as a guaranteed-profit candidate unless one of the structural facts materially changes, e.g. winning identifiers become player-selectable/reservable before payment or the effective acquisition cap exceeds the entire remaining non-winning inventory.

Reproducible files:

- `src/loto_research/h314_winwink_coinflip_cap_bound.py`
- `data/derived/h314_winwink_coinflip_cap_bound.json`
- `research/H314_STATUS.md`

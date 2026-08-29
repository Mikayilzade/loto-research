# H357 — UK NS&I Premium Bonds principal-preserving lottery bound

Status: **CLOSED FOR STRICT GUARANTEED PROFIT UNDER CURRENT STRUCTURE — NO SUCCESS**

## Why this packet
H356 left a narrow forward filter: look for genuinely external subsidy rather than another wager-funded multiplier. Premium Bonds are structurally different from ordinary lottery tickets: the deposited principal is withdrawable and HM Treasury-backed, while monthly prizes are funded separately instead of consuming the stake.

## Current rule facts checked (2026-08-29)
Official NS&I material states:
- holdings from £25 up to a maximum £50,000;
- capital is backed by HM Treasury and can be withdrawn without notice or penalty;
- no interest is paid; eligible £1 Bonds instead enter a monthly prize draw;
- August 2026 had exactly 136,946,390,805 eligible £1 Bonds, 6,224,837 prizes, and £433,663,575 total prize value;
- August odds were 22,000:1 per £1 Bond;
- from the September 2026 draw the announced prize-fund rate is 4.35% and odds improve to 21,000:1.

Sources: official NS&I Premium Bonds product page; official 3 Aug 2026 draw release; official 18 Aug 2026 rate announcement.

## Exact worst-case separator
Take the maximum permitted holding H = 50,000 £1 Bonds.

For the August 2026 draw:
- eligible universe N = 136,946,390,805;
- number of prizes K = 6,224,837;
- eligible Bonds outside our maximum holding = N-H = 136,946,340,805.

Even under the player-favourable structural assumption that every prize must go to a distinct Bond number, all K prizes can be assigned outside our portfolio because:

`N - H - K = 136,940,115,968 > 0`.

Therefore a legal zero-prize branch exists for the entire maximum holding. Smaller holdings inherit the same separator a fortiori.

The principal is still redeemable, so after cashing in the nominal deterministic gross floor is exactly the principal itself:

`£50,000 principal + £0 guaranteed prizes = £50,000 gross`.

Thus nominal guaranteed profit floor = **£0**, not strictly positive. The structure reaches 100% capital preservation but cannot cross >100% in every draw outcome.

This conclusion does not depend on expected return, tax treatment, or the September odds improvement: those affect distribution/expectation, not the existence of a zero-prize outcome.

## Closure
Premium Bonds are an important boundary case: external prize funding plus principal preservation removes the normal lottery loss floor, but random allocation among an enormous external eligible universe leaves zero guaranteed prize income.

**Arithmetic inconclusive: 0. Closure-relevant inconclusive: 0.**

Reopen criterion: a principal-preserving lottery/savings product with a binding minimum prize/interest/bonus paid to every eligible holding, or a finite eligible pool that can be deterministically monopolized within the holding cap.

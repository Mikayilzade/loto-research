# H272 VALIDATION — Japan Takarakuji Day draw 1118

Date: 2026-08-25
Validation state: **PASS for rejection bound**

## Inputs independently rechecked

Official 2026-08-05 Japan Lottery announcement states:
- draw 1118;
- sale period 2026-08-01 through 2026-08-25;
- draw date 2026-08-28;
- ticket price JPY 200;
- total issuance value JPY 4,000,000,000;
- 2 units;
- 10,000,000 tickets per unit;
- complete listed prize counts and values used by H272.

## Arithmetic gates

- issued tickets = `2 * 10,000,000 = 20,000,000`;
- acquisition cost = `20,000,000 * 200 = JPY 4,000,000,000`;
- prize sum = `300,000,000 + 100,000,000 + 19,800,000 + 200,000,000 + 100,000,000 + 200,000,000 + 400,000,000 + 400,000,000 + 180,000,000 = JPY 1,899,800,000`;
- return ratio = `1,899,800,000 / 4,000,000,000 = 0.47495 = 47.495%`;
- deficit = `JPY 2,100,200,000`.

The bound grants impossible-perfect ownership of every issued ticket, so there is no external-duplicate or missed-winning-identifier dilution left to model. Since even this dominating scenario is below cost, strict guaranteed profit from a complete inventory takeover is impossible for the checked draw.

## Reproducibility gate

`src/loto_research/h272_japan_takarakuji_day_full_issue_bound.py` contains assertions for the 20,000,000-ticket issuance, JPY 4bn cost, and JPY 1.8998bn complete prize total. The committed JSON mirrors those exact values.

## Result

**H272 CLOSED / REJECTED.** Reopen only if a Japanese finite-ticket issue adds a deterministic external subsidy large enough to exceed the full-issuance deficit, or publishes a fundamentally different prize schedule above 100% of complete face value.

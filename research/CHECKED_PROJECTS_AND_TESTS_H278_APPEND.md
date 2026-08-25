# CHECKED PROJECTS AND TESTS — H278 APPEND

## H278 — Georgia Lottery iHOPE 50% first-deposit bonus

Checked 2026-08-26 against current Georgia Lottery promotion/game pages.

Mechanism tested: deterministic external subsidy. Promotion 27012 gives eligible never-deposited iHOPE accounts a 50% first-deposit bonus, up to $125. Both deposit and bonus are restricted to lottery purchases, creating a strict wager-return hurdle of **2/3** if the objective is to recover more cash prize value than original deposited cash.

Exact constructions tested:
- Georgia FIVE full 100,000-number cover and additive symmetry bound: **53.6500%** wager return; **80.4750%** after bonus vs deposited cash.
- CASH POP all-15-number cover: legal minimum assigned-prize state gives **33.3333%** wager floor; **50.0000%** vs deposited cash after bonus.
- KENO base complete-combination covers for every 1–10 Spot size: best = **7 Spot, 65.0263524%**; **97.5395286%** vs deposited cash after bonus.
- KENO+BULLS-EYE complete-combination covers for every 1–10 Spot size: best = **4 Spot, 64.3343998%**; **96.5015997%** vs deposited cash after bonus.
- KENO MULTIPLIER: rejected for guarantee because the add-on doubles cost and has a legal `None` multiplier branch.

Result: **REJECTED for these exact-cover routes.** The deterministic subsidy is real and KENO 7 Spot is a close arithmetic near-miss, but no checked route crosses strict cash break-even.

Do not mark the entire Georgia promotion universe exhausted: other game families would require their own worst-case proof.

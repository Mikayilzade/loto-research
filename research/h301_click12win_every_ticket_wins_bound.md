# H301 — Click12Win Every Ticket Wins #3 full-pool bound

Status: **CLOSED / BELOW BREAK-EVEN**
Date checked: 2026-08-27

## Candidate

Current Click12Win listing: **Every Ticket Wins #3 — £18,000 Prize Pool**.

Published structure checked from the live competition page:
- 6,757 total tickets;
- £5.00 per ticket;
- every ticket is an instant win;
- instant schedule: 2×£500 cash, 5×£250 cash, 10×£100 cash, 20×£50 cash, 20×£25 Amazon eGift Card, 200×£10 Website Credit, 500×£5 Website Credit, 2,000×£2 Website Credit, 4,000×£1 Website Credit;
- final live-draw prize: £750;
- advertised total prize pool: £18,000.

The page also shows a finite 6,757-ticket cap and a published closing date of 8 November 2026.

## Exact bound

Full acquisition at face ticket price:

`6,757 × £5 = £33,785`.

Instant schedule count check:

`2 + 5 + 10 + 20 + 20 + 200 + 500 + 2,000 + 4,000 = 6,757`.

Instant face value:

`£17,250`.

Adding the entire final £750 prize gives the deliberately player-favourable full liability:

`£17,250 + £750 = £18,000`.

Therefore even under impossible-perfect ownership of every ticket and counting **website credit and Amazon gift cards at full cash-equivalent face value**:

- acquisition cost: **£33,785**;
- maximum advertised full-pool face liability: **£18,000**;
- return: **53.2780819890%**;
- deficit: **£15,785**.

The true withdrawable-cash result is much weaker. Counting only the explicitly cash-labelled instant prizes plus the £750 final prize gives **£5,000**, only **14.7994672192%** of full-pool cost.

## Closure logic

This is stronger than an execution objection. Even granting full deterministic ownership of all identifiers, full payment of every prize, no failed purchases, no taxes/fees, and treating non-cash credit at 100% face value, total player-facing liabilities remain below acquisition cost.

Therefore this current finite every-ticket-wins pool cannot yield a strict guaranteed positive gross via complete takeover.

No deeper ticket-allocation or residual-outcome search is warranted for this candidate unless a future version materially raises guaranteed liabilities or reduces exact full-pool acquisition cost by more than £15,785.

## Reproducibility

- `src/loto_research/h301_click12win_every_ticket_wins_bound.py`
- `data/derived/h301_click12win_every_ticket_wins_bound.json`

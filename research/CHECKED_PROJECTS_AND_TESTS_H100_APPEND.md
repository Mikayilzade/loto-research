# H100 append — prefunded notary-deposit claim assignment

Updated: 2026-08-19
Terminal state after this packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H100 Azerbaijan prefunded notary-deposit claim assignment** | buy a claim only after debtor cash is already deposited with notary; transfer creditor position to buyer | Civil Code Arts. 193–199 broadly allow assignment of non-personal claims; Notariat Arts. 74–75 require notary to pay creditor and restrict debtor recovery of deposited funds absent creditor consent/court order | **MECHANISM VALIDATED IN PRINCIPLE**; `research/h100_prefunded_notary_deposit_claim_assignment.md` |
| H100 execution theorem | verify deposit + assign + notify/recognize assignee before seller payment; require `deposit - deductions - price - all costs > 0` | construction can produce a deterministic floor if all gates are atomically locked | **PROMISING STRUCTURAL CLASS / NO LIVE INSTANCE** |
| H100 public-market search | official Azerbaijan Electronic Auction portal and web search for claim-right sales | official portal currently exposes seized-property auctions, not a visible class of already-funded notary-deposit claims; no verifiable below-face live claim found | **LIVE-SOURCE GATED** |
| H100 fee screen | current Ministry of Justice notarial fee schedule | unrelated-party 'other valued contracts' show 100 AZN state fee; exact classification/service fee for a specific assignment must be confirmed | **COST GATE IDENTIFIED** |

## New permanent control
Do not treat an ordinary receivable or court judgment as equivalent to a prefunded claim. H100 is only materially stronger when the cash is already held by the notary/custodian and the assignee's right to that exact funded amount can be recognized before acquisition price becomes irreversible.

## Reopen condition
Reopen only on a concrete below-face claim, an official assignee-payment procedure, or a notary-confirmed atomic assignment workflow.

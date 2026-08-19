# CHECKED_PROJECTS_AND_TESTS — H105 append

Updated: 2026-08-19

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H105 Azerbaijan private-enforcement advance** | Treat claimant's 2026 private-enforcement advance as a possible prefunded guaranteed refund | Current law makes refund depend on collection of the standard fee from the debtor; if collection is impossible, some/all advance can remain consumed. Money-claim advance is currently 20% of fixed standard-fee component. | **REJECTED as standalone prefunded guaranteed-refund class**; `research/h105_private_enforcement_advance_control.md` |
| **H105 matured private-enforcement refund subtype** | Screen only after debtor standard-fee collection is already complete and refund amount is final | Could become an ordinary matured receivable, but no public below-face live instance with assignee-payout lock found | **OPEN ONLY AS H101/H103-style live-instance subtype; do not treat unresolved advances as deterministic** |

Strategic effect: H105 prevents false equivalence between the strong H103 state-enforcement refund structure and the 2026 private-enforcement advance. Search stays focused on cash already segregated / refund already matured / successor payout lockable before buyer payment.

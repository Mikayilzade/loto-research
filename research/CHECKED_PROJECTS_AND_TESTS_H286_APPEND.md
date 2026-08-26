# CHECKED PROJECTS AND TESTS — H286 APPEND

## H286 — Michigan Lottery Daily Spin to Win
- Date checked: 2026-08-26.
- Mechanism class: guaranteed promotional reward / deterministic subsidy candidate.
- Positive structural fact: every eligible daily spin wins a prize.
- Fatal strict-guarantee blocker: the allowed prize classes include monthly giveaway entries; such an entry has a legal non-winning later drawing outcome and therefore $0 guaranteed withdrawable cash value.
- Exact strict cash floor per spin: **$0**.
- Repeated finite spins: no public bounded terminal rule was found that forces withdrawable Bonus Cash.
- State: **CLOSED / REJECTED for current mechanism**.
- Reopen gate: every possible wheel prize becomes positive withdrawable cash/cash-equivalent, or a finite terminal rule guarantees such cash after bounded spins.

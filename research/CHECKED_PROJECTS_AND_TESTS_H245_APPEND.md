# CHECKED_PROJECTS_AND_TESTS — H245 append

Date: 2026-08-24
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H245 UK Lotto current two-round format** | Buy all `C(59,6)=45,057,474` lines once; same £2 lines enter both rounds; exact deterministic fixed-prize count in each round; exclude jackpot from guaranteed floor | Full-space spend **£90,114,948**; two-round fixed cash **£32,846,150**; deterministic return **36.4492%**; fixed deficit **£57,268,798**. Full coverage itself guarantees Match-6 in both rounds, so the Must-Be-Won no-jackpot-winner rolldown branch cannot occur. Jackpot sharing with external winners has no useful hard pre-draw cap. | **REJECTED guaranteed-profit full coverage**; `research/h245_uk_lotto_two_round_full_space_closure.md` |

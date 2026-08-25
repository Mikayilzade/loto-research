# H275 — Singapore TOTO cascade / full-cover strict-guarantee screen

Date: 2026-08-25
Branch: `research-work`
Verdict: **REJECTED for the checked strict guaranteed-profit construction**.

## Why this candidate was opened
Singapore Pools TOTO has a real terminal-style cascade mechanism. Current official materials say that after the configured run of consecutive draws without a Group 1 winner, the unwon Jackpot is cascaded to the next prize group with winner(s). Current public FAQ describes the ordinary configuration as a cascade after the fourth consecutive draw. This is exactly the kind of externally accumulated-money mechanism prioritized by `STATUS.md`.

## Current rule facts used
- TOTO uses six selected numbers from 1–49; ordinary minimum cost is SGD 1.
- Six Winning Numbers plus one Additional Number are drawn.
- Fixed lower prizes are Group 5 = SGD 50 for 4 Winning Numbers, Group 6 = SGD 25 for 3 Winning Numbers + Additional Number, Group 7 = SGD 10 for 3 Winning Numbers.
- Group 1–4 are share-based pools; multiple winning shares divide the relevant amount.
- If the Jackpot remains unwon through the configured cascade sequence, the Jackpot is paid to the next prize group with winner(s), starting from Group 2 and moving downward.

Official sources checked:
- Singapore Pools rules index (TOTO Game Rules listed): https://www.singaporepools.com.sg/en/rules/pages/index.html
- Singapore Pools TOTO Game Rules PDF: https://www.singaporepools.com.sg/en/rules/Pages/pdf/toto-game-rules.pdf
- Singapore Pools FAQ on cascade draws: https://www.singaporepools.com.sg/en/faq/Pages/lottery-betting.html
- Singapore Pools current how-to-play page: https://online.singaporepools.com/en/lottery/how-play-toto
- Singapore Pools bet types: https://online2.singaporepools.com/en/lottery/toto-bet-types
- GRA search currently lists TOTO Game Rules effective 11 Aug 2026: https://www.gra.gov.sg/search?indexCatalogue=site-search&searchQuery=2026&wordsMode=AllWords

Recent result sanity check: 20 Aug 2026 had no Group 1 winner and the SGD 2,953,462 Group 1 amount was snowballed, consistent with the checked mechanism.

## Gate 1 — cascade cannot be forced by any nonempty portfolio
Let the portfolio contain any ordinary six-number selection `x`. The lottery can legally draw exactly `x` as its six Winning Numbers. In that legal outcome the portfolio has a Group 1 winning share.

Therefore every nonempty portfolio preserves at least one legal outcome in which Group 1 **is won**. It cannot guarantee the prerequisite `no Group 1 winner` branch in every legal draw.

A full cover makes the blocker even stronger: it always contains the actual six Winning Numbers, so it necessarily creates Group 1 in every draw and suppresses the cascade branch we wanted to exploit.

## Gate 2 — exact one-copy full-cover lower-tier floor
There are

`C(49,6) = 13,983,816`

ordinary six-number selections, so one-copy full coverage costs exactly **SGD 13,983,816** at SGD 1 each.

For any fixed draw (6 winning numbers, 1 additional, 42 other numbers), the full cover has the following exact fixed-tier multiplicities:

- Group 5 (exactly 4 winning, no additional): `C(6,4) C(42,2) = 12,915`;
- Group 6 (3 winning + additional): `C(6,3) C(42,2) = 17,220`;
- Group 7 (exactly 3 winning, no additional): `C(6,3) C(42,3) = 229,600`.

Fixed guaranteed gross:

- Group 5: `12,915 × 50 = SGD 645,750`;
- Group 6: `17,220 × 25 = SGD 430,500`;
- Group 7: `229,600 × 10 = SGD 2,296,000`;
- total = **SGD 3,372,250**.

Return on complete acquisition cost:

**SGD 3,372,250 / SGD 13,983,816 = 24.1153773762%**.

Deficit before relying on any shared pool = **SGD 10,611,566**.

## Gate 3 — duplicate stress closes reliance on Groups 1–4
Groups 1–4 are explicitly share-based. The checked rules do not publish a useful hard pre-draw cap on external winning shares that a player can monopolize or reserve.

For strict-guarantee analysis, shared pools therefore cannot be assigned a positive duplicate-robust floor: legal external duplicate winning shares can dilute our share. This is the same core obstruction previously seen in multiple H-packets, but here it is combined with the stronger fact that full coverage itself prevents the cascade branch.

Hence the only draw-invariant duplicate-robust amount for the checked full-cover takeover is the fixed Group 5–7 gross above, only **24.1154%** of cost.

## Conclusion
Singapore TOTO is a genuine cascade mechanism, but it fails both structural requirements needed for a strict guaranteed-profit takeover:

1. no nonempty portfolio can force the no-Group-1 trigger in every legal draw;
2. complete coverage necessarily wins Group 1 and therefore suppresses cascade;
3. after external-duplicate stress, the invariant fixed lower-tier floor is only 24.1154% of cost.

Close H275 for this construction. Reopen only if rules introduce a deterministic external payment that is paid even when Group 1 is won, a hard monopolizable cap on eligible winning shares, or a fixed per-winning-selection cascade/subsidy that survives duplicate stress.

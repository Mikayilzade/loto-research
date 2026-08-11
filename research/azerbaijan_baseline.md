# Azerbaijan baseline — exact combinatorial EV

Updated: 2026-08-11
Status: initial exact baseline, no historical prediction used

This note establishes a strict mathematical baseline for two current Azərlotereya games using the published rules and prize tables. The calculations are analytical, not Monte Carlo.

Official sources:
- Beşdə 5: https://www.azerlotereya.com/game/besde5
- Beşdə 5 FAQ: https://www.azerlotereya.com/faq/besde5
- Super Keno: https://www.azerlotereya.com/game/superkeno

## 1. Beşdə 5

### Published mechanics
- Player selects 5 numbers from 36.
- Draw selects 5 numbers from 36.
- One variant costs 1 AZN.
- A ticket must contain at least 2 variants, so the minimum ticket price is 2 AZN.
- Published per-variant prizes:
  - 5 matches: 50,000 AZN large prize, subject to special multi-winner rule;
  - 4 matches: 100 AZN;
  - 3 matches: 10 AZN;
  - 2 matches: 2 AZN.
- Top-prize sharing rule is nonlinear:
  - one winning variant: 50,000 AZN;
  - two winning variants: each receives 50,000 AZN;
  - three or more winning variants: a total 100,000 AZN is split among them.

### Exact match probabilities
For exactly `m` matches:

`P(m) = C(5,m) * C(31,5-m) / C(36,5)`

| Matches | Probability | Approx. percent | Published prize | EV contribution per 1 AZN variant |
|---:|---:|---:|---:|---:|
| 0 | 0.450701871658 | 45.07018717% | 0 | 0 |
| 1 | 0.417316547831 | 41.73165478% | 0 | 0 |
| 2 | 0.119233299380 | 11.92332994% | 2 | 0.238466599 |
| 3 | 0.012334479246 | 1.23344792% | 10 | 0.123344792 |
| 4 | 0.000411149308 | 0.04111493% | 100 | 0.041114931 |
| 5 | 0.000002652576 | 0.00026526% | 50,000 | 0.132628809 |

Jackpot/top-match probability is exactly `1 / C(36,5) = 1 / 376,992`.

### Upper-bound base EV
If we make the favorable assumption that **every** 5-match variant receives the full 50,000 AZN, ignore tax, ignore execution cost and ignore any sharing reduction:

- expected gross payout per 1 AZN variant = **0.535555131 AZN**;
- net EV per variant = **-0.464444869 AZN**;
- gross return ratio = **53.5555%**;
- house-edge-equivalent gap before tax/sharing = **46.4445%**.

This is deliberately an upper bound. The actual expectation can only be lower when a 5-match prize is split among 3+ winning variants or when tax applies.

### Immediate implication
Ordinary combination systems/wheels cannot turn this baseline positive merely by rearranging the same number of variants, because expectation is linear. They can change variance and coverage, and unusual number choices may affect top-prize sharing if player choices are non-uniform, but the base per-variant payout gap is large.

This does **not** rule out:
- promotions/cashback;
- a rule or implementation anomaly;
- exploitable non-randomness that survives out-of-sample testing;
- crowd-selection effects large enough to change the top-prize share;
- a future rule/prize change.

## 2. Super Keno

### Published mechanics
- Player selects 10 numbers from 70.
- Draw selects 20 numbers from 70.
- Base ticket/stake shown as 1 AZN.
- Published base prize table:
  - 10 matches: 100,000 AZN;
  - 9: 1,500 AZN;
  - 8: 150 AZN;
  - 7: 15 AZN;
  - 6: 5 AZN;
  - 5: 2 AZN;
  - exactly 1: 1 AZN.
- The operator also advertises up to 1,000,000 AZN and provides 2x/5x/10x multiplier choices. The exact stake-to-multiplier economics must be modeled separately rather than assuming the advertised maximum is the 1-AZN base prize.

### Exact match probabilities
For exactly `m` of the player's 10 selected numbers appearing among the 20 drawn:

`P(m) = C(10,m) * C(60,20-m) / C(70,20)`

| Matches | Probability | Approx. percent | Base prize | EV contribution per 1 AZN base entry |
|---:|---:|---:|---:|---:|
| 0 | 0.025894028283 | 2.58940283% | 0 | 0 |
| 1 | 0.126312333087 | 12.63123331% | 1 | 0.126312333 |
| 2 | 0.257135820928 | 25.71358209% | 0 | 0 |
| 3 | 0.287035334989 | 28.70353350% | 0 | 0 |
| 4 | 0.194075027635 | 19.40750276% | 0 | 0 |
| 5 | 0.082805345124 | 8.28053451% | 2 | 0.165610690 |
| 6 | 0.022501452479 | 2.25014525% | 5 | 0.112507262 |
| 7 | 0.003830034465 | 0.38300345% | 15 | 0.057450517 |
| 8 | 0.000388987875 | 0.03889879% | 150 | 0.058348181 |
| 9 | 0.000021169408 | 0.00211694% | 1,500 | 0.031754112 |
| 10 | 0.000000465727 | 0.00004657% | 100,000 | 0.046572698 |

### Base EV before tax
Using the displayed base prize table and a 1 AZN base entry:

- expected gross payout = **0.598555794 AZN**;
- net EV = **-0.401444206 AZN**;
- gross return ratio = **59.8556%**;
- gap before tax = **40.1444%**.

The official rules state a 10% tax formula for sufficiently large winnings based on the prize less ticket price and 500 AZN, so post-tax EV is lower. The exact after-tax model will be added once the stake/multiplier combinations are fully normalized.

### Important data-quality observation
The page simultaneously shows a 100,000 AZN base top tier and advertises a 1,000,000 AZN maximum. This is not treated as a contradiction or exploit: the published multiplier mechanism appears to explain it. The model must store base stake and multiplier as separate variables.

## 3. What these baselines tell us

These calculations are useful controls:

1. Historical draw-frequency patterns must overcome a very large negative baseline before they can create positive EV.
2. A model that merely predicts numbers slightly better than random is economically irrelevant unless the improvement is large enough to overcome the payout gap.
3. Portfolio/wheel strategies should be evaluated primarily for coverage/variance unless prize nonlinearities or sharing rules create an EV effect.
4. Structural mechanisms, promotions, taxes, multiplier pricing, winner sharing and operator rules are likely to be more promising research targets than raw frequency chasing.

## Next analysis
- Capture exact Super Keno multiplier pricing.
- Model Beşdə 5 top-prize sharing as a function of total sales and player-number popularity.
- Capture 4+4 full prize table and compute exact EV.
- Discover the official archive/API endpoints and ingest historical draws.
- Compare all calculations with the reusable code in `src/loto_research/probability.py`.

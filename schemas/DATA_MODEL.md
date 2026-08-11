# DATA MODEL

Updated: 2026-08-11

The data model is intentionally split into immutable raw source data, normalized game definitions, normalized draws and derived research outputs.

## 1. Game definition
Minimum fields for each rule version:

- `game_id` — stable project identifier.
- `rule_version_id` — unique version for a period with unchanged mechanics.
- `jurisdiction` — country/state/market where the entry is sold.
- `operator` — official operator.
- `name` — public game name.
- `category` — draw_numbers / multi_pool_jackpot / keno / bingo / scratch / instant / raffle / pool / promo / other.
- `valid_from`, `valid_to` — dates for this rule version.
- `base_price`, `currency`.
- `purchase_channel` — retail / online / subscription / mixed.
- `main_pool_size`, `main_numbers_selected`, `main_numbers_drawn`.
- `bonus_pool_size`, `bonus_numbers_selected`, `bonus_numbers_drawn` where relevant.
- `replacement_between_pools` — whether balls/numbers are returned between stages.
- `draw_schedule`.
- `prize_model` — fixed / pari_mutuel / progressive / hybrid.
- `jackpot_rollover_rule`.
- `rolldown_or_must_win_rule`.
- `multiplier_rule`.
- `tax_rule`.
- `claim_rule`.
- `purchase_limit`.
- `official_rules_source_id`.

A game that changes price, matrix, prize table or rollover logic gets a new `rule_version_id`; historical draws must reference the correct version.

## 2. Prize tier
One row per tier and rule version:

- `rule_version_id`
- `tier_id`
- `main_matches`
- `bonus_matches`
- `other_condition`
- `base_prize`
- `currency`
- `fixed_or_variable`
- `multiplier_eligible`
- `share_rule`
- `allocation_percent` where a prize pool is percentage-based

## 3. Draw record
Normalized draw fields:

- `game_id`
- `rule_version_id`
- `draw_id`
- `draw_datetime_local`
- `draw_datetime_utc` where known
- `main_numbers`
- `bonus_numbers`
- `multiplier`
- `advertised_jackpot`
- `cash_jackpot_value`
- `sales` where published
- `winner_count_by_tier` where published
- `prize_value_by_tier` where variable
- `rollover_count`
- `rolldown_flag`
- `source_id`
- `retrieved_at`
- `raw_record_hash`

Numbers should be stored canonically sorted only when draw order is irrelevant. If draw order can carry information, preserve both original order and sorted representation.

## 4. Raw source storage
Raw source data is immutable.

Suggested layout:

```text
data/raw/<game_id>/<retrieval_date>/...
data/normalized/<game_id>/draws.parquet
```

Every collector should retain:
- source URL;
- request/retrieval timestamp;
- raw response or reproducible snapshot when permitted;
- parser version / commit hash.

## 5. Strategy / hypothesis result
Each experiment records:

- `hypothesis_id`
- `game_id`
- `rule_version_id`
- `dataset_version`
- `train_period`
- `test_period`
- `baseline`
- `method`
- `random_seed` where relevant
- `gross_ev`
- `net_ev`
- `variance`
- `probability_of_profit`
- `confidence_interval`
- `capital_required`
- `execution_assumptions`
- `multiple_testing_adjustment`
- `status`
- `code_commit`

## 6. Economic normalization
Never compare games on advertised jackpot alone.

For any candidate strategy calculate at least:

`net payoff = gross prize - taxes - commissions - ticket cost - execution cost - FX cost`

For shared jackpots calculate expected share conditional on winning. For annuities record both advertised value and a discounted present-value estimate with an explicit discount-rate assumption.

## 7. Quality flags
Rows may carry flags such as:

- `official_source`
- `rule_ambiguous`
- `missing_draws`
- `rule_change_boundary`
- `scraped_dynamic_page`
- `prize_table_inconsistent`
- `tax_treatment_pending`

Ambiguity is not silently filled by assumption; it becomes a research task.

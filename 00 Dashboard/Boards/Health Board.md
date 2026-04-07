# Health Board

This board is the health detail view. It uses daily notes plus imported health logs. The baseline summary lives under the Health area, not Knowledge.

## Core Links

- [[03 Areas/Health/Health|Health]]
- [[04 Projects/Personal/Spring 2026 Health Reset|Spring 2026 Health Reset]]
- [[03 Areas/Health/Baselines/2026-03 Fitness And Diet Baseline|2026-03 Fitness And Diet Baseline]]

## Daily Check-Ins

Only log what is realistic to keep up: weight, meals, and training.

```dataview
TABLE date AS Date, weight_kg AS "Weight (kg)", meals AS Meals, training AS Training
FROM "02 Daily"
WHERE type = "daily" AND (weight_kg OR meals OR training)
SORT date DESC
LIMIT 30
```

## Imported Baseline History

The imported March baseline does not have real calendar dates, so it is shown as inferred day order instead of fake dates.

```dataview
TABLE inferred_day AS "Imported Day", weight_kg AS "Weight (kg)", meal_entries AS "Meal Logs", training_entries AS "Training Logs", meals AS Meals, training AS Training
FROM "03 Areas/Health/Logs"
WHERE type = "health_log" AND log_source = "gemini_fitness_daily_summary"
SORT inferred_day ASC
```

## Baselines

```dataview
TABLE source_type AS "Source Type", updated AS Updated, source AS Source
FROM "03 Areas/Health/Baselines"
WHERE type = "health_baseline"
SORT updated DESC
```

## Weekly Reviews

```dataview
TABLE date AS Date, file.link AS Review
FROM "08 Reviews/Weekly"
WHERE type = "review"
SORT date DESC
LIMIT 12
```

## Monthly Reviews

```dataview
TABLE date AS Date, file.link AS Review
FROM "08 Reviews/Monthly"
WHERE type = "review"
SORT date DESC
LIMIT 12
```

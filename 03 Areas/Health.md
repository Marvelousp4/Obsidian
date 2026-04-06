---
type: area
status: active
focus: Maintain energy, recovery, and resilience
review_rhythm: weekly
tags:
  - area
---

# Health

## Purpose

Support performance with sleep, movement, nutrition, and recovery.

## Standards

- Capture trends, not only incidents.
- Keep protocols simple enough to follow.

## Current Focus

- Sleep
- Training
- Recovery

## Core Notes

- [[05 Knowledge/Personal/2026-03 Fitness And Diet Baseline|2026-03 Fitness And Diet Baseline]]
- [[04 Projects/Personal/Spring 2026 Health Reset|Spring 2026 Health Reset]]

## Daily Metrics

Record body data directly inside the daily note using inline fields.

```dataview
TABLE date AS Date, weight_kg AS "Weight (kg)", sleep_hours AS "Sleep", steps AS Steps, training_sessions AS "Training", cardio_minutes AS "Cardio", protein_g AS "Protein (g)", water_l AS "Water (L)", energy_score AS Energy, mood_score AS Mood, digestion AS Digestion
FROM "02 Daily"
WHERE type = "daily" AND (weight_kg OR sleep_hours OR steps OR training_sessions OR cardio_minutes OR protein_g OR water_l OR energy_score OR mood_score OR digestion)
SORT date DESC
LIMIT 30
```

## Weekly Report

```dataview
TABLE round(avg(rows.weight_kg), 2) AS "Avg Weight", sum(rows.training_sessions) AS "Training Sessions", round(avg(rows.sleep_hours), 1) AS "Avg Sleep", round(avg(rows.steps), 0) AS "Avg Steps", round(avg(rows.protein_g), 0) AS "Avg Protein", round(avg(rows.water_l), 1) AS "Avg Water"
FROM "02 Daily"
WHERE type = "daily" AND (weight_kg OR sleep_hours OR steps OR training_sessions OR protein_g OR water_l)
GROUP BY week
SORT key DESC
LIMIT 8
```

## Monthly Report

```dataview
TABLE round(avg(rows.weight_kg), 2) AS "Avg Weight", sum(rows.training_sessions) AS "Training Sessions", round(avg(rows.sleep_hours), 1) AS "Avg Sleep", round(avg(rows.steps), 0) AS "Avg Steps", round(avg(rows.protein_g), 0) AS "Avg Protein", round(avg(rows.water_l), 1) AS "Avg Water"
FROM "02 Daily"
WHERE type = "daily" AND (weight_kg OR sleep_hours OR steps OR training_sessions OR protein_g OR water_l)
GROUP BY dateformat(date, "yyyy-MM") AS Month
SORT Month DESC
LIMIT 6
```

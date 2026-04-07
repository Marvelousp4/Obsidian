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

Run a simple health system that is sustainable: body weight, food notes, training, and recovery patterns.

## What Belongs Here

- Daily weight, meals, and training signals
- Baselines and trend summaries
- Health projects with a clear intervention window

## What Does Not Belong Here

- Medical diagnosis without source context
- Over-detailed metrics that you will not maintain

## Operating Rule

Daily health capture stays minimal: `weight_kg::`, `meals::`, and `training::`. Baselines and imported logs live inside this area, not in Knowledge.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "health" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "health"
SORT file.mtime DESC
LIMIT 20
```

## Health Data

- [[00 Dashboard/Boards/Health Board|Health Board]]
- [[03 Areas/Health/Baselines/2026-03 Fitness And Diet Baseline|2026-03 Fitness And Diet Baseline]]
- [[04 Projects/Personal/Spring 2026 Health Reset|Spring 2026 Health Reset]]

```dataview
TABLE inferred_day AS "Imported Day", weight_kg AS "Weight (kg)", meals AS Meals, training AS Training
FROM "03 Areas/Health/Logs"
WHERE type = "health_log"
SORT inferred_day ASC
```

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

---
type: area
status: active
focus: Build a clear capital and cash discipline
review_rhythm: weekly
tags:
  - area
---

# Finance

## Purpose

Keep money decisions explicit, reviewable, and separated from market noise.

## What Belongs Here

- Net worth and liquidity review
- Investment principles and decision logs
- Spending rules and recurring obligations

## What Does Not Belong Here

- Raw broker statements without interpretation
- One-off market headlines unless they change a rule

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "finance" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "finance"
SORT file.mtime DESC
LIMIT 20
```

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

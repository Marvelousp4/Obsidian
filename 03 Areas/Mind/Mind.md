---
type: area
status: active
focus: Improve clarity, emotional regulation, and self-observation
review_rhythm: weekly
tags:
  - area
---

# Mind

## Purpose

Track mental patterns, decision quality, stress signals, and reflection routines.

## What Belongs Here

- Reflection patterns
- Stress/recovery signals
- Private decision retrospectives

## What Does Not Belong Here

- Generic self-help quotes
- Sensitive raw writing that should stay private outside Git

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "mind" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "mind"
SORT file.mtime DESC
LIMIT 20
```

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

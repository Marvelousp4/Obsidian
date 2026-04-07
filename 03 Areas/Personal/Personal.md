---
type: area
status: active
focus: Keep life admin, identity, and direction coherent
review_rhythm: weekly
tags:
  - area
---

# Personal

## Purpose

Keep personal commitments, profile, logistics, and long-term direction from fragmenting.

## What Belongs Here

- Personal profile and identity assets
- Life admin projects
- Important personal decisions

## What Does Not Belong Here

- Work CRM objects
- Raw health metrics that belong to Health

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "personal" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "personal"
SORT file.mtime DESC
LIMIT 20
```

## Personal Profile

- [[06 People/Personal/Personal Profile - Linhao Bai|Personal Profile - Linhao Bai]]

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

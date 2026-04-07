---
type: area
status: active
focus: Keep important relationships intentional
review_rhythm: weekly
tags:
  - area
---

# Relationships

## Purpose

Maintain context around people who matter beyond transactional work records.

## What Belongs Here

- Important personal/professional relationship context
- Follow-up reminders that should not vanish
- Relationship review notes

## What Does Not Belong Here

- Work contacts that belong to 09 Work/Accounts
- Random name drops without context

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "relationships" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "relationships"
SORT file.mtime DESC
LIMIT 20
```

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

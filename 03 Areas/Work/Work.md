---
type: area
status: active
focus: Build and compound professional leverage
review_rhythm: weekly
tags:
  - area
---

# Work

## Purpose

Operate customer delivery, industry knowledge, and professional execution without mixing it into personal systems.

## What Belongs Here

- Work standards and review rhythm
- Links into the work CRM
- Work knowledge synthesis

## What Does Not Belong Here

- Raw customer issues; those belong in 09 Work/Issues
- Personal health/finance notes

## Operating Rule

Use this area page as the work domain doorway. Operational records live in `09 Work`; bounded work initiatives live in `04 Projects/Work`; reusable work lessons live in `05 Knowledge/Work`.

## Active Projects

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND status != "archived"
SORT status ASC, account ASC, file.name ASC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "work"
SORT file.mtime DESC
LIMIT 20
```

## Work System

- [[09 Work/Work Index|Work Index]]
- [[00 Dashboard/Boards/Work Control Board|Work Control Board]]
- [[09 Work/Issues/Issue Index|Current Issue Index]]
- [[09 Work/Issues/Archive/Completed/Completed Issues Index|Completed Issues Index]]

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

---
type: area
status: active
focus: Turn study into usable models and skill
review_rhythm: weekly
tags:
  - area
---

# Learning

## Purpose

Convert courses, videos, and study notes into skills or reusable knowledge.

## What Belongs Here

- Learning plans
- Course notes after synthesis
- Skill practice projects

## What Does Not Belong Here

- Raw transcripts; those start in 10 Raw
- Bookmarks without extraction

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "learning" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "learning"
SORT file.mtime DESC
LIMIT 20
```

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

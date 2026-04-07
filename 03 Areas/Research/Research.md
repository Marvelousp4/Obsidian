---
type: area
status: active
focus: Build a pipeline of questions, hypotheses, and experiments
review_rhythm: weekly
tags:
  - area
---

# Research

## Purpose

Manage research questions, papers, labs, hypotheses, and synthesis.

## What Belongs Here

- Research questions and hypotheses
- Paper synthesis
- Lab/team context and research people

## What Does Not Belong Here

- Raw PDFs before extraction
- Work support issues unless they become reusable research questions

## Operating Rule

Capture raw input in the daily note first. Promote it here only when it changes standards, projects, or review focus for this area.

## Active Projects

```dataview
TABLE status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area = "research" AND status != "archived"
SORT file.mtime DESC
```

## Related Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area = "research"
SORT file.mtime DESC
LIMIT 20
```

## Research People

- [[06 People/Professional/STAR Lab|STAR Lab]]

## Review Prompt

- What changed in this area this week?
- What standard or project should be updated?
- What can be ignored or archived?

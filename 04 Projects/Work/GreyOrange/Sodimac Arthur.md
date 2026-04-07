---
type: "project"
area: work
account: "GreyOrange"
project_kind: "site_issue_bucket"
site: "Sodimac Arthur"
status: "support_only"
owner: "bai"
started: ""
next: "Backfill deployment details when a confirmed source appears."
tags: []
---

# GreyOrange - Sodimac Arthur

## Goal

Hold issue history for a site or sub-site that appears in support data but was not found in the GreyOrange deployment workbook.

## Background

- Created automatically from imported issue history.
- Deployment details still need confirmation from live ops records or customer context.

## Current Status

- Status: support_only

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "GreyOrange" AND site = "Sodimac Arthur" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND site = "Sodimac Arthur"
SORT last_updated_date DESC
LIMIT 20
```

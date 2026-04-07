---
type: "project"
account: "GreyOrange"
project_kind: "site_issue_bucket"
site: "Sodimac Flr"
status: "support_only"
owner: "bai"
started: ""
next: "Backfill deployment details when a confirmed source appears."
tags: []
---

# GreyOrange - Sodimac Flr

## Goal

Hold issue history for a site or sub-site that appears in support data but was not found in the GreyOrange deployment workbook.

## Background

- Created automatically from imported issue history.
- Deployment details still need confirmation from live ops records or customer context.

## Current Status

- Status: support_only

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Sodimac Flr"
SORT last_updated_date DESC
```

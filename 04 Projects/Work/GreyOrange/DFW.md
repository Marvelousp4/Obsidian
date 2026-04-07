---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "DFW"
status: "stopped"
owner: "bai"
started: ""
next: "Confirm whether this site is decommissioned and capture the historical context if it is."
tags: []
---

# GreyOrange - DFW

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 24
- Notes: Deployment appears stopped.

## Site / Deployment Information

- Customer: GreyOrange
- Site: DFW
- Deployment Type: L
- Fleet Size: 24
- Address: 

## Current Status

- Status: stopped
- Operational note: Deployment appears stopped.

## Next Steps

- [x] Confirm whether this site is decommissioned and capture the historical context if it is.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "GreyOrange" AND site = "DFW" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND site = "DFW"
SORT last_updated_date DESC
LIMIT 20
```

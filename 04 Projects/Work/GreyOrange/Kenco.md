---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Kenco"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kenco

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L&H
- Fleet size: 
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kenco
- Deployment Type: L&H
- Fleet Size: 
- Address: Kenco Reckitt
345 Toy Wright Rd Jefferson, GA 30549

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues"
WHERE type = "issue" AND account = "GreyOrange" AND site = "Kenco" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Archive/Completed Issues/GreyOrange"
WHERE type = "issue" AND site = "Kenco"
SORT last_updated_date DESC
LIMIT 20
```

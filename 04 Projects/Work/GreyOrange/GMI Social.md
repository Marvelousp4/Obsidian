---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "GMI Social"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - GMI Social

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L&H&AP
- Fleet size: 
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: GMI Social
- Deployment Type: L&H&AP
- Fleet Size: 
- Address: 1871 Willow Springs Church Rd, Social Circle. GA 30025

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "GreyOrange" AND site = "GMI Social" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND site = "GMI Social"
SORT last_updated_date DESC
LIMIT 20
```

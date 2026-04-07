---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Fairlife"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Fairlife

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: AP
- Fleet size: 12
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Fairlife
- Deployment Type: AP
- Fleet Size: 12
- Address: 17000 W Glendale Ave, Litchfield Park, AZ 85340

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues"
WHERE type = "issue" AND account = "GreyOrange" AND site = "Fairlife" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Archive/Completed Issues/GreyOrange"
WHERE type = "issue" AND site = "Fairlife"
SORT last_updated_date DESC
LIMIT 20
```

---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Kenco Goodyear"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kenco Goodyear

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L case picking
- Fleet size: 
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kenco Goodyear
- Deployment Type: L case picking
- Fleet Size: 
- Address: Kenco Goodyear
Kenco Logistic Services,LLc..16811 WCommerce
Drve, Goodyear AZ 85338, United States
Donna Dame  donna.dame@kencogroup.com
+812-4806492

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "GreyOrange" AND site = "Kenco Goodyear" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND site = "Kenco Goodyear"
SORT last_updated_date DESC
LIMIT 20
```

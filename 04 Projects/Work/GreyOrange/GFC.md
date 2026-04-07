---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "GFC"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - GFC

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: 
- Fleet size: 
- Notes: Fleet note: 2 AP units, 2 L units, and 2 H units.

## Site / Deployment Information

- Customer: GreyOrange
- Site: GFC
- Deployment Type: 
- Fleet Size: 
- Address: Grey Orange Inc
3975 Lakefield Court Suite 110 Suwanee, GA 30024        Harshita Puri
+1 (857) 437-8426

## Current Status

- Status: active
- Operational note: Fleet note: 2 AP units, 2 L units, and 2 H units.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "GFC"
SORT last_updated_date DESC
```

---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Dorman Warsaw"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Dorman Warsaw

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L &M
- Fleet size: 
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Dorman Warsaw
- Deployment Type: L &M
- Fleet Size: 
- Address: RB Distribution ,lNc.25 Dorman Drive, Warsaw, KY 41095

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Dorman Warsaw"
SORT last_updated_date DESC
```

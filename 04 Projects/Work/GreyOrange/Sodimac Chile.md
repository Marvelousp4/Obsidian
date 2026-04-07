---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Sodimac Chile"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Sodimac Chile

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 63
- Notes: Very old deployment site with 63 robots in total.

## Site / Deployment Information

- Customer: GreyOrange
- Site: Sodimac Chile
- Deployment Type: L
- Fleet Size: 63
- Address: Sodimac S.A.(R.U.T. 96.792.430-K) ( 100173 ) 
Av.Presidente Eduardo FreiN N°3092 Santiago RENCA, , 
Chile

## Current Status

- Status: active
- Operational note: Very old deployment site with 63 robots in total.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Sodimac Chile"
SORT last_updated_date DESC
```

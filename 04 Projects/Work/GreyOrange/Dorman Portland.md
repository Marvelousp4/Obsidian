---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Dorman Portland"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Dorman Portland

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Dorman Portland
- Deployment Type: L
- Fleet Size: 
- Address: RB Distribution , INC.1140 Vaughn Parkway Portland TN 37148 United States
Christopher Adcock 
+1 (615) 992-4125

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Dorman Portland"
SORT last_updated_date DESC
```

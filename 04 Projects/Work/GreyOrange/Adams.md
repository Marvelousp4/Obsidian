---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Adams"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Adams

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L &H
- Fleet size: 18 L units 8 H units
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Adams
- Deployment Type: L &H
- Fleet Size: 18 L units 8 H units
- Address: Adams Beverages, LLC, 7505 Statesville Rd, Charlotte,
North Carolina 28269, United States
Raj
+1 (716) 256-5600
raj.k@greyorange.com 

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Adams"
SORT last_updated_date DESC
```

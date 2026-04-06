---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "H&M"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - H&M

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L &H
- Fleet size: 
- Notes: Fleet note: 2 forklifts with lithium pallet configuration.

## Site / Deployment Information

- Customer: GreyOrange
- Site: H&M
- Deployment Type: L &H
- Fleet Size: 
- Address: H&M warehouse,
210 Kerrison Drive East,
Ajax L1ZOR8
Ontario - Canada.

## Current Status

- Status: active
- Operational note: Fleet note: 2 forklifts with lithium pallet configuration.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "H&M"
SORT last_updated_date DESC
```

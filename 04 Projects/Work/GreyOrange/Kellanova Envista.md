---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Kellanova Envista"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kellanova Envista

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: AP
- Fleet size: 
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kellanova Envista
- Deployment Type: AP
- Fleet Size: 
- Address: Envista / HCM Systems
7150 S. Madison St.
Willowbrook, IL 60527

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Kellanova Envista"
SORT last_updated_date DESC
```

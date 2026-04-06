---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Sodimac Colombia"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Sodimac Colombia

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 21+14
- Notes: SRC2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Sodimac Colombia
- Deployment Type: L
- Fleet Size: 21+14
- Address: Sodimac Colombia S.ACentro de distribución Funza Via la Funzhe, km 1.7 Vereda Platanitos – Funza Cundinamarca
250020, Bogota

## Current Status

- Status: active
- Operational note: SRC2000

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Sodimac Colombia"
SORT last_updated_date DESC
```

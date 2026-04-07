---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Kellanova Minooka"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kellanova Minooka

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: AP
- Fleet size: 6
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kellanova Minooka
- Deployment Type: AP
- Fleet Size: 6
- Address: Kellanova Minooka 
NUSC - Kellogg Sales Co 1499 - NSD – DC – Minooka Annex~ IL, 1460 Cargo 
Court, Minooka, Illinois, United States, 60447-9430 

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Kellanova Minooka"
SORT last_updated_date DESC
```

---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Kerry"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kerry

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 12
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kerry
- Deployment Type: L
- Fleet Size: 12
- Address: 315 Clarence King Drive, Calhoun, GA 30701

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Kerry"
SORT last_updated_date DESC
```

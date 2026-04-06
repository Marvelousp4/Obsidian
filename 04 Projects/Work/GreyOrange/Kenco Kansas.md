---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Kenco Kansas"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Kenco Kansas

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L case picking
- Fleet size: 12
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kenco Kansas
- Deployment Type: L case picking
- Fleet Size: 12
- Address: 

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Kenco Kansas"
SORT last_updated_date DESC
```

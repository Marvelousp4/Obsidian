---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "Casey"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - Casey

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: AP
- Fleet size: 21
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Casey
- Deployment Type: AP
- Fleet Size: 21
- Address: 2902 S Jaguar Rd, Joplin, MO 64804

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "09 Work/Issues/GreyOrange"
WHERE type = "issue" AND site = "Casey"
SORT last_updated_date DESC
```

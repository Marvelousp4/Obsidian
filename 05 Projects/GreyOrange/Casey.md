---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Casey"
status: "active"
owner: "bai"
started: ""
next: "Link current site issues and update latest operating status."
tags: []
---

# GreyOrange - Casey

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
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

- [ ] Link current site issues and update latest operating status.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Casey"
SORT last_updated_date DESC
```

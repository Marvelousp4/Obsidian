---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "H&M"
status: "active"
owner: "bai"
started: ""
next: "Link current site issues and update latest operating status."
tags: []
---

# GreyOrange - H&M

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L &H
- Fleet size: 
- Notes: 2台叉车，锂平

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
- Operational note: 2台叉车，锂平

## Next Steps

- [ ] Link current site issues and update latest operating status.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "H&M"
SORT last_updated_date DESC
```

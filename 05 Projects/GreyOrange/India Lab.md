---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "India Lab"
status: "active"
owner: "bai"
started: ""
next: "Link current site issues and update latest operating status."
tags: []
---

# GreyOrange - India Lab

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: 
- Fleet size: 
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: India Lab
- Deployment Type: 
- Fleet Size: 
- Address: 

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link current site issues and update latest operating status.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "India Lab"
SORT last_updated_date DESC
```

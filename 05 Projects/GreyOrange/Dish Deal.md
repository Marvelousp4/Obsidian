---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Dish Deal"
status: "active"
owner: "bai"
started: ""
next: "Link current site issues and update latest operating status."
tags: []
---

# GreyOrange - Dish Deal

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L
- Fleet size: 2
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Dish Deal
- Deployment Type: L
- Fleet Size: 2
- Address: DISH Purchasing Corporation- 
1285 Joe Battle Blvd., Suite -A, El Paso, TX 79936

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] Link current site issues and update latest operating status.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Dish Deal"
SORT last_updated_date DESC
```

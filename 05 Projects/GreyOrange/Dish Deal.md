---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Dish Deal"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
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

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Dish Deal"
SORT last_updated_date DESC
```

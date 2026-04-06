---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "H&M"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
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

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "H&M"
SORT last_updated_date DESC
```

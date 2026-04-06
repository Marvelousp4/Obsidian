---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Kenco Goodyear"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
tags: []
---

# GreyOrange - Kenco Goodyear

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L case picking
- Fleet size: 
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kenco Goodyear
- Deployment Type: L case picking
- Fleet Size: 
- Address: Kenco Goodyear
Kenco Logistic Services,LLc..16811 WCommerce
Drve, Goodyear AZ 85338, United States
Donna Dame  donna.dame@kencogroup.com
+812-4806492

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Kenco Goodyear"
SORT last_updated_date DESC
```

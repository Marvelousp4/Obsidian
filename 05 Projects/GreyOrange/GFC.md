---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "GFC"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
tags: []
---

# GreyOrange - GFC

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: 
- Fleet size: 
- Notes: 2台AP，2台L 车，2台H 

## Site / Deployment Information

- Customer: GreyOrange
- Site: GFC
- Deployment Type: 
- Fleet Size: 
- Address: Grey Orange Inc
3975 Lakefield Court Suite 110 Suwanee, GA 30024        Harshita Puri
+1 (857) 437-8426

## Current Status

- Status: active
- Operational note: 2台AP，2台L 车，2台H 

## Next Steps

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "GFC"
SORT last_updated_date DESC
```

---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "YKK"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
tags: []
---

# GreyOrange - YKK

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L
- Fleet size: 4
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: YKK
- Deployment Type: L
- Fleet Size: 4
- Address: YKK AP America Inc-
140 Tractor Drive, Macon
GA 31216, United States
Christy Miller,
+1 478-508-4759, +1 330-987-4115

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "YKK"
SORT last_updated_date DESC
```

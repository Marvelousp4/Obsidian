---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Adams"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
tags: []
---

# GreyOrange - Adams

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L &H
- Fleet size: 18台L
8台H
- Notes: 

## Site / Deployment Information

- Customer: GreyOrange
- Site: Adams
- Deployment Type: L &H
- Fleet Size: 18台L
8台H
- Address: Adams Beverages, LLC, 7505 Statesville Rd, Charlotte,
North Carolina 28269, United States
Raj
+1 (716) 256-5600
raj.k@greyorange.com 

## Current Status

- Status: active
- Operational note: No additional note provided in workbook.

## Next Steps

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Adams"
SORT last_updated_date DESC
```

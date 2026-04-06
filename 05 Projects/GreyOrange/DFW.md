---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "DFW"
status: "stopped"
owner: "bai"
started: ""
next: "确认该站点是否已经停用；如果停用，补一个停用结论并保留历史背景。"
tags: []
---

# GreyOrange - DFW

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L
- Fleet size: 24
- Notes: 已停止

## Site / Deployment Information

- Customer: GreyOrange
- Site: DFW
- Deployment Type: L
- Fleet Size: 24
- Address: 

## Current Status

- Status: stopped
- Operational note: 已停止

## Next Steps

- [ ] 确认该站点是否已经停用；如果停用，补一个停用结论并保留历史背景。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "DFW"
SORT last_updated_date DESC
```

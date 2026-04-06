---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Kellanova Rialto"
status: "active"
owner: "bai"
started: ""
next: "把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。"
tags: []
---

# GreyOrange - Kellanova Rialto

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: AP
- Fleet size: 6
- Notes: src2000

## Site / Deployment Information

- Customer: GreyOrange
- Site: Kellanova Rialto
- Deployment Type: AP
- Fleet Size: 6
- Address: Kellanova, Inc
1686 W Base Line Rd, Rialto, California 92376

## Current Status

- Status: active
- Operational note: src2000

## Next Steps

- [ ] 把该站点的历史问题链接进来，并补最新运行状态、负责人和下一次跟进时间。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Kellanova Rialto"
SORT last_updated_date DESC
```

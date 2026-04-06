---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Sam's ATL"
status: "active"
owner: "bai"
started: ""
next: "补电池异常分析结论，并把相关问题、会议和责任人串起来。"
tags: []
---

# GreyOrange - Sam's ATL

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L
- Fleet size: 30+
- Notes: 现场电池异常，目前已使用备品正常运行，需要分析报告

## Site / Deployment Information

- Customer: GreyOrange
- Site: Sam's ATL
- Deployment Type: L
- Fleet Size: 30+
- Address: SAM'S EAST INC.
SAMS ECOM FC ATLANTA GA
980 Douglas Hills Rd. Lithia Springs, GA, 30122

## Current Status

- Status: active
- Operational note: 现场电池异常，目前已使用备品正常运行，需要分析报告

## Next Steps

- [ ] 补电池异常分析结论，并把相关问题、会议和责任人串起来。

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Sam's ATL"
SORT last_updated_date DESC
```

---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Sodimac Chile"
status: "active"
owner: "bai"
started: ""
next: "Link current site issues and update latest operating status."
tags: []
---

# GreyOrange - Sodimac Chile

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: /Users/bai/Downloads/GO 人员简介.xlsx
- Platform / robot type: L
- Fleet size: 63
- Notes: 非常旧的现场，一共有63台车

## Site / Deployment Information

- Customer: GreyOrange
- Site: Sodimac Chile
- Deployment Type: L
- Fleet Size: 63
- Address: Sodimac S.A.(R.U.T. 96.792.430-K) ( 100173 ) 
Av.Presidente Eduardo FreiN N°3092 Santiago RENCA, , 
Chile

## Current Status

- Status: active
- Operational note: 非常旧的现场，一共有63台车

## Next Steps

- [ ] Link current site issues and update latest operating status.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Sodimac Chile"
SORT last_updated_date DESC
```

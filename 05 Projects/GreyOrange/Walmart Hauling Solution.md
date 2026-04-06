---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Walmart Hauling Solution"
status: "stopped"
owner: "bai"
started: ""
next: "Confirm whether this site is decommissioned and capture the historical context if it is."
tags: []
---

# GreyOrange - Walmart Hauling Solution

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: 
- Fleet size: 
- Notes: Deployment appears stopped.

## Site / Deployment Information

- Customer: GreyOrange
- Site: Walmart Hauling Solution
- Deployment Type: 
- Fleet Size: 
- Address: 

## Current Status

- Status: stopped
- Operational note: Deployment appears stopped.

## Next Steps

- [ ] Confirm whether this site is decommissioned and capture the historical context if it is.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Walmart Hauling Solution"
SORT last_updated_date DESC
```

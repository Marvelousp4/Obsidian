---
type: "project"
account: "GreyOrange"
project_kind: "site_deployment"
site: "YKK"
status: "active"
owner: "bai"
started: ""
next: "Link the historical site issues here and update the latest operating status, owner, and next follow-up date."
tags: []
---

# GreyOrange - YKK

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
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

- [x] Link the historical site issues here and update the latest operating status, owner, and next follow-up date.

## Open Issues

```dataview
TABLE category, status, severity, priority, last_updated_date
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "GreyOrange" AND site = "YKK" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, last_updated_date DESC
```

## Completed Issue Archive

```dataview
TABLE category, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND site = "YKK"
SORT last_updated_date DESC
LIMIT 20
```

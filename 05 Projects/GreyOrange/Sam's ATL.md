---
type: "project"
account: "GreyOrange"
client: "GreyOrange"
project_kind: "site_deployment"
site: "Sam's ATL"
status: "active"
owner: "bai"
started: ""
next: "Add the battery anomaly analysis conclusion and link the related issues, meetings, and owners."
tags: []
---

# GreyOrange - Sam's ATL

## Goal

Track one live or historical GreyOrange deployment site as an operational object that can collect meetings, issues, local context, and follow-ups.

## Background

- Source workbook: GreyOrange internal workbook
- Platform / robot type: L
- Fleet size: 30+
- Notes: Battery anomaly on site. A spare unit is currently keeping operations running. Analysis report still needed.

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
- Operational note: Battery anomaly on site. A spare unit is currently keeping operations running. Analysis report still needed.

## Next Steps

- [ ] Add the battery anomaly analysis conclusion and link the related issues, meetings, and owners.

## Open Issues

```dataview
TABLE category, status, severity, last_updated_date
FROM "08 Issues/GreyOrange"
WHERE type = "issue" AND site = "Sam's ATL"
SORT last_updated_date DESC
```

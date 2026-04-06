---
type: "account"
account_name: "GreyOrange"
stage: "active"
industry: "Warehouse automation and robotics"
region: "North America; LATAM; India"
website: "https://www.greyorange.com/"
linkedin: "https://www.linkedin.com/company/greyorange/"
owner: "bai"
last_contact: ""
next_contact: ""
tags: []
---

# GreyOrange

## Account Overview

GreyOrange should be treated as one strategic account with many deployment sites, many internal stakeholders, and a large support surface.

## Business Context

The workbook provided is effectively a lightweight account book: it has GreyOrange internal contacts plus a deployment list covering GFC, Adams, Sodimac, Kenco, Kellanova, Sam's ATL, YKK and more. This is exactly the pattern that needs an account-centric system instead of one flat customer note.

## Stakeholder Map

```dataview
TABLE team, title, relationship, verification_status
FROM "04 Clients/GreyOrange"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind, site, status, next
FROM "05 Projects"
WHERE type = "project" AND account = "GreyOrange"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date, organizations, project
FROM "06 Meetings"
WHERE type = "meeting" AND contains(organizations, "GreyOrange")
SORT date DESC
```

## Open Issues

```dataview
TABLE site, category, status, severity, last_updated_date
FROM "08 Issues"
WHERE type = "issue" AND client = "GreyOrange" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Support load is fragmented across many sites and site conditions.
- Stakeholders span supply chain, technical, software, field operations, and quality.
- Several deployments appear stopped or aging, so historical context matters.

## Next Moves

- [ ] Keep all new site issues linked to the correct deployment note.
- [ ] Promote repeated issue patterns into SOP or knowledge notes.
- [ ] Use weekly review to identify sites with repeated unresolved issues.

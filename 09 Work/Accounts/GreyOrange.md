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
TABLE team AS Team, title AS Role, relationship AS Relationship, verification_status AS Verification
FROM "09 Work/Accounts/GreyOrange"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND account = "GreyOrange"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "09 Work/Meetings"
WHERE type = "meeting" AND contains(organizations, "GreyOrange")
SORT date DESC
```

## Open Issues

```dataview
TABLE site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND client = "GreyOrange" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Support load is fragmented across many sites and site conditions.
- Stakeholders span supply chain, technical, software, field operations, and quality.
- Several deployments appear stopped or aging, so historical context matters.

## Next Moves

- [ ] Attach new site issues to the correct deployment note instead of leaving them floating in the inbox.
- [ ] Promote repeated patterns into SOPs or formal knowledge notes.
- [ ] Review high-frequency unresolved issues every week and prioritize the sites that keep repeating.

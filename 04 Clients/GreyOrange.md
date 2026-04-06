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
FROM "04 Clients/GreyOrange"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "05 Projects"
WHERE type = "project" AND account = "GreyOrange"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "06 Meetings"
WHERE type = "meeting" AND contains(organizations, "GreyOrange")
SORT date DESC
```

## Open Issues

```dataview
TABLE site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "08 Issues"
WHERE type = "issue" AND client = "GreyOrange" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Support load is fragmented across many sites and site conditions.
- Stakeholders span supply chain, technical, software, field operations, and quality.
- Several deployments appear stopped or aging, so historical context matters.

## Next Moves

- [ ] 把新增站点问题挂到正确的部署页，不要让问题漂在收件箱里。
- [ ] 把重复出现的问题沉淀成 SOP 或正式知识卡片。
- [ ] 每周复盘一次高频未解决问题，优先找反复出问题的站点。

---
type: "account"
account_name: "Outland Robotics"
stage: "active"
industry: "Robotics integration and autonomy"
region: "US"
website: ""
linkedin: ""
owner: "bai"
last_contact: ""
next_contact: ""
tags: []
---

# Outland Robotics

## Account Overview

Outland Robotics is the potential downstream product owner or go-to-market partner for a mobile manipulator offering built on Fairino + Wellwit hardware.

## Business Context

From the transcript, Outland has experience in manipulation, vision, and autonomy, and wants a mobile platform to broaden its offering.

## Stakeholder Map

```dataview
TABLE team, title, relationship, verification_status
FROM "04 Clients/Outland Robotics"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind, site, status, next
FROM "05 Projects"
WHERE type = "project" AND account = "Outland Robotics"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date, organizations, project
FROM "06 Meetings"
WHERE type = "meeting" AND contains(organizations, "Outland Robotics")
SORT date DESC
```

## Open Issues

```dataview
TABLE site, category, status, severity, last_updated_date
FROM "08 Issues"
WHERE type = "issue" AND client = "Outland Robotics" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Requirements are exploratory and still market-facing rather than locked to one SKU.
- Commercial model and volume assumptions remain early.

## Next Moves

- [ ] Capture target use cases and payload/compute envelope in the linked project note.
- [ ] Keep all technical trade-offs visible in one place so product assumptions do not drift.

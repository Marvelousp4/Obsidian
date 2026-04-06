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
TABLE team AS Team, title AS Role, relationship AS Relationship, verification_status AS Verification
FROM "09 Work/Accounts/Outland Robotics"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND account = "Outland Robotics"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "09 Work/Meetings"
WHERE type = "meeting" AND contains(organizations, "Outland Robotics")
SORT date DESC
```

## Open Issues

```dataview
TABLE site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND client = "Outland Robotics" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Requirements are exploratory and still market-facing rather than locked to one SKU.
- Commercial model and volume assumptions remain early.

## Next Moves

- [ ] Capture target use cases and payload/compute envelope in the linked project note.
- [ ] Keep all technical trade-offs visible in one place so product assumptions do not drift.

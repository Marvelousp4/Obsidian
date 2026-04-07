---
type: "account"
account_name: "Wellwit Robotics"
stage: "active"
industry: "AMR / AGV platform vendor"
region: "Global; Atlanta support noted in transcript"
website: "https://wellwit.com/"
linkedin: ""
owner: "bai"
last_contact: ""
next_contact: ""
tags: []
---

# Wellwit Robotics

## Account Overview

Wellwit is the mobile base vendor in this ecosystem and is already involved in technical feasibility around the 300J platform, power budget, maintenance, and SLAM/API topics.

## Business Context

This account should be treated as both a vendor relationship and an engineering knowledge source because its platform details directly affect project feasibility and field support.

## Stakeholder Map

```dataview
TABLE team AS Team, title AS Role, relationship AS Relationship, verification_status AS Verification
FROM "09 Work/Accounts/Wellwit Robotics"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND account = "Wellwit Robotics"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "09 Work/Meetings"
WHERE type = "meeting" AND contains(organizations, "Wellwit Robotics")
SORT date DESC
```

## Open Issues

```dataview
TABLE site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND account = "Wellwit Robotics" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- ROS 2 is not native according to the transcript; integration may require wrappers.
- Battery life can be constrained by the proposed GPU-heavy compute stack.

## Next Moves

- [ ] Track platform documentation, maintenance requirements, and integration limits here.
- [ ] Link future field issues to both customer site and Wellwit platform context.

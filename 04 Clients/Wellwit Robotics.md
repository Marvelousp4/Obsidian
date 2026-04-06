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
TABLE team, title, relationship, verification_status
FROM "04 Clients/Wellwit Robotics"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind, site, status, next
FROM "05 Projects"
WHERE type = "project" AND account = "Wellwit Robotics"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date, organizations, project
FROM "06 Meetings"
WHERE type = "meeting" AND contains(organizations, "Wellwit Robotics")
SORT date DESC
```

## Open Issues

```dataview
TABLE site, category, status, severity, last_updated_date
FROM "08 Issues"
WHERE type = "issue" AND client = "Wellwit Robotics" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- ROS 2 is not native according to the transcript; integration may require wrappers.
- Battery life can be constrained by the proposed GPU-heavy compute stack.

## Next Moves

- [ ] Track platform documentation, maintenance requirements, and integration limits here.
- [ ] Link future field issues to both customer site and Wellwit platform context.

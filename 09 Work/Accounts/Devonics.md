---
type: "account"
account_name: "Devonics"
stage: "active"
industry: "Industrial automation integration"
region: "US; China coordination"
website: ""
linkedin: ""
owner: "bai"
last_contact: ""
next_contact: ""
tags: []
---

# Devonics

## Account Overview

Devonics appears to be the integrator and commercial bridge in this opportunity, connecting Fairino, Wellwit, and Outland Robotics around a mobile manipulation offering.

## Business Context

The transcript describes a discovery conversation around using a Wellwit mobile base plus a Fairino FR10 and Outland's compute/vision/autonomy stack. Devonics owns customer-facing technical scoping and customization.

## Stakeholder Map

```dataview
TABLE team AS Team, title AS Role, relationship AS Relationship, verification_status AS Verification
FROM "09 Work/Accounts/Devonics"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Deployments / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND account = "Devonics"
SORT file.name ASC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "09 Work/Meetings"
WHERE type = "meeting" AND contains(organizations, "Devonics")
SORT date DESC
```

## Open Issues

```dataview
TABLE site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND account = "Devonics" AND status != "resolved"
SORT last_updated_date DESC
```

## Risks

- Public company profile was not confidently verified from official web sources during this pass.
- Opportunity is still in evaluation, so requirements and product boundaries can shift.
- Power budget and packaging constraints are open engineering questions.

## Next Moves

- [ ] Capture the proposed architecture as one project note and keep action items linked there.
- [ ] Confirm whether the external name is Devonics or Devonix Automation in signed documents.
- [ ] Track package-space, battery, and API integration follow-ups in one opportunity thread.

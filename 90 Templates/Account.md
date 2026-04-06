---
type: account
account_name:
stage: active
industry:
region:
website:
linkedin:
owner: bai
last_contact:
next_contact:
tags: []
---

# <% tp.file.title %>

## Account Overview


## Business Context


## Stakeholder Map

```dataview
TABLE team AS Team, title AS Role, relationship AS Relationship, verification_status AS Verification
FROM "04 Clients/<% tp.file.title %>"
WHERE type = "contact"
SORT team ASC, file.name ASC
```

## Active Opportunities / Projects

```dataview
TABLE project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "05 Projects"
WHERE type = "project" AND account = "<% tp.file.title %>"
SORT file.name ASC
```


## Risks


## Next Moves

- [ ] 

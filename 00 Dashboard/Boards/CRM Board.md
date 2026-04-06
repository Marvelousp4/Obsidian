# CRM Board

## Key Accounts

```dataview
TABLE industry, region, last_contact, next_contact
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.mtime DESC
```

## Stakeholders

```dataview
TABLE organization, team, title, relationship, last_contact, verification_status
FROM "09 Work/Accounts"
WHERE type = "contact"
SORT organization ASC, team ASC, file.name ASC
```

## Opportunities And Deployments

```dataview
TABLE account, project_kind, site, status, next
FROM "04 Projects/Work"
WHERE type = "project"
SORT account ASC, file.name ASC
```

## Meetings To Process

```dataview
TABLE date, organizations, project
FROM "09 Work/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 20
```

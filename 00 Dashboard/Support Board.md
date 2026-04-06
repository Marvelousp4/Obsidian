# Support Board

## Open Issues

```dataview
TABLE client, site, category, status, severity, priority, last_updated_date
FROM "08 Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 30
```

## Site-Centric Projects

```dataview
TABLE account, site, status, next
FROM "05 Projects"
WHERE type = "project" AND (project_kind = "site_deployment" OR project_kind = "site_issue_bucket")
SORT account ASC, site ASC
```

## Recent Support Meetings

```dataview
TABLE date, organizations, project
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 20
```

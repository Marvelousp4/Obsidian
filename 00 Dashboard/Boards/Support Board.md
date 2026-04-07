# Support Board

## Open Issues

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, priority AS Priority, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 30
```

## Site-Centric Projects

```dataview
TABLE account, site, status, next
FROM "04 Projects/Work"
WHERE type = "project" AND (project_kind = "site_deployment" OR project_kind = "site_issue_bucket")
SORT account ASC, site ASC
```

## Recent Support Meetings

```dataview
TABLE date, organizations, project
FROM "09 Work/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 20
```

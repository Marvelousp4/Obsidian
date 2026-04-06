# Issue Index

```dataview
TABLE client, site, project, category, status, severity, priority, created_date, last_updated_date
FROM "08 Issues"
WHERE type = "issue"
SORT last_updated_date DESC
```

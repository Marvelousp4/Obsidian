# Issue Index

```dataview
TABLE client, site, category, status, severity, priority, created_date, last_updated_date
FROM "09 Work/Issues"
WHERE type = "issue"
SORT last_updated_date DESC
```

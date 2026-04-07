# Issue Index

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, priority AS Priority, created_date AS Created, last_updated_date AS Updated, source_type AS Source, source_id AS "Source ID"
FROM "09 Work/Issues"
WHERE type = "issue"
SORT last_updated_date DESC
```

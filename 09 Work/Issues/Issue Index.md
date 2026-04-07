# Issue Index

This index is for current work only. Completed historical issues live in [[09 Work/Issues/Archive/Completed/Completed Issues Index|Completed Issues Index]].

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, priority AS Priority, created_date AS Created, last_updated_date AS Updated, source_type AS Source, source_id AS "Source ID"
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND status != "resolved" AND status != "done" AND status != "closed"
SORT last_updated_date DESC
```

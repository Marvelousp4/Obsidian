# Knowledge Board

## Recent Tech Notes

```dataview
TABLE source, updated, tags
FROM "03 Knowledge/Tech"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 20
```

## Recent Industry Notes

```dataview
TABLE source_type, source, updated, tags
FROM "03 Knowledge/Industry"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 20
```

## Reusable Issue Patterns

```dataview
TABLE client, site, category, priority, last_updated_date
FROM "08 Issues"
WHERE type = "issue" AND status != "resolved"
SORT category ASC, last_updated_date DESC
LIMIT 30
```

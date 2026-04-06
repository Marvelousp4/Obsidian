# Knowledge Board

## Recent Knowledge Notes

```dataview
TABLE area AS Area, domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 30
```

## Work Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge/Work"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 20
```

## Personal And Research Knowledge

```dataview
TABLE domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge/Personal"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 20
```

## Reusable Work Issue Patterns

```dataview
TABLE client AS Account, site AS Site, category AS Category, priority AS Priority, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 20
```

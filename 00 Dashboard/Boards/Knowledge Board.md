# Knowledge Board

## Pipeline Control

- [[10 Raw/Raw Index|Raw Index]]
- [[05 Knowledge/Knowledge Index|Knowledge Index]]
- [[99 System/Knowledge Factory|Knowledge Factory]]

## Raw Queue

```dataview
TABLE source_kind AS Kind, capture_status AS Status, captured AS Captured, source_url AS URL
FROM "10 Raw"
WHERE type = "raw_source"
SORT file.mtime DESC
LIMIT 30
```

## Recently Compiled Notes

```dataview
TABLE area AS Area, domain AS Domain, compiled_from AS "Compiled From", updated AS Updated
FROM "05 Knowledge/Compiled"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 20
```

## Concept Pages

```dataview
TABLE area AS Area, domain AS Domain, source_count AS Sources, updated AS Updated
FROM "05 Knowledge/Concepts"
WHERE type = "concept"
SORT file.mtime DESC
LIMIT 20
```

## All Recent Knowledge Notes

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

## Latest Wiki Health Reports

```dataview
TABLE date AS Date, file.link AS Report
FROM "08 Reviews/Wiki Health"
WHERE type = "review"
SORT date DESC
LIMIT 10
```

## Reusable Work Issue Patterns

```dataview
TABLE client AS Account, site AS Site, category AS Category, priority AS Priority, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 20
```

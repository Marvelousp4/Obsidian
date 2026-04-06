# Concept Index

Concept pages are durable wiki entries that should connect multiple sources over time.

```dataview
TABLE area AS Area, domain AS Domain, source_count AS Sources, updated AS Updated
FROM "05 Knowledge/Concepts"
WHERE type = "concept"
SORT file.mtime DESC
```

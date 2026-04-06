# Knowledge Index

Knowledge notes are reusable conclusions, methods, and models. Raw markdown sources belong in `10 Raw`. Binary originals belong in `07 Resources`.

```dataview
TABLE area AS Area, domain AS Domain, source AS Source, updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge"
SORT file.mtime DESC
```

## Compiled Notes

```dataview
TABLE area AS Area, domain AS Domain, compiled_from AS "Compiled From", updated AS Updated
FROM "05 Knowledge/Compiled"
WHERE type = "knowledge"
SORT file.mtime DESC
```

## Concept Pages

```dataview
TABLE area AS Area, domain AS Domain, source_count AS Sources, updated AS Updated
FROM "05 Knowledge/Concepts"
WHERE type = "concept"
SORT file.mtime DESC
```

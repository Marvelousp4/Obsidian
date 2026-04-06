# Raw Index

This is the intake layer for durable source material. Keep raw notes close to the source. Compile them later.

## Capture Rules

- Web articles: clip to markdown
- Papers: extract text into markdown
- Repos: create one repo digest note, not a file dump
- Long transcripts: keep the full text here before synthesis

## Raw Queue

```dataview
TABLE source_kind AS Kind, capture_status AS Status, captured AS Captured, source_url AS URL, compiled_note AS "Compiled Note"
FROM "10 Raw"
WHERE type = "raw_source"
SORT file.mtime DESC
```

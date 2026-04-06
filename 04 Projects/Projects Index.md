# Projects Index

Projects are bounded initiatives. They can belong to work, health, finance, learning, research, or personal life.

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## Knowledge Factory Support

- Use `04 Projects` only for bounded initiatives.
- Do not use projects as a dumping ground for source material.
- Source material should enter through [[10 Raw/Raw Index|Raw Index]] first.

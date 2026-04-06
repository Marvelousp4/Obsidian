# Knowledge Index

Knowledge notes are reusable conclusions, methods, and models. Raw sources belong in `07 Resources`.

```dataview
TABLE area AS Area, domain AS Domain, source AS Source, updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge"
SORT file.mtime DESC
```

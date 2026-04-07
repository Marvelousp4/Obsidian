# Compiled Index

Compiled notes are the first structured pass over raw sources.

```dataview
TABLE area AS Area, domain AS Domain, compile_quality AS Quality, compiled_from AS "Compiled From", updated AS Updated
FROM "05 Knowledge/Compiled"
WHERE type = "knowledge"
SORT file.mtime DESC
```

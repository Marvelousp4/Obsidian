# Projects Index

Projects are bounded initiatives. They can belong to work, health, finance, learning, research, or personal life.

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

# Meeting Index

```dataview
TABLE date, participants, project, client
FROM "06 Meetings"
WHERE type = "meeting"
SORT file.mtime DESC
```

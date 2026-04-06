# Meeting Index

```dataview
TABLE date, organizations, participants, project, client
FROM "06 Meetings"
WHERE type = "meeting"
SORT file.mtime DESC
```

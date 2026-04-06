# Client Index

```dataview
TABLE stage, focus, last_contact
FROM "04 Clients"
WHERE type = "client"
SORT file.mtime DESC
```

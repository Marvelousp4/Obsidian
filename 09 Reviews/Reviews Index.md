# Reviews Index

Use reviews for compression and direction, not raw capture.

## Weekly Reviews

```dataview
TABLE file.link AS Weekly, date
FROM "09 Reviews/Weekly"
WHERE type = "review"
SORT file.name DESC
```

## Monthly Reviews

```dataview
TABLE file.link AS Monthly, date
FROM "09 Reviews/Monthly"
WHERE type = "review"
SORT file.name DESC
```

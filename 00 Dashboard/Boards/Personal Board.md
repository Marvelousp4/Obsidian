# Personal Board

This board controls non-work life operations. It should not show work CRM data; use [[00 Dashboard/Boards/Work Control Board|Work Control Board]] for that.

## Personal Areas

```dataview
TABLE status AS Status, focus AS Focus, review_rhythm AS "Review Rhythm"
FROM "03 Areas"
WHERE type = "area" AND file.name != "Work"
SORT file.name ASC
```

## Active Personal Projects

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area != "work" AND status != "archived" AND status != "done" AND status != "closed"
SORT area ASC, file.mtime DESC
```

## Personal And Research Knowledge

```dataview
TABLE area AS Area, domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge" AND area != "work"
SORT file.mtime DESC
LIMIT 25
```

## People Outside Work CRM

```dataview
TABLE person_kind AS Kind, relationship AS Relationship, organization AS Organization, title AS Title, last_contact AS "Last Contact"
FROM "06 People"
WHERE type = "person"
SORT file.name ASC
LIMIT 30
```

## Health Shortcut

- [[00 Dashboard/Boards/Health Board|Health Board]]
- [[03 Areas/Health/Health|Health Area]]

## Review Queue

```dataview
TABLE date AS Date, file.link AS Review
FROM "08 Reviews"
WHERE type = "review"
SORT date DESC
LIMIT 15
```

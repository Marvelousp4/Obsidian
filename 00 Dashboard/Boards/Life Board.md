# Life Board

## Core Views

- [[00 Dashboard/Start Here|Operating Hub]]
- [[03 Areas/Areas Index|Areas Index]]
- [[04 Projects/Projects Index|Projects Index]]
- [[05 Knowledge/Knowledge Index|Knowledge Index]]
- [[06 People/People Index|People Index]]
- [[08 Reviews/Reviews Index|Reviews Index]]
- [[09 Work/Work Index|Work Index]]

## Areas

```dataview
TABLE status AS Status, focus AS Focus, review_rhythm AS "Review Rhythm"
FROM "03 Areas"
WHERE type = "area"
SORT file.name ASC
```

## Active Projects

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND status != "archived"
SORT file.mtime DESC
LIMIT 20
```

## Recent Knowledge

```dataview
TABLE area AS Area, domain AS Domain, source_type AS "Source Type", updated AS Updated
FROM "05 Knowledge"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 25
```

## Direct People Notes

```dataview
TABLE person_kind AS Kind, relationship AS Relationship, organization AS Organization, title AS Title, last_contact AS "Last Contact"
FROM "06 People"
WHERE type = "person"
SORT file.name ASC
LIMIT 20
```

## Work Snapshot

```dataview
TABLE industry AS Industry, region AS Region, next_contact AS "Next Contact"
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.mtime DESC
LIMIT 10
```

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 10
```

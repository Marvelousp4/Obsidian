# Operating Hub

Use this page as the default entry point for your personal operating system. Daily notes are the universal input layer. Formal notes are the long-term asset layer.

## Today

- Run `Daily notes: Open today's daily note`
- [[01 Inbox/Inbox|Inbox]]
- [[00 Dashboard/Boards/Weekly Focus Board|Weekly Focus Board]]
- [[99 System/System Index|System Index]]

## Core Navigation

- [[03 Areas/Areas Index|Areas]]
- [[04 Projects/Projects Index|Projects]]
- [[05 Knowledge/Knowledge Index|Knowledge]]
- [[06 People/People Index|People]]
- [[08 Reviews/Reviews Index|Reviews]]
- [[09 Work/Work Index|Work]]
- [[00 Dashboard/Databases|Databases]]

## Work Boards

- [[00 Dashboard/Boards/Operations Board|Operations Board]]
- [[00 Dashboard/Boards/CRM Board|CRM Board]]
- [[00 Dashboard/Boards/Support Board|Support Board]]
- [[00 Dashboard/Boards/Knowledge Board|Knowledge Board]]

## Recent Daily Notes

```dataview
TABLE file.link AS Daily, week AS Week
FROM "02 Daily"
WHERE type = "daily"
SORT date DESC
LIMIT 3
```

## Areas

```dataview
TABLE status AS Status, focus AS Focus
FROM "03 Areas"
WHERE type = "area"
SORT file.name ASC
```

## Active Projects

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project"
SORT file.mtime DESC
LIMIT 12
```

## Recent Knowledge

```dataview
TABLE area AS Area, source, updated
FROM "05 Knowledge"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 12
```

## Recent People

```dataview
TABLE person_kind AS Kind, relationship AS Relationship, organization AS Organization, last_contact AS "Last Contact"
FROM "06 People"
WHERE type = "person"
SORT file.mtime DESC
LIMIT 10
```

## Review Rhythm

```dataview
TABLE file.link AS Weekly, date
FROM "08 Reviews/Weekly"
WHERE type = "review"
SORT file.name DESC
LIMIT 4
```

```dataview
TABLE file.link AS Monthly, date
FROM "08 Reviews/Monthly"
WHERE type = "review"
SORT file.name DESC
LIMIT 3
```

## Work Snapshot

```dataview
TABLE industry AS Industry, region AS Region, last_contact AS "Last Contact", next_contact AS "Next Contact"
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.mtime DESC
LIMIT 10
```

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project"
SORT file.mtime DESC
LIMIT 10
```

```dataview
TABLE client AS Client, site AS Site, category AS Category, status AS Status, priority AS Priority, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 10
```

## Tasks

```tasks
not done
sort by due
limit 20
```

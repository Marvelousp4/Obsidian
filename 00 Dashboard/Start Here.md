# Operating Hub

Use this page as the default entry point. The goal is not to build a note graveyard. The goal is to keep raw input moving into reusable account, project, issue, and knowledge assets.

## Today

- Run `Daily notes: Open today's daily note`
- [[01 Inbox/Inbox|Quick Capture]]
- [[00 Dashboard/Boards/Weekly Focus Board|Weekly Focus Board]]
- [[99 System/System Index|System Index]]

## Navigation

- [[00 Dashboard/Databases|Databases]]
- [[00 Dashboard/Boards/CRM Board|CRM Board]]
- [[00 Dashboard/Boards/Support Board|Support Board]]
- [[00 Dashboard/Boards/Knowledge Board|Knowledge Board]]
- [[09 Reviews/Reviews Index|Reviews Index]]

## Indices

- [[03 Knowledge/Tech/Tech Index]]
- [[03 Knowledge/Industry/Industry Index]]
- [[04 Clients/Account Index]]
- [[04 Clients/Contact Index]]
- [[05 Projects/Project Index]]
- [[06 Meetings/Meeting Index]]
- [[08 Issues/Issue Index]]

## Recent Daily Notes

```dataview
TABLE file.link AS Daily, week AS Week
FROM "02 Daily"
WHERE type = "daily"
SORT date DESC
LIMIT 3
```

## Review Rhythm

```dataview
TABLE file.link AS Weekly, date
FROM "09 Reviews/Weekly"
WHERE type = "review"
SORT file.name DESC
LIMIT 4
```

```dataview
TABLE file.link AS Monthly, date
FROM "09 Reviews/Monthly"
WHERE type = "review"
SORT file.name DESC
LIMIT 3
```

## Active Accounts

```dataview
TABLE industry AS Industry, region AS Region, last_contact AS "Last Contact", next_contact AS "Next Contact"
FROM "04 Clients"
WHERE type = "account"
SORT file.mtime DESC
LIMIT 12
```

## Active Projects / Deployments

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "05 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## Recent Tech Knowledge

```dataview
TABLE tags, source, updated
FROM "03 Knowledge/Tech"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 10
```

## Recent Industry Knowledge

```dataview
TABLE tags, source, updated
FROM "03 Knowledge/Industry"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 10
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 10
```

## Open Issues

```dataview
TABLE client AS Client, site AS Site, category AS Category, status AS Status, priority AS Priority, last_updated_date AS Updated
FROM "08 Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 15
```

## Tasks

```tasks
not done
sort by due
limit 20
```

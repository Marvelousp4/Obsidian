# Start Here

This is the global operating hub. It should stay light: today, global snapshot, and links to the domain boards.

## Today

- Run `Daily notes: Open today's daily note`
- Capture everything in the daily note first unless it is already a formal object.

## Today Important Tasks

```dataview
TASK
FROM "02 Daily"
WHERE !completed AND file.day = date(today)
GROUP BY file.link
```

## Global Snapshot

### Active Personal Projects

```dataview
TABLE area AS Area, status AS Status, next AS Next
FROM "04 Projects"
WHERE type = "project" AND area != "work" AND status != "archived" AND status != "done" AND status != "closed"
SORT file.mtime DESC
LIMIT 10
```

### Active Work Priorities

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project" AND status != "done" AND status != "closed" AND status != "stopped"
SORT file.mtime DESC
LIMIT 10
```

### Current Field Issues

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, priority AS Priority, assignee AS Assignee, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue"
SORT priority ASC, last_updated_date DESC
LIMIT 10
```

## Domain Boards

- [[00 Dashboard/Boards/Personal Board|Personal Board]]
- [[00 Dashboard/Boards/Work Control Board|Work Control Board]]
- [[00 Dashboard/Boards/Knowledge Board|Knowledge Board]]
- [[00 Dashboard/Boards/Health Board|Health Board]]

## Core Indices

- [[01 Inbox/Inbox|Inbox]]
- [[03 Areas/Areas Index|Areas]]
- [[04 Projects/Projects Index|Projects]]
- [[05 Knowledge/Knowledge Index|Knowledge]]
- [[06 People/People Index|People]]
- [[08 Reviews/Reviews Index|Reviews]]
- [[09 Work/Work Index|Work]]
- [[10 Raw/Raw Index|Raw]]

## Rules

- Start Here is the global view.
- Personal Board is for non-work life operations.
- Work Control Board is for customer, project, meeting, and issue execution.
- Knowledge Board is for raw-to-wiki compilation and reusable knowledge quality.
- Areas are standards and review dashboards, not dumping folders.

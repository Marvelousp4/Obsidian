# Operating Hub

This page is now intentionally light. Use it as a reset point, not as a giant control panel.

## Start Here

- Run `Daily notes: Open today's daily note`
- [[01 Inbox/Inbox|Inbox]]
- [[10 Raw/Raw Index|Raw]]
- [[03 Areas/Areas Index|Areas]]
- [[04 Projects/Projects Index|Projects]]
- [[05 Knowledge/Knowledge Index|Knowledge]]
- [[06 People/People Index|People]]
- [[08 Reviews/Reviews Index|Reviews]]
- [[09 Work/Work Index|Work]]

## Today Important Tasks

```dataview
TASK
FROM "02 Daily"
WHERE !completed AND file.day = date(today)
GROUP BY file.link
```

## Core Boards

- [[00 Dashboard/Boards/Life Board|Life Board]]
- [[00 Dashboard/Boards/Work Control Board|Work Control Board]]
- [[00 Dashboard/Boards/Knowledge Board|Knowledge Board]]
- [[00 Dashboard/Boards/Health Board|Health Board]]

## System

- [[99 System/System Index|System Index]]

## Rules

- Daily note is the default capture path.
- Raw sources belong in `10 Raw`. Structured knowledge belongs in `05 Knowledge`.
- QuickAdd is only for notes that are clearly formal objects now.
- Reviews compress direction. Boards are views, not the source of truth.
- The knowledge pipeline is `raw -> compile -> health check`.
- `Work` is a domain under the system, not a second system.

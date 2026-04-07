# Work Control Board

This is the work-domain control surface. It answers the operational questions: what projects exist, what field issues are open, what is blocked, who owns what, what is most urgent, and what is moving.

## Project Master Table

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, owner AS Owner, next AS "Next Action"
FROM "04 Projects/Work"
WHERE type = "project"
SORT account ASC, status ASC, file.name ASC
```

## Account List

```dataview
TABLE stage AS Stage, industry AS Industry, region AS Region, last_contact AS "Last Contact", next_contact AS "Next Contact"
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.name ASC
```

## Active Field Issue List

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, priority AS Priority, assignee AS Assignee, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND status != "resolved" AND status != "done" AND status != "closed"
SORT last_updated_date DESC
```

## Blocker List

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, priority AS Priority, assignee AS Assignee, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND status != "resolved" AND status != "done" AND status != "closed" AND (status = "blocked" OR priority = "P0" OR priority = "P1")
SORT priority ASC, last_updated_date DESC
```

## Owner And Stakeholder List

```dataview
TABLE organization AS Account, team AS Team, title AS Role, relationship AS Relationship, last_contact AS "Last Contact", verification_status AS Verification
FROM "09 Work/Accounts"
WHERE type = "contact"
SORT organization ASC, team ASC, file.name ASC
```

## Project Owner Load

```dataview
TABLE key AS Owner, length(rows) AS Count, rows.file.link AS Projects
FROM "04 Projects/Work"
WHERE type = "project"
GROUP BY owner
SORT length(rows) DESC
```

## Issue Assignee Queue

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, priority AS Priority, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND status != "resolved" AND status != "done" AND status != "closed" AND assignee
SORT assignee ASC, priority ASC, last_updated_date DESC
```

## Recent Meetings

```dataview
TABLE date AS Date, organizations AS Organizations, project AS Project, account AS Account
FROM "09 Work/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 20
```

## Priority Queue

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, priority AS Priority, assignee AS Assignee, last_updated_date AS Updated
FROM "09 Work/Issues/Active"
WHERE type = "issue" AND status != "resolved" AND status != "done" AND status != "closed"
SORT priority ASC, severity ASC, last_updated_date DESC
LIMIT 50
```

## Progress Status List

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS "Next Action"
FROM "04 Projects/Work"
WHERE type = "project"
SORT status ASC, account ASC, file.name ASC
```

## Status Summary

```dataview
TABLE key AS Status, length(rows) AS Count, rows.file.link AS Items
FROM "04 Projects/Work"
WHERE type = "project"
GROUP BY status
SORT status ASC
```

## Stale Follow-Up List

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS "Next Action", file.mtime AS Updated
FROM "04 Projects/Work"
WHERE type = "project" AND status != "done" AND status != "closed" AND status != "stopped"
SORT file.mtime ASC
LIMIT 30
```

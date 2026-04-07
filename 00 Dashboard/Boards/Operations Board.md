# Operations Board

## Control Surface

- [[00 Dashboard/Start Here|Operating Hub]]
- [[00 Dashboard/Boards/Weekly Focus Board|Weekly Focus Board]]
- [[08 Reviews/Reviews Index|Reviews Index]]

## Active Accounts

```dataview
TABLE industry AS Industry, region AS Region, last_contact AS "Last Contact", next_contact AS "Next Contact"
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.mtime DESC
```

## Active Projects

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "04 Projects/Work"
WHERE type = "project"
SORT file.mtime DESC
```

## Recent Issues

```dataview
TABLE account AS Account, site AS Site, category AS Category, status AS Status, severity AS Severity, last_updated_date AS Updated
FROM "09 Work/Issues"
WHERE type = "issue"
SORT last_updated_date DESC
LIMIT 15
```

## Recent Meetings

```dataview
TABLE date, organizations, project, account
FROM "09 Work/Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 15
```

## Accounts Needing Follow-Up

```tasks
not done
path includes 09 Work/Accounts
sort by due
```

## Projects Needing Follow-Up

```tasks
not done
path includes 04 Projects/Work
sort by due
```

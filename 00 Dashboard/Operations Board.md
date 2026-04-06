# Operations Board

## Control Surface

- [[00 Dashboard/Start Here|Operating Hub]]
- [[00 Dashboard/Weekly Focus Board|Weekly Focus Board]]
- [[02 Daily/Weekly]]
- [[02 Daily/Monthly]]

## Active Accounts

```dataview
TABLE industry AS Industry, region AS Region, last_contact AS "Last Contact", next_contact AS "Next Contact"
FROM "04 Clients"
WHERE type = "account"
SORT file.mtime DESC
```

## Active Projects

```dataview
TABLE account AS Account, project_kind AS Type, site AS Site, status AS Status, next AS Next
FROM "05 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## Recent Issues

```dataview
TABLE client, site, category, status, severity, last_updated_date
FROM "08 Issues"
WHERE type = "issue"
SORT last_updated_date DESC
LIMIT 15
```

## Recent Meetings

```dataview
TABLE date, organizations, project, account
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 15
```

## Accounts Needing Follow-Up

```tasks
not done
path includes 04 Clients
sort by due
```

## Projects Needing Follow-Up

```tasks
not done
path includes 05 Projects
sort by due
```

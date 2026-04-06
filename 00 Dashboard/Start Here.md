# Operating Hub

Use this page as the default entry point. The goal is not to build a note graveyard. The goal is to keep raw input moving into reusable account, project, issue, and knowledge assets.

## Today

- Run `Daily notes: Open today's daily note`
- [[01 Inbox/Inbox|Quick Capture]]
- [[00 Dashboard/Weekly Focus Board|Weekly Focus Board]]
- [[99 System/Workflow Guide|Workflow Guide]]
- [[99 System/Daily Operating System|Daily Operating System]]
- [[99 System/GitHub Sync|GitHub Sync]]
- [[99 System/AI and Automation|AI and Automation]]
- [[99 System/Command Playbook|Command Playbook]]
- [[99 System/Plugin Fit Guide|Plugin Fit Guide]]
- [[99 System/AI Automation Stack|AI Automation Stack]]
- [[99 System/MODEX 2026 Playbook|MODEX 2026 Playbook]]
- [[99 System/Tool Division|Tool Division]]

## Navigation

- [[03 Knowledge/Tech/Tech Index]]
- [[03 Knowledge/Industry/Industry Index]]
- [[04 Clients/Account Index]]
- [[04 Clients/Contact Index]]
- [[05 Projects/Project Index]]
- [[06 Meetings/Meeting Index]]
- [[08 Issues/Issue Index]]
- [[00 Dashboard/Operations Board|Operations Board]]
- [[00 Dashboard/CRM Board|CRM Board]]
- [[00 Dashboard/Support Board|Support Board]]
- [[00 Dashboard/Knowledge Board|Knowledge Board]]
- [[00 Dashboard/Accounts Database|Accounts Database]]
- [[00 Dashboard/Contacts Database|Contacts Database]]
- [[00 Dashboard/Projects Database|Projects Database]]
- [[00 Dashboard/Issues Database|Issues Database]]
- [[02 Daily/Weekly]]
- [[02 Daily/Monthly]]

## Recent Daily Notes

```dataview
TABLE file.link AS Daily, week AS Week
FROM "02 Daily"
WHERE type = "daily" AND !contains(file.path, "02 Daily/Weekly") AND !contains(file.path, "02 Daily/Monthly")
SORT date DESC
LIMIT 3
```

## Review Rhythm

```dataview
TABLE file.link AS Weekly, date
FROM "02 Daily/Weekly"
WHERE type = "review"
SORT file.name DESC
LIMIT 4
```

```dataview
TABLE file.link AS Monthly, date
FROM "02 Daily/Monthly"
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

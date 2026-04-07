# Completed Issues Index

This is the archive for resolved issues that still have reuse value. Current support work should stay in [[09 Work/Issues/Issue Index|Issue Index]].

Archive policy:
- Keep resolved issues that preserve technical diagnosis, customer impact, recurring failure patterns, product requirements, or escalation context.
- Delete pure Slack noise: channel join/leave messages, scheduling chatter, one-line thanks, raw attachment drops, and follow-up prompts without reusable context.
- Do not use this page for current execution. Re-open an item by moving it back to `09 Work/Issues` and changing `status`.

## Completed Issue Archive

```dataview
TABLE account AS Account, site AS Site, category AS Category, severity AS Severity, priority AS Priority, created_date AS Created, last_updated_date AS Updated
FROM "09 Work/Issues/Archive/Completed"
WHERE type = "issue" AND (status = "resolved" OR status = "done" OR status = "closed")
SORT account ASC, site ASC, last_updated_date DESC, file.name ASC
```

## GreyOrange Completed Issues

```dataview
TABLE site AS Site, category AS Category, severity AS Severity, priority AS Priority, created_date AS Created, last_updated_date AS Updated
FROM "09 Work/Issues/Archive/Completed/GreyOrange"
WHERE type = "issue" AND status = "resolved"
SORT site ASC, priority ASC, created_date DESC
```

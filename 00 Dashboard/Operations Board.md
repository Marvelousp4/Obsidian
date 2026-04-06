# Operations Board

## 活跃客户

```dataview
TABLE stage AS 阶段, focus AS 关注点, last_contact AS 上次联系, next_contact AS 下次联系
FROM "04 Clients"
WHERE type = "client"
SORT last_contact DESC
```

## 活跃项目

```dataview
TABLE status AS 状态, owner AS 负责人, next AS 下一步
FROM "05 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## 最近问题单

```dataview
TABLE client, project, status, severity, date
FROM "01 Inbox"
WHERE type = "issue"
SORT file.mtime DESC
LIMIT 15
```

## 最近会议

```dataview
TABLE meeting_type, client, project, date
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 15
```

## 待跟进客户

```tasks
not done
path includes 04 Clients
sort by due
```

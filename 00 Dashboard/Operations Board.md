# Operations Board

## 活跃账户

```dataview
TABLE industry AS 行业, region AS 区域, last_contact AS 上次联系, next_contact AS 下次联系
FROM "04 Clients"
WHERE type = "account"
SORT file.mtime DESC
```

## 活跃项目

```dataview
TABLE account AS 账户, project_kind AS 类型, site AS 站点, status AS 状态, next AS 下一步
FROM "05 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## 最近问题单

```dataview
TABLE client, site, category, status, severity, last_updated_date
FROM "08 Issues"
WHERE type = "issue"
SORT last_updated_date DESC
LIMIT 15
```

## 最近会议

```dataview
TABLE date, organizations, project, account
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 15
```

## 待跟进账户

```tasks
not done
path includes 04 Clients
sort by due
```

## 待跟进项目

```tasks
not done
path includes 05 Projects
sort by due
```

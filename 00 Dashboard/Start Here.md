# 工作中枢

先用这一个入口，不要一上来把 Obsidian 用成文件坟场。

## 今天

- 用命令 `Daily notes: Open today's daily note` 打开今日日记
- [[01 Inbox/收件箱|快速捕获]]
- [[99 System/Workflow Guide|工作流说明]]
- [[99 System/Daily Operating System|Daily OS]]
- [[99 System/GitHub Sync|GitHub 同步]]
- [[99 System/AI and Automation|AI / Agent]]
- [[99 System/Command Playbook|Command 手册]]
- [[99 System/AI Automation Stack|AI / Automation Stack]]
- [[99 System/Tool Division|工具分工]]

## 快速入口

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

## 今日视图

```dataview
TABLE file.link AS Daily, week AS Week
FROM "02 Daily"
WHERE type = "daily"
SORT date DESC
LIMIT 3
```

## 活跃账户

```dataview
TABLE industry AS 行业, region AS 区域, last_contact AS 上次联系, next_contact AS 下次联系
FROM "04 Clients"
WHERE type = "account"
SORT file.mtime DESC
LIMIT 12
```

## 进行中的项目 / 部署

```dataview
TABLE account AS 账户, project_kind AS 类型, site AS 站点, status AS 状态, next AS 下一步
FROM "05 Projects"
WHERE type = "project"
SORT file.mtime DESC
```

## 最近技术积累

```dataview
TABLE tags, source, updated
FROM "03 Knowledge/Tech"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 10
```

## 最近行业积累

```dataview
TABLE tags, source, updated
FROM "03 Knowledge/Industry"
WHERE type = "knowledge"
SORT file.mtime DESC
LIMIT 10
```

## 最近会议

```dataview
TABLE date AS 日期, organizations AS 组织, project AS 项目
FROM "06 Meetings"
WHERE type = "meeting"
SORT date DESC
LIMIT 10
```

## 重点问题

```dataview
TABLE client AS 客户, site AS 站点, category AS 类别, status AS 状态, priority AS 优先级, last_updated_date AS 更新
FROM "08 Issues"
WHERE type = "issue" AND status != "resolved"
SORT last_updated_date DESC
LIMIT 15
```

## 待办

```tasks
not done
sort by due
limit 20
```

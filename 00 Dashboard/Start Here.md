# 工作中枢

先用这一个入口，不要一上来把 Obsidian 用成文件坟场。

## 今天

- [[02 Daily/2026-04-05|今日日志]]
- [[01 Inbox/收件箱|快速捕获]]
- [[99 System/Workflow Guide|工作流说明]]
- [[99 System/Daily Operating System|Daily OS]]
- [[99 System/GitHub Sync|GitHub 同步]]
- [[99 System/AI and Automation|AI / Agent]]

## 快速入口

- [[03 Knowledge/Tech/Tech Index]]
- [[03 Knowledge/Industry/Industry Index]]
- [[04 Clients/Client Index]]
- [[05 Projects/Project Index]]
- [[06 Meetings/Meeting Index]]

## 进行中的项目

```dataview
TABLE status AS 状态, owner AS 负责人, next AS 下一步
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

## 客户列表

```dataview
TABLE stage AS 阶段, focus AS 关注点, last_contact AS 上次联系
FROM "04 Clients"
WHERE type = "client"
SORT file.mtime DESC
```

## 待办

```tasks
not done
sort by due
limit 20
```

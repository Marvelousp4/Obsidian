# AI 和 Agent 怎么接

这套配置里，AI 不负责替你记笔记，它负责把你已经记下来的东西重新找出来、串起来、自动处理。

现在最推荐的主流程是：

1. 白天所有信息先写进 `Daily Note`
2. 晚上对这条 daily note 跑一次 AI 分流
3. 再把 AI 给出的建议同步到正式账户、项目、会议、问题、知识笔记

## 已安装

- `Smart Connections`
  作用：做语义关联和相似笔记发现，适合回忆“我之前好像记过这个”。
- `Local REST API`
  作用：给本地脚本、自动化工具、外部 agent 开接口。
- `Omnisearch`
  作用：把普通搜索做强，偏关键词和全文。

## 推荐用法

1. 日常检索先用 `Omnisearch`
2. 想找“相关想法”时用 `Smart Connections`
3. 要做自动归档、自动同步、外部 AI 工作流时用 `Local REST API`

## 为什么没直接给你塞一堆 AI 聊天插件

- 很多插件强依赖 API key、订阅或云端模型
- 很容易把主流程变成“找 AI 聊天”而不是“沉淀资产”
- 先把结构和元数据打稳，后面接任何模型都更顺

## 你下一步可以接什么

- Ollama：本地模型
- OpenAI / Claude / Gemini：云模型
- n8n / Raycast / Keyboard Maestro：自动化入口
- 我这种外部 coding agent：通过 `Local REST API` 读写笔记

## 已经给你准备好的自动整理脚本

脚本位置：`99 System/scripts/ai_process_note.sh`

推荐入口：`99 System/scripts/run_ai_process.sh`

用途：

- 读取某条会议或问题笔记
- 调 OpenAI 生成整理稿
- 写回 `01 Inbox/AI Drafts/`

示例：

```bash
cp "/Users/bai/Documents/Obsidian/Space/99 System/scripts/.env.example" "/Users/bai/Documents/Obsidian/Space/99 System/scripts/.env"
# 然后把 .env 里的 key 改成你自己的
bash "/Users/bai/Documents/Obsidian/Space/99 System/scripts/run_ai_process.sh" "06 Meetings/客户A 需求会.md" discovery
```

建议先从 `daily`、`discovery`、`support`、`issue` 四类开始。

如果你想按“每天先写 daily，再让 AI 帮你分流”的方式用，直接这样跑：

```bash
bash "/Users/bai/Documents/Obsidian/Space/99 System/scripts/run_ai_process.sh" "02 Daily/2026-04-06.md" daily
```

这样会在 `01 Inbox/AI Drafts/` 里生成一份按账户 / 项目 / 会议 / 问题 / 知识分类的整理稿。

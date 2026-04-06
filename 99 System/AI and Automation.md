# AI 和 Agent 怎么接

这套配置里，AI 不负责替你记笔记，它负责把你已经记下来的东西重新找出来、串起来、自动处理。

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

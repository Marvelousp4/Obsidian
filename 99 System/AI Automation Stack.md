# AI / Automation Stack

## 第一层：现在就能用

- `Omnisearch`：关键词检索
- `Smart Connections`：语义相关笔记
- `Local REST API`：给外部脚本和 agent 开接口
- `ai_process_note.sh`：把原始会议 / 问题记录整理成 AI 草稿

## 第二层：一周内值得加

- 语音转文字
  方案：Mac 录音 + OpenAI 转写，或者会议工具自带 transcript
- 日报 / 周报自动汇总
  来源：`02 Daily`、`06 Meetings`、`05 Projects`
- 客户跟进提醒
  来源：`04 Clients` 中的 `next_contact`

## 第三层：更强但别一开始就上

- 自动把展会和新闻拆成客户机会
- 自动从现场问题里抽出 FAQ / SOP
- 自动给知识卡加标签和候选链接
- 自动生成周会简报和客户复盘

## 可视化怎么做

- Obsidian 自带 Graph：看知识互链，不适合做 CRM 仪表盘
- Dataview 表格：最适合你现在，够直接
- Excalidraw：画系统图、流程图、现场架构
- 真要做销售或客户漏斗可视化，再考虑 Airtable Interface

## 你的 AI 原则

- AI 先做整理、提炼、建议
- 最终知识卡和关键结论由你确认
- 不让 AI 直接改原始会议记录
- 不把客户敏感信息随便喂进公共工具

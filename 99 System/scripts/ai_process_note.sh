#!/usr/bin/env bash

set -euo pipefail

VAULT_ROOT="/Users/bai/Documents/Obsidian/Space"
REST_CONFIG="$VAULT_ROOT/.obsidian/plugins/obsidian-local-rest-api/data.json"
DEFAULT_MODEL="${OPENAI_MODEL:-gpt-5-mini}"

usage() {
  cat <<'EOF'
Usage:
  ai_process_note.sh <relative-note-path> [mode]

Examples:
  ai_process_note.sh "06 Meetings/客户A 需求会.md" discovery
  ai_process_note.sh "06 Meetings/客户B 支持会.md" support
  ai_process_note.sh "01 Inbox/现场问题-机械臂急停.md" issue

Modes:
  auto discovery support issue news video event
EOF
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

require_cmd curl
require_cmd jq

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

NOTE_PATH="$1"
MODE="${2:-auto}"

if [[ ! -f "$REST_CONFIG" ]]; then
  echo "Missing Obsidian Local REST API config: $REST_CONFIG" >&2
  exit 1
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "OPENAI_API_KEY is not set." >&2
  echo "Example: export OPENAI_API_KEY='sk-...'" >&2
  exit 1
fi

API_KEY="$(jq -r '.apiKey' "$REST_CONFIG")"
if [[ -z "$API_KEY" || "$API_KEY" == "null" ]]; then
  echo "Could not read Obsidian Local REST API key." >&2
  exit 1
fi

encode_uri() {
  jq -nr --arg v "$1" '$v|@uri'
}

sanitize_name() {
  echo "$1" | tr '/:' '--' | sed 's/[?*"<>|]//g'
}

detect_mode() {
  local path="$1"
  case "$path" in
    06\ Meetings/*需求*|06\ Meetings/*discovery* ) echo "discovery" ;;
    06\ Meetings/*支持*|06\ Meetings/*support* ) echo "support" ;;
    *Field*|*现场问题*|*issue* ) echo "issue" ;;
    *News*|*新闻* ) echo "news" ;;
    *Video*|*视频* ) echo "video" ;;
    *Event*|*展会*|*GTC* ) echo "event" ;;
    * ) echo "auto" ;;
  esac
}

if [[ "$MODE" == "auto" ]]; then
  MODE="$(detect_mode "$NOTE_PATH")"
fi

PROMPT_COMMON=$(cat <<'EOF'
你是一个严谨的知识运营助手。你的任务不是重写用户内容，而是把原始笔记整理成可执行、可链接、可沉淀的资产。

输出要求：
1. 只输出 Markdown。
2. 不要解释你在做什么。
3. 优先保留原始事实，不要编造缺失信息。
4. 如果信息不足，明确写“待补充”。
5. 输出必须包含以下部分：
   - # AI整理
   - ## 一句话总结
   - ## 关键事实
   - ## 行动项
   - ## 可沉淀知识
   - ## 推荐链接
6. 在“推荐链接”里，用 Obsidian wiki link 格式给出建议，比如 [[客户A]]、[[项目B]]、[[某技术主题]]。
7. “可沉淀知识”要判断这条记录是否值得拆成正式知识卡片；如果值得，给出 1 到 3 个建议标题。
EOF
)

case "$MODE" in
  discovery)
    MODE_PROMPT="这是一次新客户需求沟通。重点提炼需求、决策信息、预算/时间线、关键风险、下一步推进动作。"
    ;;
  support)
    MODE_PROMPT="这是一次老客户支持或问题排查沟通。重点提炼问题现象、已确认事实、临时方案、根因线索、后续责任人和动作。"
    ;;
  issue)
    MODE_PROMPT="这是一条客户现场零碎技术问题记录。重点提炼环境、复现条件、根因、解决步骤、是否值得标准化沉淀。"
    ;;
  news)
    MODE_PROMPT="这是一条行业新闻记录。重点提炼发生了什么、为什么值得关注、对行业和客户的影响、是否需要跟进。"
    ;;
  video)
    MODE_PROMPT="这是一条技术视频学习记录。重点提炼核心概念、方法、案例、值得迁移到项目或客户场景的点。"
    ;;
  event)
    MODE_PROMPT="这是一条展会或前沿活动记录。重点提炼趋势、竞品、客户机会、值得会后跟进的人和方向。"
    ;;
  *)
    MODE_PROMPT="这是一次通用工作笔记整理。重点提炼事实、行动项、可复用知识和建议链接。"
    ;;
esac

ENCODED_NOTE_PATH="$(encode_uri "$NOTE_PATH")"
NOTE_CONTENT="$(curl -ks -H "Authorization: Bearer $API_KEY" "https://127.0.0.1:27124/vault/${ENCODED_NOTE_PATH}" )"

if [[ -z "$NOTE_CONTENT" ]]; then
  echo "Could not read note content for: $NOTE_PATH" >&2
  exit 1
fi

NOW_UTC="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

REQUEST_JSON="$(jq -n \
  --arg model "$DEFAULT_MODEL" \
  --arg prompt "$PROMPT_COMMON"$'\n\n'"$MODE_PROMPT"$'\n\n'"原始笔记路径："$'\n'"$NOTE_PATH"$'\n\n'"原始笔记内容："$'\n'"$NOTE_CONTENT" \
  '{
    model: $model,
    input: $prompt
  }'
)"

OPENAI_RESPONSE="$(curl -sS https://api.openai.com/v1/responses \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$REQUEST_JSON")"

OUTPUT_TEXT="$(echo "$OPENAI_RESPONSE" | jq -r '
  .output_text // [
    .output[]?.content[]?
    | select(.type == "output_text")
    | .text
  ] | join("\n\n")
')"

if [[ -z "$OUTPUT_TEXT" || "$OUTPUT_TEXT" == "null" ]]; then
  echo "OpenAI response did not contain text output." >&2
  echo "$OPENAI_RESPONSE" >&2
  exit 1
fi

NOTE_BASENAME="$(basename "$NOTE_PATH" .md)"
SAFE_BASENAME="$(sanitize_name "$NOTE_BASENAME")"
DRAFT_PATH="01 Inbox/AI Drafts/${SAFE_BASENAME} - AI整理.md"
ENCODED_DRAFT_PATH="$(encode_uri "$DRAFT_PATH")"

DRAFT_CONTENT=$(cat <<EOF
---
type: ai_draft
source_note: "[[${NOTE_PATH%.md}]]"
source_path: "$NOTE_PATH"
mode: "$MODE"
generated_at_utc: "$NOW_UTC"
model: "$DEFAULT_MODEL"
---

# ${NOTE_BASENAME} - AI整理

来源：[[${NOTE_PATH%.md}]]

$OUTPUT_TEXT
EOF
)

HTTP_CODE="$(curl -ks -o /dev/null -w "%{http_code}" \
  -X PUT "https://127.0.0.1:27124/vault/${ENCODED_DRAFT_PATH}" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: text/markdown" \
  --data-binary "$DRAFT_CONTENT")"

if [[ "$HTTP_CODE" != "204" && "$HTTP_CODE" != "200" ]]; then
  echo "Failed to write draft note. HTTP $HTTP_CODE" >&2
  exit 1
fi

echo "Created AI draft: $DRAFT_PATH"

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
  ai_process_note.sh "06 Meetings/Account A Discovery.md" discovery
  ai_process_note.sh "06 Meetings/Account B Support.md" support
  ai_process_note.sh "01 Inbox/Field Issue - Emergency Stop.md" issue
  ai_process_note.sh "02 Daily/2026-04-06.md" daily

Modes:
  auto daily discovery support issue news video event
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
    02\ Daily/* ) echo "daily" ;;
    06\ Meetings/*discovery*|06\ Meetings/*Discovery* ) echo "discovery" ;;
    06\ Meetings/*support*|06\ Meetings/*Support* ) echo "support" ;;
    *Field*|*Issue*|*issue* ) echo "issue" ;;
    *News* ) echo "news" ;;
    *Video* ) echo "video" ;;
    *Event*|*Expo*|*GTC* ) echo "event" ;;
    * ) echo "auto" ;;
  esac
}

if [[ "$MODE" == "auto" ]]; then
  MODE="$(detect_mode "$NOTE_PATH")"
fi

PROMPT_COMMON=$(cat <<EOF
You are a rigorous knowledge-operations assistant. Your job is not to rewrite the user content. Your job is to turn raw notes into actionable, linkable, reusable assets.

Output requirements:
1. Output Markdown only.
2. Do not explain what you are doing.
3. Preserve original facts and do not invent missing information.
4. If information is missing, write "Needs follow-up".
5. The output must include these sections:
   - # AI Draft
   - For a normal note: ## One-Line Summary / ## Key Facts / ## Action Items / ## Knowledge Worth Promoting / ## Suggested Links
   - For a daily note: ## Today Summary / ## Suggested Account Updates / ## Suggested Project Or Site Updates / ## Suggested Meetings / ## Suggested Issues / ## Suggested Knowledge Notes / ## Next Priorities
6. In "Suggested Links", use Obsidian wiki-link format such as [[Account A]], [[Project B]], or [[Technical Topic]].
7. In "Knowledge Worth Promoting", decide whether the note should become one or more formal knowledge notes. If yes, propose one to three titles.
EOF
)

case "$MODE" in
  daily)
    MODE_PROMPT="This is a daily note. Route the content into suggested account, contact, project, meeting, issue, and knowledge updates. Do not invent facts. For each suggestion, provide a proposed title, target folder, preserved fact summary, and suggested links. The main goal is to help the user turn the daily note into formal notes at the end of the day."
    ;;
  discovery)
    MODE_PROMPT="This is a new customer discovery conversation. Extract requirements, decision context, budget and timeline signals, major risks, and next actions."
    ;;
  support)
    MODE_PROMPT="This is an existing customer support or troubleshooting conversation. Extract symptoms, confirmed facts, temporary workarounds, root-cause clues, owners, and follow-up actions."
    ;;
  issue)
    MODE_PROMPT="This is a fragmented field technical issue note. Extract environment, reproduction conditions, root cause, resolution steps, and whether it should become a standardized knowledge note."
    ;;
  news)
    MODE_PROMPT="This is an industry news note. Extract what happened, why it matters, the impact on the industry and customers, and whether follow-up is needed."
    ;;
  video)
    MODE_PROMPT="This is a technical video learning note. Extract core concepts, methods, examples, and ideas worth moving into projects or customer contexts."
    ;;
  event)
    MODE_PROMPT="This is an event or frontier-activity note. Extract trends, competitor signals, customer opportunities, and the people or directions worth following up after the event."
    ;;
  *)
    MODE_PROMPT="This is a general work note. Extract facts, action items, reusable knowledge, and suggested links."
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
  --arg prompt "$PROMPT_COMMON"$'\n\n'"$MODE_PROMPT"$'\n\n'"Source note path:"$'\n'"$NOTE_PATH"$'\n\n'"Source note content:"$'\n'"$NOTE_CONTENT" \
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
DRAFT_PATH="01 Inbox/AI Drafts/${SAFE_BASENAME} - AI Draft.md"
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

# ${NOTE_BASENAME} - AI Draft

Source: [[${NOTE_PATH%.md}]]

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

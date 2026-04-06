# AI and Automation

In this setup, AI is not the note-taker. It processes, reconnects, and restructures material that you already captured.

## Preferred Workflow

1. Write all raw input into the daily note during the day
2. Run AI triage on that daily note at night
3. Move the AI suggestions into formal area, project, people, work, and knowledge notes

## Installed Components

- `Smart Connections`
  Purpose: semantic linking and similar-note discovery when you vaguely remember that you saw something before
- `Local REST API`
  Purpose: interface for local scripts, automation tools, and external agents
- `Omnisearch`
  Purpose: stronger full-text and keyword search

## Recommended Usage

1. Use `Omnisearch` for normal retrieval
2. Use `Smart Connections` when you want related notes or adjacent ideas
3. Use `Local REST API` for automation, sync, or external AI workflows

## Why This Vault Does Not Rely On AI Chat Plugins

- Many plugins depend on API keys, subscriptions, or cloud models
- They often turn the workflow into chatting with AI instead of building assets
- Stable structure and metadata make every future model integration cleaner

## What You Can Add Next

- Ollama: local models
- OpenAI / Claude / Gemini: cloud models
- n8n / Raycast / Keyboard Maestro: automation entry points
- External coding agents like me: read and write notes through `Local REST API`

## Prepared Processing Scripts

Script path: `99 System/scripts/ai_process_note.sh`

Recommended runner: `99 System/scripts/run_ai_process.sh`

What it does:

- Reads a daily note or a work note
- Calls a model to generate a structured draft
- Writes the result into `01 Inbox/AI Drafts/`

Example:

```bash
cp "/Users/bai/Documents/Obsidian/Space/99 System/scripts/.env.example" "/Users/bai/Documents/Obsidian/Space/99 System/scripts/.env"
# Then replace the key in `.env` with your own
bash "/Users/bai/Documents/Obsidian/Space/99 System/scripts/run_ai_process.sh" "09 Work/Meetings/Account A Discovery.md" discovery
```

Start with `daily`, `discovery`, `support`, and `issue`.

If you want the "daily first, AI triage at night" flow, run:

```bash
bash "/Users/bai/Documents/Obsidian/Space/99 System/scripts/run_ai_process.sh" "02 Daily/2026-04-06.md" daily
```

This generates one draft in `01 Inbox/AI Drafts/` grouped by area, project, people, work, and knowledge suggestions.

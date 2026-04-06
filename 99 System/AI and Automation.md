# AI and Automation

In this setup, AI is not the note-taker. It processes, reconnects, compiles, and repairs material that you already captured.

## Preferred Workflow

1. Write all raw input into the daily note during the day
2. Move durable source material into `10 Raw`
3. Run AI triage on the daily note at night
4. Run AI compile on important raw notes
5. Periodically run a wiki health check

## Three AI Jobs

### 1. Daily Triage

Turn one daily note into suggested updates for areas, projects, people, work notes, and knowledge notes.

### 2. Raw Compilation

Turn one raw markdown source into:

- one compiled knowledge note
- several concept pages
- reverse links between the new pages and the source

### 3. Wiki Health Check

Scan the whole wiki for:

- raw notes with no compiled output
- broken links
- placeholder sections
- concept pages with weak source support

## Recommended Usage

1. Use `Omnisearch` for normal retrieval
2. Use `Local REST API` for automation, sync, or external AI workflows
3. Use `10 Raw` as the AI compile queue, not as a permanent dumping ground

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

## Knowledge Factory Scripts

- `99 System/scripts/raw_ingest.py`
  Turns PDFs, markdown files, and local repos into markdown raw notes
- `99 System/scripts/compile_raw_library.py`
  Compiles raw markdown notes into structured knowledge and concept notes
- `99 System/scripts/wiki_health_check.py`
  Generates a repair report for the compiled wiki
- `99 System/scripts/run_knowledge_factory.sh`
  Runs compile and health-check in one shot

Recommended flow:

```bash
python3 "/Users/bai/Documents/Obsidian/Space/99 System/scripts/raw_ingest.py" markdown "/path/to/article.md" --kind web
python3 "/Users/bai/Documents/Obsidian/Space/99 System/scripts/compile_raw_library.py" --provider auto --only-uncompiled
python3 "/Users/bai/Documents/Obsidian/Space/99 System/scripts/wiki_health_check.py"
```

# Knowledge Factory

This vault now uses a three-stage knowledge pipeline:

1. `Raw`
   Capture durable source material as markdown in `10 Raw`
2. `Compile`
   Turn raw notes into structured knowledge and concept pages in `05 Knowledge`
3. `Health Check`
   Periodically scan the wiki for missing links, missing compilations, and weak concept coverage

## Step 1: Raw

Use `10 Raw` for:

- web articles clipped to markdown
- paper text extracted to markdown
- repo digests
- transcripts and long rough source notes

Rules:

- Raw notes should stay close to the source
- Raw notes should be markdown, not binary files
- Binary originals still belong in `07 Resources`

## Step 2: Compile

Use AI to turn raw notes into:

- compiled summaries
- encyclopedia-style concept pages
- reverse links
- reusable takeaways

The compiled wiki lives in:

- `05 Knowledge/Compiled`
- `05 Knowledge/Concepts`

Deterministic fallback output is draft-only. It can help create a skeleton, but it does not mark a raw note as `compiled`. A raw note is only compiled after it passes the quality gate in [[99 System/Metadata Contract|Metadata Contract]].

## Step 3: Health Check

The health check should ask:

- Which raw notes still have no compiled output?
- Which compiled notes have weak links?
- Which concept pages are undersourced?
- Which pages still contain placeholders or contradictions?

## Command Line Entry Points

```bash
python3 "99 System/scripts/raw_ingest.py" --help
python3 "99 System/scripts/compile_raw_library.py" --help
python3 "99 System/scripts/wiki_health_check.py" --help
bash "99 System/scripts/run_knowledge_factory.sh"
```

## Obsidian CLI Examples

Create a raw note with the raw template:

```bash
obsidian create vault="Space" path="10 Raw/Inbox/New Source.md" template="Raw Source"
```

Open the knowledge board:

```bash
obsidian open vault="Space" path="00 Dashboard/Boards/Knowledge Board.md"
```

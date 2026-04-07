# Metadata Contract

This page defines the minimum fields that scripts, boards, and templates should agree on.

## Area

Canonical fields:

- `type: area`
- `status`
- `focus`
- `review_rhythm`
- `tags`

Rules:

- Area notes live as dashboards under `03 Areas/<Area>/<Area>.md`.
- Area pages define standards, boundaries, active projects, related knowledge, and review prompts.
- Area folders may contain area-owned operational data, such as `03 Areas/Health/Logs` and `03 Areas/Health/Baselines`.
- Do not put reusable knowledge in an area folder unless it is an area-owned baseline or operating record. Reusable conclusions belong in `05 Knowledge`.

## Personal Project

Canonical fields:

- `type: project`
- `area`
- `status`
- `owner`
- `started`
- `next`
- `tags`

Rules:

- Personal projects should not use `account`, `client`, `site`, or `project_kind` unless they are explicitly work projects.
- Use area values such as `health`, `finance`, `learning`, `research`, `personal`, `relationships`, or `mind`.

## Work Project

Canonical fields:

- `type: project`
- `area: work`
- `account`
- `project_kind`
- `site`
- `status`
- `owner`
- `started`
- `next`
- `tags`

Rules:

- `account` is the canonical customer or organization key.
- `client` should not be used in work project notes. It was a legacy alias and should stay out of new templates and imports.
- `next` should contain the next concrete action, not a generic reminder to update the note.

## Issue

Canonical fields:

- `type: issue`
- `account`
- `project`
- `site`
- `vendor`
- `category`
- `item_type`
- `status`
- `severity`
- `priority`
- `created_date`
- `last_updated_date`
- `reporter`
- `assignee`
- `source_type`
- `source_id`
- `source_file`
- `bot_ids`
- `components`

Rules:

- Current issues live under `09 Work/Issues/Active`.
- Completed but useful issues live under `09 Work/Issues/Archive/Completed`.
- Import summaries live under `09 Work/Issues/Imports`.
- `account` is the canonical account key.
- `client` should not be used in issue notes. It was a legacy alias and should stay out of new imports.
- `source` should not be used in issue notes. Use `source_type`, `source_id`, and `source_file`.
- Source paths should be vault-relative labels or source filenames, not machine-specific absolute paths.

## Health Baseline

Canonical fields:

- `type: health_baseline`
- `area: health`
- `domain`
- `source`
- `source_type`
- `created`
- `updated`
- `tags`

Rules:

- Health baselines are area-owned operating records, not general knowledge notes.
- Baseline notes live under `03 Areas/Health/Baselines`.
- Daily imported or inferred health logs live under `03 Areas/Health/Logs`.

## Raw Source

Canonical fields:

- `type: raw_source`
- `source_kind`
- `capture_status`
- `captured`
- `source_path`
- `source_url`
- `repo_url`
- `compiled_note`
- `compile_quality`

Rules:

- `source_path` should be vault-relative when the source is inside the vault.
- `capture_status: compiled` means the compiled note passed the quality gate.
- Deterministic fallback output is draft-only and should remain `capture_status: needs_compile`.

## Compiled Knowledge

Canonical fields:

- `type: knowledge`
- `area`
- `domain`
- `source`
- `source_type`
- `compiled_from`
- `compile_quality`

Minimum quality gate:

- one short conclusion-style summary
- at least three takeaways
- at least two concept links
- at least one linked source
- no raw absolute source paths

`compile_quality` semantics:

- `passed`: all quality gate checks above are satisfied.
- `draft`: note exists but does not yet satisfy the full gate.
- `failed`: compile attempt failed or content is unusable and needs rework.

Rule:

- Do not set `compile_quality: passed` unless the note currently passes the gate.

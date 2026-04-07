# Metadata Contract

This page defines the minimum fields that scripts, boards, and templates should agree on.

## Work Project

Canonical fields:

- `type: project`
- `area`
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

- `account` is the canonical account key.
- `client` should not be used in issue notes. It was a legacy alias and should stay out of new imports.
- `source` should not be used in issue notes. Use `source_type`, `source_id`, and `source_file`.
- Source paths should be vault-relative labels or source filenames, not machine-specific absolute paths.

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

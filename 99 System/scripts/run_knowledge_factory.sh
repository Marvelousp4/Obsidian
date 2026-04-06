#!/usr/bin/env bash

set -euo pipefail

VAULT_ROOT="/Users/bai/Documents/Obsidian/Space"
SCRIPT_ROOT="$VAULT_ROOT/99 System/scripts"

python3 "$SCRIPT_ROOT/compile_raw_library.py" --provider auto --only-uncompiled "$@"
python3 "$SCRIPT_ROOT/wiki_health_check.py"

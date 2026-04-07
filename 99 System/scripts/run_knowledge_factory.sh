#!/usr/bin/env bash

set -euo pipefail

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_ROOT/compile_raw_library.py" --provider auto --only-uncompiled "$@"
python3 "$SCRIPT_ROOT/wiki_health_check.py"

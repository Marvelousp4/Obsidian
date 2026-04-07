#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_LOCAL_VAULT="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOCAL_VAULT="${1:-$DEFAULT_LOCAL_VAULT}"
ICLOUD_VAULT="${2:-${ICLOUD_VAULT:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Space}}"

mkdir -p "$ICLOUD_VAULT"

rsync -a --delete \
  --exclude '.git/' \
  --exclude '.obsidian/workspace.json' \
  --exclude '.obsidian/workspace-mobile.json' \
  --exclude '.obsidian/cache/' \
  --exclude '.obsidian/plugins/obsidian-local-rest-api/data.json' \
  --exclude '07 Resources/' \
  --exclude '.smart-env/' \
  "$LOCAL_VAULT/" "$ICLOUD_VAULT/"

echo "Mirrored markdown and settings from $LOCAL_VAULT to $ICLOUD_VAULT"

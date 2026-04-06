#!/usr/bin/env bash

set -euo pipefail

LOCAL_VAULT="${1:-/Users/bai/Documents/Obsidian/Space}"
ICLOUD_VAULT="${2:-/Users/bai/Library/Mobile Documents/iCloud~md~obsidian/Documents/Space}"

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

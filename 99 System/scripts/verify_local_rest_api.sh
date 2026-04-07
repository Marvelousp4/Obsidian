#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
REST_CONFIG="$VAULT_ROOT/.obsidian/plugins/obsidian-local-rest-api/data.json"

if [[ ! -f "$REST_CONFIG" ]]; then
  echo "Missing Local REST API config: $REST_CONFIG" >&2
  exit 1
fi

API_KEY="$(jq -r '.apiKey' "$REST_CONFIG")"
if [[ -z "$API_KEY" || "$API_KEY" == "null" ]]; then
  echo "Could not read API key from Local REST API config." >&2
  exit 1
fi

echo "Checking service root..."
curl -ks -H "Authorization: Bearer $API_KEY" https://127.0.0.1:27124/ | jq .

echo
echo "Checking commands endpoint..."
curl -ks -H "Authorization: Bearer $API_KEY" https://127.0.0.1:27124/commands/ | jq '.commands | length'

echo
echo "Checking vault listing..."
curl -ks -H "Authorization: Bearer $API_KEY" https://127.0.0.1:27124/vault/ | jq .

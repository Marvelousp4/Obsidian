# Local and iCloud Sync

The primary vault should live locally for speed:

- primary path: `/Users/bai/Documents/Obsidian/Space`
- optional mirror path: `/Users/bai/Library/Mobile Documents/iCloud~md~obsidian/Documents/Space`

`07 Resources` remains anchored to the iCloud copy through local subdirectory symlinks, so the mirror script syncs markdown and settings but intentionally skips `07 Resources`.

## Rule

- Write locally
- Sync to iCloud only when you actually need phone or tablet access
- Use GitHub for history and backup

## Why

- iCloud makes large vaults and plugin-heavy vaults noticeably slower
- Local storage keeps indexing and file scanning fast
- A one-way mirror to iCloud is enough for occasional mobile access

## Mirror Command

```bash
bash "/Users/bai/Documents/Obsidian/Space/99 System/scripts/sync_space_to_icloud.sh"
```

## Before Mirroring

- Run Git backup first
- Close the vault on mobile if possible
- Do not edit the local and iCloud copies at the same time

# Sync

## Rule

- Keep the primary vault local for speed.
- Use GitHub for version history, backup, and rollback.
- Use iCloud only as an optional mirror when you need mobile access.

## GitHub

- Use a private repository.
- Run `Git: Pull` before starting on another device.
- Run `Git: Commit-and-sync` before closing the day or switching devices.
- Do not push tokens, certificates, API keys, or large binary resources.

## iCloud Mirror

The vault is local by default. Mirror it only when needed:

```bash
bash "99 System/scripts/sync_space_to_icloud.sh"
```

Before mirroring:

- Run Git backup first.
- Close the vault on mobile if possible.
- Do not edit the local and iCloud copies at the same time.

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

## 07 Resources Symlink Strategy

Use a symlink so large/raw resource files can live outside the repo while notes keep stable vault paths.

Recommended layout:

- Keep the vault at `/Users/bai/Documents/Obsidian/Space`.
- Keep real resources at a stable path (for example `/Users/bai/Documents/Obsidian-Resources/07 Resources`).
- In the vault, create `07 Resources` as a symlink to that stable path.

Setup command:

```bash
ln -s "/Users/bai/Documents/Obsidian-Resources/07 Resources" "/Users/bai/Documents/Obsidian/Space/07 Resources"
```

Cross-device rule:

- On every new machine, recreate the same symlink target path or update links to a new stable root before use.
- If you use iCloud for resources, ensure the iCloud path is identical across devices before creating the symlink.

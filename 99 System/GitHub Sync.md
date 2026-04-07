# GitHub Sync

## Principles

- Use GitHub for version history and backup
- Keep the primary vault local for speed
- Treat iCloud as an optional mirror, not the primary working copy
- Do not push sensitive config or large attachments by default
- Obsidian is for writing, Git is for history

## Recommended Repository Shape

- Use a private repository
- Keep one vault per repository
- If attachments grow large, solve storage separately instead of abusing Git

## Protection Already Applied In This Vault

- `.gitignore` excludes `workspace.json`
- `.gitignore` excludes sensitive Local REST API config
- `.gitignore` excludes large resources under `07 Resources`

## Local Initialization

```bash
git init
git add .
git commit -m "Initialize Obsidian workspace"
```

## Connect A Private GitHub Repository

```bash
git remote add origin <your-private-repo-url>
git branch -M main
git push -u origin main
```

## Use The Git Plugin In Obsidian

- Open the Command Palette
- Run `Obsidian Git: Create backup`
- Run `Obsidian Git: Pull`
- Run `Obsidian Git: Open source control view`

## Recommended Rhythm

- Run `Create backup` before the day ends
- Run `Create backup` before switching devices
- Run `Pull` before starting work on a device
- Mirror to iCloud only when you actually need mobile access

## Optional iCloud Mirror

```bash
bash "99 System/scripts/sync_space_to_icloud.sh"
```

## Avoid

- Do not use a public repository by default
- Do not push certificates, tokens, or customer-sensitive information
- Do not auto-commit every few minutes; it destroys signal in history

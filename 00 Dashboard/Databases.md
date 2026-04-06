# Databases

Use these only when you want table-style scanning or bulk edits. They are not the main capture path. These database views are currently work-heavy on purpose, because the most structured part of the vault is still CRM, delivery, and support.

- [[00 Dashboard/Databases/Accounts Database|Accounts Database]]
- [[00 Dashboard/Databases/Contacts Database|Contacts Database]]
- [[00 Dashboard/Databases/Projects Database|Projects Database]]
- [[00 Dashboard/Databases/Issues Database|Issues Database]]

## When To Use Them

- Use account and contact databases when preparing outreach or cleaning CRM metadata
- Use the projects database when reviewing deployment status in bulk
- Use the issues database when scanning patterns, priorities, and stale support items
- Use the main indices in `Areas / Projects / Knowledge / People` for the broader personal system
- Do not use database views as the main writing surface; write in notes first

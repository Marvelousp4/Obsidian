# Contact Index

```dataview
TABLE organization, team, title, relationship, last_contact, verification_status
FROM "09 Work/Accounts"
WHERE type = "contact"
SORT organization ASC, team ASC, file.name ASC
```


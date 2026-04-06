# Contact Index

```dataview
TABLE organization, team, title, relationship, last_contact, verification_status
FROM "04 Clients"
WHERE type = "contact"
SORT organization ASC, team ASC, file.name ASC
```


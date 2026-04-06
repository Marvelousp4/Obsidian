# People Index

Use this page for people across your whole system. Direct person notes live under `06 People`. Work contacts tied to accounts remain nested under `09 Work/Accounts`.

## Direct People Notes

```dataview
TABLE person_kind AS Kind, relationship AS Relationship, organization AS Organization, title AS Title, last_contact AS "Last Contact"
FROM "06 People"
WHERE type = "person"
SORT file.name ASC
```

## Professional Contacts

```dataview
TABLE organization AS Organization, team AS Team, title AS Title, relationship AS Relationship, last_contact AS "Last Contact"
FROM "09 Work/Accounts"
WHERE type = "contact"
SORT organization ASC, file.name ASC
LIMIT 50
```

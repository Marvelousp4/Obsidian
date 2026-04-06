# People Index

Use this page for people across your whole system. Professional contacts remain nested under work accounts. Personal people notes live directly under `06 People`.

## Personal People

```dataview
TABLE person_kind AS Kind, relationship AS Relationship, organization AS Organization, last_contact AS "Last Contact"
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

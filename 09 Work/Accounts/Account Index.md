# Account Index

```dataview
TABLE stage, industry, region, last_contact, next_contact
FROM "09 Work/Accounts"
WHERE type = "account"
SORT file.name ASC
```

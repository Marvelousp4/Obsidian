# Account Index

```dataview
TABLE stage, industry, region, last_contact, next_contact
FROM "04 Clients"
WHERE type = "account"
SORT file.name ASC
```

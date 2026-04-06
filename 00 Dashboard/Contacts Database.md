---
database-plugin: basic
---

```yaml:dbfolder
name: Contacts Database
description: Contact records in a database view.
columns: {}
filters:
  enabled: false
  conditions: []
config:
  source_data: query
  source_form_result: 'FROM "04 Clients" WHERE type = "contact"'
  source_destination_path: 04 Clients
  pagination_size: 50
```

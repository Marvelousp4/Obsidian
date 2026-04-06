---
database-plugin: basic
---

```yaml:dbfolder
name: Issues Database
description: Issue records in a database view.
columns: {}
filters:
  enabled: false
  conditions: []
config:
  source_data: query
  source_form_result: 'FROM "08 Issues" WHERE type = "issue"'
  source_destination_path: 08 Issues
  pagination_size: 50
```

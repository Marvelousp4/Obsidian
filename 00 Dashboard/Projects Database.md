---
database-plugin: basic
---

```yaml:dbfolder
name: Projects Database
description: Project and deployment records in a database view.
columns: {}
filters:
  enabled: false
  conditions: []
config:
  source_data: query
  source_form_result: 'FROM "05 Projects" WHERE type = "project"'
  source_destination_path: 05 Projects
  pagination_size: 30
```

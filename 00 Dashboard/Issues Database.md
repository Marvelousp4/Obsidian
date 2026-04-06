---
database-plugin: basic
---

```yaml:dbfolder
name: Issues Database
description: Issue records in a database view.
columns:
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 0
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  client:
    key: client
    id: client
    input: text
    label: Client
    accessorKey: client
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 1
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  site:
    key: site
    id: site
    input: text
    label: Site
    accessorKey: site
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 2
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  category:
    key: category
    id: category
    input: text
    label: Category
    accessorKey: category
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 3
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  status:
    key: status
    id: status
    input: text
    label: Status
    accessorKey: status
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 4
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  severity:
    key: severity
    id: severity
    input: text
    label: Severity
    accessorKey: severity
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 5
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  priority:
    key: priority
    id: priority
    input: text
    label: Priority
    accessorKey: priority
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 6
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  last_updated_date:
    key: last_updated_date
    id: last_updated_date
    input: calendar
    label: Updated
    accessorKey: last_updated_date
    isMetadata: false
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 7
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
filters:
  enabled: false
  conditions: []
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: false
  group_folder_column: ""
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: query
  source_form_result: "FROM \"08 Issues\" WHERE type = \"issue\""
  source_destination_path: 08 Issues
  row_templates_folder: /
  current_row_template: ""
  pagination_size: 50
  font_size: 16
  enable_js_formulas: false
  formula_folder_path: /
  inline_default: false
  inline_new_position: last_field
  date_format: yyyy-MM-dd
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
  implementation: default
```

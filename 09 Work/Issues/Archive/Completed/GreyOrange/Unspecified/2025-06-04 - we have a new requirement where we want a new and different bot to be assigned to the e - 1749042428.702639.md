---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P4"
created_date: "2025-06-04"
last_updated_date: "2026-04-07"
reporter: "U049CDY3TGC"
assignee: ""
source_id: "1749042428.702639"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["lift", "pallet", "rds"]
tags: []
---

# we have a new requirement where we want a new and different bot to be assigned to the e...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1749042428.702639
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

we have a new requirement where we want a new and different bot to be assigned to the existing order in case the existing bot goes in any failure. example scenario- 1. Order sequence is created on RDS 2. Blocks are added. 3. Bot 1 is assigned to this order sequence. 4. Bot 1 started to move to lift the pallet. 5. Bot 1 went in hardware failure. 6. Now we want this order sequence to be picked up by other available bot (ex- Bot 2) 7. Bot 2 comes and lifts the pallet and continues with the task. Do we have any api for this. I could find something similar but nit sure if this works or how it works. <

## Progress

No progress note captured in the cleaned source.

## Next Action

Can you help with the above query and share any data which might help with above request. FYI- Can you please check this on priority. FYI-

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P4
- Created: 2025-06-04
- Last updated: 2025-06-06
- Bot IDs: 
- Components: lift, pallet, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

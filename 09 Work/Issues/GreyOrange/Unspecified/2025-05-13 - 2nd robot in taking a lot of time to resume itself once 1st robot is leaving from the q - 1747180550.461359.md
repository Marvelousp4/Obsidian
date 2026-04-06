---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "software_or_firmware"
item_type: "software"
status: "open"
severity: ""
priority: "P4"
created_date: "2025-05-13"
last_updated_date: "2025-05-18"
reporter: "U04580WJL65"
assignee: ""
source_id: "1747180550.461359"
bot_ids: []
components: []
tags: []
---

# 2nd robot in taking a lot of time to resume itself once 1st robot is leaving from the q...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1747180550.461359
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

2nd robot in taking a lot of time to resume itself once 1st robot is leaving from the queue, so for exa if we have 3 robots standing near by markers M1, M2,M3 and when M1 leave the marker then robot at M2 is taking lot of time to resume itself

## Progress

According to my collegueas, robot will play some music before it start moving, you can reduce this period by modifying following parameter. collegueas -> colleagues Ok, we are reducing this time but we can see delay before start playing sound

## Next Action

you can check 8282, 8284 and 8286 As per it's robot issue, so shared robot 8284 logs with Yangda

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: open
- Severity: 
- Priority: P4
- Created: 2025-05-13
- Last updated: 2025-05-18
- Bot IDs: 
- Components: 

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

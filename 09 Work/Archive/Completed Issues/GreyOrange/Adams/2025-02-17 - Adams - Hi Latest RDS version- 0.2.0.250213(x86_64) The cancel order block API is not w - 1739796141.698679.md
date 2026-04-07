---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Adams"
site: "Adams"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: "SEV2"
priority: "P2"
created_date: "2025-02-17"
last_updated_date: "2026-04-07"
reporter: "U06FLBATWAY"
assignee: ""
source_id: "1739796141.698679"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["pallet", "rds"]
tags: []
---

# Adams | Hi Latest RDS version: 0.2.0.250213(x86_64) The cancel order block API is not w...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C06TL405CRF_2025-01-01_to_2026-03-16.txt
- Original source id: 1739796141.698679
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

Hi Latest RDS version: 0.2.0.250213(x86_64) The cancel order block API is not working even though the response gives 200 with okay but not cancelling block task. It was working on the rds dev version 0.1.9.241113-dev & it was stable. Please fix it asap and revert back as it is a blocker for Adam's validation. ```curl --location '< \ --header 'Content-Type: application/json' \ --data '{"vehicles":[{"name":"RIL-L-8217","blockIds":["testing_order2"]}]}' { "code": 0, "create_on": "2025-02-17T10:20:13Z", "msg": "ok" }``` 📎Screenshot 2025-02-17 at 4.06.22 PM.png U0ALSB28Q0Y/F08DN44UE82

## Progress

can u please get this checked and fixed asap. we tried first cancel the blockid testing_order2 in forklaod after we also tried but it did not got cancel curl --location '< \ --header 'Content-Type: application/json' \ --data '{"vehicles":[{"name":"RIL-L-8217","blockIds":["testing_order5"]}]}' { "code": 0, "create_on": "2025-02-17T10:20:13Z", "msg": "ok" } it's reproducible also on this in version 0.2.0.250213 okay, sure. Please fix asap and revert with stable version. make sure other issue should come again e.g. pallet detections and all dev version seems working fine stable. just fyi.

## Next Action

In the screen shot and the request you shared, seems you are not sending correct request. In the screen shot, the RUNNING block is testing_order5, but in the request you are cancelling testing_order2 OK, I've already shared your mail to SEER team, they are checking this

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: SEV2
- Priority: P2
- Created: 2025-02-17
- Last updated: 2025-02-18
- Bot IDs: 
- Components: pallet, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

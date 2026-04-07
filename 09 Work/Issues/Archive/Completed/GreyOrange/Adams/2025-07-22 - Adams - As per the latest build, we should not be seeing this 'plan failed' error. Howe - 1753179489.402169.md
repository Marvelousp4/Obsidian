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
severity: ""
priority: "P2"
created_date: "2025-07-22"
last_updated_date: "2026-04-07"
reporter: "U046B9XUZRV"
assignee: ""
source_id: "1753179489.402169"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: ["8293"]
components: ["rds", "sto"]
tags: []
---

# Adams | As per the latest build, we should not be seeing this 'plan failed' error. Howe...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1753179489.402169
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

As per the latest build, we should not be seeing this 'plan failed' error. However, it is still persisting on site, occurring frequently (2-3 times a day). I am sharing the robot and RDS logs for this issue in the below google link. Can you please check and provide a permanent solution? < Bot id:9027 FYI

## Progress

Hi the plan failed for 9027 was observed betweek 10:20pm -10:40pm est on 21st July 2025 One more plan failed incident reported at adams, Please refer the attached logs and evidence for the same FYIP 📎Screenshot 2025-07-24 162119.png U0ALSB28Q0Y/F0983FPV108 📎Screenshot 2025-07-24 162050.png U0ALSB28Q0Y/F0983FTAKCG could you explain a bit more? what happened? 8291 and 9021 is not moving? You manual moved one bot to solve this? 9021 came to drop palette on flowrail, at the same time 8291 was coming from top. After dropping palette on flowrail 9021 stopped. On server it showed 8291 plan failed. In order to recover, i made 8291 offline, 9021 moved a bit then i madd 8291 online again OK, got it, thank you This issue was also solved in the last release Another "plan fail ignored" issue came up just now. This created a long queue stuck at the site and created major disruption at site. Please refer the logs for planned failed ignored issue. < This was caused by operator manual moved bot 8293 behind 8289

## Next Action

Hi, could you pls share the timestamp or location when this issue happened? I didn't see this issue in the log There is no plan failed error in the log you shared. Pls check and share again. any update here ? Hi, I checked with Yangda today, they are working on this issue now, but haven't figured out. Do you think we should have a release for the keep RUNNING issue first? Yes I think they should provide release with RUNNING issue first and Ross, our experience is not good with releases, many times we are introducing some new issues in latest releases so I hope they tested it well

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P2
- Created: 2025-07-22
- Last updated: 2025-08-21
- Bot IDs: 8293
- Components: rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

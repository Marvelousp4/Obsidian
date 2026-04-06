---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "H&M"
site: "H&M"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-12-03"
last_updated_date: "2025-12-11"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1764777484.073909"
bot_ids: ["9001", "9002", "9003", "9004", "9005", "9006", "9007", "9008"]
components: ["dock", "rds", "sto"]
tags: []
---

# H&M Canada | Hi We are facing an issue of repeated congestions in H&M Canada, affecting...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1764777484.073909
- Site: H&M
- Vendor / platform context: Wellwit Robotics

## Problem

Hi We are facing an issue of repeated congestions in H&M Canada, affecting our overall performance. BOT ID's: 9004,9007,9006,9008,9002 RDS Version: 0.1.9.240705 Time Stamp: 11:47:00 as per the logs 1)The task execution and the priorities are set perfect and No issue with the task assessment also. 2)Found a systematical deadlock, where RDS A algorithm failed to execute the tasks. 3)Bot 9002 has parking task, bot 9004 has dock-point task, but we think 9004 needs to pass the mutex and 9002 bot to complete its order. 4) Final logs we see is: `[251126 114105.432][D][d] [GM][A-Star|Out of Ability|7|7|RIL-H-9001,RIL-H-9003,RIL-H-9004,RIL-H-9005,RIL-H-9006,RIL-H-9007,RIL-H-9008,]` Can you please provide root cause analysis and suggestions to resolve this as this is coming repeatedly. Log - < Internal reference - AE-1986 FYI

## Progress

SEER ticket link: <

## Next Action

Hi Ross, can you please check this. SEER team suggest to move LM90223 to left, to let 9008 could move upward. "A circular deadlock has formed. The core issue needs to be addressed: the RIL-H-9008 problem. As it is a one-way street, the point ahead is prohibited from stopping, and the area ahead is mutually exclusive, causing vehicle 06 to be unable to avoid vehicle 08. It is suggested to adjust the map at point LM90223 so that there are vehicles waiting and it does not affect other vehicles entering the working point."

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-12-03
- Last updated: 2025-12-11
- Bot IDs: 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008
- Components: dock, rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/H&M.md|H&M]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

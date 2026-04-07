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
created_date: "2025-10-06"
last_updated_date: "2026-04-07"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1759763678.069379"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["charger", "rds"]
tags: []
---

# Adams | Hi, we faced an issue on Adams site when RDS APIs became unresponsive and opera...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1759763678.069379
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

Hi, we faced an issue on Adams site when RDS APIs became unresponsive and operations could only be resumed after restarting RDS. Attaching the full logs here: Drive link - < Internal reference - AE-1359 FYI

## Progress

Hi Can you prioritise this as we need RCA for the issue. We are seeing these type of issues on another site as well, so please look into this once. Occurence - 2 - Sodimac We also faced similar issue at another production site. At Sodimac Colombia, the RDS core is getting disconnected frequently. This was reported twice (at 2025-10-01 01:35 AM IST and 2025-10-01 02:55 AM IST) To fix this, the first time the RDS core was restarted from Roboshop and the operations resumed. The second time, it was auto-resolved. < I am not creating a separate thread for this, but let me know if its different issue. No, I still can't access 1. We can turn off the charger matching algo, but since this issue is low frequency, maybe we can run like it. We want to fix this issue, but currently can't find anyway to proceed. parameter name is "RHCRMaxNodeCount" Thanks Ross, we are going to try this on Sodimac. Also, for this at Adams: > 1. We can turn off the charger matching algo, but since this issue is low frequency, maybe we can run like it. We want to fix this issue, but currently can't find anyway to proceed. Will it have any negative impact onsite if we turn off the charger matching algo? Can you please confirm regarding the Adams case - if we turn off the charger matching algo, can it have some negative impact onsite. fyi Yes, in that case we can not ensure the lowest SOC bot go to charge first

## Next Action

Is there any update. on this? FYI Pls check. Below are my findings: 1. In RDS log, after 2025-09-19 07:31:07.201 the core API is not accessable 2. Core was keep running until manual restart 3. After 250919 073832.301, there is no any http log For the first issue, we checked the log, it was an known issue but we haven't found the cause. It's related to the charger matching algorithm. It happens with very low frequency. For the second issue, I don't have the access to the Google drive link, I've already send the request please check the access now. May be is trying to access with his personal gmail id, so I sent you an access request for Ross email id's, check and allow the access I also didnt have permission to give access. I have created a new share: < Please try to access this. Is there any update for this? Can you please provided analyis for this: 1. For first issue which occured at Adams, can we avoid this by some config in charger matching algo. Or do we have some plan to provide a fix for this? 2. For Sodimac site, is the root cause same here also? 2. Will check with Yangda please share the seer's ticket progress on it, I hope you created ticket for them 2. For Columbia site, the cause is different than Adam's, it was caused by RHCR calculation took long time. 313789: [250930 154252.702][0x00007f8329a4c700][rbk][debug] [TimeLogger][140201316108032|WSPBS|BuildInput|21|Run|242702|GetSolution|0|BuildOutput|19|log|0|total|243680] [250930 163429.853][0x00007f2886b48700][RDSDispatcher][debug] [TCost][0.2.0.250821, Linux, Aug 25 2025, 05:12:11][schedule.run|81|runOrder.runBlock|17|updateScene.resetCurrnetMap|16|runOrder.runRHCR|5151|runOrder.runRobotTask|17|copydb2mem|60|Total|5494] For this you can try to reduce the "maxnode" parameter to 5000 and check

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P2
- Created: 2025-10-06
- Last updated: 2025-11-17
- Bot IDs: 
- Components: charger, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

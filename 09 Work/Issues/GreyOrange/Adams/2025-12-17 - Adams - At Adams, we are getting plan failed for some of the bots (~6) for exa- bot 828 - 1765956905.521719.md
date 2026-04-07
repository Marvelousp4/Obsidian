---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Adams"
site: "Adams"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-12-17"
last_updated_date: "2025-12-18"
reporter: "U04580WJL65"
assignee: ""
source_id: "1765956905.521719"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: ["8282"]
components: ["lidar", "rds"]
tags: []
---

# Adams | At Adams, we are getting plan failed for some of the bots (~6) for exa: bot 828...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1765956905.521719
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

At Adams, we are getting plan failed for some of the bots (~6) for exa: bot 8282 here are the logs for that < We tried debugging at our end but didn't find anything, please check it on priority, we need to provide fix before tomorrow's operations

## Progress

From the video, I can see the rear LiDAR mounting of 8282 is abnormal, you should first fix this, this impact the localization Seems issue related to rePlan SEER ticket id: 5179 < We need some more information: 1. Is this issue happen recently? Did you make any change? 2. Is this issue reproducible? Do you know how to trigger this issue? 3. Have you tried restart the rds? Whether this issue can be solved by restart the rds? 1. Yes it happened recently and we didn't make any change. 2. Yes its reproducible, task is going into failed state as soon as we are marking bot as dispatchable, its 100% reproducible in some some specific bots 3. We already restarted RDS Let us know which logs you want Or lets jump on a call, we can reproduce or collect logs again < Replicated Logs When this issue started to occur? 16th December Est 2 days ago? Is there any parameters change made? I don't the issue will suddenly occur without any reason Is all the bots L bot or both L and H bot? As per the site time, no changes were made Only L bots Then it's more wierd Is there a way to download all the configs from RDS? So that we can compare it with the bots that working properly In this case, I doubt the issue should from bots You can arrange a meeting when site team is available I'm available after 7pm IST Okay There are 2 rds running in the same time and connect to the Adam's site robot After cut off the connection of staging rds server, issue solved Ia the issue of task failed also solved?

## Next Action

If you can capture more logs, pls share more logs Any update on this issue? 5 Bots are down at the site

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-12-17
- Last updated: 2025-12-18
- Bot IDs: 8282
- Components: lidar, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

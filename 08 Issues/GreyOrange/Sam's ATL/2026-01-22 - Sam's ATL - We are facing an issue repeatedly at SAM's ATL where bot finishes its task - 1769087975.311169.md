---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Sam's ATL"
site: "Sam's ATL"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P4"
created_date: "2026-01-22"
last_updated_date: "2026-03-10"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1769087975.311169"
bot_ids: []
components: ["rds", "scene file"]
tags: []
---

# Sam's ATL | We are facing an issue repeatedly at SAM's ATL where bot finishes its task...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1769087975.311169
- Site: Sam's ATL
- Vendor / platform context: Wellwit Robotics

## Problem

We are facing an issue repeatedly at SAM's ATL where bot finishes its task successfully at STP but after that it is not getting parking/charging tasks. There is significant delay in automatic tasks getting assigned due to which bot keep waiting at STPs. Logs: < Example for this task, it finished but didn't get assigned any new task for long time: Reference - < FYI

## Progress

From logs, we observed: • The bot correctly marked the previous task complete • No errors or path planning issues were logged. • [CanExecuteNewOrder] was triggering again and again. But its not getting next automatic task. I think it's not a new issue, If I remember correctly, it was there earlier as well. may be we have some configuration to change this behaviour Normal log should have these directory SEER ticket: < < These are new logs, this issue is happening very frequently causing operational issue at the site. Request you to look into this on priority. When analysing RDS core logs for this bot while it was performing the task PA00476125_20262983245: It completed the jackunload task at 03:45:55 EST The bot was sitting idle under STP/AP till 04:06:02. No errors were observed on the bot during this period. Confirmed the issue in the new log. Yangda checked the log today, he suggest to upgrade the rdscore. Because the current version 0.1.9.241113 does't contain enough log, they added log items for auto task and fixed some bug after that version. We have next version as linux-0.1.9.260114. Does this have all the logging? 0.1.9.260114 should contain these features.

## Next Action

There is some issue with this log, there is no scene files in the log. Could you pls check? The missing part contains model file, parameters, scene playback, which are important for debugging, pls try to provide Hi, we are facing this issue repeatedly causing operations to get block. I have shared the logs with you too, please help in debugging this on priority. This is happening daily, so if needed, you can check live also. Updated the SEER ticket and asked them to check the log items added in 0.1.9.241204, and there was an API to check the reason for not take auto task added in 0.1.9.241120 ⁠⁠‬⁠‬⁠⁠‬‬‬⁠⁠Check why the robot is not executing auto tasks - Feishu doc Hi, can you provide the release 0.1.9.241204 specifically as we want to deploy the minimal difference with current production release 0.1.9.241113-dev Also, I want to be sure that dev changes of 0.1.9.241113 is included in 0.1.9.241204 and not missed. Please confirm this.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P4
- Created: 2026-01-22
- Last updated: 2026-03-10
- Bot IDs: 
- Components: rds, scene file

## Related Links

- Account: [[04 Clients/GreyOrange|GreyOrange]]
- Site note: [[05 Projects/GreyOrange/Sam's ATL.md|Sam's ATL]]
- Vendor note: [[04 Clients/Wellwit Robotics|Wellwit Robotics]]

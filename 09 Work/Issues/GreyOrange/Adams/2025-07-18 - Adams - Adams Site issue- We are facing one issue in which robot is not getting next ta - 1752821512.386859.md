---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Adams"
site: "Adams"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P4"
created_date: "2025-07-18"
last_updated_date: "2025-08-21"
reporter: "U046B9XUZRV"
assignee: ""
source_id: "1752821512.386859"
bot_ids: ["8287", "8293"]
components: ["rds", "sto"]
tags: []
---

# Adams | Adams Site issue: We are facing one issue in which robot is not getting next ta...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1752821512.386859
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

Adams Site issue: We are facing one issue in which robot is not getting next task after one picking task. Can you please check this on the logs why this is happening at site. this issue is very frequent and stopping the fleet several time in a day. FYI Robot Id: 8293. Time Stamp: 14:10 EST.

## Progress

we need RDS logs for these issues so lets get the RDS logs with robots logs(for which you get this issue) and time FYI < Please find the logs for rds for 8293 for date 18th July 2025. The same issue was again observed today for bot 8287, please find the logs for same in the same folder. For 8287, there is only robokit log For 8283, when this issue happened? In this folder, there are 2 rds logs, no robokit log. 1. below are the rds and robokit log of 8287. Timestamp id around 12:00pm - 12:30pm est, 21st July 2025. Bot had reached its picking location NA-44. the screen was not updated to start the scan. I recovered this bot by moving the bot a bit back and the screen updated. < 2. below are the logs for bot 8293. timestamp: 13:50pm - 14:10pm est 17th July 2025. Bot reached its picking location. NC 55. It didnt update its screen and still showed approaching location. P.S The logs for 8293 might have additional logs for robokit as i am not sure if the logs uploaded were of correct timestamp. I recently uploaded logs with name 8293_17thJuly_NotGettingTask < has found the issue, it's a bug Said this issue has been fixed, do you need a release for this issue first? are they planning to include something else as well? I mean why we should wait if they fixed it any estimation Ross Ok Ross, we will be updating this issue at site after friday's operations Please help me with the data. #1 #2 the screen not updating after reaching the pick location and the state of bot as running on rds still persist. Above are attached logs for two separate instances found today between 8:15- 8:45am est

## Next Action

Could you provide the time stamp? And what do you mean by "robot is not getting next task after one picking task"? Could you provide some details on this? What was the status of the bot when this issue happened? RUNNING or WAIT? How you solve this issue after you found this? Could you provide rds log, robokit log and timestamp together when this issue happened? OK, found the issues in the log, will ask SEER team to check Any update on this Ok, btw it is causing so many manual interventions, ask Yangda to prioritise it and share asap any update here? It is causing so many interventions They were planning to provide fix for the plan failed issue and pre LM recognize retry together, but it take time, so they will provide fix for this first Hi Next task is getting issue is still persisting. This is issues is quite frequent even after the new build. I am sharing one incident with logs bot id 8287. Please check and let me know how to proceed. Except this issue there are plan failed issue which is also still there i will share respective logs in issue thread. There is one more new issue came with this L bot is detecting Other L bot as Obstacle. FYIP could you share the timestamp or point of the issue? I didn't find the issue in the log as we have target to solve these issues in this week, by keeping customer deadline in mind, please make sure to provide correct data for debugging

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P4
- Created: 2025-07-18
- Last updated: 2025-08-21
- Bot IDs: 8287, 8293
- Components: rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

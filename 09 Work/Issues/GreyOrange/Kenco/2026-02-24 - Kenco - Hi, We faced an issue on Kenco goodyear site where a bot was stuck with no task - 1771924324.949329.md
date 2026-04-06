---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Kenco"
site: "Kenco"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P4"
created_date: "2026-02-24"
last_updated_date: "2026-03-11"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1771924324.949329"
bot_ids: ["8303"]
components: ["charger", "dock", "rds", "sto"]
tags: []
---

# Kenco | Hi, We faced an issue on Kenco goodyear site where a bot was stuck with no task...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1771924324.949329
- Site: Kenco
- Vendor / platform context: Wellwit Robotics

## Problem

Hi, We faced an issue on Kenco goodyear site where a bot was stuck with no task. This caused all the bots onsite to stop and operation was halted. After we made this particular bot as undispatchable, the bot started moving. Please provide root cause analysis for this as we need to ensure this should not re-occur on site. Logs - < Internal Refernce - <

## Progress

Analysis: Our internal analysis found this: ```[260211 155703.776][D][d] [RIL-L-8303][GET|1|Kenco_Case pick_Map_15Dec_2025_V46_1|1|1|70.64]|8|0|0|1|1|0|1|0.520|0|0|new|1|0|0|hot_cannotlock|-1.000][260211 155703.779][D][d] [RIL-L-8303][NoP-C|blockId|r.eid|151|][260211 155703.784][D][d] [RIL-L-8303][OccupyRes|new|1|block:|avoid:(0,0,-1)|path:] ``` and also for the bot with issue, hot_cannotlock: this was appearing in logs again and again the bot was not able to lock the charging point 151. ```NoP-C|blockId|r.eid|151 OccupyRes|new|1|block: ``` which bot got stucked? 8303? What's the issue timestamp? Yes, bot 8303 was near charger without any task. But all bots got stuck. But 8303 is on the charger showing in the log Yes, it was at charging point. But it was neither charging, nor having any task. Then we marked this bot as undispatchable and other bots started moving. The robokit log is not valid, could you get the valid log file? I can see there was an restart of the rds in the log Was that operated by your team? The issue should caused by 8369 was disconnect with rdscore but still dispatchable, and then rdscore got restart, in this case rdscore will stop all the bots Ok I will confirm this. I will update logs as possible but we havent restarted the rds for months: ```ril-kencoprod-prod:~$ sudo docker ps | grep rds 72b7ca52c699 rds:1.0.6 "/bin/bash init.sh" 8 months ago Up 8 months 0.0.0.0:502->502/tcp,:::502->502/tcp, 0.0.0.0:8088->8088/tcp,:::8088->8088/tcp, 0.0.0.0:9301->9301/tcp,:::9301->9301/tcp, 0.0.0.0:19204-19205->19204-19205/tcp,:::19204-19205->19204-19205/tcp, 0.0.0.0:19207-19208->19207-19208/tcp,:::19207-19208->19207-19208/tcp, 0.0.0.0:19210->19210/tcp,:::19210->19210/tcp, 0.0.0.0:19301->19301/tcp,:::19301->19301/tcp, 0.0.0.0:8081->8080/tcp,:::8081->8080/tcp, 0.0.0.0:8093->8090/tcp,:::8093->8090/tcp rds ``` Logs updated on March 2 - < This is a known issue, which the list is overflow and access the invalid memory address. Fixed after 241017

## Next Action

In the log, we can't see the recovery, pls provide more logs after rdscore_2026-02-11_16-09-04.1 were you able to check this?

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P4
- Created: 2026-02-24
- Last updated: 2026-03-11
- Bot IDs: 8303
- Components: charger, dock, rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Kenco.md|Kenco]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

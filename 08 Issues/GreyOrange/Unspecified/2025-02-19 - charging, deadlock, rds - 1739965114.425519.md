---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-02-19"
last_updated_date: "2025-02-28"
reporter: "U06GFL86XUP"
assignee: ""
source_id: "1739965114.425519"
bot_ids: ["8233", "8234", "8235", "8236"]
components: ["rds"]
tags: []
---

# charging, deadlock, rds

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C06TL405CRF_2025-01-01_to_2026-03-16.txt
- Original source id: 1739965114.425519
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

@U04580WJL65 [thread replies:26 latest:2025-02-28T02:15:09]

## Progress

Hi, pls try this version, Mr. Yang said they tested this internally and there is no crash with trigger enabled Ok Ross, I will test. fyi RDS image do we need to enable any parameter?? Or simply upgrade Simply upgrade You can set the RHCR parameter like below, this is what I used for simulation Please find the below link for the RDS logs and bot logs and video for the deadlock scenario at YKK. Link: < Scenario created description: 8235 path nav to LM8270 and then bot 8234 path nav to LM8239 and then release bot 8235 first and then release bot 8234 and then bot 8235 was detecting 8234 as obstacle. Bot 8235 and bot 8234 was going to there respective parking locations. after 1-2 minutes when not resolved, released bot 8236 and also bot 8233 released automatically from charging task and got parking task and the deadlock created by 8235 and 8234 was resolved automatically by bot 8234 going to LM 8268. Video and logs attached for your reference. Even this is breaking very basic things, two bots are in same mutex, and both bots in server control. 📎WhatsApp Image 2025-02-21 at 8.26.26 PM.jpeg U0ALSB28Q0Y/F08EDKSJMUM Please find the logs for the recent 20 minutes deadlock resolution time at YKK site < FYI can u help with this on priority since we golive on monday for ykk any other medium to reach out to ross? There are a lot of issue and a few new ones after rds upgrade Yeah, this bot was blocked by laser but when third bot came in that area, it automally came out from an error and resumed itself, that was unexpected, additionally it was getting laser block because of another bot And we also need the RHCR log which need manually downloaded in below location: please arrange the logs Hi, have you got the robokit log and RHCR log? Got these 2 rhcr's in the mentioned location.. since we have reverted the build, bot logs could not get. bot logs should still there if they are not overwritten, this is important to solve the deadlock issue, could you pls get it? Thanks this is a rds log before upgrade.

## Next Action

please share details of your findings here this happened after we upgraded the rds with above version and parameters.. please check the logs and reply asap. Ykk is going live on monday. Fyi- This is quite different with the simulation, I've asked SEER team to check this In the log we find it was caused by 8234 was blocking by laser. We need robokit log of 8234 for further analysis. Pls provide. Anyway, pls provide the robokit log then we can find something more logs are available in < shared it above just now saw it.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-02-19
- Last updated: 2025-02-28
- Bot IDs: 8233, 8234, 8235, 8236
- Components: rds

## Related Links

- Account: [[04 Clients/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[04 Clients/Wellwit Robotics|Wellwit Robotics]]

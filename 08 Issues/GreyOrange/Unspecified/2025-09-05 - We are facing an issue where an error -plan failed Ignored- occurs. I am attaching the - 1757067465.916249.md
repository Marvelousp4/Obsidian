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
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-09-05"
last_updated_date: "2025-09-22"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1757067465.916249"
bot_ids: []
components: ["rds"]
tags: []
---

# We are facing an issue where an error "plan failed Ignored" occurs. I am attaching the...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1757067465.916249
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

We are facing an issue where an error "plan failed Ignored" occurs. I am attaching the video for reference. In logs, it seems its getting the task for JackLoad but not able to execute it. Also, adding RDS logs for this: Bot - RIL-L-8226 FYI 📎Screen Recording 2025-09-05 at 1.36.03 PM.mov U0ALSB28Q0Y/F09EHJW3HBJ

## Progress

But I found seems the network is not good between core and bots. Ok, let us know the analysis from SEER team. Also, this is from simulation environment, so ideally network issue should not occur right? need your attention Ok Ross, will wait for your response Hi, have you update the robod at this site? There is no rhcr log in the log update latest robod version from here is there any difficulty in providing actual marker location in next_location field with prepoint task, it will help fleet manager to decide better, lets discuss internally if you see any issue in this implementation lets discuss and understand this first in a better way.. Is this issue solved? ? the properties suggested had no impact.. we modified how we create tasks and occurrence of this reduced to negligible with 150 tasks.. Then what modification you have made? We did not user the next_location as we have golive pending and last minute changes like these pose stability concerns Could you pls help to validate this with simulation? Will try to incorporate this change soon Ross

## Next Action

any update on this? I checked the log, but I didn't find the cause. I've raised a ticket to SEER team. Hello, this issue is happening everytime we try to do bulk testing on simulation. This is blocking our stress testing further, so please let us know at the earliest if there is any update from SEER. FYI I discussed with today, he is on leave this 2 days, he will check this issue tomorrow morning after he back to office Could you provide "next_location" filed in the block of prepoint? Like when you send bot to 744, the "next_location" provide 736 The cause is that when you send the bot to pre-LM the fleet manager doesn't know the next dst, so it let other bot move the LM742, then you send the AP block but the bot can not rotate because of blocking by the bot at LM742 We have a concept of zone and subzone which can have multiple points / AP We can send multiple tasks to a subzone - more than the number of points available there - as per our solution needs. When this happens and l lot of bots go in same subzone, rds creates issues.. What we have done is to distribute the bots in the field and reduced the number of bots going to a sub-zone at any given point of time.. this solved the rds issues The "next_location" field didn't work? Do you have the log? I can ask YangDa to check this

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-09-05
- Last updated: 2025-09-22
- Bot IDs: 
- Components: rds

## Related Links

- Account: [[04 Clients/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[04 Clients/Wellwit Robotics|Wellwit Robotics]]

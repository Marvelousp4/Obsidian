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
status: "open"
severity: ""
priority: "P4"
created_date: "2025-08-11"
last_updated_date: "2025-08-21"
reporter: "U046B9XUZRV"
assignee: ""
source_id: "1754917355.028189"
bot_ids: ["8283"]
components: ["rds"]
tags: []
---

# As highlighted in previous thread, with the new build L bot is taking L bot as an obsta...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1754917355.028189
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

As highlighted in previous thread, with the new build L bot is taking L bot as an obstacle. Please find the attached logs for the same. i am sharing two similar incident for this issue. fyi

## Progress

for this we also need rds log Bot 8283 blocking 9027: Google drive link for logs: < 📎WhatsApp Image 2025-08-12 at 13.44.38_ad00c0d9.jpg U0ALSB28Q0Y/F09A7UXD4E7 Please find another instance for same issue For 9027 and 8283, the root cause is 9027 was blocked in the middle of LM220091 and LM3096. And in the same time 8283 has already got the command to LM3095. solution? #2 one more incident for this issue.< #3 One more < the #2 is not bot blocked by bot, it's plan failed #3, both of the 2 bot log is invalid. From the rds log, seems the bot can pass through Similar instances of h bot blocking each other #4

## Next Action

please share the rds logs for this issue would the rds logs be sufficient for now to further debug, i will share the robot losg first thing tomorrow morning est #1 - Bot 8283 blocking 9027: This is happening due to higher footprint of H bot. On curve, the algorithm is deciding the path for H bot which would move onto a curve, but meanwhile L bot comes on a barcode which is just previous to merging of H and L bot. This causes H bot to consider L bot as obstable. Solution - We need to increase obsExpansion from 0.05 to 0.1 on all the curves in smap, so while bot is on the curve, it will be able to take reservation of merging marker as well as the marker which is previous to merging path. #2 - bots are not bot blocked, it's plan failed The reason for plan fail is that someone moved one bot a little bit on pick location. After that, the bot was moved back, however the location is not exact causing the plan fail for the bot. #3 and #4 - Cases of H bot blocking each other. Yangda found the issue that obsExpansion is not getting applied in algorithm. He will provide a fix for this. FYI

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: open
- Severity: 
- Priority: P4
- Created: 2025-08-11
- Last updated: 2025-08-21
- Bot IDs: 8283
- Components: rds

## Related Links

- Account: [[04 Clients/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[04 Clients/Wellwit Robotics|Wellwit Robotics]]

---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Sodimac Colombia"
site: "Sodimac Colombia"
vendor: "Wellwit Robotics"
category: "software_or_firmware"
item_type: "software"
status: "open"
severity: ""
priority: "P4"
created_date: "2026-01-15"
last_updated_date: "2026-01-19"
reporter: "U04580WJL65"
assignee: ""
source_id: "1768510225.528429"
bot_ids: []
components: ["rds"]
tags: []
---

# Sodimac Colombia | need your help to understand one scenario, lets assume a robot is na...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1768510225.528429
- Site: Sodimac Colombia
- Vendor / platform context: Wellwit Robotics

## Problem

need your help to understand one scenario, lets assume a robot is navigating and reserved next 5 markers but got a laser error, then we are expecting it to release the reservation for future markers and we don't know when it will come out from the error. as we are not doing the same so it is causing navigation problem for other bots, please let me know how it can be done

## Progress

This is for GM-264216 For RDS core? Or M4? This is a generic query and we expected this behaviour - bot should release future markers if bot is in error so it doesn't block other bots. This is our expectation for both M4 and RDS. Currently, the behaviour is not such(we observed in sodimac), so how this can be achieved. Sodimac Chile or Columbia? Sodimac Colombia RHCR? Yes

## Next Action

I checked with Yangda, the bot can not release the future markers. It will cause lots of other issues when the bot got recovered from the error For this could give some layout example? Seer team can check whether they can solve in M4

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: open
- Severity: 
- Priority: P4
- Created: 2026-01-15
- Last updated: 2026-01-19
- Bot IDs: 
- Components: rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Sodimac Colombia.md|Sodimac Colombia]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

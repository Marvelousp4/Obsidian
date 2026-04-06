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
status: "open"
severity: ""
priority: "P4"
created_date: "2025-12-10"
last_updated_date: "2025-12-10"
reporter: "U09BMMW53UP"
assignee: ""
source_id: "1765358564.421929"
bot_ids: []
components: ["battery", "rds", "sto"]
tags: []
---

# Kenco | Hello Following up on an issue reported by on Nov 25 We have observed that char...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1765358564.421929
- Site: Kenco
- Vendor / platform context: Wellwit Robotics

## Problem

Hello Following up on an issue reported by on Nov 25 We have observed that charge tasks were not created for some bots at Kenco GoodYear and Kenco Kansas sites Kenco GoodYear: • At Kenco Goodyear, the case pick bots were dead with 0% battery. • On the RDS, we can see that no charge tasks were assigned to the bots between 2025-09-28 08:00:00 and 2025-09-28 18:00:00 IST. See screenshots 1,2,3 for reference • There is a single charge task (CPdc6325d1-d968-4efc-b76f-64dd335a860f) which was created at 2025-09-28 08:01:20 and got terminated at 2025-09-28 20:28:12. • RDS logs for your reference - < Kenco Kansas: • Customer reported that 5 bots ran out of battery in Kenco Kansas on 24th oct. • After following up with customer they were unable to tell us the bot IDs. • After further investigation we found out there were no charge task created in RDS between 2025-10-24 17:20:57 and 2025-10-24 23:15:56. See screenshot 4 for reference • We suspect this to be reason for bots to be dead. • RDS logs for the mentioned time-stamp: < We require a root cause explanation and a fix for this issue 📎image (4).png U0ALSB28Q0Y/F0A27U33ETZ 📎image (5).png U0ALSB28Q0Y/F0A2SUU903E 📎Screenshot 2025-09-29 at 02.08.19.png U0ALSB28Q0Y/F0A2SUVLNN8 📎Screenshot 2025-10-31 at 00.50.07.png U0ALSB28Q0Y/F0A2PBXTVS6

## Progress

No progress note captured in the cleaned source.

## Next Action

No explicit next action found in the cleaned source.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: open
- Severity: 
- Priority: P4
- Created: 2025-12-10
- Last updated: 2025-12-10
- Bot IDs: 
- Components: battery, rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Kenco.md|Kenco]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Kenco"
site: "Kenco"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "open"
severity: "SEV2"
priority: "P2"
created_date: "2025-11-10"
last_updated_date: "2025-12-04"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1762753373.554349"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["battery", "rds", "sto"]
tags: []
---

# Kenco | Hello, At Kenco Goodyear, the case pick bots were dead with 0% battery. On the...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1762753373.554349
- Site: Kenco
- Vendor / platform context: Wellwit Robotics

## Problem

Hello, At Kenco Goodyear, the case pick bots were dead with 0% battery. On the RDS, we can see that no charge tasks were assigned to the bots between 2025-09-28 08:00:00 and 2025-09-28 18:00:00 IST. (Screenshot attached). There is a single charge task (CPdc6325d1-d968-4efc-b76f-64dd335a860f) which was created at 2025-09-28 08:01:20 and got terminated at 2025-09-28 20:28:12. However, no other charge tasks were created in this interval. RDS Logs - < Internal Reference - < FYI 📎Screenshot 2025-09-29 at 02.08.19.png U0ALSB28Q0Y/F09S8GMSQG1

## Progress

We are facing this issue on other sites also where bots are not getting charge tasks and causing complete site down. Please look into this urgently. Similar issue for Kenco-kansas: • Customer reported that 5 bots ran out of battery in Kenco Kansas on 24th oct. • After following up with customer they were unable to tell us the bot IDs. • After further investigation we found out there were no charge task created in RDS between 2025-10-24 17:20:57 and 2025-10-24 23:15:56. < I don't have access to the Google drive, I've sent the request I didn't get the issue. From the log, I can see charging during the period you mentioned There are only 2 bots not get charge in this period, I think was caused by allways in the task. let us discuss here, ross already had the feedback can you point it out that which task were assigned to that bot at that point of time

## Next Action

Were you able to check this? FYI Can you please check the first case(kenco goodyear), i have shared those - < Meanwhile I will share the second logs(kenco kansas) Please check now, i have shared the logs.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: open
- Severity: SEV2
- Priority: P2
- Created: 2025-11-10
- Last updated: 2025-12-04
- Bot IDs: 
- Components: battery, rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Kenco.md|Kenco]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

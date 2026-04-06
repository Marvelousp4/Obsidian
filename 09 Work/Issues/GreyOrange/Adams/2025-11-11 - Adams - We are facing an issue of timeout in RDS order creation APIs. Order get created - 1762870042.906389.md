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
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-11-11"
last_updated_date: "2025-12-03"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1762870042.906389"
bot_ids: []
components: ["pallet", "rds", "socket"]
tags: []
---

# Adams | We are facing an issue of timeout in RDS order creation APIs. Order get created...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1762870042.906389
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

We are facing an issue of timeout in RDS order creation APIs. Order get created successfully, however, application never receives the "ok" response and timeout happens. This result in retrying of order creation in application side, but then application gets error of "order id already exist". I have checked the rds logs and it seems that we are not receiving the response from rds during that time. Can you please help in this as this is happening at multiple sites - Adams, Sodimac. internal reference - < Attaching Adam sites logs: < Fyi

## Progress

I am seeing this: 1. setOrder in rds logs but no HTTPLOG reponse ```[251015 175542.072][0x00007f81a0fe9700][RDSOrderAdapter][info] setOrder: {"complete":false,"id":"7a0dba98-7cf5-48ef-b02c-867ef2210b46","label":"PICK_L","priority":7,"blocks":[{"blockId":"a4e32cd4-42ed-421a-b929-def4673a5f82","location":"AP3121","operation":"JackLoad","operationArgs":{"rec_dir":0,"rec_target_obs":true,"recfile":"palletobject/QTEK.palletobject","recognize":true},"postAction":"< 2. Timeout in rdscore: ```2025-10-15 17:55:41.001 [Thread-5] ERROR com.seer.rds.runnable.RobotsStatusRunnable.run(172) - RobotsStatusRunnable error Java.net.SocketTimeoutException: timeout```

## Next Action

Can you please update on this?

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-11-11
- Last updated: 2025-12-03
- Bot IDs: 
- Components: pallet, rds, socket

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

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
created_date: "2025-08-21"
last_updated_date: "2025-08-21"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1755756489.782289"
bot_ids: ["9005", "9006"]
components: ["rds"]
tags: []
---

# We are facing an issue where task gets auto-terminated but no error is shown on rds web...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1755756489.782289
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

We are facing an issue where task gets auto-terminated but no error is shown on rds web_ui. Need to understand the reason behind such cases. Order id: ROLL_42_2025815175456 FYI 📎Screenshot 2025-08-21 at 2.07.15 PM.png U0ALSB28Q0Y/F09BRCAF2PK 📎Screenshot 2025-08-21 at 2.07.06 PM.png U0ALSB28Q0Y/F09B7252VGB

## Progress

It was found that the terminate is happening due to API call from RDS web_ui or service. ```[250815 135546.813][Robot][d] [RIL-H-9006][InternalMsgTime|0|1|1] [250815 135546.840][Order][d] [terminate][172.22.156.134:36657|172.22.156.137:8088|keep-alive||100|140531019392768|fc26281b-3918-410d-97c4-4a8528fd8942] [250815 135546.840][Robot][d] [RIL-H-9005][networkDelay|518|500] [250815 135546.840][Order][i] terminate: {"id":"ROLL_42_2025815175456","disableVehicle":false} [250815 135546.840][Order][d] [Service][setOrderList|RDSDispatcher|(call from C++)]``` To know exact calling service, we should add this in our services to confirm which service called the terminate function whether its rds ui or internal or greyorange service api. ```Add User-Agent in request header for all RDS Apis so rds-core can log this data from where a request came. This might help in debugging auto-termination of tasks.``` FYI Reference - < lets add User-Agent header with value as "il_server" for all the api calls to fleet manager Yes they have values for roboshop and their web UI, we should set it in rds_interface

## Next Action

Do we have this User-Agent for UI or roboshop ? At GM layer, we are aware if we send it though..

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: open
- Severity: 
- Priority: P4
- Created: 2025-08-21
- Last updated: 2025-08-21
- Bot IDs: 9005, 9006
- Components: rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

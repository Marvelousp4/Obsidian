---
type: issue
account: "GreyOrange"
project: ""
site: "Dorman Warsaw"
vendor: "Wellwit"
status: "in_progress"
severity: ""
priority: "P2"
category: "Hardware"
item_type: "weekly_site_tracker"
created_date: "2026-03-16"
last_updated_date: "2026-04-07"
reporter: "GreyOrange"
assignee: "Wellwit"
bot_ids: []
components: []
source_type: "weekly_site_issue_tracker"
source_id: "weekly_tracker_08"
source_file: "07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv"
gor_status: "Closed"
supplier_status: "RCA awaited"
jira_ticket: "RPE-28020"
due_date: "2026-03-24"
product: "RU-L"
department: "Hardware Support"
impact: "Bot Uptime"
tags:
  - work
  - issue
  - greyorange
  - weekly-tracker
---

# Dorman Warsaw | 3D Camera

## Source Context

- Imported from: [[07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv]]
- Source row: 8
- Department: Hardware Support
- Product: RU-L
- JIRA / source ticket: RPE-28020
- GOR status: Closed
- Supplier status: RCA awaited

## Issue Summary

Livox disconnection Bot 8316|| Dorman Warsaw

## Findings / How

Bot 8316 is experiencing frequent disconnections from Livox camera. The power and data connections were inspected thoroughly, and no issues were found with the wiring or connectors. Based on the checks performed, the disconnections appear to be related to the Livox LiDAR unit itself.  We dixed the new Livox but that is also giving same error.

## Next Action

The issue has been resolved after performing the following steps by replacing and reconfiguring the 3D Livox camera:
1. Replaced the faulty 3D Livox camera with a new unit.
2. Connected the Livox camera to a PC using a LAN cable and configured the laptop with a static IP in the range of 192.168.192.XXX.
3. Opened Livox Viewer and performed an IP reset to restore the camera to factory default settings.
4. After resetting the IP, followed the standard SOP to complete the configuration.
The bot is now functioning as expected

Next Steps: Olivia /QA will check the configuration before shipping it to Site

## Owner / Due

- Owner: Wellwit
- Due: Mar 24, 2026

## Related Context

- Site: Dorman Warsaw
- Similar issue at other site: 
- Picture: 

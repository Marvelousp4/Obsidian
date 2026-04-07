---
type: issue
account: "GreyOrange"
project: ""
site: "Dorman Warsaw"
vendor: "Wellwit"
status: "in_progress"
severity: ""
priority: "P1"
category: "Hardware"
item_type: "weekly_site_tracker"
created_date: "2026-01-22"
last_updated_date: "2026-04-07"
reporter: "GreyOrange"
assignee: "Wellwit"
bot_ids: []
components: []
source_type: "weekly_site_issue_tracker"
source_id: "weekly_tracker_21"
source_file: "07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv"
gor_status: "Open"
supplier_status: "RCA awaited"
jira_ticket: "ILH-1069"
due_date: "2026-01-29"
product: "RU-L"
department: "Hardware Support"
impact: "Bot Uptime"
tags:
  - work
  - issue
  - greyorange
  - weekly-tracker
---

# Dorman Warsaw | SRC Controller

## Source Context

- Imported from: [[07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv]]
- Source row: 21
- Department: Hardware Support
- Product: RU-L
- JIRA / source ticket: ILH-1069
- GOR status: Open
- Supplier status: RCA awaited

## Issue Summary

Bot 8266 unable to view its parameters. Additionally, the bot name was automatically changed to AMB-01 without any manual intervention. (Parameter override)

## Findings / How

Root Cause: Sudden power loss during contactor burn led to filesystem corruption.

## Next Action

RIL-8266 – Filesystem Corruption
Action Taken: Ran FSCK check, unmounted and remounted the filesystem, and deleted corrupted log files.

RIL-8266 – RDK Software Failure
Action Taken: The issue was automatically recovered after filesystem repair followed by a robot restart.
Root Cause: Directly linked to the filesystem corruption.

RIL-8266 – Emergency Stop Circuit (DI0/DI1 Mismatch)
Action Taken: Identified and fixed a loose connection at the emergency stop button contact.

This issue happened again and the system files were re-uploaded to resolve the issue

## Owner / Due

- Owner: Wellwit
- Due: Jan 29, 2026

## Related Context

- Site: Dorman Warsaw
- Similar issue at other site: 
- Picture: 

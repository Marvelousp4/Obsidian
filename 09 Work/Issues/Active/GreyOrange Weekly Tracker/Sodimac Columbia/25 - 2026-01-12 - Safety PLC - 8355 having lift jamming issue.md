---
type: issue
account: "GreyOrange"
project: ""
site: "Sodimac Columbia"
vendor: "Wellwit"
status: "in_progress"
severity: ""
priority: "P1"
category: "Hardware"
item_type: "weekly_site_tracker"
created_date: "2026-01-12"
last_updated_date: "2026-04-07"
reporter: "GreyOrange"
assignee: "GreyOrange, Sistemo"
bot_ids: []
components: []
source_type: "weekly_site_issue_tracker"
source_id: "weekly_tracker_25"
source_file: "07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv"
gor_status: "In Progress"
supplier_status: "Open"
jira_ticket: "ILH-1065"
due_date: "2026-01-22"
product: "RU-L"
department: "Hardware Support"
impact: "Bot Uptime"
tags:
  - work
  - issue
  - greyorange
  - weekly-tracker
---

# Sodimac Columbia | Safety PLC

## Source Context

- Imported from: [[07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv]]
- Source row: 25
- Department: Hardware Support
- Product: RU-L
- JIRA / source ticket: ILH-1065
- GOR status: In Progress
- Supplier status: Open

## Issue Summary

8355 having lift jamming issue

## Findings / How

Bot 8355 Lift motor encountered abnormal mechanical resistance during operation, leading to motor abnormal protection.We think that As a safety response, STO was triggered, followed by a CW limit activation

## Next Action

The issue is not yet resolved. on the debugging call ,We were able to identify the root cause of the EMC trigger issue:Flexibus communication error detected in safety PLC diagnostics.

## Owner / Due

- Owner: GreyOrange, Sistemo
- Due: Jan 22, 2026

## Related Context

- Site: Sodimac Columbia
- Similar issue at other site: 
- Picture: 

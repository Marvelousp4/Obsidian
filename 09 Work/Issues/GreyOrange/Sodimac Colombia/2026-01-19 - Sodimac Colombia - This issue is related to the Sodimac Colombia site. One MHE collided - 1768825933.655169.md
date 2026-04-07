---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Sodimac Colombia"
site: "Sodimac Colombia"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P4"
created_date: "2026-01-19"
last_updated_date: "2026-04-07"
reporter: "U046B9XUZRV"
assignee: ""
source_id: "1768825933.655169"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: ["8355"]
components: ["activation", "lidar", "lift", "motor", "sto"]
tags: []
---

# Sodimac Colombia | This issue is related to the Sodimac Colombia site. One MHE collided...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C0602U5PLMS_2026.txt
- Original source id: 1768825933.655169
- Site: Sodimac Colombia
- Vendor / platform context: Wellwit Robotics

## Problem

This issue is related to the Sodimac Colombia site. One MHE collided with a robot and damaged its LiDAR. Although the site team has replaced the LiDAR, the issue still persists and the robot is throwing random errors. Logs and images related to the incident are shared below. As per initial analysis, Bot 8355 Lift motor encountered abnormal mechanical resistance during operation, leading to motor abnormal protection. We think that As a safety response, STO was triggered, followed by a CW limit activation. The issue is likely caused by mechanical obstruction, lift jamming. Please help us understand the root cause and resolve the issue. FYI

## Progress

Hi, please help to have a look this Stall indicates overload; safety torque disable means STO is triggered; forward rotation prohibition suggests upper limit trigger or loose wiring of prohibition harness. It is recommended to troubleshoot from these three aspects.

## Next Action

Have you checked this?? Please update on this. please update. i checked with my team, the error shows 0x20000000: Motor Stall 0x00020000: Safety Torque Disable 0x00000004: Forward Rotation Limit Prohibition

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P4
- Created: 2026-01-19
- Last updated: 2026-01-29
- Bot IDs: 8355
- Components: activation, lidar, lift, motor, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Sodimac Colombia.md|Sodimac Colombia]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

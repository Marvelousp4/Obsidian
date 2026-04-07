---
type: issue
account: "GreyOrange"
project: ""
site: "Sodimac Columbia"
vendor: "Wellwit"
status: "open"
severity: ""
priority: "P1"
category: "Software"
item_type: "weekly_site_tracker"
created_date: "2026-03-24"
last_updated_date: "2026-04-07"
reporter: "GreyOrange"
assignee: "Wellwit"
bot_ids: []
components: []
source_type: "weekly_site_issue_tracker"
source_id: "weekly_tracker_05"
source_file: "07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv"
gor_status: "Open"
supplier_status: "Open"
jira_ticket: "ILH-1138"
due_date: ""
product: "RU-L"
department: "Supplier Quality, Engineering"
impact: "Site Operation"
tags:
  - work
  - issue
  - greyorange
  - weekly-tracker
---

# Sodimac Columbia | Wheel Encoder

## Source Context

- Imported from: [[07 Resources/Work/Wellwit Weekly Discussion Points - Site issues Tracker_Wellwit.csv]]
- Source row: 5
- Department: Supplier Quality, Engineering
- Product: RU-L
- JIRA / source ticket: ILH-1138
- GOR status: Open
- Supplier status: Open

## Issue Summary

Safety Encoder Disable & Configuration Alignment || Sodimac FLR ||

## Findings / How

Driver Diagnostics: LUNA software shows Error E003 (Driver Overvoltage), suggesting a possible conflict between the regenerative braking and the safety encoder's deceleration logic.

Isolation Attempt: Physically disconnected the safety encoder wire; however, the SRC logic continues to trigger a safety lockout, indicating the check is embedded in the software parameters.

Parameter:
1. Skid Detection:  RobotPosEKF.StartSkidDetection set to True
2. Encoder Expansion: DSPChassis.EncoderMaxDiffExpansionCoeff set to 5
3.Control Timing: MoveFactory.ControlTime has been reduced from 0.06s to 0.03s

## Next Action

Provide the authorized method to disable the Safe Encoder check within the newer firmware (Ver 0.1.0.1) logic.

Confirm if changing RobotPosEKF.StartSkidDetection to False is sufficient for this bot generation or if additional DSPChassis parameters must be modified to prevent E003 overvoltage errors during safety stops.

## Owner / Due

- Owner: Wellwit
- Due: 

## Related Context

- Site: Sodimac Columbia
- Similar issue at other site: 
- Picture: 

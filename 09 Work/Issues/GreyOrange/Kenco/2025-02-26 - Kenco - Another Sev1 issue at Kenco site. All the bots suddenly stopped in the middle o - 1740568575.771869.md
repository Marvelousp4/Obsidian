---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Kenco"
site: "Kenco"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "blocked"
severity: "SEV1"
priority: "P1"
created_date: "2025-02-26"
last_updated_date: "2025-03-07"
reporter: "U046W74R38V"
assignee: ""
source_id: "1740568575.771869"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["rds", "sto"]
tags: []
---

# Kenco | Another Sev1 issue at Kenco site. All the bots suddenly stopped in the middle o...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C06TL405CRF_2025-01-01_to_2026-03-16.txt
- Original source id: 1740568575.771869
- Site: Kenco
- Vendor / platform context: Wellwit Robotics

## Problem

Another Sev1 issue at Kenco site. All the bots suddenly stopped in the middle of operation. Site support team marked the bots undispatchable and then dispatchable after which bots started moving again. RDS logs are attached. FYI

## Progress

generally this happens when one of the bot gets disconnected from network.. It is visible in RDS UI and also in RIL MD for better debugging. If you only make that bot undispatchable, others would start automatically. Hope that this was not the case here and someone did that basic debugging onsite as confirmed this was not the case This was the status of Robots tab during the 2nd occurence yaha pe shayad dispatchable hi dikhta hai.. but if you hover over the dispatchable, then probably you will see 4-5 things.. network disconnect wil be one of them. But again.. this is merely a possibility which is generally seen.. this could be diff. please find the logs attached FYI: - FYI As discussed, Please Discuss with & update here on this issue. Ross is on a plane to America. He'll get back to you when he gets off the plane by tomorrow Pls find the attached logs. There is no robokit log in the zip file, I think the log has been overwritten.

## Next Action

By any chance were you able to check the logs on why the whole fleet went down ?? Hi I've already raised a ticket to SEER team, they are checking it We checked the log, found that rds send command to bots, but bots not execute. We need bots log for analysis, pls provide log for below bots. Can you please get these logs as requestd by and share here. any update on this thread?? We have now breached the SLA with our customer for the RCA of this issue and this is being asked at leadership level. Please help get this prioritised and share the RCA ASAP. FYI- We need log for 8308, could you provide it can you please coordinate with to provide these logs today ? Please try to share the analysis, on why all the bots stopped working simultaneously, asap. Request you to pls prioritise this.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: SEV1
- Priority: P1
- Created: 2025-02-26
- Last updated: 2025-03-07
- Bot IDs: 
- Components: rds, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Kenco.md|Kenco]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

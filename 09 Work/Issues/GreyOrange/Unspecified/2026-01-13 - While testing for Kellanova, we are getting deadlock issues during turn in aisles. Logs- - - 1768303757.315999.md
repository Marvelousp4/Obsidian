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
status: "in_progress"
severity: ""
priority: "P4"
created_date: "2026-01-13"
last_updated_date: "2026-03-10"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1768303757.315999"
bot_ids: []
components: ["rds"]
tags: []
---

# While testing for Kellanova, we are getting deadlock issues during turn in aisles. Logs: <

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1768303757.315999
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

While testing for Kellanova, we are getting deadlock issues during turn in aisles. Logs: < Internal Reference: < Can you please help in debugging this. 📎bandicam 2026-01-07 21-17-24-366.mp4 U0ALSB28Q0Y/F0A8SRHBRA5

## Progress

I am thinking that this might be due to expansion length parameter, can you check and confirm if this might resolve the issue if I set this to 1: RHCRExpansionLength RHCRExpansionWidth 1 mean 1 meter, I think that is too much I meant 0.1 as currently RHCRExpansionLength is 0.05 so I thought to increase this to 0.1 Or please suggest if some other cause is there, then we can do accordingly. > Please approve my permission request. I am currently unable to download the logs without the required access rights. > Please set the RDS parameter RHCRfixedpriority to 0 and change RHCRDetourLength to 20. In the log I can't see the deadlock In the logs we can observe the deadlock at 12:50. The Onsite team has applied manual intervention as well for the robot RIL-AP-7005. this is causing a lot of manual interventions onsite, so would need suggestions on this.

## Next Action

Pls check the log and raise ticket to SEER I have shared with you now. We are still facing similar deadlock issues on site. Can you provide suggestions on how we can resolve this? <

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: in_progress
- Severity: 
- Priority: P4
- Created: 2026-01-13
- Last updated: 2026-03-10
- Bot IDs: 
- Components: rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: "Kenco"
site: "Kenco"
vendor: "Wellwit Robotics"
category: "software_or_firmware"
item_type: "software"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-12-02"
last_updated_date: "2026-02-03"
reporter: "U046XLG7D36"
assignee: ""
source_id: "1764673997.127979"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["rds"]
tags: []
---

# Kenco | We have encountered an issue in Kenco Kansas, where some tasks were terminated...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1764673997.127979
- Site: Kenco
- Vendor / platform context: Wellwit Robotics

## Problem

We have encountered an issue in Kenco Kansas, where some tasks were terminated on RDS due to error: 'Cannot find path to new block target [AP831565]' • Tasks that got terminated due to this reason are: ◦ 3e3e07e0-8c13-4345-8eeb-0696335034a8 ◦ 7cd44b68-1aab-4c1e-b844-61b3fe4e3933 I checked logs and I can see the error - ```[251121 174520.892][D][d] [RIL-L-8327][locations2check|AP831565:0|] [251121 174520.897][R][d] [{}AstarFail{}][328-831550:831650,327,336,``` However, this path is present in map and also no one changed or updated the map. I saw from robocare that path is there in the map when bot is executing the block. Could you please help us find the root cause of this termination? internal-reference - AE-1883

## Progress

FYI Logs - < Hello, did we get any inputs to commit SEER ticket: < reference for < Seer team suggest to upgrade the rdscore to the new version, and increase the pathPropertyDeviation value to 0.5 in model file. If there is no pathPropertyDeviation value after update, pls pull first when you are saying upgrade to new version, which means version 0.2.0 ? (RDS ) 0.1.9.250708, which I've uploaded in this thread

## Next Action

Any update on this? FYI Ok, can you please share the root cause and the fix in this release. Current running version on this site is 0.1.9.241113 - NO RHCR (so I am assuming that new version will not have any issue) Can you please confirm on this? We need to provide RCA to client as this is pending from long. Can you help in this. Thanks Can you please check this. for < ok, then lets provide release notes, we need to know what change you make. as these are production sites and we are not confident on the changes seer deliver, as their changes broke multiple times in the past so how you are making sure that it will not break. Hi, this becomes confusing currently. We are also trying to resolve one earlier issue for which release linux-0.1.9.250814-0.1.9.zip was provided(for an earlier mutex region deadlock issue). Now, we have linux-0.1.9.250708-0.1.9.zip for this new fix(for auto task termination issue). Without some release notes or reference, its hard to decide and track the releases and which to deploy.

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-12-02
- Last updated: 2026-02-03
- Bot IDs: 
- Components: rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Kenco.md|Kenco]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

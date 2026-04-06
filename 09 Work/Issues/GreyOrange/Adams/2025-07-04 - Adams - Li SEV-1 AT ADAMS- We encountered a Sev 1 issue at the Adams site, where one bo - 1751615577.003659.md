---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Adams"
site: "Adams"
vendor: "Wellwit Robotics"
category: "software_or_firmware"
item_type: "software"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-07-04"
last_updated_date: "2025-07-04"
reporter: "U046B9XUZRV"
assignee: ""
source_id: "1751615577.003659"
bot_ids: ["8294"]
components: ["rds"]
tags: []
---

# Adams | Li SEV-1 AT ADAMS: We encountered a Sev 1 issue at the Adams site, where one bo...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1751615577.003659
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

Li SEV-1 AT ADAMS: We encountered a Sev 1 issue at the Adams site, where one bot 8294 remained idle at the waiting point, and its status was showing as "Running". This resulted in nearly 15 bots getting queued behind it, creating severe congestion and halting operations for almost 2 hours. All the bots stuck behind reported “Plan Failed” errors in RDS during this period. The RDS logs and video related to this incident are attached here for your analysis. < Can you please help us identify the root cause? We would like to know: 1. Was this issue related to the same “Plan Failed” bug for which you are releasing a new build today? 2. Or is this a different issue that we need to investigate and address separately? We’re concerned that if this is different, we may need to prioritize it and look for a different resolution. FYI

## Progress

Time stamp is from 3-4 pm est OK From the log, we can see 8294 was moved to LM10611 manually In this case, operator should confirm the state in roboshop, if block not finished, then press manual complete

## Next Action

Pls share the timestamp of the issue, the log is 1.8GB, it will take long time to locate the issue

## Metadata

- Category: software_or_firmware
- Item type: software
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-07-04
- Last updated: 2025-07-04
- Bot IDs: 8294
- Components: rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

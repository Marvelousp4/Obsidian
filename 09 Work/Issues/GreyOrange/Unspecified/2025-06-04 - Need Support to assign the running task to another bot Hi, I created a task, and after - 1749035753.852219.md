---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "blocked"
severity: ""
priority: "P2"
created_date: "2025-06-04"
last_updated_date: "2025-06-05"
reporter: "U04D80T8GJF"
assignee: ""
source_id: "1749035753.852219"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["lift", "pallet", "rds"]
tags: []
---

# Need Support to assign the running task to another bot Hi, I created a task, and after...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C06TL405CRF_2025-01-01_to_2026-03-16.txt
- Original source id: 1749035753.852219
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

Need Support to assign the running task to another bot Hi, I created a task, and after the bot started running for the JackLoad task, a hardware issue occurred with the bot. Therefore, I want to assign that task to a different bot. I tried this < curl --location '< \ --header 'Content-Type: application/json' \ --data '{"vehicle":"RIL-L-8233"}' RIL-L-8233 was the bot having order, got hardware issue also tried with task external id, but somehow this api seems not working. could you suggest how can i assign Running task to different bot. core version:0.1.9.240705 Thanks FYI

## Progress

curl --location '< \ --header 'Content-Type: application/json' \ --data '{ "problemVehicle": "RIL-L-8233" }' we want a new and different bot to be assigned to the existing order. example scenario- 1. Order sequence is created on RDS 2. Blocks are added. 3. Bot 1 is assigned to this order sequence. 4. Bot 1 started to move to lift the pallet. 5. Bot 1 went in hardware failure. 6. Now we want this order sequence to be picked up by other available bot (ex- Bot 2) 7. Bot 2 comes and lifts the pallet and continues with the task. Will the above payload and api do this ??? The system will automatically: ◦ Terminate the current task. ◦ Generate new tasks and assign them to other robots. ◦ Disable RIL-L- 8233 What will be the order sequence id for that new task ? The task ID will be new and different from the ID of the task Bot 1 was attempting In that case, how will we know what is the new task id that you have created? Is there any way you delete the existing task and create a new task with the same id, because we use that ID for goving new blocks to that order sequence. Without which we would not be able to give new block information. I used the above api to terminate a task: curl --location '< --header 'Content-Type: application/json' --data '{"problemVehicle":"RIL-L-8217"}' The task got terminated and bot went into Undispatchable and Online status. But a new order was never created. Can you tell me is there any issue with this??

## Next Action

Can you share any example payload for this: < any update on this?? What will be the new order sequence id for the new order.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: blocked
- Severity: 
- Priority: P2
- Created: 2025-06-04
- Last updated: 2025-06-05
- Bot IDs: 
- Components: lift, pallet, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

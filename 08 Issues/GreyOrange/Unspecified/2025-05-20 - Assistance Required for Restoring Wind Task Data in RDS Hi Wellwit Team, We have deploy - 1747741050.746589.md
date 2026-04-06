---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "open"
severity: "SEV2"
priority: "P2"
created_date: "2025-05-20"
last_updated_date: "2025-06-05"
reporter: "U044YH122LA"
assignee: ""
source_id: "1747741050.746589"
bot_ids: []
components: ["dock", "rds", "sto"]
tags: []
---

# Assistance Required for Restoring Wind Task Data in RDS Hi Wellwit Team, We have deploy...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C06TL405CRF_2025-01-01_to_2026-03-16.txt
- Original source id: 1747741050.746589
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

Assistance Required for Restoring Wind Task Data in RDS Hi Wellwit Team, We have deployed a new version of RDS at one of the Dorman sites, which included an update to the MariaDB folder structure. As a result, the Wind task data is currently unavailable in the RDS. Could you please assist us in recovering all the data from the backup folder and consolidating both the previous and current data into a single path? FYI

## Progress

What update you did? Only rdscore or RDS Frontend and Backend? Or both? From which version to which version? team please help us get the data.. Dorman team is urgently looking for this. I saw there are wind tasks there I think customer already created them manually lets export wind tasks from rds UI and take a backup for that at confluence Customer has raised a specific query to fetch all the wind task for the following time slots: 5/16/2025 5am CST - 5/17/2025 5am CST 5/17/2025 5am CST - 5/18/2025 5am CST 5/18/2025 5am CST - 5/19/2025 5am CST Hi customer is still looking for this specific data on the RDS UI, Please help here to get the data and solve customer's ask. Please help get this historic data for Dorman ASAP. Let us know what would you need and we can get that from the servers. Hi this is a follow up reminder, Please help here to get the data of the wind tasks and solve customer's ask asap. What do you mean by wind task? and I together saw the wind task is already there, you are talking about wind task executed record? They create different wind task everyday? yes Customer is asking about the wind task execution record data for the following time slots: 5/16/2025 5am CST - 5/17/2025 5am CST 5/17/2025 5am CST - 5/18/2025 5am CST 5/18/2025 5am CST - 5/19/2025 5am CST after creation of new wind task customer is getting Abnormal InterruptionRetry due to below error. [CSelectAgvBp]Block Run Failure:[Error: could not access: b1; in class: java.util.concurrent.ConcurrentHashMap] [Near: {... blocks.b1.selectedAgvId....}] ^ [Line: 1, Column: 8] 📎Task Records.xls U0ALSB28Q0Y/F08V1057KPT Pls help here 📎Task Records (2).task U0ALSB28Q0Y/F08V5QKEQP4 AGV ID Reference Errors: Sub-operations in the second AGV selection block (b4) incorrectly reference the AGV from the first block (b1), making b4's AGV selection ineffective. Operational Redundancy: Due to the AGV ID error, both AGV selection branches often perform identical tasks using the same AGV, despite differing priorities. Could you help us recover the task record data for that specific point in time, along with the previous WIND tasks? It appears that the new tasks created by the customer are encountering this issue, which is preventing the flow from running. recover from where? can we connect I can explain you better over the call? yes < So breaking into smaller chunk zips here is the MariaDB folder from the backup data: if we have logs in those files, then we can delete those log files no that step is already been care, Volume is too big with logs while extracting data into zip I can see maps and all files from bots. But not able to find it's location in the folder structure! 28GB Jun 3 12:54 UTC volume_dorman_bkp.zip how about try to use `find. -name ".task"` are these wind tasks can you please confirm? yes and how about the extraction of the wind task execution record data for the following time slots: 1. 5/16/2025 5am CST - 5/17/2025 5am CST 2. 5/17/2025 5am CST - 5/18/2025 5am CST 3. 5/18/2025 5am CST - 5/19/2025 5am CST can you please help me out to find this asked data from that backed up folder? Normally what is the format of record? Maybe you can also use the find command

## Next Action

Can you guys check this please.. This is for Dorman portland wait amoment, let me check internally any updates ? Hi Following the recent RDS upgrade (both core and front/backend) at the Dorman Portland site, we encountered an issue where the UI failed to display any data. Due to time constraints within the deployment window, we backed up the `rds-docker` folder and proceeded with a fresh RDS setup. The customer has now requested access to the Wind task data on the newly deployed UI, which is currently stored in the backup folder from the previous setup. Could you please assist in retrieving the data from the backup folder and integrating it into the new setup, so both historical and new data are visible in the RDS UI? Current RDS Versions: • Frontend: F-1.9.54 • Backend: B-1.8.4 • Core: 0.1.9.241113-dev We’re happy to jump on a quick call if needed to clarify any details. Appreciate your support in helping us complete this activity as soon as possible. FYI Hi please check and let me know if you need more information from our end. FYI hi, or any updates any help you need here we can connect and close this! Can you send me the wind task detail? It seems the b1 block has issue please join here as discussed over the call you want RDS-docker backed up files in zip format but it's too big ~30GB unable to copy and share it here from the Production VM

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: open
- Severity: SEV2
- Priority: P2
- Created: 2025-05-20
- Last updated: 2025-06-05
- Bot IDs: 
- Components: dock, rds, sto

## Related Links

- Account: [[04 Clients/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[04 Clients/Wellwit Robotics|Wellwit Robotics]]

---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "resolved"
severity: ""
priority: "P2"
created_date: "2025-05-08"
last_updated_date: "2026-04-07"
reporter: "U04580WJL65"
assignee: ""
source_id: "1746732929.525759"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["dock", "rds"]
tags: []
---

# Priority not working on orders, robots are still following FCFS order 📎Screenshot 2025-...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1746732929.525759
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

Priority not working on orders, robots are still following FCFS order 📎Screenshot 2025-05-09 at 12.45.26 AM.png U0ALSB28Q0Y/F08R46Q69V5 📎Screenshot 2025-05-09 at 12.44.44 AM.png U0ALSB28Q0Y/F08RN0FQTQC 📎Screenshot 2025-05-09 at 12.44.29 AM.png U0ALSB28Q0Y/F08RG99G1HB

## Progress

All orders received in log period have same priority. Is this log time wrong? In this snapshot you can see, we have tasks with higher priority but stil robots are executing low priority tasks 📎Screenshot 2025-05-09 at 12.44.44 AM.png U0ALSB28Q0Y/F08RE5GPPGE 📎Screenshot 2025-05-09 at 12.44.29 AM.png U0ALSB28Q0Y/F08S8MRCFCY Let me know if you need more information, we can jump on the call to get more information(logs or anything else) from the site Please download logs around this time: all the H robot has order to do at that time. capturing the logs for time period you mentioned See in this image, we have one order here in To Be distributed with priority 5 and rest of the order in To Be distributed was with priority 7 so ideally system should not pick this priority 5 task but it was not happened, RDS pick this priority 5 task 📎Screenshot 2025-05-09 at 12.44.29 AM.png U0ALSB28Q0Y/F08RNTRCJ83 Ok. One problem in the model file `Choose-AGV` section. waitimeratio is too high waittimeratio = 1000, means, for every second the order waits, our weighted score will plus 1000 It's default and we didn't make any change in it, yeah but I can get what you want to say usually waittimeratio is 0.1 or lower please try lower wait time ratio btw if you are saying waittimeration usually remains 0.1, then it should come as default value Here are the logs for asked time interval ok < can you read this document? This is how we compute matching weight Priority score is out-weighted by wait time score Lowering `WaitTimeRatio` should solve this problem Ok, Let me lower down the waittimeratio As per your calculation cost of 1 higher priority is equal to around 16 min of aging, right ? yes so if I will change waittimeratio from 1000 to 100 then 1 higher priority will be equal to 160 mins yes Ok Thanks Here are the modified values, I followed below steps to make these changes 1. Download model 2. Make the changes 3. Save 4. Upload 📎file 📎Screenshot 2025-05-09 at 12.35.00 PM.png U0ALSB28Q0Y/F08RQAEFJGL Let me know if I need to do the docker restart ? Thas seems to be ok Btw, I think most people will think that high priority order will execute first regardless how long the lower priority order waited In my opinion default value of waittimeratio should not have 1000, because around 16 min of aging is cacelling out to a high priority task and creating this confusion

## Next Action

Check the tasks with label PICK_H priorityratio/waittimeratio = 100, 1 priority means 100 seconds of waiting share your cost formula so we can see how it is getting considered

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: resolved
- Severity: 
- Priority: P2
- Created: 2025-05-08
- Last updated: 2025-05-09
- Bot IDs: 
- Components: dock, rds

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

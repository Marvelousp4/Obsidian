---
type: "issue"
source_type: "support_history_import"
account: "GreyOrange"
project: ""
site: "Unspecified"
vendor: "Wellwit Robotics"
category: "support_coordination"
item_type: "coordination"
status: "open"
severity: ""
priority: "P4"
created_date: "2026-01-07"
last_updated_date: "2026-01-09"
reporter: "U04580WJL65"
assignee: ""
source_id: "1767796280.147689"
source_file: "wellwit_issue_history_clean.csv"
bot_ids: []
components: ["sto"]
tags: []
---

# we are exploring M4 integration right now so need your help in below 1. Need english ve...

## Source Context

- Imported from: wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1767796280.147689
- Site: Unspecified
- Vendor / platform context: Wellwit Robotics

## Problem

we are exploring M4 integration right now so need your help in below 1. Need english version of api document 2. Some of the api's are giving response code 404(not available) 3. Many of the parameters are not understood to us so need a session where you guys can explain about these parameters 4. Need callback URL to get robots/task status 5. Do we need to update robots firmware to run with M4? It's a priority so let me know when we can connect tomorrow ?

## Progress

5. Which version you are refering? 2 and 3. Do you have a list? Will get back to you after discuss with seer team when we can connect help answer above questions btw in my opinion, many of things are not understable to us because of Chinese version so i think in english version things will be smooth, sometimes translator didn't work perfectly 1. English Version API document is working, but it will take around 1 month to finish. Currently you can try with the AI translation feature of Lark as below: 4. Currently the callback mechanism is not available, they will develop this, ETA is before CNY Point 5? Do we need to Update Bot firmware in lab to run them on m4 ? 5. Which version you are using in lab bot? Rbk version above 3.4 is compatible with M4. unable to create account on Lark 📎Screenshot 2026-01-09 at 12.09.20 PM.png U0ALSB28Q0Y/F0A7M0E576Z Query 2 Need understanding on rbkArgs field, it's uses and how to configure and use these action parameters. Also, they is no block Id field present in the API which is required by Grey Matter. 📎Screenshot 2026-01-09 at 12.19.38 PM.png U0ALSB28Q0Y/F0A7U27QPDJ 📎Screenshot 2026-01-09 at 12.19.30 PM.png U0ALSB28Q0Y/F0A7QE8J7BL

## Next Action

1. Will check with SEER team 4. Will check with SEER team My suggestion is you can provide list of 2 and 3, I can ask SEER team to check first. Query: 1 ```Create a waybill POST /api/fleet/orders/create We are not able to create any new waybill without sending any keyLocations. In the contract it's not a required field but still we are getting error.``` 📎Screenshot 2026-01-09 at 12.12.28 PM.png U0ALSB28Q0Y/F0A790SB6H5 📎Screenshot 2026-01-09 at 12.13.44 PM.png U0ALSB28Q0Y/F0A790SA54P

## Metadata

- Category: support_coordination
- Item type: coordination
- Status: open
- Severity: 
- Priority: P4
- Created: 2026-01-07
- Last updated: 2026-01-09
- Bot IDs: 
- Components: sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: 
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

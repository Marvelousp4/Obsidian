---
type: "issue"
source_type: "support_history_import"
client: "GreyOrange"
account: "GreyOrange"
project: "Adams"
site: "Adams"
vendor: "Wellwit Robotics"
category: "hardware_or_mechanical"
item_type: "hardware"
status: "open"
severity: "SEV1"
priority: "P1"
created_date: "2025-07-07"
last_updated_date: "2025-07-10"
reporter: "U04580WJL65"
assignee: ""
source_id: "1751892448.099179"
bot_ids: []
components: ["charger", "dock", "rds", "socket", "sto"]
tags: []
---

# Adams | we got one Sev1 issue at adams, where we can't see any robot at RDS and connect...

## Source Context

- Imported from: /Users/bai/Documents/Playground/wellwit_issue_history_clean.csv
- Source channel/file: C08GU4VBN1G_2025-01-01_to_2026-03-16.txt
- Original source id: 1751892448.099179
- Site: Adams
- Vendor / platform context: Wellwit Robotics

## Problem

we got one Sev1 issue at adams, where we can't see any robot at RDS and connection timeout popup was there at robotshop RDS tab, after investigation we find out some timeout crash logs in rds component, so we restarted the RDS docker containers and after that it worked. Attaching the logs here, help us to figure out the reason

## Progress

What do you mean by "where we can't any robot at RDS and connection timeout popup was there are robotshop RDS tab" I'm not getting this You mean you can't SEE any robot at RDS web console? yes, I corrected out the message above We were getting this popup 📎WhatsApp Image 2025-07-06 at 5.33.52 PM.jpeg U0ALSB28Q0Y/F09496SHH8X and when I saw RDS logs, it was printing timeout error and crashing continiously these logs were coming continiously These logs are come from the RDS log, not the rdscore log, right? yes you can see these logs in Rds_2025-07-06_09-00-00.log file Did you upgraded the rdscore? no, it was on older version only Got it These issue happens only once? I saw the timestamp was on Sunday, you are doing some test? see the version 📎Screenshot 2025-07-07 at 6.35.35 PM.png U0ALSB28Q0Y/F095A3TKTQ8 it was in actual operations, friday was holiday in USA so customer ran operations on sunday OK, got it But SEER team can not figured out the root cause of this, and this is an very low probability issue. We already enabled the charger match algorithm for several month, this is the first time we got this issue do you feel, it is because of charger ? No, I don't think so

## Next Action

"after investigation we find out some timeout crash logs in rds component" could you share some screenshot for your investigation? 2025-07-06 09:00:45.010 [orderCache] ERROR com.seer.rds.schedule.RobotStatusSchedule.recordVehicleStatus(56) - get core error, set vehicle status to disconnected. 2025-07-06 09:00:45.160 [orderCache] ERROR com.seer.rds.schedule.AlarmsSchedule.alarmsRecord(97) - get core error, set vehicle status to disconnected. 2025-07-06 09:00:49.002 [orderCache] ERROR com.seer.rds.schedule.queryOrderListSchedule.run(107) - query core error java.net.SocketTimeoutException: timeout at okio.Okio$4.newTimeoutException(Okio.java:232) at okio.AsyncTimeout.exit(AsyncTimeout.java:286) in logs folder of shared logs We checked this issue, it was caused by the charger match algorithm stucked.

## Metadata

- Category: hardware_or_mechanical
- Item type: hardware
- Status: open
- Severity: SEV1
- Priority: P1
- Created: 2025-07-07
- Last updated: 2025-07-10
- Bot IDs: 
- Components: charger, dock, rds, socket, sto

## Related Links

- Account: [[09 Work/Accounts/GreyOrange|GreyOrange]]
- Site note: [[04 Projects/Work/GreyOrange/Adams.md|Adams]]
- Vendor note: [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]

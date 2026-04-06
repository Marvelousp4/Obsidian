# Account Architecture

这套系统里，一个客户不是一张笔记，而是一组关联对象。

## 关系模型

1. `Account`
   代表客户账号本身，比如 `GreyOrange`、`Devonics`
2. `Contact`
   代表这个账号里的具体人，归属于某个团队和职责
3. `Project / Site`
   代表客户下的具体项目、现场或部署站点
4. `Meeting`
   代表一次沟通事件，关联账号、联系人、项目
5. `Issue`
   代表一个现场问题、产品问题或支持问题，关联账号、项目、设备

## 为什么这样设计

- 一个客户会有很多项目，所以 `客户 != 项目`
- 一个客户会有很多人，所以 `客户 != 联系人`
- 一个项目会有很多问题，所以 `项目 != 问题`
- 一次会议往往牵涉多个组织和多个人，所以 `会议` 要单独存在

## 目录约定

- `04 Clients/<Account>.md`
  账号总览
- `04 Clients/<Account>/Contacts/*.md`
  联系人
- `05 Projects/<Account>/*.md`
  项目 / 现场
- `06 Meetings/<Account>/*.md`
  会议
- `08 Issues/<Account>/**/*.md`
  问题单

## 操作原则

- 新客户先建 `Account`
- 有明确负责人或关键人，就建 `Contact`
- 有明确交付现场或长期运行点，就建 `Project / Site`
- 每次重要沟通建 `Meeting`
- 有现场故障、软件问题、阻塞，就建 `Issue`

## GreyOrange 这种客户怎么落

- `GreyOrange` 是账号
- `Harshita / Mohit / Sumit ...` 是联系人
- `Sam's ATL / Kenco Kansas / Sodimac Colombia ...` 是项目 / 现场
- 每个现场产生的问题进入 `08 Issues/GreyOrange`

## Devonics 这种会议怎么落

- `Devonics` 是账号
- `Joe / Frank / Joy` 是联系人
- 会议单独建成 `Meeting`
- 会议里提到的技术需求、动作项再分别挂到项目或问题


# Account Architecture

In this system, one customer is not one note. It is a linked set of objects.

## Relationship Model

1. `Account`
   Represents the customer entity itself, such as `GreyOrange` or `Devonics`
2. `Contact`
   Represents one person under that account, tied to a team and responsibility
3. `Project / Site`
   Represents a deployment, opportunity, or site under that account
4. `Meeting`
   Represents one communication event linked to accounts, contacts, and projects
5. `Issue`
   Represents one field, product, or support problem linked to an account, project, and equipment

## Why This Design Works

- One customer can have many projects, so `customer != project`
- One customer can have many people, so `customer != contact`
- One project can have many issues, so `project != issue`
- One meeting often includes multiple organizations and people, so `meeting` must stand alone

## Folder Convention

- `09 Work/Accounts/<Account>.md`
  account overview
- `09 Work/Accounts/<Account>/Contacts/*.md`
  contacts
- `04 Projects/Work/<Account>/*.md`
  projects / sites
- `09 Work/Meetings/<Account>/*.md`
  meetings
- `09 Work/Issues/<Account>/**/*.md`
  issues

## Operating Rules

- Create an `Account` first for a new customer
- Create a `Contact` when a real owner or stakeholder becomes relevant
- Create a `Project / Site` when there is a real deployment, opportunity, or operating location
- Create a `Meeting` for any important conversation
- Create an `Issue` for failures, bugs, support blockers, or field problems

## GreyOrange Example

- `GreyOrange` is the account
- `Harshita / Mohit / Sumit ...` are contacts
- `Sam's ATL / Kenco Kansas / Sodimac Colombia ...` are projects / sites
- Site-specific support history goes into `09 Work/Issues/GreyOrange`

## Devonics Example

- `Devonics` is the account
- `Joe / Frank / Joy` are contacts
- The discovery call exists as its own `Meeting`
- Technical requirements and action items from that meeting get linked into projects or issues

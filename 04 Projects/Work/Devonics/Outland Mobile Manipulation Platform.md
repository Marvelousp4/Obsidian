---
type: "project"
account: "Devonics"
client: "Devonics"
project_kind: "solution_opportunity"
site: ""
status: "discovery"
owner: "bai"
started: "2026-04-05"
next: "Collect CAD / internal layout drawings and evaluate power + packaging trade-offs for FR10 on 300J."
tags: []
---

# Devonics - Outland Mobile Manipulation Platform

## Goal

Evaluate a productized mobile manipulator based on a Wellwit mobile base, Fairino FR10 arm, and Outland's autonomy / compute stack.

## Background

- Source transcript: /Users/bai/Downloads/cleaned_meeting_transcript_labeled.txt
- Core organizations: [[09 Work/Accounts/Devonics|Devonics]], [[09 Work/Accounts/Outland Robotics|Outland Robotics]], [[09 Work/Accounts/Wellwit Robotics|Wellwit Robotics]]
- Candidate base discussed: 300J
- Arm discussed: FR10

## Current Status

- Stage: discovery
- Strong fit for warehouse movement and flexible manipulation scenarios.
- Open questions remain around compute packaging, battery life, ROS 2 integration, and what should be standard vs semi-custom.

## Technical Constraints

- FR10 on Wellwit base appears feasible and close to standard according to Devonics.
- GPU-heavy compute stack around 500W creates battery pressure.
- Secondary battery or option A/B/C packaging paths were discussed.
- Wellwit stated ROS 2 is not native; a wrapper may be required.
- Weekly maintenance includes LiDAR cleaning and battery-related checks.
- Clean-room or washdown variants may be possible but are not default.

## Next Steps

- [ ] Receive files / drawings for the three units Darshan showed.
- [ ] Evaluate 300J internal space against Outland compute box dimensions.
- [ ] Model battery impact and whether secondary battery is needed.
- [ ] Decide what belongs in a standard package versus semi-custom upgrade path.

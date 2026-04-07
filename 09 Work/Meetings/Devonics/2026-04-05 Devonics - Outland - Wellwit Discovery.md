---
type: "meeting"
date: "2026-04-05"
organizations: ["Devonics", "Outland Robotics", "Wellwit Robotics"]
participants: ["Joe Fautas", "Frank Handel", "Joy", "Darshan", "Leo", "Samantha", "Vincent"]
contacts: ["Joe Fautas", "Frank Handel", "Joy", "Darshan", "Leo", "Samantha", "Vincent"]
account: "Devonics"
project: "Devonics - Outland Mobile Manipulation Platform"
client: "Devonics"
tags: []
---

# 2026-04-05 Devonics / Outland / Wellwit Discovery

## Agenda

- Introductions across Devonics, Outland Robotics, and Wellwit Robotics
- Evaluate a mobile manipulation offering
- Discuss deployment fit, platform choice, power budget, software stack, and next technical artifacts

## Key Information

- Outland wants a wider robot offering and is evaluating the right mobile platform.
- Devonics reported strongest success in warehouse movement use cases, including Walmart and Sam's Club contexts.
- FR10 on a Wellwit base was described as relatively straightforward.
- 300J became the candidate platform for the current concept.
- Outland's compute package is large and power-hungry; around 500W worst-case was discussed.
- Battery life is therefore a design constraint, with secondary battery and hot-swap options discussed.
- Wellwit uses LiDAR-based SLAM and said ROS 2 is not native.
- Weekly maintenance should include LiDAR cleaning and battery checks.
- Clean-room and IP65-related extensions exist, but are not standard launch assumptions.

## Decisions

- Keep evaluating the 300J for the current project.
- Treat packaging and power as first-order constraints before committing to a standard product shape.

## Action Items

- [ ] Wellwit / Vincent to provide files or drawings for the three units Darshan showed.
- [ ] Compare Outland compute dimensions with 300J internal envelope.
- [ ] Model option A / B / C around battery and accessory battery design.
- [ ] Clarify API / wrapper approach for ROS-based stack.

## Raw Transcript

- Source file: cleaned_meeting_transcript_labeled.txt

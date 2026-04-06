---
type: knowledge
domain: tech
source_type: video
source: "/Users/bai/Documents/Obsidian/Space/07 Resources/Transcripts/2026-04-06 - Video2Sim2Real Presentation.txt"
speaker: "Yunhai Han"
platform: presentation
watched_on: 2026-04-06
topic: "robot_learning"
updated: 2026-04-06
tags:
  - robot-learning
  - sim2real
  - dexterous-manipulation
  - foundation-models
  - reinforcement-learning
---

# 2026-04-06 - RoboDex - Video2Sim2Real Learning for Dexterous Manipulation

## Video Information

- Title: RoboDex: Video-to-Sim-to-Real Learning for Dexterous Manipulation using Foundation Models
- Speaker: Yunhai Han
- Source transcript: [[07 Resources/Transcripts/2026-04-06 - Video2Sim2Real Presentation.txt]]

## Key Takeaways

- The pipeline starts from only a human manipulation video and aims to end with a real-world dexterous robot policy.
- The stack combines foundation models, pose estimation, hand retargeting, simulator generation, RL policy training, and transfer to real deployment.
- The motivation is to avoid expensive large-scale offline data collection and reduce dependence on opaque black-box robot foundation models.
- A key angle is specialist policy generation from user-specific demonstrations rather than relying only on broad general-purpose robot policies.

## Structured Notes

### Concepts

- Video-to-sim-to-real is a structured path from human demonstration to robot policy.
- Specialist policies can be more practical than one giant generic robot model in narrow dexterous tasks.
- The presentation frames interpretability, user preference, and sample efficiency as reasons to prefer a more structured learning stack.

### Methods

- Extract object trajectories and spatial configurations from human video.
- Retarget human hand behavior into robot trajectories.
- Build or parameterize the simulator from those observations.
- Train a state-based policy via reinforcement learning and then transfer it to real deployment.

### Examples

- The presentation references CIMER and related work on dexterous manipulation from state-only observations.
- It explicitly contrasts the method against the cost and opacity of large pre-trained foundation-model pipelines.
- It positions the approach as one-shot or low-data adaptation from a human demonstration.

## Actionable Moves

- [ ] Create a separate note on how video-to-sim-to-real could apply to mobile manipulation or your robotics product thinking.
- [ ] Extract the pipeline into a visual flow diagram in Excalidraw.
- [ ] Compare this approach with teleoperation-first and large-dataset foundation-model approaches.

## Links

- knowledge: [[05 Knowledge/Work/Tech/Tech Index]]
- resource: [[07 Resources/Transcripts/2026-04-06 - Video2Sim2Real Presentation.txt]]


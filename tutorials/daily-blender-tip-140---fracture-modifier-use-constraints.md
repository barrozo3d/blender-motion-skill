---
title: Daily Blender Tip 140 - Fracture Modifier: Use Constraints
source: YouTube
url: https://www.youtube.com/watch?v=Lh1wtY2uRPE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Custom \"Fracture Modifier\" build of Blender (third-party fork, not stock Blender), same as Tip 139"
tags: [rigid-body, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 140 - Fracture Modifier: Use Constraints

**Source:** [YouTube](https://www.youtube.com/watch?v=Lh1wtY2uRPE)
**Author:** Blender Secrets
**Duration:** 1m58s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'FRACTURE MODIFIER USE CONSTRAINTS'
- **CRITICAL:** Empty transcript in chapter 'Turn on Use Constraints in Fracture Constraint Settings'
- **CRITICAL:** Total transcript only 11 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (11 chars) in 'Then experiment with the Angle values.'

---


Frames captured — see "Captured Frames" section below.


### FRACTURE MODIFIER USE CONSTRAINTS [0:00]

### Turn on Use Constraints in Fracture Constraint Settings [0:21]

### Then experiment with the Angle values. [0:29]
**Transcript (timestamped):**
[1:30] Doesn't Log



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_000.jpg
- [0:21] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_001.jpg
- [0:29] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_002.jpg
- [1:00] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_004.jpg
- [1:58] tutorials/frames/daily-blender-tip-140---fracture-modifier-use-constraints/frame_005.jpg

---

## Structured Notes

### Core Technique
A direct follow-up to Tip 139: **Fracture Constraint Settings** in the Fracture Modifier build let pre-shattered shards stay glued together (rather than immediately flying apart as loose rigid bodies) until a physical stress threshold is exceeded — controlled mainly via an **Angle** value that determines how much bending/deformation a joint between shards can tolerate before it breaks. Demo footage/credit at the end points to "Mandala Motion" (Instagram.com/mandalamotion), suggesting this specific demonstration clip's source/inspiration.

### Summary
Frame 000 shows the test setup: a green cube sitting in a dark blue-floored scene with a large blue cylinder positioned above it, about to roll down and crush it, captioned "Fracture Modifier Use Constraints." Frame 001 shows the **Fracture Constraint Settings** panel (Constraint Building Settings: Use Constraints checked, Breakable checked, Constrained Collision, Self Collision, Use Compounds, Activate Broken, Constraint Type: Fixed) below the earlier Fracture Settings (Splinter X/Y/Z, Splinter Length, Advanced Fracture Settings, Execute Fracture, Threaded), captioned "Turn on Use Constraints in Fracture Constraint Settings." Frame 002 shows the deeper constraint-breaking settings: Cluster Group/Type: Fixed, Constraint Breaking Settings (Threshold 10.00000, Cluster Breaking threshold 1000.00000), Constraint Special Breaking Settings (Percentage, Cluster Percentage, **Angle** highlighted red with the cursor on it, Cluster Angle, Distance, Cluster Distance, Solver/Cluster Solver Iterations Override, Weighted Angle/Percentage/Distance, Mass Dependent Thresholds), captioned "Then experiment with the Angle values." Frame 003 shows a low Angle value (4°) tested: the cylinder rests on the cube, which stays mostly intact — only a small, contained deformation, captioned "Angle: 4°" — the shards' constraints held because the angle of deformation stayed under the low threshold. Frame 004 shows a higher Angle value (7°) tested: the same setup now results in the cube's shell visibly peeling/breaking open like tinfoil under the cylinder's weight, captioned "Angle: 7°" — a higher allowed angle before breaking meant more visible deformation happened before the constraints gave way, producing a more dramatic destruction. Frame 005 is a credits/outro card for "Mandala Motion" (logo, Instagram.com/mandalamotion, "Thanks for watching!") — crediting the source of this specific demo setup/footage.

### Key Steps
1. Continuing from a Fracture Modifier setup (per Tip 139), open **Fracture Constraint Settings** below the main Fracture Settings panel.
2. Enable **Use Constraints** — this makes pre-fractured shards start out rigidly connected to their neighbors (like an intact object) instead of immediately behaving as separate loose rigid bodies.
3. Also relevant/visible: **Breakable** (allows those constraints to eventually fail under enough stress), Constrained Collision, Self Collision, Use Compounds, Activate Broken, and a Constraint Type (Fixed shown).
4. In the deeper **Constraint Breaking Settings** / **Constraint Special Breaking Settings**, the key value to experiment with is **Angle** — this sets how much a shard-to-shard joint can bend/deform before that constraint breaks and the shards separate. Related fields include Threshold, Cluster Breaking Threshold, Percentage/Cluster Percentage, Cluster Angle, Distance/Cluster Distance, and various Weighted/Mass-Dependent override options for fine-tuning per-shard-mass or per-connection break behavior.
5. Test the effect: a low Angle value (4° in this demo) keeps the shattered object holding together under load, absorbing the impact with only minor visible give; a higher Angle value (7°) allows more bending before breaking, producing a more dramatic, tinfoil-like tearing/peeling failure once the threshold is finally exceeded.

### Nodes / Settings
- **Fracture Constraint Settings panel:** Use Constraints, Breakable, Constrained Collision, Self Collision, Use Compounds, Activate Broken, Constraint Type (Fixed).
- **Constraint Breaking Settings:** Threshold, Cluster Breaking Threshold.
- **Constraint Special Breaking Settings:** Percentage, Cluster Percentage, **Angle** (primary experiment variable), Cluster Angle, Distance, Cluster Distance, Solver/Cluster Solver Iterations Override, Weighted Angle/Percentage/Distance toggles, Mass Dependent Thresholds.

### Difficulty
Intermediate

### Blender Version
Custom "Fracture Modifier" build of Blender (third-party fork, not stock Blender) — same non-standard build referenced in Tip 139.

### Tags
rigid-body, simulation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start](daily-blender-tip-139---blender-fracture-modifier-build---quick-start.md) — shares rigid-body, simulation; direct predecessor covering the base Fracture Settings (Shard Count, Execute Fracture) that this tip's Constraint Settings build on top of.

---
title: Daily Blender Tip 89 - Riggin With Seperate Objects Or Not?
source: YouTube
url: https://www.youtube.com/watch?v=9takya3FrtI
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — this is a modeling/rigging strategy discussion, not tied to specific Blender version features"
tags: [rigging, character, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 89 - Riggin With Seperate Objects Or Not?

**Source:** [YouTube](https://www.youtube.com/watch?v=9takya3FrtI)
**Author:** Blender Secrets
**Duration:** 1m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 16 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (16 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] sources
[1:36] finished



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_004.jpg
- [1:40] tutorials/frames/daily-blender-tip-89---riggin-with-seperate-objects-or-not/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 6 of the rigging series — a conceptual comparison (not a step-by-step how-to) between two character-modeling approaches under the same armature: **one single connected mesh** (skin + clothes merged as one object/"skin") versus **separate clothing objects** layered over a body — demonstrating that a single connected mesh deforms without overlap/clipping problems when stretched, while separate-object clothing can visually separate from the body during extreme poses.

### Summary
Frame 000 shows two nearly-identical characters (one in a green shirt, one in a red shirt) sharing "the exact same armature," captioned "These two characters have the exact same armature." Frame 001 shows a close-up of the red-shirted character's torso, captioned "The guy in the red shirt consists of seperate objects, the clothes are seperate parts" — his shirt is its own mesh object layered over a separate body mesh. Frame 002 shows a close-up of the green-shirted character's legs, captioned "The green guy is one single object. The clothes are connected, even to his 'skin'" — his entire body and clothing form one continuous connected mesh. Frame 003 shows the green character's leg stretched into an exaggerated pose without any visible seam or clipping, captioned "As you can see, with the same rig, his body can be stretched without overlapping problems" — the single-mesh approach deforms cleanly because there's no separate geometry to clip through. Frame 004 shows the green character from behind mid-pose, torso and legs deforming smoothly. Frame 005 shows both characters side by side in a crouched pose, captioned "Check the talk by Junya Motomura on Youtube about Guilty Gear X. Those characters have 400 bones!" — a reference to a professional game-rigging talk for viewers wanting to go deeper.

### Key Steps
1. **Separate-object approach** (red character): model the body and clothing as distinct mesh objects, each weight-painted/skinned to the same armature independently — easier to swap/edit individual garments, but risks visible clipping/gaps between the body and clothing meshes during extreme poses since they deform as separate skinned meshes.
2. **Single connected mesh approach** (green character): model the body and clothing as one continuous, fully-joined mesh (the clothing geometry is merged into the "skin") skinned to the armature as a single object — deforms cleanly with no seams or overlap issues even under extreme stretching, since there's no boundary between separate objects to clip through.
3. Trade-off: the single-mesh approach is more robust for deformation but harder to edit/vary clothing on (since it's fused geometry), while the separate-object approach is more modular but needs careful weight painting to avoid clipping in extreme poses.
4. For advanced/production-grade character rigs needing many more bones and finer control (e.g. professional game characters), the video points to Junya Motomura's public talk on the Guilty Gear -X- character rigs (reportedly using around 400 bones per character) as further reference.

### Nodes / Settings
- No specific operators/modifiers demonstrated — this is a conceptual comparison of mesh topology strategies (single fused mesh vs. separate skinned objects) under a shared armature.

### Difficulty
Intermediate

### Blender Version
Not specified — this is a modeling/rigging strategy discussion, not tied to specific Blender version features.

### Tags
rigging, character, modelling, intermediate

---

## Related Tutorials
- [Daily Blender Tip 88 - How To Make A Character Follow A Path](daily-blender-tip-88---how-to-make-a-character-follow-a-path.md) — shares rigging, character, animation; part of the same character rigging series, continuing the discussion with a path-following animation setup.

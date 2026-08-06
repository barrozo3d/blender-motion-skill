---
title: Daily Blender Tip 88 - How To Make A Character Follow A Path
source: YouTube
url: https://www.youtube.com/watch?v=k19Gg094jOA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — NLA Editor Action strips and the Follow Path constraint are version-agnostic core Blender animation tools"
tags: [rigging, character, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 88 - How To Make A Character Follow A Path

**Source:** [YouTube](https://www.youtube.com/watch?v=k19Gg094jOA)
**Author:** Blender Secrets
**Duration:** 2m2s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'SIMPLE CHARACTER FOLLOW PATH'
- **CRITICAL:** Empty transcript in chapter 'In object mode shift-select the armature and the path, ctrl+p and choose Path Constraint. Choose "follow curve" and "animate path".'
- **CRITICAL:** Total transcript only 13 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (13 chars) in 'Change the speed of the character following the path in the curve settings under "Frames".'

---


Frames captured — see "Captured Frames" section below.


### SIMPLE CHARACTER FOLLOW PATH [0:00]

### In object mode shift-select the armature and the path, ctrl+p and choose Path Constraint. Choose "follow curve" and "animate path". [0:58]

### Change the speed of the character following the path in the curve settings under "Frames". [1:29]
**Transcript (timestamped):**
[2:00] ava,
[2:07] bounced,



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_001.jpg
- [0:58] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_002.jpg
- [1:20] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_003.jpg
- [1:40] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_004.jpg
- [2:00] tutorials/frames/daily-blender-tip-88---how-to-make-a-character-follow-a-path/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 5 of the rigging series: converting the walk-cycle keyframes from [Part 3](daily-blender-tip-86---simple-character-walk-cycle.md) into a reusable **NLA Action strip**, then making the whole rigged character follow a hand-drawn curve path using a **Path Constraint** (Follow Curve + Animate Path) — so the character walks in place while the constraint moves it physically along the path, with the walk cycle looping as it travels.

### Summary
Frame 000 shows a curved, meandering path (a Curve object) drawn in the viewport, a dense Dope Sheet full of keyframes on the right, captioned "Create a path for you character to follow." Frame 001 shows the NLA (Nonlinear Animation) Editor with the walk-cycle keys about to be converted, captioned "In the NLA editor press the down arrow on the keys to convert them to an action (the yellow block). Give it a name, 'walk' for example." Frame 002 shows the character selected alongside the path curve, an Add Object Constraint panel with a **Follow Path** constraint added (Target set to the curve), captioned "In object mode shift-select the armature and the path, ctrl+p and choose Path Constraint. Choose 'follow curve' and 'animate path'." Frame 003 shows the character now positioned oddly relative to the path direction, the Follow Path constraint's Forward axis setting visible, captioned "You may have to change the 'forward' direction. Position the character correctly at the beginning of the path." Frame 004 shows the character correctly walking along the winding path, the constraint's **Curve Radius / Fixed Position / Frames** settings visible in the sidebar, captioned "Change the speed of the character following the path in the curve settings under 'Frames'." Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Draw a **Curve** (path) in the viewport for the character to walk along.
2. In the **NLA Editor**, select the existing walk-cycle keyframes/action and press the **down arrow** to convert/push it down into a proper **Action strip** (the yellow block) — name it (e.g. "walk") so it becomes a reusable, loopable animation clip rather than raw scene keyframes.
3. In Object Mode, **Shift-select** the armature and then the path curve, then **Ctrl+P > Path Constraint**, checking **Follow Curve** and **Animate Path** — this adds a **Follow Path** constraint to the armature targeting the curve.
4. If the character faces the wrong way relative to the path's direction, adjust the constraint's **Forward** axis setting, and reposition the character correctly at the path's starting point.
5. Adjust the **Frames** value in the Follow Path constraint's curve settings to control how fast the character travels along the path (fewer frames = faster traversal, more frames = slower).
6. With the NLA action set to loop/repeat and the Follow Path constraint animating position along the curve, the character now visually walks (looping in place) while physically traveling along the winding path.

### Nodes / Settings
- **NLA Editor:** convert Dope Sheet keyframes into a named Action strip (down-arrow / Push Down).
- **Constraint:** Follow Path (Target = path curve; Follow Curve; Animate Path; Forward axis; Fixed Position/Frames for speed).
- **Shortcut:** Ctrl+P > Path Constraint (from Object Mode, with armature + curve selected).

### Difficulty
Intermediate

### Blender Version
Not specified — NLA Editor Action strips and the Follow Path constraint are version-agnostic core Blender animation tools.

### Tags
rigging, character, animation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 86 - Simple Character Walk Cycle](daily-blender-tip-86---simple-character-walk-cycle.md) — shares rigging, character, animation; this tutorial converts that walk cycle into an NLA Action and drives it along a path with a Follow Path constraint.
- [Daily Blender Tip 87 - Adding Props To Your Character (like a stylish hat)](daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat.md) — shares rigging, character, animation; continues the same character rig series with a bone-parented prop before this path-following step.

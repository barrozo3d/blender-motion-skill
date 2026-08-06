---
title: Daily Blender Tip 87 - Adding Props To Your Character (like a stylish hat)
source: YouTube
url: https://www.youtube.com/watch?v=eQTkprbLxfA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Ctrl+P > Bone (Parent to Bone) is a version-agnostic core Blender rigging/parenting tool"
tags: [rigging, character, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 87 - Adding Props To Your Character (like a stylish hat)

**Source:** [YouTube](https://www.youtube.com/watch?v=eQTkprbLxfA)
**Author:** Blender Secrets
**Duration:** 1m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 31 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (31 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Bevel armies, Linus fillinging,



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_004.jpg
- [1:35] tutorials/frames/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 4 of the rigging series: attaching a separate prop object (a top hat) to the rigged character from [Parts 1–3](daily-blender-tip-84---rigging-a-simple-character-part-1.md) by parenting it directly to the rig's **head bone** (**Ctrl+P > Bone**), rather than to the whole armature or the head mesh — so the hat follows head rotation/movement correctly during animation.

### Summary
Frame 000 shows the character now wearing a black top hat, positioned on the head with a Shape Keys / UV Maps / Vertex Colors panel visible in the sidebar, captioned "Let's give our dude a stylish hat. Append or model the hat, and place it on his head..." Frame 001 shows a closer view of the hat correctly seated on the character's head. Frame 002 shows the armature's bone layers with a specific layer toggled on, the character mesh hidden (H), and both the hat and the head control bone selected (hat highlighted white/active, bone highlighted orange), captioned "Turn this armature layer on and hide the character (h to hide). Select the hat and shift+select the head-bone." Frame 003 shows the hat mesh in a wireframe pose, a bone extending down through it, with the Bone Groups panel visible, captioned "Press Ctrl+p, but this time choose 'Bone'. Unhide the character and test if it worked." Frame 004 shows the finished result: the character (unhidden, mid-walk-cycle pose) with the hat now following correctly on the head, captioned with no visible new instructions (continuation frame). Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Add or append the prop object (a hat) and manually position it correctly on the character's head in Object Mode.
2. Enable the armature bone layer containing the **head bone** (a Rigify control bone), and temporarily **Hide** the character mesh (**H**) to make bone selection easier without the mesh in the way.
3. Select the **hat** object first, then **Shift+select the head bone** last (so the bone is the active element) — parenting always targets whatever was selected/made-active last.
4. Press **Ctrl+P** and this time choose **Bone** (as opposed to "Object" or "Armature Deform") — this parents the hat directly to that single bone's transform, so it moves/rotates exactly with head motion.
5. **Unhide** the character mesh and test the parenting by posing/scrubbing the animation — the hat should now follow the head bone precisely through any pose.

### Nodes / Settings
- **Armature Layers:** toggle to show the specific control bone (e.g. head) needed for parenting.
- **Shortcut:** H — hide selected object (character mesh) to simplify bone selection.
- **Shortcut:** Ctrl+P > Bone — parent the selected object directly to a single bone (as opposed to the whole Armature with automatic weights).

### Difficulty
Intermediate

### Blender Version
Not specified — Ctrl+P > Bone (Parent to Bone) is a version-agnostic core Blender rigging/parenting tool.

### Tags
rigging, character, animation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 86 - Simple Character Walk Cycle](daily-blender-tip-86---simple-character-walk-cycle.md) — shares rigging, character, animation; this uses the same character rig, continuing the series by adding a bone-parented prop after Part 3's walk cycle.
- [Daily Blender Tip 84 - Rigging A Simple Character Part 1](daily-blender-tip-84---rigging-a-simple-character-part-1.md) — shares rigging, character, animation; Part 1 of the same series, providing the original Rigify rig this prop is parented to.
- [Daily Blender Tip 88 - How To Make A Character Follow A Path](daily-blender-tip-88---how-to-make-a-character-follow-a-path.md) — shares rigging, character, animation; continues the same character rig series, making the (now hat-wearing) character follow a curve path via a Follow Path constraint.

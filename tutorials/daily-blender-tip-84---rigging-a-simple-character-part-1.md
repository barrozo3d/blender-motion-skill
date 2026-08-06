---
title: Daily Blender Tip 84 - Rigging A Simple Character Part 1
source: YouTube
url: https://www.youtube.com/watch?v=_OZVTOF1U_U
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Rigify Basic Human Meta-Rig and Armature Symmetrize are version-agnostic core/built-in Blender rigging tools"
tags: [rigging, character, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 84 - Rigging A Simple Character Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=_OZVTOF1U_U)
**Author:** Blender Secrets
**Duration:** 1m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 8 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (8 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Palette,



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_004.jpg
- [1:48] tutorials/frames/daily-blender-tip-84---rigging-a-simple-character-part-1/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 1 of a 7-part character rigging series: adding a **Rigify** Basic Human meta-rig, fitting only one side's bones to the character mesh in Edit Mode (using **Shift+S > Cursor to Selected** to reposition the 3D cursor as a pivot point), then using **Armature > Symmetrize** to mirror the fitted bones to the other side instead of manually positioning both.

### Summary
Frame 000 shows a blocky humanoid character mesh with a default Rigify meta-rig (light blue bone octahedrons) just added inside it, captioned "Add a simple Rigify armature. Shift+A > Armature > Basic > Basic Human (Meta Rig)." Frame 001 shows the armature in Edit Mode with bones on one side of the body being moved/scaled to roughly match the character's arm and torso shape, captioned "In edit mode, move the bones on one side so they fit the character. We can mirror the other side later." Frame 002 shows a closer view of the shoulder/arm bones with the 3D cursor positioned precisely at a joint, captioned "To do that, select a point you want to pivot around, Shift+S > cursor to selected." — using the cursor-to-selected trick to get an exact rotation/scale pivot for bone adjustments. Frame 003 shows the bones further refined to fit the hand/wrist area, captioned "The first time you may have to experiment and try again a few times. It gets easier." Frame 004 shows the head/face bone area, all bones selected, captioned "When the bones look good on one side, select them all and choose Armature > Symmetrize." Frame 005 shows the Symmetrize operator's redo panel with a **Direction** dropdown set from +X to -X, highlighted in red, captioned "In the tool panel you can change the direction of Symmetrize, here it was from +x to -x. To be continued!"

### Key Steps
1. Add a **Rigify** meta-rig: **Shift+A > Armature > Basic > Basic Human (Meta-Rig)** — provides a pre-built, humanoid bone template ready to be fitted to any character.
2. In Edit Mode, work on **only one side** of the character (e.g. the character's left) — move, scale, and rotate that side's bones to match the mesh's actual proportions (arms, legs, spine, head).
3. Use **Shift+S > Cursor to Selected** on a specific joint/vertex to reposition the 3D cursor there, giving an exact pivot point for subsequent bone rotate/scale operations.
4. Expect to iterate — fitting bones accurately takes a few attempts, especially the first time; it becomes faster with practice.
5. Once one side's bones look correctly fitted, select **all** the bones and run **Armature > Symmetrize** — this mirrors the fitted side onto the opposite side automatically, so both arms/legs match without manually repositioning everything twice.
6. Check the Symmetrize operator's redo panel **Direction** setting (e.g. +X to -X) to make sure it mirrored from the correct source side to the correct target side.

### Nodes / Settings
- **Add-on:** Rigify (built-in, enable in Preferences if not active) — Basic Human Meta-Rig.
- **Shortcut:** Shift+S > Cursor to Selected — precise pivot placement for bone editing.
- **Armature menu > Symmetrize** — mirrors one side's edited bones to the other; Direction setting (+X to -X or vice versa) in the operator redo panel.

### Difficulty
Intermediate

### Blender Version
Not specified — Rigify Basic Human Meta-Rig and Armature Symmetrize are version-agnostic core/built-in Blender rigging tools.

### Tags
rigging, character, animation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 85 - Rigging A Simple Character Part 2](daily-blender-tip-85---rigging-a-simple-character-part-2.md) — shares rigging, character, animation; the direct Part 2 continuation, generating and cleaning up the final control rig from this tutorial's fitted meta-rig. This is Part 1 of a 7-part character rigging series continuing through Tips 85–90.

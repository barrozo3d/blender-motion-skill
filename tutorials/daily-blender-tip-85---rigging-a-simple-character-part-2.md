---
title: Daily Blender Tip 85 - Rigging A Simple Character Part 2
source: YouTube
url: https://www.youtube.com/watch?v=I-OSWKJg0ss
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Rigify-generated control rig, Armature Layers, and Pose Mode hide/unhide are version-agnostic core/built-in Blender rigging tools"
tags: [rigging, character, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 85 - Rigging A Simple Character Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=I-OSWKJg0ss)
**Author:** Blender Secrets
**Duration:** 1m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 3 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (3 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] and



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_004.jpg
- [1:40] tutorials/frames/daily-blender-tip-85---rigging-a-simple-character-part-2/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 2 of the rigging series: after generating the final **Rigify** control rig from the fitted meta-rig ([Part 1](daily-blender-tip-84---rigging-a-simple-character-part-1.md)), cleaning up the viewport by hiding the raw/technical deform-bone layers and the character mesh's selectability so only the animator-friendly **control shapes** remain visible and selectable in **Pose Mode** — ready for actual animation.

### Summary
Frame 000 shows the character mesh with a "Selectable" toggle icon in the Object Properties Viewport Display, highlighted red, captioned "Turn the selection icon back on so we can select the character object again." Frame 001 shows the generated Rigify control rig in Pose Mode, all bones selected (orange), captioned "Go to Pose Mode and select all of the armature objects (press A) and then hide them all (press H)" — hiding the technical/deform bone layer that shouldn't be directly animated. Frame 002 shows the Armature Data Properties' **Layers** grid with one specific layer square highlighted red, captioned "Shift+click on this specific layer in the armature tab" — selecting the layer that holds the animator-facing control shapes. Frame 003 shows the same layers grid with a different layer now toggled off, captioned "Turn off that layer again in the armature tab. Alt+H to unhide the armature control shapes." — revealing just the colorful, easy-to-grab IK/FK control widgets instead of the raw deform bone octahedrons. Frame 004 shows the finished character (a simple humanoid with a teal shirt) posed with an arm control raised, captioned "That's all! You can now animate your character in Pose Mode." Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. After generating the Rigify rig, make the original character mesh **selectable** again (Object Properties > Viewport Display > Selectable toggle) if it had been disabled during rigging.
2. In **Pose Mode**, select all armature bones (**A**) and **Hide** them (**H**) — this clears the cluttered raw deform-bone view.
3. In **Armature Data Properties > Layers**, **Shift+click** the specific layer that holds the rig's animator-facing **control shapes** (as opposed to the raw deform bones) to isolate it.
4. Turn off the deform-bone layer (leaving only the control layer active), then press **Alt+H** to unhide — revealing just the colorful, easy-to-grab control widgets (arms, legs, spine, head handles) instead of the technical bone octahedrons.
5. With only the clean control rig visible and selectable in Pose Mode, the character is now ready to be posed/animated directly by grabbing its control shapes.

### Nodes / Settings
- **Object Properties > Viewport Display > Selectable** — toggle for the character mesh.
- **Pose Mode:** A (select all), H (hide selected bones), Alt+H (unhide).
- **Armature Data Properties > Layers** — Shift+click to isolate the control-shape layer vs. the raw deform-bone layer.

### Difficulty
Intermediate

### Blender Version
Not specified — Rigify-generated control rig, Armature Layers, and Pose Mode hide/unhide are version-agnostic core/built-in Blender rigging tools.

### Tags
rigging, character, animation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 84 - Rigging A Simple Character Part 1](daily-blender-tip-84---rigging-a-simple-character-part-1.md) — shares rigging, character, animation; this is the direct Part 2 continuation, cleaning up and isolating the control rig generated from Part 1's fitted Rigify meta-rig.

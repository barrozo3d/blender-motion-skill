---
title: Daily Blender Tip 82 - Using Empties For Transformations And Mirroring
source: YouTube
url: https://www.youtube.com/watch?v=tUU0zFfMaEE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Empty objects, Mirror modifier's Mirror Object field, and Make Links (Ctrl+L) are version-agnostic core Blender features"
tags: [modelling, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 82 - Using Empties For Transformations And Mirroring

**Source:** [YouTube](https://www.youtube.com/watch?v=tUU0zFfMaEE)
**Author:** Blender Secrets
**Duration:** 1m37s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'USING EMPTIES FOR TRANSFORMATIONS'
- **CRITICAL:** Empty transcript in chapter 'Create an empty: Shift+A Empty Plain Axes (type doesn't really matter).'
- **CRITICAL:** Empty transcript in chapter 'Also useful is to use the empty as the center point for a mirror modifier. Add a mirror modifier to an object.'
- **CRITICAL:** Empty transcript in chapter 'In the modifier choose as Mirror Object the empty.'
- **CRITICAL:** Empty transcript in chapter 'Here I select the other objects, then Shift+select the object with the mirror modifier on it to make it active.'
- **CRITICAL:** Empty transcript in chapter 'Press ctrl+L and choose "modifiers". This copies the modifiers of the active object to the other selected objects.'
- **CRITICAL:** Total transcript only 6 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (6 chars) in 'You can now use the empty to control which point the mirror modifier uses as its centre.'

---


Frames captured — see "Captured Frames" section below.


### USING EMPTIES FOR TRANSFORMATIONS [0:00]

### Create an empty: Shift+A Empty Plain Axes (type doesn't really matter). [0:05]

### Also useful is to use the empty as the center point for a mirror modifier. Add a mirror modifier to an object. [0:36]

### In the modifier choose as Mirror Object the empty. [0:46]

### Here I select the other objects, then Shift+select the object with the mirror modifier on it to make it active. [1:06]

### Press ctrl+L and choose "modifiers". This copies the modifiers of the active object to the other selected objects. [1:14]

### You can now use the empty to control which point the mirror modifier uses as its centre. [1:23]
**Transcript (timestamped):**
[1:30] Indian



---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_000.jpg
- [0:36] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_001.jpg
- [0:46] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_002.jpg
- [1:06] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_003.jpg
- [1:14] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_004.jpg
- [1:25] tutorials/frames/daily-blender-tip-82---using-empties-for-transformations-and-mirroring/frame_005.jpg

---

## Structured Notes

### Core Technique
Using an **Empty** object as a controllable, independent center-point for a **Mirror modifier's Mirror Object** field — instead of mirroring around an object's own origin, the empty can be moved/rotated to reposition the mirror axis freely — then propagating that modifier setup to multiple other objects at once via **Ctrl+L > Modifiers** (Make Links).

### Summary
Frame 000 shows a cluster of cube-like blocky shapes with the Shift+A Add menu open (Empty > Plain Axes highlighted among Arrows/Single Arrow types), captioned "Create an empty: Shift+A > Empty > Plain Axes (type doesn't really matter)." Frame 001 shows the same cube cluster with an Empty (axis cross icon) now placed off to the side, captioned "Also useful is to use the empty as the center point for a mirror modifier. Add a mirror modifier to an object." Frame 002 shows the Mirror modifier panel (Axis X/Y/Z, Options: Merge/Clipping/Vertex Groups, Merge Limit, **Mirror Object** field) with the empty about to be assigned, captioned "In the modifier choose as Mirror Object the empty." Frame 003 shows multiple cube objects selected (highlighted orange) with one additional object selected last/active (highlighted white with the mirror modifier), captioned "Here I select the other objects, then Shift+select the object with the mirror modifier on it to make it active." Frame 004 shows the **Make Links** menu open (Objects to Scene, Object Data, Animation Data, Group, DupliGroup, **Modifiers**, Fonts, Transfer UV Maps), captioned "Press ctrl+L and choose 'modifiers'. This copies the modifiers of the active object to the other selected objects." Frame 005 shows the finished result: the original cube cluster now mirrored as a matching duplicate cluster on the other side of the empty's position, captioned "You can now use the empty to control which point the mirror modifier uses as its centre."

### Key Steps
1. Add an **Empty** (Shift+A > Empty > Plain Axes — the specific empty display type doesn't matter functionally) near the objects to be mirrored.
2. Add a **Mirror** modifier to one object, and in its settings set the **Mirror Object** field to the newly-created Empty — this makes the empty's transform (not the object's own origin) the pivot point for the mirroring.
3. Move/rotate the Empty at any time to reposition or reorient the mirror axis freely, without having to re-origin the actual mesh object.
4. To apply the same Mirror-modifier-with-empty setup to several other objects at once: select all the target objects first, then **Shift+select** the object that already has the configured Mirror modifier last (making it the active object).
5. Press **Ctrl+L** and choose **Modifiers** (Make Links > Modifiers) — this copies the active object's full modifier stack (including the Mirror Object assignment) onto every other selected object.
6. All objects now mirror around the same shared empty's position, so moving the empty repositions the mirror center for the whole group simultaneously.

### Nodes / Settings
- **Object:** Empty (Plain Axes or any type) — used purely as a transform reference point.
- **Modifier:** Mirror — Mirror Object field set to the Empty.
- **Shortcut:** Ctrl+L > Modifiers (Make Links) — copies the active object's modifier stack to all other selected objects.

### Difficulty
Beginner

### Blender Version
Not specified — Empty objects, Mirror modifier's Mirror Object field, and Make Links (Ctrl+L) are version-agnostic core Blender features.

### Tags
modelling, workflow, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover using Empties as Mirror modifier centers or Make Links > Modifiers specifically.

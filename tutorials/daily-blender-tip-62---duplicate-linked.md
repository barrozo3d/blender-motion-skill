---
title: Daily Blender Tip 62 - Duplicate Linked
source: YouTube
url: https://www.youtube.com/watch?v=W3EtoiG99mo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Alt+D (Duplicate Linked) and U (Make Single User) are version-agnostic core Blender shortcuts"
tags: [workflow, modelling, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-62---duplicate-linked/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 62 - Duplicate Linked

**Source:** [YouTube](https://www.youtube.com/watch?v=W3EtoiG99mo)
**Author:** Blender Secrets
**Duration:** 1m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 12 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (12 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Pal Soviets.



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_004.jpg
- [1:40] tutorials/frames/daily-blender-tip-62---duplicate-linked/frame_005.jpg

---

## Structured Notes

### Core Technique
Duplicating objects with **Alt+D** ("Duplicate Linked") instead of the default **Shift+D** — linked duplicates share the same mesh data, so editing one instance's geometry in Edit Mode updates every linked copy simultaneously; any copy that later needs unique geometry can be broken off into an independent "Single User" copy with **U > Object & Data**.

### Summary
Frame 000 shows three identical monkey-head models side by side, captioned "Instead of duplicating with SHIFT+D make it a habit to use ALT+D instead ... this has a big advantage." Frame 001 shows six duplicated toy-robot-style character heads in a two-row grid, all sharing the same mesh detail, captioned "The duplicates are 'linked', which means if I edit any of them the others will update as well." Frame 002 shows the same grid of models with a right-click context menu open ("Make Single User" > Object, Object & Data, Object & Data & Materials+Tex, Materials+Tex, Object Animation — "Object & Data" highlighted), captioned "If one still needs to have specific changes, you can still make it a 'single user' copy..." Frame 003 shows one of the six models now in wireframe/edit view separated from the still-linked others, captioned "Just select it and press 'u', then choose 'object and data'. Now that one can be edited individually." Frame 004 shows the finished grid with one model highlighted uniquely editable via a Bevel-like wireframe overlay, captioned "Thanks for following me! Feel free to ask questions in the comments section. I'll do my best to help." Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Instead of the default **Shift+D** (Duplicate, which creates fully independent mesh data), use **Alt+D** (Duplicate Linked) to create copies that all reference the **same underlying mesh data-block**.
2. Editing the mesh geometry of any one linked duplicate in Edit Mode instantly updates every other linked copy — extremely useful for repeated/instanced props or characters that should iterate together.
3. When one specific copy eventually needs unique geometry (a variant, damage, a pose-specific edit), select it and press **U** (Make Single User) > **Object & Data** — this breaks that one instance off with its own independent mesh copy, leaving the rest still linked to each other.
4. The Make Single User menu also offers narrower/broader options (Object, Object & Data, Object & Data & Materials+Tex, Materials+Tex, Object Animation) depending on exactly what needs to become independent.

### Nodes / Settings
- **Shortcut:** Alt+D — Duplicate Linked (shares mesh data across copies).
- **Shortcut:** U — Make Single User menu (Object / Object & Data / Object & Data & Materials+Tex / Materials+Tex / Object Animation).

### Difficulty
Beginner

### Blender Version
Not specified — Alt+D (Duplicate Linked) and U (Make Single User) are version-agnostic core Blender shortcuts.

### Tags
workflow, modelling, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover linked duplicates or Make Single User specifically.

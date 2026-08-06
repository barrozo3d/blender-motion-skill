---
title: Daily Blender Tip 224 - Growing Plant animation (part 2) (Blender 2.7 & 2.8)
source: YouTube
url: https://www.youtube.com/watch?v=qJgbhKcHKsY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 2.7 and 2.8 (explicitly named in the title)"
tags: [animation, organic, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 224 - Growing Plant animation (part 2) (Blender 2.7 & 2.8)

**Source:** [YouTube](https://www.youtube.com/watch?v=qJgbhKcHKsY)
**Author:** Blender Secrets
**Duration:** 2m23s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'GROWING PLANT (PART 2)'
- **CRITICAL:** Empty transcript in chapter 'Model a simple leaf and give it a green material.'
- **CRITICAL:** Empty transcript in chapter 'Select the base vertices and set the pivot point there.'
- **CRITICAL:** Empty transcript in chapter 'Create another bezier for a twig.'
- **CRITICAL:** Empty transcript in chapter 'Use a bezier curve for the Taper and Bevel object and check Fill Caps and Map Taper'
- **CRITICAL:** Total transcript only 13 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (13 chars) in 'Animate the Bevel Start value to grow the twig.'

---


Frames captured — see "Captured Frames" section below.


### GROWING PLANT (PART 2) [0:00]

### Model a simple leaf and give it a green material. [0:06]

### Select the base vertices and set the pivot point there. [0:18]

### Create another bezier for a twig. [0:26]

### Use a bezier curve for the Taper and Bevel object and check Fill Caps and Map Taper [0:33]

### Animate the Bevel Start value to grow the twig. [0:48]
**Transcript (timestamped):**
[2:00] HD Sovlog Job



---

## Captured Frames

- [0:06] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_000.jpg
- [0:18] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_001.jpg
- [0:26] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_002.jpg
- [0:40] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_003.jpg
- [0:55] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_004.jpg
- [1:30] tutorials/frames/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 2 of a growing-vine/plant animation: a Bezier curve "twig" is given real thickness via Taper and Bevel curve objects, then animated to visually grow by keyframing its **Bevel Start** value from 1.0 down to 0.0 — revealing more of the curve's length over time, like a vine extending — while individual pre-placed leaves along the twig pop into existence via Scale keyframes (0 → final scale) timed to when the growing tip passes each leaf's position.

### Summary
Frame 000 shows the target final look: a curling green vine/twig covered in leaves, viewed in Rendered/Material Preview shading, captioned "Model a simple leaf and give it a green material." Frame 001 shows a single modeled leaf mesh with its base vertices selected and the 3D cursor/pivot point set there, viewed in Edit Mode, captioned "Select the base vertices and set the pivot point there" — so the leaf can later be scaled from its base (attachment point) rather than its center. Frame 002 shows the Add menu open (Mesh/Curve/Surface/Metaball/Text/Grease Pencil/Armature/Lattice) with a green curved twig shape already in the viewport, captioned "Create another bezier for a twig" — modeling the vine's path as a Bezier curve. Frame 003 shows the Add > Curve submenu open (Bezier, Circle, Nurbs Curve, Nurbs Circle, Path) over the same green twig, captioned "Use a bezier curve for the Taper and Bevel object and check Fill Caps and Map Taper" — small circle/profile curves used as the twig curve's Taper and Bevel objects for realistic tapering thickness. Frame 004 shows the Curve Properties panel (Geometry: Offset, Extrude, Taper Object with Map Taper checked; Bevel: Depth, Resolution, Object, Fill Caps; Bevel Start/End sliders; Bevel Mapping/Path Animation: Frames, Evaluation Time) over a twig that's only partially "grown" (thin/short at the near end, full-diameter further along), captioned "Animate the Bevel Start value to grow the twig" — keyframing Bevel Start progressively lower reveals more of the curve's length as if it's extending in real time. Frame 005 shows the vine mid-animation with several leaves already visible and one leaf highlighted mid-transition, a Timeline with keyframe markers at the bottom, captioned "Set keyframes for the Scale of the leafs. One for the final scale and one for scale at zero" — leaves individually keyframed to pop into view.

### Key Steps
1. Model a simple leaf mesh and give it a green material.
2. In Edit Mode, select the leaf's base vertices (the point where it attaches to the twig) and set the 3D cursor/pivot point there — so later Scale animation grows the leaf outward from its attachment point rather than from its geometric center.
3. Create a Bezier curve shaped like a twig/vine, following the desired growth path.
4. Create small profile curves (also Bezier) to use as the twig curve's **Taper Object** and **Bevel Object** in Curve Properties > Geometry — giving the twig real 3D thickness that can vary along its length; enable **Fill Caps** (so the tube's ends are capped, not hollow) and **Map Taper** (so the taper profile maps correctly along the curve's length).
5. Duplicate/place instances of the leaf mesh at various points along the twig's path.
6. **Animate the growth:** keyframe the twig curve's **Bevel Start** value — starting near 1.0 (almost nothing visible) and animating down toward 0.0 over time — since Bevel Start hides the portion of the curve before that percentage point, animating it downward makes the twig appear to extend and grow in real time, tip-first.
7. **Animate the leaves popping in:** for each leaf, set a Scale keyframe at 0 (invisible) at the frame just before the growing twig tip reaches that leaf's position, then another Scale keyframe at its normal/final scale shortly after — so leaves appear to sprout right as the vine grows past them, rather than all existing from frame one.

### Nodes / Settings
- **Curve Geometry settings:** Taper Object (+ Map Taper), Bevel (Depth, Resolution, Object, Fill Caps), Bevel Start/End (animated for the growth effect), Bevel Mapping / Path Animation (Frames, Evaluation Time).
- **Modeling:** leaf mesh with pivot point set to its base vertices (for correct outward Scale animation).
- **Animation:** Bevel Start keyframes (curve growth), per-leaf Scale keyframes (0 → final, timed to the growth tip's position).

### Difficulty
Beginner

### Blender Version
Blender 2.7 and 2.8 — explicitly named in the title.

### Tags
animation, organic, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Bevel Start curve-growth animation technique.

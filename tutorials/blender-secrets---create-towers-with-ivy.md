---
title: Blender Secrets - Create Towers with Ivy
source: YouTube
url: https://www.youtube.com/watch?v=3cllYcT-MRg
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.3.1 -- observed in frame_000"
tags: [procedural, organic, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---create-towers-with-ivy/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Create Towers with Ivy

**Source:** [YouTube](https://www.youtube.com/watch?v=3cllYcT-MRg)
**Author:** Blender Secrets
**Duration:** 2m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Enable the extra objects addon that comes with Blender.
[0:09] Press Shift A and go to Mesh Extras Wall Factory.
[0:16] Increase the end value to 30 or more.
[0:18] Select all in Edit Mode and scale the stones with Alt S until they almost overlap.
[0:27] Add a bevel modifier.
[0:30] Add a simple deform modifier and set it to Bend 360 degrees along the Z-axis.
[0:38] You can type higher values in this field if you need to close the loop.
[0:44] To increase the height of the tower, add an Array modifier with relative offset in the
[0:48] Z-axis.
[0:50] To add some variation on the top, hide the current object and add another wall.
[0:57] Add some granules.
[1:02] Repeat the previous steps to make this part circular and place it at the top of the tower.
[1:09] Then unhide the previous wall.
[1:12] Apply these modifiers with Ctrl A, Vigimal, Geometry to Mesh.
[1:17] You can use a Remesh modifier set to Foxhole to make the wall look a bit more organic and
[1:21] realistic.
[1:28] Now let's add some IV to this.
[1:31] In Preferences, enable the Add Curve IV Gen addon that comes with Blender by default.
[1:36] Hold Shift and right-click to place the 3D cursor where you want the IV to start.
[1:41] Make sure the wall is selected and click on Add New IV.
[1:46] You can experiment with the settings and then click on Update IV to see the changes.
[1:51] Max IV length controls how far the IV grows.
[1:56] Gravity makes it look like it's being pulled down by its own weight.
[2:01] Randomness makes it more random.
[2:04] Wherever you place the 3D cursor is where the new IV will grow.
[2:08] Once you click somewhere else, you can no longer change the settings.
[2:13] Then you can add materials to the leaves and to the stem curves.
[2:18] Even mind that the more IV you have, the heavier the scene will be.
[2:23] Click on the square field on the right to get my free eBook sample PDF.



---

## Captured Frames

- [0:20] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_000.jpg
- [0:38] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_001.jpg
- [0:55] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_002.jpg
- [1:20] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_003.jpg
- [1:45] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_004.jpg
- [2:15] tutorials/frames/blender-secrets---create-towers-with-ivy/frame_005.jpg

---

## Structured Notes

### Core Technique
Build a stone tower entirely from Blender's built-in add-ons: the Extra Objects add-on's "Wall Factory" mesh generator bent into a cylinder via Simple Deform, heightened with an Array modifier, roughened with a Voxel Remesh, and finally covered in procedurally-grown ivy via the built-in Add Curve: IvyGen add-on.

### Summary
Frame 000 shows the Wall Factory-generated stone wall in Edit Mode — a dense grid of individually-scaled stone blocks (Ctrl overlay hints at a modal scale operation) with a doorway/window gap already present, matching the transcript's "increase End value, scale stones with Alt+S until they almost overlap" step. Frame 001 shows the payoff: the same wall bent into a full cylindrical tower via a Simple Deform modifier (Bend, Angle 360°, Axis Z) stacked under a Bevel modifier — a visible vertical seam remains where the wall doesn't perfectly close. Frame 002 shows exactly where this wall generator lives: Shift+A → Mesh → Extras → Wall Factory (arrow highlighting it in the Add menu), next to an Array modifier (Relative Offset, Factor X) already in the stack for extending tower height. Frame 003 confirms the "Foxhole" mentioned in the audio transcript is actually **Voxel** remesh mode — the Remesh modifier panel shows Blocks/Smooth/Sharp/Voxel with Voxel selected (arrow) and a Voxel Size field, applied to soften/organicize the tower's silhouette. Frame 004 shows the Add Curve: IvyGen add-on's generation panel (Random Seed, Maximum Time, Max Ivy Length, Max Float Length, Adhesion, weight/branch/leaf settings) with ivy actively growing up the side of the tower from a 3D-cursor start point. Frame 005 shows the finished ivy result from further back: dense green leaf clusters climbing the full tower height, with Stem and Leaves as separate objects in the Outliner (and a Cycles Render Properties panel visible, confirming Cycles as the render engine used for the final shots).

### Key Steps
1. Enable the built-in **Extra Objects** add-on in Preferences.
2. Shift+A → Mesh → Extras → **Wall Factory**; increase the End value to 30+ for enough stone segments to wrap a full tower.
3. In Edit Mode, select all and Alt+S (scale along normals) to grow the individual stone blocks until they nearly overlap, closing the gaps between them.
4. Add a Bevel modifier for softened stone edges.
5. Add a **Simple Deform** modifier set to Bend, 360°, along the Z-axis — this curls the flat wall into a closed cylindrical tower shape (type a value slightly over/under 360 if needed to fully close the seam).
6. Add an **Array** modifier with Relative Offset on the Z-axis to stack the wall vertically and increase the tower's height.
7. **Add variation at the top:** hide the current tower object, build a second Wall Factory wall following the same steps, add some granule/rubble detail, and make this second section circular, positioning it at the top of the tower; unhide the original tower wall afterward.
8. Apply all modifiers (Ctrl+A → Visual Geometry to Mesh) to bake the result into static geometry.
9. Add a **Remesh modifier set to Voxel mode** (not "Foxhole" — a transcription error, confirmed from the on-screen panel) to soften/organicize the blocky procedural silhouette into something more naturally weathered-looking.
10. **Grow ivy:** enable the built-in **Add Curve: IvyGen** add-on in Preferences; Shift+RMB to place the 3D cursor at the ivy's starting point on the tower surface; select the tower (target) object and click "Add New Ivy"; tune settings (Max Ivy Length controls growth distance, Gravity pulls growth downward for a natural hanging look, Randomness adds variation) and click "Update Ivy" to regenerate with new settings — note that once you click elsewhere in the viewport, that ivy instance's settings can no longer be edited, so dial them in before deselecting. Add materials to the generated Leaves and Stem curve objects separately. More ivy instances = heavier scene, so use sparingly for performance.

### Nodes / Settings
- **Add-ons (all built into Blender, enable via Preferences):** Extra Objects (Wall Factory generator), Add Curve: IvyGen (procedural ivy growth).
- **Modifiers:** Bevel, Simple Deform (Bend, Angle 360°, Axis Z — wraps a flat wall into a cylinder), Array (Relative Offset, Z-axis — extends height), Remesh (Voxel mode, Voxel Size — organic weathering).
- **Ivy settings:** Random Seed, Maximum Time, Max Ivy Length, Max Float Length, Adhesion, Primary/Random/Gravity Weight, Branching, Ivy Branch Size, Grow Leaves, Ivy Leaf Size, Leaf Probability.
- **Edit-mode operators:** Alt+S (scale along normals), Ctrl+A → Visual Geometry to Mesh.

### Difficulty
Intermediate

### Blender Version
Not specified — all techniques use long-standing built-in Blender add-ons/modifiers, version-agnostic across 2.8x-5.x.

### Tags
procedural, organic, modelling, intermediate

---

## Related Tutorials
- [12 Tips for Creating Epic Trees in Blender Without Paid Add-Ons](12-tips-for-creating-epic-trees-in-blender-without-paid-add-ons.md) — shares procedural, organic, intermediate; same channel, complementary organic-detail-via-add-on approach (trees vs. ivy).
- [Blender Secrets - Blender GIS (Extra Bonus Tutorial)](blender-secrets---blender-gis-extra-bonus-tutorial.md) — shares procedural, intermediate; same channel, both lean on lesser-known built-in/free add-ons for environment work.

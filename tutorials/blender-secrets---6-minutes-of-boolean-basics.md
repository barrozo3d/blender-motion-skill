---
title: Blender Secrets - 6 Minutes of Boolean Basics
source: YouTube
url: https://www.youtube.com/watch?v=_S3D8djM5bE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (Boolean Fast/Exact solver + BoolTool add-on, 2.9x-5.x)"
tags: [procedural, modelling, materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - 6 Minutes of Boolean Basics

**Source:** [YouTube](https://www.youtube.com/watch?v=_S3D8djM5bE)
**Author:** Blender Secrets
**Duration:** 6m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's turn this cube into something instead of deleting it.
[0:13] Delete one edge and bevel another one with Ctrl B.
[0:18] Scroll the middle mouse wheel up to increase the amount of segments.
[0:24] You can bevel these corner vertices with Shift Ctrl B.
[0:28] In Object Mode, right-click and choose Shade Smooth and enable Auto Smooth as well.
[0:36] Add a Solidify modifier and increase the thickness.
[0:40] Add a cylinder and scale it down, then enable Shade Smooth and Auto Smooth as well.
[0:48] Duplicate the cylinder a few times and join these cylinders into one object with Ctrl J.
[0:55] Add a boolean modifier to the cube, set to Difference with the cylinders as the object.
[1:01] Under Viewport Display, set the maximum draw type of the cylinders to Wire.
[1:07] You can also just disable their render visibility in the Outliner.
[1:12] Finally, add a Bevel modifier.
[1:33] Pool Tool is a useful cutting tool that you can enable in preferences.
[1:38] First, create an object that acts like a cutter.
[1:43] With the cutter selected, hold Shift and select the other object.
[1:47] Press Ctrl and minus on the numpad to cut.
[1:51] You can still see the cutter object as a bounding box and you can move, rotate and scale it.
[1:58] When you press Tab, you can still edit the object like a normal mesh, so you can add bevels to it, for example.
[2:05] In Edit Mode, you can also duplicate the mesh if you want to create some kind of array quickly.
[2:11] If it doesn't work, try moving the cutter slightly until it does.
[2:19] You can find all the other functions in the Edit tab in the Option panel.
[2:24] What I like to do in a boolean workflow is add some useful things to the Quick Favorites menu.
[2:29] For example, you'll always need Shade Smooth and Auto Smooth.
[2:35] Shadow and Gavety from the Viewport Shading menu are also nice for some extra visual appeal.
[2:41] Apply All is a function that is added by enabling the modifier tools in preferences.
[2:50] It applies all modifiers at once.
[3:06] To make slice cuts like this, create a second object that acts like a cutter and then assuming you have the bool tool add on enabled,
[3:13] press Ctrl and minus on the numpad.
[3:16] This adds a boolean modifier with a difference operation on your object.
[3:20] Now, select the cutter object and add a solidify modifier.
[3:24] Change the thickness value to change the thickness of the slice.
[3:28] Then you can add a bevel to the cutter object to make the slice look around like this.
[3:33] You can add more segments to make the bevel rounder.
[3:38] You can also add a bevel to the original object.
[3:46] To create more than one slice, just keep adding solidify modifier to the cutter object.
[3:56] Make sure that they are above the bevel modifier.
[3:59] Adjusting thickness values will change the way it looks.
[4:12] You can create a lot of variation with just these modifiers.
[4:16] Select the cylinder, hold shift and select the cube.
[4:22] Then press Ctrl and minus on the numpad.
[4:26] Apply all modifiers and delete the cutter object.
[4:30] As you can see, some unnecessary further changes are made.
[4:34] You can also add a boolean modifier to the cutter object.
[4:38] As you can see, some unnecessary vertices are left over.
[4:42] We can fix this in a couple of ways.
[4:44] We can select them and then merge them one by one.
[4:50] Or we can turn on auto merge vertices.
[4:54] Then just slide the vertices to their neighbors by pressing G twice.
[4:58] The vertices are then merged automatically.
[5:01] Now we just have to repeat this step as we do the other vertices.
[5:04] To create some support loops around this hole, an easy way is to select the interfaces and press
[5:09] I to insert, but don't move the mouse.
[5:12] Then press Alt S and scale the selection inwards.
[5:16] Now add an inch loop on the inside with Ctrl R.
[5:24] Subdivide it, it looks perfect.
[5:28] Now we can add a new layer to the inside of the mouse.
[5:32] No boolean issues left.
[5:40] The weld modifier also comes in handy when cleaning up unnecessary vertices left over from boolean cutting.
[5:50] Simply add the weld modifier
[5:54] and turn on the on cage button so we can see the result in edit mode.
[5:58] Then increase the value until you get something that works.
[6:02] If you want to limit the modifier to a specific area, you can also use a vertex group.
[6:18] If you found this topic interesting and would like to know more, don't forget that you can find it in my Blender Secrets ebook.
[6:24] Along with almost 2000 pages of other tips.
[6:28] To get an idea of what the ebook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:24] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_000.jpg
- [1:00] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_001.jpg
- [1:47] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_002.jpg
- [3:28] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_003.jpg
- [3:59] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_004.jpg
- [4:38] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_005.jpg
- [5:16] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_006.jpg
- [5:58] tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/frame_007.jpg

---

## Structured Notes

### Core Technique
A full non-destructive Boolean hard-surface workflow: modifier-based Boolean Difference with hidden cutter objects, the BoolTool add-on's fast Ctrl+Numpad- destructive/live cutting, layered Solidify+Bevel cutters for rounded slice cuts, and multiple cleanup techniques (merge, auto-merge+slide, support-loop insets, and the Weld modifier) for the leftover geometry booleans leave behind.

### Summary
Frame 000 shows the base part being hand-shaped first: a folded L-bracket-style cube edited with Ctrl+Shift+B (vertex bevel, live Segments/Profile HUD visible) before any booleans are applied. Frame 001 shows the finished non-destructive setup: an L-bracket with 4 bolt-hole cylinders, modifier stack showing Solidify → Boolean (Difference, Fast solver, Object = Cylinder.001, arrow highlighting the Object field) — the cylinders are visible here only because Wire/render-visibility hasn't been toggled off yet in this shot. Frame 002 shows the BoolTool add-on's live-cut result: a cube with a smaller cube cutter still visible as an editable orange bounding box after Ctrl+Numpad-. Frame 003 shows the slice-cut technique: the cutter object (orange wireframe box) has a Solidify modifier (Thickness 0.06m, Offset -1.000, Even Thickness, Rim Fill) controlling slice width. Frame 004 shows the same cutter with a Bevel modifier added atop multiple Solidify modifiers (stack order: Solidify → Solidify.001 → Solidify.002 → Bevel), rounding the slice's edges. Frame 005 shows the Quick Favorites (Q) pie menu with "Apply All" highlighted — the one-click way to bake all modifiers at once (added via the Modifier Tools preference). Frame 006 shows leftover triangulated geometry (Alt-selected face loop, orange) at a boolean seam after Apply All — exactly the kind of "unnecessary vertices" the transcript warns about. Frame 007 shows the fix: a Weld modifier (Mode=All, Distance 0.001m, On Cage enabled) cleanly closing a circular boolean hole's leftover geometry, visible directly in Edit Mode.

### Key Steps
1. **Hand-shape the base part:** delete an edge, Ctrl+B to bevel another with scroll-wheel segment control, Shift+Ctrl+B to bevel corner vertices; in Object Mode, Shade Smooth + enable Auto Smooth; add a Solidify modifier and increase thickness for wall thickness.
2. **Non-destructive Boolean holes:** add a cylinder, scale it down, Shade Smooth + Auto Smooth; duplicate it as many times as needed and Ctrl+J to join all copies into one cutter object; add a Boolean modifier to the base object set to Difference with the joined cylinders as the target; hide the cutters visually by setting their Viewport Display Maximum Draw Type to Wire, or by disabling their render visibility in the Outliner; finish with a Bevel modifier on the base object for clean edges.
3. **BoolTool add-on for fast destructive/live cuts:** enable BoolTool in Preferences; model a cutter object; select the cutter, Shift-select the target object, press Ctrl+Numpad− to cut — the cutter stays visible/editable as a bounding box (move/rotate/scale it, or Tab into it and edit like a normal mesh, even duplicate its geometry for a quick array). If the cut doesn't register, nudge the cutter slightly. All other BoolTool operations live under the Edit tab in the N-panel.
4. **Workflow speed-ups:** add Shade Smooth, Auto Smooth, and Viewport Shading's Shadow/Cavity toggles to the Quick Favorites (Q) menu; enable the Modifier Tools add-on in Preferences to get an "Apply All" button that bakes the entire modifier stack in one click.
5. **Rounded slice cuts:** create a second cutter object, BoolTool Ctrl+Numpad− (Difference) against the target; select the cutter and add a Solidify modifier — its Thickness controls slice width; add a Bevel modifier to the cutter (more segments = rounder) to make the slice edge look rounded; a Bevel can also be added to the original object for softened outer edges. To create multiple slices, stack additional Solidify modifiers on the same cutter (keep them above the Bevel modifier in the stack) — varying each Solidify's thickness produces different slice-spacing variations from one cutter object.
6. **Cleaning up leftover boolean geometry:** after Ctrl+Numpad− and Apply All (then deleting the cutter), booleans often leave unwanted extra vertices/edges at the seam. Fix options: (a) select and merge (M) leftover vertices one at a time; (b) enable Auto Merge Vertices and slide stray verts onto their neighbors with G,G so they merge automatically, repeating around the seam; (c) for support loops around a boolean hole, select the inner faces, press I (Inset, don't move the mouse) then Alt+S to scale the inset inward along normals, add an inset loop cut with Ctrl+R and Subdivide it for a clean, boolean-issue-free support ring; (d) add a Weld modifier, enable "On Cage" so the result is visible directly in Edit Mode, and increase its Distance value until stray vertices merge — optionally limit its effect to a specific area via a Vertex Group.

### Nodes / Settings
- **Modifiers:** Boolean (Operation: Difference/Union/Intersect, Solver: Fast/Exact, Object target), Solidify (Thickness, Offset, Rim Fill — used both for wall thickness and for slice width on cutter objects, stackable for multiple slices), Bevel (on both cutter and target objects), Weld (Mode: All, Distance, On Cage, optional Vertex Group limiting).
- **Add-ons:** BoolTool (Ctrl+Numpad− live/destructive Boolean Difference, Edit tab for more operations), Modifier Tools (adds the "Apply All" quick-favorite operator).
- **Edit-mode operators:** Ctrl+B / Shift+Ctrl+B (edge/vertex bevel), Ctrl+J (join objects), M (merge vertices), G,G (edge slide, with Auto Merge Vertices enabled), I (inset faces), Alt+S (scale along normals), Ctrl+R (loop cut) + Subdivide.
- **Viewport/Outliner:** Maximum Draw Type = Wire (hide cutter geometry visually), render-visibility toggle in Outliner (hide from final render), Quick Favorites (Q) menu for Shade Smooth/Auto Smooth/Shadow/Cavity/Apply All.

### Difficulty
Intermediate

### Blender Version
Not specified — Boolean modifier's Fast/Exact solver naming and BoolTool add-on are consistent with modern Blender 2.9x-5.x.

### Tags
procedural, modelling, materials, intermediate

---

## Related Tutorials
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares procedural, materials, intermediate; same channel, complementary hard-surface modifier-stack workflow.
- [Blender Secrets - 5 minutes of N-Gons to Quads tips](blender-secrets---5-minutes-of-n-gons-to-quads-tips.md) — shares modelling, procedural, intermediate; directly relevant follow-up for cleaning up boolean-created n-gons.
- [Daily Blender Secrets - 10 ways to make Holes in Blender](daily-blender-secrets---10-ways-to-make-holes-in-blender.md) — shares modelling, procedural, intermediate; that tutorial surveys 9 other hole-cutting alternatives (Knife Project, LoopTools, curves, Carver, Box Cutter) alongside the same BoolTool method covered here in depth.
- [Daily Blender Secrets - 15 Tips Compilation (Part 2)](daily-blender-secrets---15-tips-compilation-part-2.md) — shares modelling, procedural, materials; that compilation's Tip 3 (Cut Tool) covers the same BoolTool cut-and-cleanup workflow as one of 13 shorter tips.
- [How do you model that? Wrench - Blender Secrets](how-do-you-model-that-wrench---blender-secrets.md) — shares modelling, procedural, intermediate; a real-world application of this tutorial's boolean cleanup techniques, cutting a pliers jaw notch and manually resolving the resulting messy topology.
- [Step by Step: Boolean Holes to Quad Topology | Blender Secrets](step-by-step-boolean-holes-to-quad-topology-blender-secrets.md) — shares modelling, procedural, intermediate; shares the same boolean-cleanup philosophy (Weld modifier, Auto Merge, support loops), applied here specifically to prepare a complex boolean-cut hole for subdivision.

---
title: Easy hole modeling for beginners - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=jrR1T-dIA8c
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 5 (explicitly named: \"Blender 5 has really nice matcaps\")"
tags: [modelling, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Easy hole modeling for beginners - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=jrR1T-dIA8c)
**Author:** Blender Secrets
**Duration:** 3m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] An easy way to add a circular hole is by beveling a vertex.
[0:03] You can do this by selecting a vertex and pressing Shift Ctrl B.
[0:07] Then scroll the mouse wheel up to add more segments.
[0:11] You can also increase or decrease the segments with the plus and minus keys on the numpad.
[0:16] Or, after left clicking to confirm, increase the segments in the operator panel.
[0:22] To make it round, adjust the profile shape to 0.0865.
[0:28] Or, even easier, right click and use Loop Tools, Circle for a perfect circle.
[0:33] Loop Tools is an extension that you need to enable in preferences.
[0:36] Then you can extrude these faces inwards.
[0:39] You can even do this with several vertices at once.
[0:43] And then press Alt E and choose Extrude Faces along normals.
[0:47] This works fine in a quick boolean workflow, but it creates endgones.
[0:51] Faces with more than four edges.
[0:53] Although in some cases endgones are fine even in a sub-diff workflow,
[0:57] if you're going for an old Kuat workflow, for scoping for example, you'll want to avoid endgones.
[1:02] In that case, you'll need at least three intersecting edge loops.
[1:06] In Edge Selection Mode, select two intersecting edges and press Ctrl B to bevel them.
[1:12] Here too, you can increase segments with the middle mouse button,
[1:15] or by pressing the plus key on the numpad.
[1:17] Or, after left clicking to confirm, by adjusting the segments in the operator panel.
[1:23] You need two segments to get three intersecting edges like this.
[1:27] Switch back to Vertex Selection Mode and bevel the vertex in the center as before with Shift
[1:32] Ctrl B. You can also do this by going to Vertex Bevel Vertices and move the mouse until you see
[1:39] it change. Adjust the profile in the operator panel or use Loop Tools Circle.
[1:44] Now to get all Kuat topology, select two vertices at a time while holding Shift,
[1:49] and then press J to connect them. Switch to Face Selection Mode and select the faces.
[1:55] Press E to extrude them to create a hole. If you don't want to keep those extruded faces,
[2:00] press Delete or X and choose Faces. Now when you add a sub-diff modifier,
[2:06] it will become more round but also smooth. To keep the corners sharp, you can do a couple of things.
[2:12] You can select the corner edges and increase them by pressing Shift E and 1 on the numpad.
[2:18] Or slide the mean crease value to the right in the option panel with those edges selected.
[2:24] Now despite the sub-diff modifier, the corner remains sharp.
[2:28] Alternatively, we can do some more beveling. With those edges selected, press Ctrl B and
[2:33] then move the mouse. You want a profile shape of one for this and two segments is enough to
[2:38] keep the corners sharp. The closer together those edge loops are, the sharper the corner will be.
[2:43] When exporting a mesh to other software, you want to add geometry like this to keep corners sharp,
[2:49] because creasing only works inside of Blender. Right-click and choose Shade Auto Smooth to
[2:54] make it look even smoother. Blender 5 has really nice matte caps that you can use to make your
[2:59] models more visually appealing in the viewport. Learning how to make holes, either with Booleans
[3:04] or with Subdivision Ready Topology, is one of the key skills that you need to have as a 3D artist.
[3:09] I've learned this the hard way, but I've struggled so you don't have to.
[3:13] I've connected all my knowledge about hole modeling in a new PDF, The Big Book of Holes.
[3:18] You can get this now on my website or on YouTube. If you already have my Big Blender
[3:22] Sequence book, you don't need this PDF as you already have all these topics in that book.
[3:26] So if you want to learn all there is about holes in 3D modeling, go and get that PDF.



---

## Captured Frames

- [0:03] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_000.jpg
- [0:22] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_001.jpg
- [0:28] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_002.jpg
- [0:47] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_003.jpg
- [1:06] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_004.jpg
- [1:49] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_005.jpg
- [2:04] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_006.jpg
- [2:14] tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Two escalating approaches to modeling a round hole: (1) a fast vertex-bevel + boolean-style extrude workflow that's quick but leaves n-gons, and (2) an all-quad, subdivision-ready topology workflow using three intersecting edge loops, edge bevels, and vertex-connect (J) — plus edge creasing/support-loop techniques to keep corners sharp under a Subdivision modifier.

### Summary
Frame 000 shows the starting point: a bare 2×2-subdivided plane in a trapezoid-shaped perspective view, before any hole work. Frame 001 shows the fast method's payoff mid-bevel: the center vertex bevel operator panel open (Width Type Offset, Profile Shape ~0.089) with a dense orange circular fan of new vertices at the plane's center. Frame 002 shows the same setup with the right-click context menu open, "Vertices" submenu visible — the point where LoopTools > Circle would be chosen for a perfect circle instead of manually tuning the bevel profile. Frame 003 shows the fast method scaled up to production use: a cube whose faces are covered in the extruded circular holes (Alt+E "Extrude Faces Along Normals" prompt shown), demonstrating the technique working at scale despite the resulting n-gons. Frame 004 shows the start of the all-quad method: two intersecting orange edge loops crossing the plane's center, with a Bevel operator panel open (Width Type Offset, Width 0.32m, Loop Slide enabled) — beveling the two crossing edges to produce the three-intersecting-edge-loop pattern the quad topology needs. Frame 005 shows a close, wireframe-style view of the resulting octagon-like vertex ring at the intersection after the edge bevel and center vertex bevel are both applied — the geometry about to be connected pairwise with J. Frame 006 shows the completed all-quad hole: a clean octagonal hole extruded into the plane with a Subdivision modifier applied (Catmull-Clark, Levels Viewport 4, Optimal Display), rounding the opening smoothly. Frame 007 shows the same hole with the Subdivision modifier's "Display modifier in Edit Mode" icon being disabled (highlighted with a red arrow, tooltip "By disabling this icon, the modifier is disabled in Edit Mode, making it easier to work"), a workflow tip for editing underlying cage geometry without visual clutter.

### Key Steps
**Fast method (creates n-gons):**
1. Select a single vertex where the hole should go and press Shift+Ctrl+B to bevel it into a circular vertex fan; scroll the mouse wheel (or use Numpad +/−, or the operator redo panel) to add more segments.
2. Set the bevel's Profile Shape to ≈0.0865 for a rounded circular profile, or simply right-click and choose LoopTools > Circle (requires enabling the LoopTools add-on in Preferences) for a mathematically perfect circle instead of hand-tuning the profile.
3. Select the resulting circular face(s) — this works for several holes selected at once — and press Alt+E > Extrude Faces Along Normals to punch the hole inward.
4. Trade-off: this quick boolean-style workflow produces n-gons (faces with 5+ edges) at the hole boundary. N-gons are acceptable in many boolean or non-subdivided workflows, but must be avoided for a clean subdivision ("all-quad") workflow, e.g. hard-surface sculpting prep.

**All-quad method (subdivision-ready, no n-gons):**
1. In Edge Select mode, select two intersecting edges at the hole location and press Ctrl+B to bevel them together, needing 2 segments to produce three intersecting edge loops (adjust segment count via middle-mouse-drag, Numpad +, or the redo panel).
2. Switch back to Vertex Select mode and bevel the now-present center vertex with Shift+Ctrl+B as before, adjusting the profile in the redo panel or using LoopTools > Circle.
3. Select vertex pairs around the ring two at a time (Shift-click) and press J (Connect Vertex Path) to stitch them into all-quad faces.
4. Switch to Face Select mode, select the resulting center faces, and press E to extrude them into the hole (or press X/Delete > Faces to just remove them for an open hole).
5. A Subdivision Surface modifier now rounds the hole smoothly since there are no n-gons to distort — but it will also round off the mesh's outer corners unintentionally.
6. To keep specific corners sharp under Subdivision: either select the corner edges and press Shift+E then type 1 on the numpad to set Edge Crease to maximum (crease only works inside Blender, not on export), or add extra support-loop geometry via Ctrl+B on those edges with Profile Shape 1 and 2 segments — the closer together the two loops, the sharper the corner stays; this geometry-based approach is required when exporting to other software since creasing doesn't survive export.
7. Finish with Shade Auto Smooth (right-click menu) for a smoother viewport look; Blender 5's matcaps are called out as a nice way to preview hard-surface models like this in the viewport.

### Nodes / Settings
- **Vertex Bevel:** Shift+Ctrl+B, Width Type: Offset, adjustable Segments and Profile Shape (≈0.0865-0.089 for round).
- **Edge Bevel:** Ctrl+B on two intersecting edges, 2 Segments needed for 3 resulting intersecting loops, Loop Slide enabled.
- **LoopTools add-on:** Circle operator (enable in Preferences) for perfect circular vertex rings, used on both the vertex-bevel fan and the edge-bevel ring.
- **Connect Vertex Path:** J, applied pairwise around the ring to build all-quad faces.
- **Extrude:** E (faces), Alt+E > Extrude Faces Along Normals (multi-selection extrude for the fast method).
- **Edge Crease:** Shift+E, then 1 on the numpad for max crease (Blender-only, doesn't survive export).
- **Subdivision Surface modifier:** Catmull-Clark, Levels Viewport (seen at 4), Optimal Display, "Display modifier in Edit Mode" toggle for cleaner editing.
- **Shading:** Shade Auto Smooth (right-click context menu).

### Difficulty
Beginner (fast method) to Intermediate (all-quad topology method)

### Blender Version
Blender 5 — explicitly named in the transcript ("Blender 5 has really nice matcaps that you can use to make your models more visually appealing in the viewport").

### Tags
modelling, procedural, beginner, intermediate

---

## Related Tutorials
- [Daily Blender Secrets - 10 ways to make Holes in Blender](daily-blender-secrets---10-ways-to-make-holes-in-blender.md) — shares modelling, procedural; that survey's "Bevel vertex" and "LoopTools Circle" methods (#3-4) are the same fast technique taught here in more depth, alongside this video's added all-quad topology method.
- [Daily Blender Secrets - 15 Tips Compilation (Part 2)](daily-blender-secrets---15-tips-compilation-part-2.md) — shares modelling, procedural; Tips 5-6 (Bevel Holes, Round Holes with Quad Topology) cover both the fast and all-quad hole methods taught here, as two of many shorter tips.
- [For Beginners: Easiest Modeling Technique (long version)](for-beginners-easiest-modeling-technique-long-version.md) — shares modelling, procedural; that video's robot build applies this same fast vertex-bevel hole method as one step in a much larger blockout-to-detail workflow.

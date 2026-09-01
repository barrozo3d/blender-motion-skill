---
title: Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)
source: YouTube
url: https://www.youtube.com/watch?v=hpFaDiTDZgc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.2.2 -- observed in frame_000"
tags: [cloth, simulation, materials, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)

**Source:** [YouTube](https://www.youtube.com/watch?v=hpFaDiTDZgc)
**Author:** Blender Secrets
**Duration:** 5m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In Edit Mode, scale the cube down by pressing S, Z and 0.01 on the numpad.
[0:21] Add edge loops with Ctrl R and increase the number of cuts.
[0:27] Add a closed modifier and go to the properties.
[0:31] Under field weights, set gravity to 0.
[0:34] Enable pressure and set it to 1.
[0:39] Press the spacebar to play the simulation or click on bake.
[0:47] Find the frame where the pillow looks the best and apply the closed modifier.
[0:52] Hold Alt and click on a face in the middle to select the row of faces.
[0:56] Press Alt E and choose Extrude along normals.
[1:01] Add a sub-div modifier, right click and choose Shade Smooth.
[1:08] Using the Cloth Brush in Sculpt mode, you can add some wrinkles and variation.
[1:22] In Edit Mode, select edges where you want to add decorative edges.
[1:26] To duplicate the selection and separate it to a new object.
[1:30] With only the new object selected, go to Object, Convert, Curve.
[1:34] Give the curve some depth and enable Shade Smooth.
[1:39] If the object has more complicated geometry like a 3D scanned sofa, it's a little different.
[1:46] Turn on snapping to face and project individual elements.
[1:50] Select, duplicate and separate one vertex.
[1:54] Convert it to create the edge by pressing E or holding Ctrl and right clicking.
[2:14] Convert it to a curve and give it depth as explained before.
[2:18] If you want rounder corners, subdivide some vertices and smooth them a few times.
[2:36] Add a cube.
[2:39] Subdivide it twice in Edit Mode.
[2:41] From the face menu, choose Poke Faces.
[2:44] Then choose Trice to Quad.
[2:46] Choose Poke Faces again and press Shift R to repeat.
[2:50] In Vertex Selection mode, select one of the vertices that are at the center of 16 edges.
[2:56] Then go to Select, select Similar, Amount of Connecting Edges.
[3:01] Press Shift Ctrl B to bevel the selected vertices.
[3:05] In Face Selection mode, press Alt E and choose Extrude Along Face Normals.
[3:10] You can extrude the face inwards.
[3:12] Don't deselect anything yet.
[3:14] Press Alt E and choose Extrude Along Face Normals again.
[3:18] This time extrude them to slightly outside the cube.
[3:22] Press Ctrl plus on the numpad twice to grow the selection.
[3:25] That transforms pivot points to individual origins.
[3:29] Then press S and scale selection inwards.
[3:32] In Object Mode, right click and choose Shades Moves.
[3:35] Finally, press Ctrl 1 to add a level of subdivisions.
[3:51] To drape a piece of cloth over one of these objects, add a plane and place it above that object.
[3:57] In Edit Mode, right click and choose Subdivide.
[4:01] Press Shift R a couple of times to add more subdivisions.
[4:04] You'll need these subdivisions later for the class deformations to work.
[4:08] Enable Collision for any object that you want the class to interact with.
[4:15] Select the vertex on the plane and assign it to a new vertex group.
[4:19] Press Ctrl H to add a new hook to the vertex.
[4:25] Enable Class Physics for the plane.
[4:29] Use the vertex group as a pin group.
[4:33] Enable Self-Collisions for more realism.
[4:39] Start the simulation by pressing the space bar from the first frame on the timeline.
[4:44] Now you can use the hook to move the cloth object around.
[5:04] If you found this topic interesting and would like to know more,
[5:07] don't forget that you can find it in my Blender Secrets ebook,
[5:10] along with almost 2,000 pages of other tips.
[5:14] To get an idea of what the ebook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:39] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_000.jpg
- [1:08] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_001.jpg
- [1:34] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_002.jpg
- [2:18] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_003.jpg
- [2:44] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_004.jpg
- [3:18] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_005.jpg
- [3:35] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_006.jpg
- [4:44] tutorials/frames/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in/frame_007.jpg

---

## Structured Notes

### Core Technique
Four ArchViz soft-furnishing techniques: a gravity-free Cloth-sim pillow, curve-based decorative piping/edges (including a version that hugs complex 3D-scanned geometry), diamond-tufted button upholstery via Poke Faces + Bevel + dual Extrude-Along-Normals, and a draped cloth simulation pinned/moved with a hook.

### Summary
Frame 000 shows the pillow setup: a subdivided plane with a Cloth modifier, Field Weights Gravity set to 0, and Pressure enabled — ready to bake into a puffed pillow shape with no gravity sag. Frame 001 shows the payoff after baking + Subdivision + Shade Smooth + Cloth Brush detailing in Sculpt Mode: a soft, wrinkled pillow. Frame 002 shows a duplicated/separated edge loop (from a simple cube) about to be converted to a Curve for decorative piping. Frame 003 shows the more advanced version on a scanned armchair: a curve with Bevel Depth and a Taper Object, snapped along the complex organic upholstery seam (Shift indicator visible, Curve Deform panel open). Frame 004 shows diamond-tufting step 1: the Face menu open with Poke Faces highlighted, about to be run on a twice-subdivided cube. Frame 005 shows the mid-process result: Alt+E "Extrude Region and Shrink/Fatten" pulling the beveled diamond-pattern vertices inward, creating dimpled indentations across the cube's faces. Frame 006 shows the finished diamond-tufted button-upholstery cube — a dense, symmetric quilted pattern with pronounced button divots at each diamond intersection. Frame 007 shows the final technique: a cloth-simulated drape sagging naturally over a box, being pulled/reshaped interactively via a hook (three axis-handle lines visible at the pull point).

### Key Steps
1. **Gravity-free pillow (Cloth sim):** scale a cube flat (S, Z, 0.01) to make a thin plane; add edge loops (Ctrl+R, increase cuts for resolution); add a Cloth modifier; under Field Weights set Gravity to 0 and enable/set Pressure to 1 (this inflates the cloth like a balloon instead of letting it sag); press Spacebar or Bake to run the sim; scrub to the frame where the pillow shape looks best and Apply the Cloth modifier to freeze it as a static mesh.
2. **Pillow corner detail + wrinkles:** Alt-click a face in the middle to select a full face-loop/ring; Alt+E → Extrude Along Normals to add a corner seam; add a Subdivision modifier and Shade Smooth; switch to Sculpt Mode and use the Cloth Brush to hand-add wrinkles and asymmetric variation for realism.
3. **Decorative piping/edges (simple geometry):** in Edit Mode select the edges you want piped, duplicate and Separate (P) them into a new object; with only that new object selected, Object → Convert → Curve; give the curve some Bevel Depth and enable Shade Smooth to get a rounded piping profile.
4. **Decorative piping on complex/scanned geometry:** enable snapping to Face; select, duplicate, and separate a single vertex; extrude it along the seam by pressing E or Ctrl+RMB-click repeatedly to build up the edge path vertex by vertex; convert to a Curve and add Bevel Depth as before. For rounder corners, subdivide a few extra vertices at the corners and run Smooth Vertices a couple of times.
5. **Diamond tufting (button upholstery):** start from a cube, subdivide twice in Edit Mode; Face menu → Poke Faces, then Face menu → Tris to Quads, then Poke Faces again (Shift+R to repeat the last operator quickly). In Vertex select mode, pick one of the vertices with 16 connecting edges (the diamond-pattern centers), then Select → Select Similar → Amount of Connecting Edges to grab all of them at once; Ctrl+Shift+B to bevel just those vertices. In Face select mode, Alt+E → Extrude Along Face Normals to push faces inward for the recessed diamond channels, then immediately Alt+E → Extrude Along Face Normals again (without deselecting) to push a second set slightly outward for the puffed button faces; grow the selection twice with Ctrl+Numpad+ (this also switches pivot point to Individual Origins), then S to scale each selection inward for the button-divot taper. Shade Smooth in Object Mode, then Ctrl+1 to add one level of Subdivision Surface for the final soft quilted look.
6. **Draped cloth with an interactive hook:** add a plane above the target object, Subdivide (right-click → Subdivide) and Shift+R a few more times for enough resolution for the cloth to deform correctly; enable Collision on the object(s) the cloth should drape over; select one plane vertex, assign it to a new Vertex Group, Ctrl+H to add a Hook to that vertex; enable Cloth physics on the plane, set the new vertex group as the Pin Group, enable Self-Collisions for extra realism; press Spacebar from frame 1 to run the sim, then use the hook (an Empty) to interactively drag and reshape the draped cloth.

### Nodes / Settings
- **Modifiers:** Cloth (Field Weights → Gravity 0, Pressure 1 for the pillow; Pin Group + Self-Collisions for the drape), Subdivision Surface, Bevel (on curve piping via Bevel Depth + Taper Object), Curve Deform.
- **Sculpt:** Cloth Brush (wrinkle/variation detailing on the finished pillow).
- **Mesh ops:** Poke Faces, Tris to Quads, Select Similar → Amount of Connecting Edges, Bevel Vertices (Ctrl+Shift+B), Extrude Along Face Normals (Alt+E), Ctrl+Numpad+ (grow selection / switch pivot to Individual Origins).
- **Rigging-lite:** Vertex Group + Hook modifier (Ctrl+H) for interactive cloth manipulation via an Empty.
- **Object conversion:** Object → Convert → Curve (turns a duplicated edge selection into a beveled piping profile).

### Difficulty
Intermediate

### Blender Version
Not specified — core modifier/mesh-editing/Cloth-sim workflow, version-agnostic across modern Blender (3.x-5.x).

### Tags
cloth, simulation, materials, procedural, intermediate

---

## Related Tutorials
- [Realistic Cloth Physics in Blender – Full Tutorial](realistic-cloth-physics-in-blender-full-tutorial.md) — shares cloth, simulation, intermediate; direct complement (general cloth-sim fundamentals vs. these applied ArchViz recipes).
- [15 Blender Secrets (Compilation of 15 Blender Tutorials in 11 minutes)](15-blender-secrets-compilation-of-15-blender-tutorials-in-11-minutes.md) — shares materials, cloth, simulation, intermediate; same channel, overlapping cloth-curtain-to-mesh technique.
- [Interactive Cloth + new Cloth Brushes & more - Blender Secrets](interactive-cloth-new-cloth-brushes-more---blender-secrets.md) — shares cloth, simulation, intermediate; this video's "Interactive Cloth" pillow-placement tip is expanded into a full dedicated tutorial there, covering the Hook+Pin-Group rig and Blender 4.3's Cloth sculpt brushes in depth.

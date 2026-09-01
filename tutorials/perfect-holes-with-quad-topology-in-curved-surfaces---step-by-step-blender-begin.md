---
title: Perfect Holes with Quad Topology in Curved Surfaces - Step by step Blender beginner version
source: YouTube
url: https://www.youtube.com/watch?v=bfdI_-ymkas
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.0.0 -- observed in frame_000"
tags: [modelling, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Perfect Holes with Quad Topology in Curved Surfaces - Step by step Blender beginner version

**Source:** [YouTube](https://www.youtube.com/watch?v=bfdI_-ymkas)
**Author:** Blender Secrets
**Duration:** 4m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This method of making holes is useful when you want to make a perfectly circular hole in a curved surface.
[0:08] Press Shift A and add a cylinder.
[0:11] As cap fill type we choose nothing.
[0:16] I'm just going to move this up on the Z-axis by pressing G, Z and 1 on the numpad and then pressing Enter.
[0:24] In Edit Mode I'll add some horizontal edge loops by pressing Ctrl R and scrolling the mouse wheel up.
[0:31] Left click to confirm, then right click to cancel the transformation.
[0:36] In Object Mode add a couple of levels of subdivision by pressing Ctrl 2 just to make it smoother.
[0:43] And right click and choose Shade Smooth.
[0:47] Press Shift D to duplicate the cylinder and right click to cancel the transformation so that it's exactly in the same location as the original.
[0:56] We can disable the viewport visibility of the duplicate.
[1:02] In Edit Mode select a square of faces.
[1:06] Right click and choose Loop Tools, Circle to make the selection circular.
[1:11] I'll disable the Subdiv modifier temporarily so that you can see better what I'm doing next.
[1:19] Inset the selection with I to create a loop of faces around the hole.
[1:23] This helps to protect the boundary when it's subdivided later.
[1:27] Extrude Inwards for another loop of faces for boundary protection.
[1:31] Then extrude again to create some depth.
[1:33] Then extrude and insert a little bit again for some more boundary protection face loops.
[1:38] Now if we turn the Subdiv modifier back on we can see what that gets us.
[1:44] We can see the surface better by using a Matte Cap, especially one that shows imperfections.
[1:51] You can see that the area around the hole is quite lumpy.
[1:55] There are some Matte Caps that are specifically designed to spot lumpy surfaces like this.
[1:59] Ideally those lines should be straight, like at the back of the hole.
[2:03] I'll show you how to fix this.
[2:05] First increase the selection in Edit Mode by pressing Ctrl and plus on the numpad.
[2:11] Create a new vertex group.
[2:14] And click on Remove to give the selection a weight of 0.
[2:18] Press Ctrl I to invert the selection and click on Assign to give that selection a weight of 1.
[2:24] In Weight Pane Mode we can see these values are very similar to the ones in the previous video.
[2:30] In Weight Pane Mode we can see these values as colors.
[2:34] Everything that's red has a value of 1 and the blue part has a value of 0.
[2:42] I'll go back to Edit Mode by pressing Tab and I'll turn the Subdiv modifier on again.
[2:49] Let's use a shiny Matte Cap so we can inspect the surface better.
[2:54] Add a Shrinkwrap modifier to the cylinder.
[2:58] And as the target, pick the duplicate of the cylinder.
[3:02] This destroys the hole so we need to exclude it from the modifier by using the vertex group.
[3:08] Now we have a perfect hole.
[3:10] You can see the difference the Shrinkwrap modifier makes when I turn the modifier off.
[3:18] This Matte Cap makes it even more obvious.
[3:22] Now what happens if we try to apply the Shrinkwrap modifier?
[3:27] Unfortunately that brings back the lumpiness of the surface so let's undo that with Ctrl Z.
[3:33] Instead press Ctrl A and choose Visual Geometry to Mesh to apply all the modifiers at once.
[3:39] Now we keep the perfect surface.
[3:41] However, it also means that we have a lot of subdivided geometry which may not be what we want.
[3:47] We can solve this by adding a Decimate modifier.
[3:51] Set it to Unsubdivide and use an even number of iterations.
[3:55] First let's try a value of 2.
[3:58] Apply the modifier.
[4:01] In Edit Mode you can see that the geometry is less dense and we still keep the smooth surface.
[4:08] We can add a subdivid modifier to it to make it more smooth.
[4:16] Let's see if we can unsubdivide it one more time to make the geometry even simpler.
[4:21] Again use an even number and then apply the modifier.
[4:26] As you can see when I add a subdivid modifier back on it with two levels we keep the perfectly smooth surface.
[4:32] But with a lower resolution geometry.
[4:36] How high or low the resolution needs to be depends on your use case.
[4:41] For example a game might be low poly with normal maps for detail,
[4:45] but on the other hand a movie asset may be sculpted on so it can be very high poly.



---

## Captured Frames

- [0:47] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_000.jpg
- [1:19] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_001.jpg
- [1:51] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_002.jpg
- [2:34] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_003.jpg
- [3:08] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_004.jpg
- [3:18] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_005.jpg
- [3:39] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_006.jpg
- [4:26] tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/frame_007.jpg

---

## Structured Notes

### Core Technique
A quad-topology circular hole cut into a curved (cylindrical) surface using boundary-protection inset/extrude loops around the opening — plus a key trick to eliminate the "lumpy" distortion that a Subdivision modifier otherwise introduces near the hole: a Shrinkwrap modifier targeting an undisplaced duplicate of the surface, excluded from the hole area via a vertex group, then baked and optionally decimated back down for a lean final mesh.

### Summary
Frame 000 shows the starting cylinder (Cap Fill Type: None, Shade Smooth, a Subdivision modifier in the sidebar) — the base curved surface the hole will be cut into. Frame 001 shows the hole location selected: a square patch of faces on the cylinder's side, right-click LoopTools menu open, about to run Circle to make the selection perfectly round. Frame 002 shows the result after inset/extrude boundary-protection loops and depth extrusion, viewed with the Subdivision modifier re-enabled and a matte/studio-lighting Material Preview setup — a clean circular recessed hole in the curved wall. Frame 003 shows the diagnostic step: Weight Paint mode with the whole surface colored solid red (Weight 1) except a distinct blue ring around the hole boundary (Weight 0) — the vertex group used to protect/exclude the hole area from the upcoming Shrinkwrap modifier. Frame 004 shows the fix applied: a Shrinkwrap modifier in the sidebar (Wrap Method: Nearest Surface Point, Target: the duplicate cylinder, Vertex Group: the hole-exclusion group highlighted in red) — the cylinder now reads as a perfectly smooth curved surface again, hole intact, under a chrome/reflective Matcap. Frame 005 shows the same result under a striped "lumpiness-revealing" Matcap — confirming the stripes run perfectly straight and even across the surface (no distortion), aside from a small tightening right at the hole. Frame 006 shows the Convert To Mesh dialog open (Target: Mesh, Keep Original, Merge UVs) — the "Ctrl+A > Visual Geometry to Mesh" step that bakes all modifiers (Subdivision + Shrinkwrap) into real geometry. Frame 007 shows the final, simplified result: the same perfectly smooth hole-in-cylinder shape after adding a Decimate modifier (visible as a fresh "Add Modifier" prompt in the sidebar, i.e. right after applying the decimation pass) — proving the surface stays smooth even at reduced polygon density.

### Key Steps
1. **Base shape:** Shift+A > Cylinder with Cap Fill Type set to None; move it into position (G, Z, 1, Enter); in Edit Mode add horizontal edge loops with Ctrl+R, scroll to add several, left-click to confirm placement then right-click to cancel the slide transform (keeping them evenly spaced); in Object Mode add a Subdivision modifier at 2 levels (Ctrl+2) for smoothness; Shade Smooth.
2. **Create an undisplaced reference duplicate:** Shift+D to duplicate the cylinder, immediately right-click to cancel the move so it sits exactly on top of the original; disable this duplicate's viewport visibility — it will later serve as the Shrinkwrap target, i.e. the "ideal" smooth surface without a hole.
3. **Cut the hole:** in Edit Mode, select a square patch of faces where the hole should go; right-click > LoopTools > Circle to make that selection perfectly round; temporarily disable the Subdivision modifier for a clearer view; Inset (I) to create a boundary-protection loop around the hole (protects the edge from distortion once subdivided); Extrude inward for a second protection loop; Extrude again for hole depth; Extrude + Inset once more for additional boundary protection near the bottom of the hole.
4. **Diagnose the subdivision "lumpiness":** re-enable the Subdivision modifier; switch to a Matcap specifically designed to reveal surface imperfections (grazing/striped matcaps make uneven curvature obvious) — the area immediately around the hole will look lumpy/uneven compared to the perfectly straight lines elsewhere on the cylinder.
5. **Build the hole-exclusion vertex group:** in Edit Mode, grow the current selection around the hole with Ctrl+Numpad+; create a new Vertex Group; with that (grown) selection active, click Remove to assign it a weight of 0; Ctrl+I to invert the selection, then click Assign to give the rest of the mesh a weight of 1. Weight Paint mode confirms this visually — red (weight 1) everywhere except a blue ring (weight 0) around the hole.
6. **Apply the Shrinkwrap fix:** back in Edit Mode with the Subdivision modifier re-enabled, add a Shrinkwrap modifier to the cylinder targeting the hidden duplicate cylinder; because Shrinkwrap would otherwise "erase" the hole by snapping it back to the duplicate's unbroken surface, restrict its effect via the vertex group created in step 5 (weight-0 hole area excluded, weight-1 elsewhere included) — the result is a perfectly smooth, undistorted curved surface everywhere except exactly where the hole is meant to be. Toggling the modifier off and on (or comparing matcaps) makes the before/after difference obvious.
7. **Bake correctly (important gotcha):** simply applying the Shrinkwrap modifier directly brings back the original lumpiness, since Apply re-evaluates the modifier stack in a way that reintroduces the distortion — undo that (Ctrl+Z) and instead use **Ctrl+A > Visual Geometry to Mesh**, which bakes the entire modifier stack (Subdivision + Shrinkwrap) at once and correctly preserves the smooth, fixed surface.
8. **Reduce resulting density if needed:** this baking approach leaves heavily subdivided geometry, which may be more than necessary; add a Decimate modifier set to **Un-Subdivide** with an even number of iterations (try 2 first) and apply it — geometry becomes much less dense while the surface, once a Subdivision modifier is added back, remains perfectly smooth; repeat Un-Subdivide (again with an even iteration count) for an even lighter mesh if desired. How much to simplify depends on the use case — real-time/game assets favor low-poly with normal maps, while film/VFX assets can stay very high-poly (e.g. sculpted).

### Nodes / Settings
- **Modifiers:** Subdivision Surface (Catmull-Clark, 2 levels via Ctrl+2), Shrinkwrap (Wrap Method: Nearest Surface Point, Target: undisplaced duplicate, Vertex Group: hole-exclusion group), Decimate (Un-Subdivide mode, even iteration counts).
- **Selection/weighting:** LoopTools > Circle (perfect circular selection), Ctrl+Numpad+ (grow selection), Vertex Group Remove/Assign (weights 0 and 1), Weight Paint mode (visual verification).
- **Modeling:** Inset (I), Extrude (E) — boundary-protection loop pattern around the hole.
- **Finalizing:** Ctrl+A > Visual Geometry to Mesh (correct way to bake Subdivision + Shrinkwrap together, vs. a plain Apply which reintroduces distortion).
- **Diagnostics:** grazing/striped Matcaps designed to reveal surface lumpiness.

### Difficulty
Beginner to Intermediate (the video is explicitly labeled a "step by step Blender beginner version")

### Blender Version
Not specified — the Shrinkwrap + vertex-group-exclusion technique is a standard modifier workflow available since Blender 2.8+.

### Tags
modelling, procedural, beginner, intermediate

---

## Related Tutorials
- [Daily Blender Secrets - 10 ways to make Holes in Blender](daily-blender-secrets---10-ways-to-make-holes-in-blender.md) — shares modelling, procedural; that survey covers flat-surface hole techniques, this video solves the specific problem of keeping a hole's *surrounding curved surface* perfectly smooth.
- [Easy hole modeling for beginners - Blender Secrets](easy-hole-modeling-for-beginners---blender-secrets.md) — shares modelling, procedural, beginner, intermediate; shares the same boundary-protection inset/extrude loop pattern around a circular hole, applied here specifically to a curved surface with the added Shrinkwrap fix.
- [Step by Step: Boolean Holes to Quad Topology | Blender Secrets](step-by-step-boolean-holes-to-quad-topology-blender-secrets.md) — shares modelling, procedural; the advanced version of this same Shrinkwrap+vertex-group curvature-preservation trick, applied to a complex (heart-shaped) boolean-cut hole instead of a simple circle.

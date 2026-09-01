---
title: Modeling a Devil Fruit from One Piece - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=_-a8k2LaZbA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.3.0 Alpha -- observed in frame_000"
tags: [organic, procedural, modelling, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Modeling a Devil Fruit from One Piece - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=_-a8k2LaZbA)
**Author:** Blender Secrets
**Duration:** 6m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's make this devil fruit.
[0:02] Start by adding an icosphere.
[0:04] With two subdivisions we have the amount of detail that we need.
[0:07] Add a subdiff modifier.
[0:09] This gives us geometry that helps place these world shapes more evenly,
[0:12] especially when using the cavity option in viewport overlays.
[0:17] You could use a curve, but I find it easier to start with a vertex.
[0:20] Collapse any primitive in edit mode to get one vertex,
[0:23] and then just extrude it to get the shape that you want.
[0:26] After that, you can convert it to a curve.
[0:29] Now that it's a curve, it's easy to give it some thickness by increasing the depth value.
[0:34] Shade Smooth to make it easier on the eyes.
[0:36] You can fine-tune the curve by moving the individual vertices.
[0:39] By pressing Alt S, the thickness around the vertices can be adjusted.
[0:43] To get the curve to end in a spherical shape, we need to convert it back to a mesh.
[0:48] You can do that by pressing Ctrl A and choosing visual geometry to mesh,
[0:52] or by choosing convert to mesh.
[0:56] Add a subdiff modifier to make it all smoother.
[0:59] Enable on-cage on the modifier to see better what you're getting as you fine-tune the shape in edit mode.
[1:04] To get the spherical shape here, we need to fill the gap first.
[1:08] To do that, select the boundary loop and press Ctrl F, and then choose grid fill.
[1:13] Moving the middle face already gives it a more spherical shape.
[1:17] Pressing Ctrl and plus on the numpad grows the selection.
[1:21] Then by pressing E, we extrude the selection, which gives us another loop around the spherical end of this shape,
[1:27] and scale it up by pressing S, or even better Alt S, which scales along the normal directions.
[1:32] Now it's just a matter of fine-tuning the shape to your liking in edit mode.
[1:36] Make sure that the 3D cursor is at world origin, and set the transform orientation to 3D cursor,
[1:42] so you can transform around it as a pivot point.
[1:45] Select all in edit mode by pressing A, then press Shift D, S, X, and type minus 1 on the numpad, and press Enter.
[1:53] In other words, Shift D to duplicate, then scale it to negative 1 on the X axis.
[1:58] This also flips the normals in the wrong direction, so press Shift N to fix that while everything is still selected.
[2:05] Rotate the duplicated part 180 degrees on the X axis by pressing R, X, and 180 on the numpad, and pressing Enter.
[2:13] To make sure it's connected here, select all vertices and press M, then choose Collapse by Distance.
[2:19] Now we can dissolve some edge loops and adjust the shape in edit mode.
[2:23] It's easier to select all the vertices with X-ray mode enabled.
[2:30] We need to rotate the whole object slightly to make it more symmetrical.
[2:34] Don't forget to turn transform orientation back to medium.
[2:38] After some further fine-tuning, we get a nice swirly shape.
[2:42] Finally, give it a name.
[2:43] To make it easy to deform the swirl geometry to fit on the surface of the aquasphere, we'll need some simple geometry to bind it to first.
[2:51] So add a plane and scale it to fit around the swirl in edit mode.
[2:55] Add an edge loop to make the geometry more evenly divided and subdivide it a few times in edit mode.
[3:00] Set the visibility of the plane to wireframe so you can still see it, but also see through it.
[3:06] If you have a sub-diff modifier on the swirl, make sure that the viewport and render levels are the same before the next step.
[3:13] Otherwise, the surface-diff form modifier won't work properly.
[3:17] Now add a surface-diff form modifier to this swirl geometry and pick the plane as the target.
[3:22] Then click on bind.
[3:25] Now, moving the vertices of the plane in edit mode deforms the swirl geometry.
[3:30] This is especially effective with proportional editing.
[3:32] We also want the swirl to follow the plane in object mode, so it's easier to place both on the surface of the aquasphere.
[3:38] To achieve this, select the swirl, hold shift and select the plane.
[3:42] Press Ctrl P and parent the swirl to the plane.
[3:45] Now, moving the plane in object mode makes the swirl follow along.
[3:49] We can move these two to the side and unhide the aquasphere.
[3:52] Duplicate both the swirl and plane in object mode with Shift D.
[3:56] Then move it to the aquasphere.
[3:58] By holding Ctrl, it snaps to the surface, which makes it easier to place it where you want.
[4:03] You'll also need to scale and rotate it to fit.
[4:09] Once it's in a good spot, add a shrink wrap modifier to the plane.
[4:12] Choose the aquasphere as the target.
[4:14] It works best with the project option and both negative and positive options checked.
[4:19] This makes the plane conform to the aquasphere and in turn the swirl follows the shape of the plane.
[4:25] Now it's just a matter of duplicating these objects again and fitting the aquasphere with them.
[4:29] You can save some time by copying the scale of this plane to the original plane,
[4:33] so that you don't have to scale it down every time you duplicate it.
[4:39] And instead of adding the shrink wrap modifier manually each time,
[4:43] you can select the plane you're currently placing, hold shift and select a previously placed plane.
[4:48] Then press Ctrl L and choose modifiers to copy the shrink wrap modifier, including the correct settings.
[4:53] After repeating these steps, the aquasphere is full of swirls.
[4:57] If you render this and these swirls don't follow the curvature of the sphere in the render,
[5:01] that's because you need to have the same level of subdivisions for both viewport and render.
[5:06] So make sure those are all the same.
[5:08] Now let's make the stem.
[5:10] Hold shift and right click here to put the 3D cursor there.
[5:13] Then add a single vertex or add any primitive and collapse it to a single vertex.
[5:17] Extrude it in edit mode to make the shape of the stem.
[5:20] Separate the horizontal and vertical parts by deleting an edge.
[5:24] Then separate them by selecting all and pressing P, then choose separate by loose parts.
[5:29] Convert it to a curve and then add some thickness to it.
[5:32] You can scale the vertices with all S just like we did with the swirl.
[5:36] The very end can be scaled to zero, so it ends in a sharp point.
[5:40] Convert the vertical parts to a curve and give it thickness as well.
[5:43] To make sure there's no hole here, check the fill caps option.
[5:47] Then convert it back to a mesh.
[5:49] You can turn these triangles to quads by selecting them in face selection mode and pressing Alt J.
[5:54] If it doesn't work for all of them, select two triangles and press F to turn them into a quad.
[5:59] We can inset this selection and add in edge loop to protect this corner from the subdiff modifier.
[6:05] And that's it, we've modeled the devil fruit.
[6:08] On my Patreon you can find the longer version of this video as well as the blend file.
[6:12] Thank you for watching until the end.



---

## Captured Frames

- [0:04] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_000.jpg
- [0:34] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_001.jpg
- [1:08] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_002.jpg
- [1:53] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_003.jpg
- [3:22] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_004.jpg
- [4:03] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_005.jpg
- [4:53] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_006.jpg
- [5:40] tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Modeling a One Piece "Devil Fruit" (a swirly, spiral-patterned sphere): swirl shapes are built as vertex-to-curve extrusions with adjustable thickness, mirrored into a full spiral, then bound to a flat wireframe plane via a Surface Deform modifier so the plane's placement (via Shrinkwrap onto the base sphere) drags the swirl along and conforms it to the sphere's curvature.

### Summary
Frame 000 shows the base shape: a two-subdivision Icosphere with a Subdivision modifier, a reference image of the target devil fruit visible in the top-right corner. Frame 001 shows an early spiral curve mid-extrusion: a nested, tapering spiral ring built up from a single extruded/converted curve with visible Bevel settings (Round profile, Depth, Fill Caps) in the sidebar. Frame 002 shows the same spiral refined into a smooth 3D coil (Subdivision modifier, Catmull-Clark, Optimal Display) — a clean tapered snail-shell-like swirl shape. Frame 003 shows the mirroring step: the original green swirl next to an orange-highlighted duplicate mid-transform (Shift+D, Scale X -1, Rotate X 180°) with a numeric input field open, about to be joined into a symmetric S-shape. Frame 004 shows the completed two-lobed "S" swirl motif (light green) with a SurfaceDeform modifier visible in the sidebar (Target, Interpolation Falloff, Strength) sitting on a flat rectangular plane boundary. Frame 005 shows the placement step: a purple-tinted copy of the swirl+plane pair being moved onto the base Icosphere's surface, a Shrinkwrap modifier's settings (Wrap Method, Snap Mode) visible in the sidebar, with the flat original pair still present off to the side for reference. Frame 006 shows several swirls (pink and light-blue) already conforming to the sphere's curved surface, proving the Shrinkwrap+SurfaceDeform combo bends the swirl geometry believably around a curved base. Frame 007 shows the finished, densely-covered devil fruit sphere (many pastel-colored swirls fully tiling its surface) alongside the in-progress stem/curl piece being modeled separately above it, with a Bevel modifier's Depth/Resolution/Start-End Mapping options open in the sidebar.

### Key Steps
**Base sphere:** Add an Icosphere with 2 subdivisions (enough surface detail); add a Subdivision modifier — this extra geometry helps distribute swirl placements evenly later, especially when using the Cavity viewport overlay to judge spacing.

**Building one swirl motif:**
1. Collapse any primitive down to a single vertex in Edit Mode (easier starting point than a Curve object) and extrude it repeatedly to trace the desired spiral shape.
2. Convert the resulting vertex-chain to a Curve (Object > Convert > Curve); increase its Geometry > Bevel > Depth to give it round thickness; Shade Smooth.
3. Fine-tune per-vertex thickness with Alt+S (scales the curve's radius around individual control points) while adjusting vertex positions for the desired taper/shape.
4. Convert the curve back to mesh (Ctrl+A > Visual Geometry to Mesh, or Object > Convert > Mesh) to get a spherical, cappable end.
5. Add a Subdivision modifier for smoothness; enable On Cage so Edit Mode previews the smoothed result directly.
6. **Cap the open end into a rounded tip:** select the boundary loop, Ctrl+F > Grid Fill; move the resulting center face(s) inward/outward to read as more spherical; grow the selection (Ctrl+Numpad+), then Extrude (E) and Alt+S (scale along normal) to add one more supporting loop around the rounded end, then fine-tune the shape freely in Edit Mode.
7. **Mirror into a two-lobed "S" swirl:** with the 3D cursor at world origin and Transform Orientation set to 3D Cursor (as pivot), select all (A), Shift+D to duplicate, then S, X, -1, Enter to flip it across X — this also inverts normals, so immediately Shift+N (Recalculate/Flip Normals) while everything is still selected to fix them; rotate the duplicate 180° on X (R, X, 180, Enter) to position it as the second spiral lobe; select all and M > By Distance (Collapse/Merge by Distance) to weld the two halves together at the seam; dissolve stray edge loops and fine-tune the shape (X-Ray mode makes it easier to select through both layers); rotate the whole combined object slightly for better symmetry, then set Transform Orientation back to Median/Global.

**Placing swirls conformed to the sphere's curvature (the key trick):**
8. Add a flat Plane sized to roughly bound the swirl shape in Edit Mode; add an edge loop for more even subdivision, and subdivide a few more times; set its Viewport Display to Wireframe so it stays visible-but-see-through while working.
9. **Important prerequisite:** if the swirl object has its own Subdivision modifier, make sure its Viewport and Render subdivision levels match exactly — otherwise the next step (Surface Deform) won't behave correctly, and swirls can visibly fail to follow the sphere's curvature specifically in the final render even though they looked right in the viewport.
10. Add a Surface Deform modifier to the swirl object, set the plane as its Target, and click Bind — now moving the plane's vertices in Edit Mode deforms the bound swirl geometry (works especially well combined with Proportional Editing for smooth, broad deformation).
11. Parent the swirl to the plane (select swirl, Shift-select plane, Ctrl+P) so moving the plane in Object Mode carries the swirl along with it — makes joint placement on the sphere much easier.
12. Hide the swirl+plane pair aside, unhide the base sphere, then Shift+D duplicate the swirl+plane pair and move the duplicate onto the sphere's surface — holding Ctrl while moving snaps it to the surface for easy placement; scale and rotate as needed to fit.
13. Once positioned, add a Shrinkwrap modifier to the plane targeting the base sphere; the Project wrap method with both the Negative and Positive direction options enabled works best — this makes the plane conform to the sphere's curved surface, and since the swirl is Surface-Deform-bound to the plane, the swirl bends to match automatically.
14. **Speed up repeated placement:** copy the already-fitted plane's Scale value to the original (unplaced) template plane so future duplicates don't need re-scaling from scratch each time; instead of manually re-adding a Shrinkwrap modifier to each new placement, select the new plane, Shift-select a previously-placed plane, and Ctrl+L > Copy Modifiers to inherit its Shrinkwrap setup (including target and settings) directly. Repeat placement across the sphere until it's fully covered in swirls.
15. **Render-time gotcha (same root cause as step 9):** if swirls don't visibly follow the sphere's curvature in a final render despite looking correct in the viewport, the Subdivision modifier's Viewport and Render level values are mismatched somewhere in the chain — make sure they're equal.

**The stem:** Shift+right-click to place the 3D cursor at the top of the sphere; add a primitive and collapse to a single vertex (or add a vertex directly), extrude in Edit Mode to build the stem's curling shape; delete an edge to separate the horizontal (curled) and vertical (straight) portions, then select all and P > Separate by Loose Parts to split them into two objects; convert each to a Curve and add thickness the same way as the swirls (Alt+S per-vertex scaling); taper the very tip to a sharp point by scaling its end vertices to zero; enable Fill Caps on the vertical stem piece to avoid an open hole at its join, then convert both back to mesh. Clean up resulting triangles into quads with Alt+J (Face menu: Tris to Quads) — for pairs that don't auto-convert, select exactly two adjacent triangles and press F to merge them into one quad manually. Finish with an Inset plus a protective edge loop around any sharp corner to keep it stable under the Subdivision modifier.

### Nodes / Settings
- **Base shape:** Icosphere (2 subdivisions), Subdivision Surface modifier (used both for detail distribution and final smoothing, with matched Viewport/Render levels — critical for Surface Deform and Shrinkwrap to render correctly).
- **Curve workflow:** vertex extrusion → Object > Convert > Curve → Geometry > Bevel > Depth (thickness) → Alt+S (per-vertex radius scaling) → Ctrl+A Visual Geometry to Mesh / Convert to Mesh (back to editable mesh with rounded caps).
- **Mesh cleanup/mirroring:** Grid Fill (Ctrl+F), Extrude (E) + Alt+S (scale along normal), Shift+D + S,X,-1 (mirror duplicate) + Shift+N (fix flipped normals), R,X,180 (180° rotate), Merge > By Distance (M), Transform Orientation = 3D Cursor for pivot-accurate mirroring.
- **Placement rig:** Surface Deform modifier (Target: wireframe plane, Bind button — lets Edit-Mode plane edits deform the bound swirl), Ctrl+P (Parent swirl to plane for Object-Mode-following), Shrinkwrap modifier (Target: base sphere, Project method, both Negative and Positive directions enabled), Ctrl+L > Copy Modifiers (propagate Shrinkwrap setup between placements), Ctrl-held move (snap-to-surface placement).
- **Stem:** P > Separate by Loose Parts, Curve conversion + Bevel Depth + Fill Caps, Alt+J (Tris to Quads) / F (manual quad merge), Inset + support loop.

### Difficulty
Intermediate

### Blender Version
Not specified — the Surface Deform + Shrinkwrap conforming technique is a standard modifier workflow consistent with Blender 3.x through 5.x.

### Tags
organic, procedural, modelling, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Surface Deform modifier or this curve-to-mesh swirl-building technique.

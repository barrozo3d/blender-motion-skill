---
title: 4 new retopology tips to discover! - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=24EtrCpg4Iw
author: Blender Secrets
ingested: 2026-07-19
blender_version: "Blender 5.0.1 -- observed in frame_000"
tags: [modeling, organic, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/4-new-retopology-tips-to-discover---blender-secrets/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 4 new retopology tips to discover! - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=24EtrCpg4Iw)
**Author:** Blender Secrets
**Duration:** 3m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] If you've done retopology in Blender, you probably know the old workflow.
[0:04] You start by adding a plane or a single face and then you turn on snapping and you set
[0:08] it to face project.
[0:14] And then to improve the visibility, you can turn on in front.
[0:18] However, because you turn on in front, you can also see it from the other side, which
[0:22] can be confusing.
[0:23] You can enable back face calling and that improves it somewhat, but it's still not ideal.
[0:29] Instead, in the mesh edit mode overlays, turn on this retopology checkbox and then carefully
[0:38] adjust the value to just enough so you can see the retopology mesh.
[0:42] Now you can really see the retopology mesh only where you need to see it.
[0:46] Be careful that you don't set this value too high because if it's too high, you can still
[0:50] see it from the other side.
[0:52] So now you can retopologize your mesh without the confusion of seeing the back face from
[0:56] the other side.
[0:58] When doing retopology, you're usually creating new geometry by either using the F2 add-on
[1:02] and pressing F or by pressing E for extrude to create new vertices and new edges.
[1:08] Unfortunately, that means you often have to do a lot of adjustments of the position of
[1:12] the new vertices.
[1:13] You can save a lot of time already by setting it to tweak selection, that way you don't
[1:18] always have to press G to adjust the position of a vertex.
[1:21] But an even faster way to extrude is by holding CTRL and right mouse clicking where you want
[1:26] to extrude to.
[1:27] The benefit of this extrusion method besides the speed is that you can adjust the rotation
[1:32] of what you're extruding while you're extruding it.
[1:35] That way you don't have to adjust the resulting geometry so much.
[1:38] After you finish retopologizing, you can redistribute the created vertices using the
[1:43] relax slide brush in sculpt mode.
[1:45] To do this, select the relax slide brush in sculpt mode and hold the shift brush and
[1:50] then brush over the topology.
[1:52] It relaxes and redistributes the new geometry without deflating the volume, which is what
[1:57] would happen if you used the normal smooth brush in sculpt mode.
[2:01] When you retopologize a mesh in blender, you probably have snapping enabled with the face
[2:06] project option.
[2:08] That way the vertices of the retopology mesh snap to the underlying geometry, which works
[2:13] great in most cases.
[2:15] But in situations where you want to extrude along for example an arm, where the geometry
[2:19] goes all the way around the original mesh, this can lead to a kind of snapping chaos
[2:23] where all the vertices get snapped to the side that you're looking at.
[2:27] To avoid this kind of situation, enable face nearest instead of face project in the snapping
[2:32] options.
[2:33] Now you can extrude around an object where the vertices are snapping even to the other
[2:37] side of the mesh.
[2:38] In my experience, sometimes the face nearest extrusion leads to vertices being too close
[2:43] together or unevenly spaced, but you can easily solve that by using the loop tools space
[2:48] option.
[2:49] The other things you can do with control R, you can add more loops in between.
[2:52] If you liked this tip, you'll love my Blender Secrets ebook, which has 2000 pages of Blender
[2:57] tips.
[2:58] And if you prefer watching videos instead, the complete hard service bundle has over
[3:02] 31 hours of Blender knowledge.



---

## Captured Frames

- [0:38] tutorials/frames/4-new-retopology-tips-to-discover---blender-secrets/frame_000.jpg
- [1:25] tutorials/frames/4-new-retopology-tips-to-discover---blender-secrets/frame_001.jpg
- [1:48] tutorials/frames/4-new-retopology-tips-to-discover---blender-secrets/frame_002.jpg
- [2:31] tutorials/frames/4-new-retopology-tips-to-discover---blender-secrets/frame_003.jpg

---

## Structured Notes

### Core Technique
Four modern retopology workflow upgrades: the Retopology overlay (replacing In Front + backface culling), Ctrl+RMB extrude, the Relax Slide sculpt brush, and Face Nearest snapping.

### Summary
Blender Secrets replaces the old retopology setup (plane + face-project snapping + In Front display, which confusingly shows the mesh from both sides) with four newer tools: the dedicated Retopology overlay checkbox with a tunable depth offset, Ctrl+right-click extrusion that orients geometry while extruding, the Relax Slide brush to redistribute vertices without volume loss, and Face Nearest snapping for extruding around limb-like shapes where Face Project snaps everything to the camera-facing side.

### Key Steps
1. **Retopology overlay** [frame_000, 0:38] — instead of In Front + backface culling, enable Mesh Edit Mode Overlays → Retopology and tune the offset value (0.037 shown) just enough to see the retopo mesh on the near side only; too high and it shows through from the back again.
2. **Faster extrusion** [frame_001, 1:25] — beyond F (F2 addon) or E-extrude: set the active tool to Tweak so vertices drag without pressing G, and extrude with **Ctrl+right-click** at the target position — it also rotates the new geometry toward the click, reducing cleanup (shown on a skull with a Mirror modifier: Clipping on, Merge 0.001 m).
3. **Redistribute with Relax Slide** [frame_002, 1:48] — in Sculpt Mode pick the Relax Slide brush (with Shift held as the shift-brush) and brush over the new topology; it evens out spacing without deflating volume like the Smooth brush would.
4. **Face Nearest snapping** [frame_003, 2:31] — when extruding around a form (an arm/snout), Face Project snaps all vertices to the visible side; switch Snap Target for Individual Elements from **Face Project** to **Face Nearest** so vertices wrap to the truly nearest surface, even the far side. If spacing ends up uneven, fix with LoopTools → Space, and add loops with Ctrl+R.

### Nodes / Settings
- Overlays → Retopology: on, offset ≈ 0.037 (scene-dependent; keep as low as possible)
- Snapping: Face Project (default) vs Face Nearest (for wrap-around extrusion); Align Rotation to Target visible in the snapping popover
- Mirror modifier: Clipping ✓, Merge 0.001 m (typical retopo symmetry setup)
- Sculpt Mode: Relax Slide brush (use as Shift/shift-brush); avoids Smooth-brush volume loss
- Shortcuts: Ctrl+RMB extrude-to-cursor, F (F2 addon) fill, E extrude, G move, Ctrl+R loop cut; LoopTools → Space

### Difficulty
Beginner–Intermediate

### Blender Version
Not specified (modern 4.x/5.x UI; Retopology overlay and Face Nearest snapping exist since 3.x)

### Tags
modeling, organic, beginner, intermediate

---

## Related Tutorials
- [Blender 5.0: How to UV Unwrap Anything](blender-50-how-to-uv-unwrap-anything.md) — the natural next step after retopology: unwrapping the clean topology
- [How to fix SHADING ERRORS in Blender](how-to-fix-shading-errors-in-blender.md) — mesh-quality troubleshooting that clean retopology prevents

---
title: Blender Secrets - Car Modeling Tips
source: YouTube
url: https://www.youtube.com/watch?v=jcSDF917dBo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.3.0 -- observed in frame_000"
tags: [modelling, procedural, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---car-modeling-tips/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Car Modeling Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=jcSDF917dBo)
**Author:** Blender Secrets
**Duration:** 5m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] A good place to find blueprints is the website dblueprints.com, although a quick Google image
[0:10] search can often give you a good enough result as well.
[0:15] Press 1 on the numpad to go to the front orthographic view.
[0:18] If you don't have a numpad on a laptop for example, you can go to view, viewport, front.
[0:25] Alternatively, you can hold ALT while orbiting the viewport until it snaps to the front orthographic view.
[0:31] Before dropping reference images into Blender, make sure they align in the image editing software that you like.
[0:37] Save them as separate, clearly named images.
[0:43] Drag the front reference image into the front viewport.
[0:48] Press ALT G to reset its location.
[0:51] And then drag the side reference image into the side viewport.
[0:55] The more views you have, the more accurate it will be.
[0:59] I personally like to enable transparency and reduce the opacity.
[1:04] If you don't want to see the reference images in perspective view, simply uncheck display perspective.
[1:10] That way they are only visible in the orthographic views.
[1:14] Select the reference image and press M then choose new collection.
[1:24] This way you can turn off their selectability so you don't keep accidentally selecting them while modeling.
[1:37] Press Tab to go into edit mode then subdivide the default cube ones.
[1:42] Exit the edit mode by pressing Tab and add a mirror modifier to the cube.
[1:47] Turn on by sect so that half of the cube is removed automatically.
[1:51] Enable on cage so you see the modifier result in the viewport.
[1:55] Toggle X-ray on so that you can select vertices on the other side of the mesh as well.
[2:00] Add a subdivision modifier to the cube.
[2:03] Make sure smooth shading is turned on.
[2:06] And make sure that if you add more modifiers, the mirror modifier is always on top for the correct result.
[2:18] Enable quad view by pressing Alt-ctrl-q so we can check all angles at the same time.
[2:24] Just like with a real car, we will create this model out of separate parts.
[2:28] In edit mode select all and delete all the faces.
[2:33] Now we can create a new vertex by holding Ctrl and right-clicking.
[2:37] The vertex still has the modifiers that we added to the original cube.
[3:32] Now we can cut the whole part blocked out.
[3:38] Enable on cage on the subdivide modifier and fine tune the shape.
[3:44] You can use matte caps to check the smoothness.
[3:47] The black and white matte caps in particular are made for this purpose.
[3:51] To add holes, duplicate the model in object mode and create the holes in the duplicate.
[4:02] Increase the subdivisions on the original part so that it's extra smooth and hide it.
[4:12] Then use a shrink wrap modifier with the original as the target so the duplicate with the holes in it follows the underlying topology.
[4:19] The reason we do this is to avoid pinching of the geometry.
[4:23] Make sure the shrink wrap modifier is in the original part so that it's extra smooth and hide it.
[4:28] Make sure the shrink wrap modifier is placed underneath the subdivide modifier.
[4:48] If you found this topic interesting and would like to know more, don't forget that you can find it in my Blender Secrets eBook.
[4:54] Along with almost 2000 pages of other tips.
[4:58] To get an idea of what the eBook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:55] tutorials/frames/blender-secrets---car-modeling-tips/frame_000.jpg
- [1:20] tutorials/frames/blender-secrets---car-modeling-tips/frame_001.jpg
- [1:55] tutorials/frames/blender-secrets---car-modeling-tips/frame_002.jpg
- [2:20] tutorials/frames/blender-secrets---car-modeling-tips/frame_003.jpg
- [2:35] tutorials/frames/blender-secrets---car-modeling-tips/frame_004.jpg
- [3:00] tutorials/frames/blender-secrets---car-modeling-tips/frame_005.jpg
- [3:45] tutorials/frames/blender-secrets---car-modeling-tips/frame_006.jpg
- [4:15] tutorials/frames/blender-secrets---car-modeling-tips/frame_007.jpg

---

## Structured Notes

### Core Technique
A full hard-surface car-body modeling pipeline: multi-view blueprint reference setup, box-modeling from a single vertex under a Mirror+Subdivision modifier stack in 4-way Quad View, matcap-based smoothness checking, and a Shrink Wrap technique for cutting clean holes into a duplicated high-detail shell without pinching geometry.

### Summary
Frame 000 shows the reference setup: a red Ferrari 166mm Berlinetta blueprint loaded as a Right Orthographic background/reference Empty, with front/side/rear thumbnails visible in the top-left asset list and a real-world width dimension (2250) annotated. Frame 001 shows the front blueprint being moved into a new Collection (dialog open) to organize and later disable its selectability. Frame 002 shows the core rig: a Mirror modifier (X axis, Bisect enabled, arrow pointing at it) on a cube positioned at the car's centerline over the rear blueprint. Frame 003 shows the resulting smooth, rounded starting blob after adding a Subdivision Surface modifier (Catmull-Clark) on top of the Mirror modifier. Frame 004 shows Quad View (Alt+Ctrl+Q) active — Top, Front, User Perspective, and Right Orthographic panes simultaneously — with the blocked-out car roof/window pillar shape checked against all views at once. Frame 005 shows the same Quad View mid-edit, dragging (G) a row of vertices to shape the A-pillar/roof curve, matched precisely against the blueprint in each pane. Frame 006 shows the Viewport Shading Matcap picker open with the black-and-white sphere matcap selected — used specifically to check surface smoothness/continuity without color or texture distraction. Frame 007 shows the same black-and-white matcap applied to the blocked-out car body across all four Quad View panes, revealing the surface flow clearly against the blueprint.

### Key Steps
1. **Get reference blueprints:** thebluprints.com is a good source, or a plain Google Image search; align the different views (front/side/rear/top) precisely against each other in external image-editing software first, and save each as a separate, clearly named file.
2. **Load references into Blender:** press Numpad1 for Front Orthographic (View → Viewport → Front if no numpad, or Alt-orbit until it snaps); drag the front reference image directly into the front viewport, Alt+G to reset its position to origin, then drag the side reference into the side viewport — more reference views = more accuracy. Enable transparency and lower opacity for easier tracing; uncheck "Display in Perspective" so references only show in orthographic views, not perspective.
3. **Organize references:** select all reference images, press M → New Collection, so their selectability can be toggled off later to avoid accidentally clicking them while modeling.
4. **Set up the base modifier rig:** Tab into Edit Mode on the default cube and Subdivide once, Tab back to Object Mode, add a Mirror modifier — enable Bisect (auto-removes the far half) and On Cage (see the mirrored result live in the viewport); enable X-Ray to select vertices through the mesh. Add a Subdivision Surface modifier with Smooth Shading enabled; always keep the Mirror modifier above Subdivision in the stack for correct results as more modifiers are added.
5. **Enable Quad View** (Alt+Ctrl+Q) to check the model against all reference angles simultaneously while modeling.
6. **Box-model the body from scratch:** in Edit Mode, select all and delete all faces (leaving nothing but the modifier setup); create new vertices with Ctrl+RMB — each new vertex still inherits the Mirror/Subdivision modifiers from the original cube — and build the body's control cage vertex by vertex, extruding/connecting to match the blueprint silhouette from every Quad View angle. Toggle On Cage on the Subdivision modifier to fine-tune the low-poly cage while watching the smoothed result live.
7. **Check smoothness with matcaps:** switch Viewport Shading to Matcap and pick the black-and-white matcap specifically — its high-contrast, texture-free shading makes surface flow, pinches, and continuity errors immediately visible.
8. **Cut clean holes (windows, grilles, etc.) without pinching:** in Object Mode, duplicate the finished smooth body; cut the actual holes into the duplicate. Increase the Subdivision level on the original (un-holed) part so it's extra-smooth, then hide it. Add a Shrink Wrap modifier to the holed duplicate targeting the hidden original — this makes the cut-open duplicate conform tightly to the original's smooth underlying surface, preventing the pinching artifacts that direct boolean/cut operations on a shared mesh would otherwise cause. The Shrink Wrap modifier must sit below the Subdivision modifier in the duplicate's stack.

### Nodes / Settings
- **Modifiers:** Mirror (Axis X, Bisect, On Cage, Clipping, Merge), Subdivision Surface (Catmull-Clark, Levels Viewport/Render, Smooth Shading), Shrink Wrap (target = hidden high-subdivision original, placed below Subdivision in the stack).
- **Reference setup:** Image as background/reference Empty (Depth, Side, Opacity, Display in Orthographic/Perspective toggle), Collections (for selectability toggling).
- **Viewport:** Quad View (Alt+Ctrl+Q), X-Ray toggle, Matcap shading (black-and-white matcap for smoothness checks).
- **Edit-mode operators:** Ctrl+RMB (create new vertex, inherits modifiers), Alt+G (clear/reset location).

### Difficulty
Advanced

### Blender Version
Not specified — core modifier/reference/Quad-View workflow, version-agnostic across modern Blender (2.8x-5.x).

### Tags
modelling, procedural, intermediate, advanced

---

## Related Tutorials
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares procedural, intermediate, advanced; same channel, complementary hard-surface detailing once the car body shell exists.
- [4 new retopology tips to discover! - Blender Secrets](4-new-retopology-tips-to-discover---blender-secrets.md) — shares modelling, intermediate; same channel, relevant to cleaning up the final car body topology.

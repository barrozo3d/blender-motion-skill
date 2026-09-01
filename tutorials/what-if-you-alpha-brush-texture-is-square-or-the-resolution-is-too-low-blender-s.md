---
title: What if you Alpha Brush texture is square? Or the resolution is too low? Blender Sculpting tips
source: YouTube
url: https://www.youtube.com/watch?v=rtnsLjP1ebo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.3.2 -- observed in frame_000"
tags: [displacement, procedural, organic, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# What if you Alpha Brush texture is square? Or the resolution is too low? Blender Sculpting tips

**Source:** [YouTube](https://www.youtube.com/watch?v=rtnsLjP1ebo)
**Author:** Blender Secrets
**Duration:** 6m29s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alphas are black and white height maps that you can use as a texture for a sculpt brush
[0:06] in order to quickly add some detail to it.
[0:10] To create these maps from geometry, you can use a simple geometry position shader node
[0:15] and use the separate XYZ node to only show the Z axis.
[0:20] And then you get this kind of black and white material where black represents no height
[0:25] and the closer it goes to white, the more height there is.
[0:29] And this texture is then rendered.
[0:31] However, the way I bake these is I have set up this reference circle here and this circle
[0:37] represents the brush radius of the sculpt brush.
[0:42] And the reason I have this setup in my alpha texture baking file with this reference circle
[0:48] is because everything that is outside of the circle will also not be shown in the brush
[0:54] in sculpt mode.
[0:55] Let me show you what I mean.
[0:57] So to give you an example, now I have loaded an alpha texture where there are parts that
[1:01] are outside of this circle.
[1:04] And so now when I apply it as a brush, you can see that there are parts that are cut
[1:09] off and that's because those fall outside of the brush radius.
[1:14] Now, fortunately, this is very easy to solve.
[1:16] You don't need to rebake or recreate the alpha texture.
[1:21] So let me just real quick go over all the correct settings for creating this kind of
[1:24] brush.
[1:25] So first of all, this is a duplicates of the standard draw brush.
[1:28] So you can right click here and then duplicate assets to create a duplicate.
[1:33] And then you can give it a new name and you can also give it a preview image.
[1:37] And then under texture, you can click on new to load a texture and then click on this icon
[1:42] here to go to the texture tab.
[1:44] And then here you have to click on new texture and then you can load your alpha texture and
[1:50] just make sure this is not set to sRGB because then it won't use all of the 32 bit color
[1:55] space.
[1:56] And there are a few settings we need to take care of in the tool panel of the brush.
[2:01] So the mapping of the texture should be set to area plane.
[2:04] Otherwise, it will be distorted based on the view you have in your 3D viewport.
[2:09] And the stroke is drag dot so that you can drag the alpha around.
[2:14] And if you want to cancel a brush instead of clicking undo, it's better to click on
[2:18] escape.
[2:20] That's much faster.
[2:21] And then finally the falloff should be set to constant.
[2:24] Otherwise, you won't get the full texture.
[2:27] And then finally the solution to make sure that the corners here are not cut off of the
[2:32] texture that is outside of the brush radius.
[2:34] It's actually very easy.
[2:36] You just need to increase this size X and size Y value to something slightly higher like
[2:41] 1.1.
[2:43] And so now if I try again, you can see that the whole texture is included.
[2:49] Just be sure not to set this too high like 2 because then your texture will be very small.
[2:54] So just 1.1 or 1.2 will give you the result that you need.
[2:59] So now as you can see, these corners are still included.
[3:02] So that kind of shrinks the alpha texture to fit inside of that circle.
[3:07] I've got a couple more tips after this, but first I want to mention real quick that I
[3:10] have a whole hard surface sculpting course for Blender.
[3:13] And about half of this course is dedicated to creating alpha brushes in great detail,
[3:18] as well as how to come up with a 2D concept and how to transfer that to a 3D model in
[3:22] Blender.
[3:23] It also shows some things that you won't find anywhere else like how to create a tiling
[3:27] hard service displacement map and hard service VDM brushes.
[3:31] You can find it on BlenderSecrets.org.
[3:34] Now one more thing you can do to make sure you can use a square alpha texture like this
[3:39] is to set the mapping to stencil.
[3:42] And that gives you this image which you can move by right clicking and dragging, where
[3:45] you can rotate it by control and right clicking.
[3:49] Or with shift and right click, you can scale it in and out.
[3:52] And then what that does is you can just place it where you want and rotate it the way you
[3:57] want.
[3:58] And I would recommend setting the strength to 1 also with all these brushes so that
[4:02] you can get the full depth of the height map.
[4:05] And then by left clicking, you can get that detail where you placed it.
[4:10] But this is something that is maybe more useful for organic models.
[4:14] And with that, I would also recommend using the smooth falloff.
[4:18] Now just in case if the resolution of your alpha brushes looks really low like this,
[4:23] there are a couple of reasons for that.
[4:25] First of all, when your object is not selected, like for example now I have selected this
[4:30] head part.
[4:32] And if I select this body part again, Alt Q and hovering over it, you can see that it
[4:36] becomes sharp again.
[4:38] And that's just because the multi-res modifier will try to save resources when you are not
[4:43] sculpting on something and just show a lower resolution version of it.
[4:47] And another reason why you might be getting lower resolution in your alpha brush like
[4:51] this is simply because you don't have enough geometry.
[4:55] So let me show you this has a very low geometry.
[4:59] And so what you would do then is make sure that this has enough subdivisions in the geometry
[5:04] in edit mode and then add a multi-res modifier and just subdivide it a few times.
[5:10] And as you can see, that gives it almost half a million faces.
[5:13] So now when I add my alpha, it looks a bit sharper.
[5:17] And if I subdivide one more time, it has almost two million faces.
[5:20] So now my alpha looks really sharp.
[5:22] But again, if I then switch to this object with Alt Q, then you can see that this alpha
[5:28] actually disappears.
[5:29] And it's not gone.
[5:30] It's still there.
[5:31] Let me just show you by going back to it.
[5:33] It's just that on this object, the viewport level is set to zero.
[5:37] So if we set it to one and then switch back to this object with Alt Q, then you can see
[5:43] now we can see the alpha, but it's a bit blurry.
[5:46] And that's because now it's just showing the first level of subdivision.
[5:50] And that's just to make sure that it's not too heavy for your computer.
[5:53] So you can adjust that to your liking based on the system that you're using.
[5:58] And one other reason that it can look not as good is because it's set to flat shading.
[6:03] So if you right-click in object mode, you can use shade smooth.
[6:08] And that actually helps a lot, as you can see with the alphas as well.
[6:12] So definitely recommend doing that.
[6:14] I hope that helps those of you who are trying to use alpha textures and maybe have some questions.
[6:20] If you have any other questions about alpha textures, please feel free to leave them in
[6:24] the comments and I will see if I can help.



---

## Captured Frames

- [1:09] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_000.jpg
- [1:44] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_001.jpg
- [2:04] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_002.jpg
- [2:41] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_003.jpg
- [3:39] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_004.jpg
- [4:36] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_005.jpg
- [5:13] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_006.jpg
- [6:08] tutorials/frames/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s/frame_007.jpg

---

## Structured Notes

### Core Technique
A troubleshooting-focused sculpting tips video covering two common alpha-brush problems: (1) a square/rectangular alpha texture getting its corners clipped because sculpt brushes only sample within a circular radius — fixed by increasing the brush texture's Size X/Y slightly beyond 1.0, or alternatively using Stencil mapping for a freely movable/rotatable/scalable texture placement; and (2) alpha brushes rendering blurry/low-res — caused either by a Multiresolution modifier temporarily lowering an unselected object's preview resolution, insufficient underlying geometry, or missing Shade Smooth.

### Summary
Frame 000 shows a hard-surface robotic model close-up with a brush-radius circle overlay and an alpha texture thumbnail panel open in the sidebar — illustrating the brush-radius concept the whole "square alpha" problem is built on. Frame 001 shows the actual problem: a black-and-white striped alpha texture thumbnail in the Texture panel (Image Sequence, Color Space non-sRGB) applied to a smooth robot shoulder — the alpha's rectangular shape doesn't match the brush's circular sampling area. Frame 002 shows the brush's Texture Mapping settings open (Mapping: Area Plane, Angle, Offset X/Y/Z, Sample Bias) alongside Stroke settings (Draw Method: Drag Dot) — the core settings checklist for correct alpha behavior. Frame 003 shows the Size X field being edited in the Texture Mapping panel (value being typed, partially visible) with the alpha now stamped cleanly onto the surface without visible corner-cutting — the "increase Size X/Y to ~1.1" fix in action. Frame 004 shows Stencil mapping mode selected instead (Mapping: Stencil, with a wavy/striped thumbnail preview) — the alternate placement method that allows freely moving, rotating, and scaling a square texture over the surface before stamping. Frame 005 shows a Multiresolution modifier's panel (Level Viewport/Sculpt/Render, Optimal Display) on a robot torso, with the alpha detail visible sharp when this object is the active sculpt target — the "object must be selected/active to show full resolution" behavior. Frame 006 shows a lower-poly head/helmet piece (Vertices/Edges/Faces counts visible top-left) with a low-resolution Multiresolution setup, its alpha detail appearing comparatively blurry — the "not enough underlying geometry" problem. Frame 007 shows a right-click Object context menu open with "Shade Smooth" highlighted over the same head piece, a Multiresolution modifier (Subdivide, Unsubdivide options) visible in the sidebar — the final fix for blurry/faceted-looking alpha results.

### Key Steps
**Fixing a square/rectangular alpha that gets its corners cut off:**
1. Understand why: a sculpt brush only samples texture within its circular radius — anything in a square/rectangular alpha texture that falls in the "corner" area outside that inscribed circle simply won't show up when stamped, even though the source texture file is intact and doesn't need to be re-baked or recreated.
2. Correct baseline brush setup for alpha textures (duplicate the standard Draw brush first via right-click > Duplicate Asset, rename, optionally add a preview image): under Texture, click New to load the texture, then open the Texture tab and click New Texture, loading the actual alpha image file — make sure its Color Space is **not** set to sRGB, so the full 32-bit value range is used correctly as height data.
3. Required brush tool-panel settings: Texture **Mapping = Area Plane** (prevents distortion based on current 3D-viewport view angle), Stroke Method = **Drag Dot** (lets you drag/place the alpha), Falloff = **Constant** (otherwise the alpha won't render at its full/correct intensity), and press **Escape** rather than Ctrl+Z to cancel an in-progress placement you don't like — much faster than waiting for undo.
4. **The actual corner-clipping fix:** in the Texture Mapping settings, increase **Size X and Size Y** slightly above 1.0 — around 1.1 to 1.2 is usually enough to include the texture's corners within the brush's circular sample radius. Avoid going too high (e.g. 2) — that shrinks the effective texture down too much within the brush footprint.
5. **Alternative — Stencil mapping (better suited to organic work):** set Texture Mapping to **Stencil** instead of Area Plane; this projects a movable overlay of the texture that can be repositioned (right-click drag), rotated (Ctrl+right-click drag), and scaled (Shift+right-click drag) freely before stamping — letting you place and orient a square texture exactly where and how you want on an organic surface. Recommended alongside Stencil mode: set brush Strength to 1 (for full height-map depth) and use Smooth falloff.

**Fixing blurry/low-resolution alpha brush results:**
6. **Cause 1 — inactive-object resolution saving:** a Multiresolution modifier automatically shows a lower-resolution preview on any object that isn't the currently active sculpt target, to save system resources; switch objects with **Alt+Q** and hover over the one you want to check — it sharpens back up once it becomes active/hovered.
7. **Cause 2 — insufficient underlying geometry:** if an object simply doesn't have enough polygon density, the alpha will look blurry regardless of anything else. Fix: in Edit Mode, ensure the base mesh has enough subdivisions, then add a Multiresolution modifier and subdivide it a few times (subdividing from a low base to ~500K faces already sharpens results noticeably; going further to ~2M faces makes alphas look very sharp) — note that Multiresolution's own **Viewport** subdivision level (separate from Sculpt/Render levels) also caps how much detail is shown in the 3D viewport even while actively sculpting on that object, independent of the "active object" behavior in point 6 — raise it if the alpha still looks soft/blurry while working directly on that object.
8. **Cause 3 — flat shading:** if an object is still using flat (non-smoothed) shading, alphas read noticeably worse. Right-click in Object Mode and choose **Shade Smooth** — this measurably improves how alpha detail reads, and is recommended as a standard step when sculpting with alphas.

### Nodes / Settings
- **Alpha texture baking reference (mentioned, not the video's main focus):** Geometry (Position) node → Separate XYZ (Z output only) → rendered as a black-and-white height map, baked using a reference-circle guide matching the intended brush radius so nothing important falls outside the brush's circular sample area.
- **Brush Texture settings:** Color Space (must not be sRGB), Mapping (Area Plane vs. Stencil), Size X/Y (1.1-1.2 fix for square alphas), Angle/Offset (Stencil placement).
- **Brush Stroke/Falloff:** Stroke Method: Drag Dot, Falloff: Constant (Area Plane) or Smooth (Stencil), Strength (1 recommended for full height-map depth).
- **Stencil controls:** right-click-drag (move), Ctrl+right-click-drag (rotate), Shift+right-click-drag (scale).
- **Resolution:** Multiresolution modifier (Levels: Viewport/Sculpt/Render, Subdivide), Alt+Q (switch active sculpt object), Shade Smooth (Object Mode right-click menu).
- **Workflow:** Escape (fast-cancel a stamp vs. slow Ctrl+Z undo), Duplicate Asset (for creating a reusable alpha-brush variant of the Draw brush).

### Difficulty
Intermediate

### Blender Version
Not specified — Area Plane/Stencil brush texture mapping and Multiresolution's per-object viewport-resolution behavior are consistent with Blender 3.x through 5.x.

### Tags
displacement, procedural, organic, intermediate

---

## Related Tutorials
- [This technique lets you make Hard Surface models easily](this-technique-lets-you-make-hard-surface-models-easily.md) — shares procedural, organic, intermediate; that video's alpha-brush "View Plane" mapping mode (for tiling) and this one's Area Plane/Stencil modes cover Blender's alpha-brush mapping options together.
- [Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna](monster-sculpting-full-process-blender-secrets-stranger-things-vecna.md) — shares organic, procedural; that video's purchased-alpha skin-detailing pass runs into the exact resolution/shading issues this tutorial explains how to fix.

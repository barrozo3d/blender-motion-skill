---
title: Grease Pencil Fundamentals: 2D Animation
source: Blender Studio
url: https://studio.blender.org/training/grease-pencil-fundamentals/5c40c0d679f30a0147c0c194/
author: Matias Mendiola (Blender Studio)
ingested: 2026-09-03
blender_version: "2.80 (status bar reads v2.80.37 / v2.80.39) — see the version caveat: Grease Pencil was rewritten as GPv3 in 4.3"
tags: [animation, grease-pencil, 2d-animation, onion-skinning, beginner]
extraction_status: complete
frames_dir: tutorials/frames/grease-pencil-fundamentals-2d-animation/
frame_count: 6
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Grease Pencil Fundamentals: 2D Animation

**Source:** [Blender Studio](https://studio.blender.org/training/grease-pencil-fundamentals/5c40c0d679f30a0147c0c194/)
**Author:** Matias Mendiola (Blender Studio)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] The first step is to create a new layer.
[0:06] Grease Pencil is basically a 2D animation tool, so why not start with the famous Bonson Ball animation and show you how to animate with the tool?
[0:14] Before start with our Bonson Ball animation, I will shorten the playback range.
[0:20] Next, I will add a new layer to draw a reference motion path for our ball.
[0:29] The best way to draw in Grease Pencil is through the camera view, because in this way we know exactly what our final animation will look.
[0:42] Once I finish drawing the path, I will lock the layer to avoid unwanted changes.
[0:51] To start with the rough animation, I will draw our ball on the fair frame.
[0:59] Then you can just move to other frame and start a new drawing.
[1:03] Grease Pencil will add a new keyframe for you.
[1:09] You can continue in this way to complete your animation.
[1:20] In the Oning Skinning panel, you can change the number of frames to be shown before and after the current one.
[1:32] Also you can modify the opacity and colors.
[1:39] To delete keyframes, first make your keyframe selection and then press Delete or the X key.
[1:50] Another way to work on the Bonson Ball animation is to duplicate frames and using Edit and Scale mode to tweak the ball shape.
[2:01] To duplicate a keyframe, use Shift T to make a copy of the selected keyframe and move it to the new frame.
[2:13] Another way to duplicate is to move first to the frame position you want the new keyframe and then move your stroke selection.
[2:21] A new keyframe will be added automatically.
[2:33] Then you can modify the drawing using the editing and sculpting tools.
[2:42] In this way you don't have to draw every single frame and it's an easier way to maintain the ball shape through all the animation.
[3:12] If you want to modify several frames at the same time, you can activate Multi-Frame Edition on the top bar.
[3:42] Multi-Frame Edition is really useful if you need to modify some already made animations, for example in this case to change the ball path.
[4:12] Use the spacebar to break back the animation.
[4:32] To continue polishing the rough animation, you can play with the timing, adding or moving keyframes.
[4:58] Once we are satisfied with the rough animation, we can add a new layer and start the cleanup process by inking our drawings.
[5:58] We can apply the same workflow we used with the Bunsen Ball sample to make more complex animation.
[6:12] Start with the rough animation with the help of the onion skinning.
[6:22] Use Edit and Sculpt mode to tweak drawings.
[6:31] We can also use some basic 3D models that help us draw in difficult perspectives.
[6:46] And finally, you can color your animation.



---

## Captured Frames

- [0:29] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_000.jpg
- [1:20] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_001.jpg
- [2:01] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_002.jpg
- [3:12] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_003.jpg
- [4:58] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_004.jpg
- [6:31] tutorials/frames/grease-pencil-fundamentals-2d-animation/frame_005.jpg

---

## Structured Notes

### Core Technique
The complete Grease Pencil 2D animation loop in Blender 2.8's **2D Animation** workspace template, taught on the classic bouncing-ball exercise: draw *through the camera view* so what you draw is what renders, separate the work across dedicated GP layers (a locked motion-path reference, roughs, ink, fills), let each new drawing on a new frame auto-create its own keyframe, use **Onion Skinning** to see the drawings before and after the current one, and then avoid redrawing every frame by **duplicating keyframes and tweaking them in Edit/Sculpt mode**. **Multiframe** editing extends that to transforming many keyframes at once — which is what makes retiming or re-pathing an already-animated sequence practical rather than a full redraw.

### Summary
The lesson builds a bouncing ball and then generalises the same workflow to character animation.

It starts by shortening the playback range and adding a dedicated layer for a **reference motion path** — the pink arc visible across [frame_001] and [frame_002] — drawn in **Camera Perspective** so the drawing is framed exactly as it will render. Once the path is drawn its layer is **locked** to prevent accidental edits; [frame_001] shows the `Path` layer carrying a padlock in the dope sheet channel list while `Lines` stays editable. The layer stack in that scene is a clean three-way split: `Path`, `Lines`, `Fills` ([frame_002], Layers panel).

Rough animation is then drawn frame by frame: draw the ball, move to another frame, draw again, and Grease Pencil creates the keyframe for you. [frame_001] shows this mid-flow in Draw mode (Draw Pencil brush, Radius 60px, Strength 0.600, Material `Black`) with **onion skinning active** — the earlier drawing ghosted in green and the later one in blue around the solid current stroke, exactly the "frames shown before and after the current one" the narration describes. The Onion Skinning panel itself lives in the Grease Pencil *data* properties, visible as a collapsed panel alongside Adjustments / Relations / Vertex Groups / Viewport Display in [frame_005]; its count, opacity and colours are all adjustable there.

The second half is about *not* drawing every frame. Keyframes can be duplicated and then reshaped with Edit and Sculpt mode tools, which keeps the ball's volume consistent across the animation instead of redrawing it and drifting. A second duplication route is shown too: move the playhead to the target frame first, then move the stroke selection — a new keyframe is created automatically. [frame_002] captures this stage in **Edit Mode** with the header's **Multiframe** toggle and **Interpolate** menu visible, the dope sheet below showing per-layer keyframe channels for `Path` / `Lines` / `Fills`.

**Multiframe** editing (top bar, Edit Mode) is then used to modify several keyframes simultaneously — the narration's own example is changing the ball's path across an already-finished animation, which is precisely the case where per-frame editing would be prohibitive. Cleanup follows on a new layer, inking over the approved roughs.

The closing section scales the identical workflow up to character work, and it is the most production-like part of the lesson. [frame_005] shows a far more complex scene: the layer stack has become `Ink` / `Smoke` / `Blast` / `Rough character` / `Character Reference`, and the Outliner carries **real 3D mesh objects — `Cube.001`, `Sphere`, `Sphere.001`, `Sphere.002` — sitting alongside the Grease Pencil `Stroke` object**. Those greyed blocky forms visible in the viewport are the "basic 3D models that help us draw in difficult perspectives": rough 3D stand-ins used purely as construction guides to keep a foreshortened arm and fist on-model, drawn over in 2D. Colour is applied last.

### Key Steps
1. Open the **2D Animation** workspace template (its tabs — `2D Animation`, `2D Full Canvas`, `Rendering` — are visible in the top bar of every frame here) and shorten the playback range to the length of the shot.
2. Add a dedicated layer for a **reference motion path** and draw the arc the subject will follow. Draw in **Camera Perspective** so the drawing is composed exactly as it will render.
3. **Lock the path layer** once it is drawn, so later drawing passes cannot disturb the reference ([frame_001], padlock on the `Path` channel).
4. On a rough layer, draw the subject on the first frame, then move to a later frame and draw again — Grease Pencil adds the keyframe automatically. Repeat to block the animation out.
5. Turn on **Onion Skinning** and set how many frames are shown before/after the current one, plus their opacity and colours, in the Grease Pencil data properties ([frame_005] shows the panel; [frame_001] shows the green/blue ghosting in use).
6. To delete keyframes, select them in the dope sheet and press **Delete** or **X**.
7. Instead of redrawing every frame, **duplicate a keyframe and tweak it** with Edit and Sculpt mode — this preserves the shape's volume across the animation. Two routes: duplicate the selected keyframe and move it to the target frame, or move the playhead to the target frame first and then move the stroke selection, which creates the keyframe automatically.
8. Enable **Multiframe** in the Edit Mode top bar to transform several keyframes at once — the practical way to re-path or retime an animation that is already drawn.
9. Polish the timing by adding and moving keyframes, playing back with **Spacebar**.
10. Add a new layer and **ink** over the approved roughs as the cleanup pass; add colour last on its own layer.
11. For harder subjects, drop **rough 3D primitives into the scene as construction guides** and draw over them to keep difficult perspectives on-model ([frame_005]).

### Nodes / Settings
- **2D Animation workspace template** — the GP-configured startup layout (`2D Animation` / `2D Full Canvas` / `Rendering` tabs).
- **Grease Pencil layers** — per-layer lock, visibility, Blend mode and Opacity. Production stacks seen here: `Path` / `Lines` / `Fills` for the ball, and `Ink` / `Smoke` / `Blast` / `Rough character` / `Character Reference` for the character shot.
- **Onion Skinning** — a panel in the Grease Pencil *data* properties: number of frames before/after, opacity, and per-side colours (green = before, blue = after, as rendered in [frame_001]).
- **Multiframe** — Edit Mode header toggle; edits apply across multiple keyframes at once. Sits beside the **Interpolate** menu ([frame_002]).
- **Draw mode brush settings** — Draw Pencil, `Radius` 60px, `Strength` 0.600/0.800, `Material` selector in the header ([frame_001], [frame_005]).
- **Drawing plane** — `Front (X-Z)` with `Origin` placement, set in the 3D viewport header.
- **Dope sheet (Grease Pencil mode)** — one channel per GP layer; keyframe select / duplicate / delete (**X** or **Delete**).
- **Materials** — GP materials are per-object slots (`Black`, `Red`, `Grey` in [frame_002]) with separate **Stroke** and **Fill** sections, each with its own Style and Colour.

### Difficulty
Beginner

### Blender Version
**2.80** — the status bar reads `v2.80.37` in [frame_002] and `v2.80.39` in [frame_005], so the course was recorded across 2.80 release-candidate builds.

⚠️ **Read this entry as foundational workflow, not as current UI.** Grease Pencil was rewritten as **Grease Pencil v3** in Blender 4.3, which changed the object's internal data structure and moved and renamed parts of the interface. The *concepts* here — camera-view drawing, layer separation, a keyframe per drawing, onion skinning, duplicate-and-tweak over redraw, multiframe editing, 3D construction guides — all survive that rewrite and are why this lesson is worth keeping. Exact panel locations and some names do not. Cross-check any specific control against a modern entry before relying on it.

⚠️ **One unresolved transcript artifact.** The narration gives the duplicate-keyframe shortcut as "Shift T"; the captured frames do not show a shortcut overlay, so this could not be confirmed against the screen. Blender's standard duplicate shortcut is **Shift+D**, and the speaker's accent produces several clear d/t and vowel substitutions elsewhere in this transcript (Whisper rendered "bouncing ball" as "Bonson Ball"/"Bunsen Ball", "onion skinning" as "Oning Skinning", "first frame" as "fair frame", and "play back" as "break back"). Treat the exact key as unverified rather than trusting either reading.

### Tags
animation, grease-pencil, 2d-animation, onion-skinning, beginner

---

## Related Tutorials
- `daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil.md` — the same rough-layer → clean-line-layer inking pass this lesson's cleanup step describes, shown in isolation.
- `daily-blender-tip-97---exploring-grease-pencil---different-brushes.md` — the Draw-mode brush set this lesson uses at default settings.
- `daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh.md` — the 3D-space side of Grease Pencil, complementing step 11's use of 3D primitives as drawing guides.
- `blender-2d-animation-tutorial-for-beginners-grease-pencil-tutorial.md` — an alternative beginner walkthrough of the same 2D animation loop.
- `grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea.md` — **read this alongside the version caveat above**: modern Grease Pencil (Blender 5) drawing tools, showing where the 2.80 UI in this entry has since moved on.

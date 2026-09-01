---
title: Blender Secrets - In Depth Cloth Sculpting tricks with Pose Brush
source: YouTube
url: https://www.youtube.com/watch?v=dtFFc6f2rK8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.5.0 Beta -- observed in frame_000"
tags: [cloth, simulation, organic, rigging, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - In Depth Cloth Sculpting tricks with Pose Brush

**Source:** [YouTube](https://www.youtube.com/watch?v=dtFFc6f2rK8)
**Author:** Blender Secrets
**Duration:** 4m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So you may know about the post brush, which you can use in sculpt mode to post a character, which is not meant for rigging, just sculpt.
[0:09] And recently they implemented a way to use face sets to your artfans that share, which makes the tool really much better.
[0:17] Let me show you what I mean.
[0:20] So I am in object mode here, I will go to edit mode, and enable X-ray view, and use the lasso select here, and I will just select the entire arm.
[0:38] So this is selected all the way through.
[0:42] In sculpt mode, I can then make a face set from the edit mode selection.
[0:46] So we have this, and I can do that again.
[0:53] Deselect X-ray view, and this time I will select everything up to the elbow, and then in sculpt mode.
[1:04] Again, face set from edit mode selection.
[1:08] So now I have these two face sets, one for the upper arm and one for the lower arm.
[1:14] So what I can do now is here with the post brush, if I go to the tool panel here.
[1:27] Normally it is set to geometry, to rotate based on the topology.
[1:32] But we can set it now to face sets, and then you can see it picks the face set, so I can move it like this, or move it like this.
[1:44] And that's okay, but it gets better, because now we can use the clotsim to do the same thing.
[1:56] And the advantage of that is that when you move this, you can see that it is actually doing some clotsimulation,
[2:09] instead of just rotating the geometry.
[2:13] Let me show you here.
[2:17] So you see you get these nice cloth folds.
[2:22] Let me show you the difference.
[2:24] So if I just use geometry, then it just bends like this.
[2:32] So you don't get any folds here, as opposed to with clotsim.
[2:39] It goes a little bit slower, but you get these beautiful folds.
[2:46] And that's difficult to sculpt, so you get that for free.
[2:51] But another thing that you can do, you have more than just rotate and twist here.
[2:56] You also have scale and squash and stretch.
[2:59] And what we can do here with squash and stretch is we can squash it, and then you get all these really cool folds.
[3:10] Of course, that makes the arm a little bit shorter.
[3:13] So what I recommend is that you do this with geometry first to stretch it out a little bit.
[3:20] And then go back to clotsim, and then you can squash it back to the original length.
[3:26] But then you get all these cool folds.
[3:32] Of course, you get a little bit of intersecting stuff here.
[3:44] Easy to solve with some smooth brush.
[3:51] So that's pretty cool.
[3:54] You get these nice folds here and here.
[3:58] And now along the lower arm.
[4:03] When I unhide the rest also here, you can see that there's now some intersecting.
[4:08] But if I just press Alt-Q and select that mesh.
[4:13] And then use the grab brush.
[4:18] I can move that back.



---

## Captured Frames

- [0:35] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_000.jpg
- [0:50] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_001.jpg
- [1:35] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_002.jpg
- [2:20] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_003.jpg
- [2:30] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_004.jpg
- [3:05] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_005.jpg
- [3:40] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_006.jpg
- [4:15] tutorials/frames/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush/frame_007.jpg

---

## Structured Notes

### Core Technique
Use the Sculpt Mode Pose brush's Face Sets deformation (instead of Topology-based) combined with its "Cloth Simulation" Deformation Target to pose a clothed character's limb and get realistic, physically-simulated fabric folds automatically — far easier than hand-sculpting creases — demoed live on a textured bomber-jacket character.

### Summary
Frame 000 shows the setup: X-ray view enabled in Edit Mode, Lasso Select used to select the entire arm mesh region straight through the model (webcam PIP of the presenter visible throughout). Frame 001 shows the payoff of that selection: two separate Face Sets created (upper arm highlighted, a yellow circle marking the boundary) via "Face Set from Edit Mode Selection," run twice — once for the upper arm, once up to the elbow. Frame 002 shows the Pose brush's Deformation Target set to Geometry with Rotate/Twist Face — bending the arm this way moves geometry smoothly but produces no cloth folds. Frame 003 shows the critical setting change: Deformation Target switched to **Cloth Simulation** — the same bend now visibly produces real fabric folds at the elbow crease. Frame 004 shows a side-by-side-style comparison confirming the Geometry-only bend stays smooth with no folds. Frame 005 shows Deformation Target = Cloth Simulation with Deformation (sub-mode) = **Squash & Stretch** — compressing the arm's length to generate a dense cluster of realistic wrinkle folds. Frame 006 is a close-up of those cloth-sim-generated wrinkles, showing convincing overlapping fabric creases that would be very difficult to hand-sculpt. Frame 007 shows post-fix cleanup: Alt+H (unhide) revealing the rest of the mesh with visible self-intersection near the shoulder seam, about to be corrected with the Grab brush.

### Key Steps
1. In Edit Mode, enable X-Ray view and use Lasso Select to select an entire limb region all the way through the mesh (front and back faces both).
2. In Sculpt Mode, create a Face Set from that Edit Mode selection ("Face Set from Edit Mode Selection"). Repeat the process for a second region (e.g. select up to the elbow only) to create a second, adjacent Face Set — giving the Pose brush two independently-posable segments (upper arm / lower arm).
3. Select the Pose brush and open its Tool settings; the Deformation Target normally defaults to **Geometry**, which rotates purely based on mesh topology (Rotation Origins: Topology or similar) — functional but produces no cloth folds when bending a clothed character.
4. Change **Deformation Target to Face Sets** so the Pose brush picks up and moves along the Face Set boundaries you created, rather than guessing from raw topology.
5. For realistic cloth behavior, change Deformation Target to **Cloth Simulation** instead — moving/rotating the limb now runs an actual lightweight cloth simulation on the fly, producing genuine fold geometry as you pose, rather than simple smooth bending. This is slower than pure Geometry mode but gives convincing folds "for free."
6. Beyond simple rotate/twist, the Pose brush also supports **Scale** and **Squash & Stretch** as Deformation types. Using Squash & Stretch with Cloth Simulation active compresses the limb and generates dense, realistic wrinkle folds — though it also shortens the limb's apparent length.
7. **Recommended workflow to avoid unwanted shortening:** first stretch the limb out slightly using Geometry-based deformation, then switch to Cloth Simulation + Squash & Stretch and squash it back down toward its original length — this yields great folds while keeping proportions closer to correct.
8. **Cleanup:** squashing/posing can cause minor self-intersection at segment boundaries — fix small overlaps with the Smooth brush; for larger intersections after unhiding the rest of the mesh (Alt+H), hover over the problem area and press Alt+Q to set it as the active sculpt object, then use the Grab brush to manually pull the geometry back into place.

### Nodes / Settings
- **Sculpt tool:** Pose brush — Deformation Target (Geometry / Face Sets / Cloth Simulation), Deformation type (Rotate/Twist, Scale, Squash & Stretch), Rotation Origins, Pose Origin Offset, Smooth Iterations, Keep Anchor Point, Connected Only.
- **Face Sets:** "Face Set from Edit Mode Selection" (built from an X-Ray + Lasso Select region in Edit Mode).
- **Other brushes used:** Smooth (minor intersection fixes), Grab (larger intersection fixes after Alt+Q sets the active sculpt target).
- **Edit Mode:** X-Ray toggle, Lasso Select (for through-mesh region selection).
- **Shortcuts:** Alt+Q (set hovered object as active sculpt target), Alt+H (unhide).

### Difficulty
Advanced

### Blender Version
Not specified — Pose brush's Cloth Simulation Deformation Target is a relatively recent addition (Blender 3.x+), consistent with modern Blender 3.x-5.x.

### Tags
cloth, simulation, organic, rigging, advanced

---

## Related Tutorials
- [Blender Secrets - Hard Surface Sculpting Tips](blender-secrets---hard-surface-sculpting-tips.md) — shares organic, advanced; same channel, complementary Sculpt Mode brush/mask knowledge.
- [Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)](blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in.md) — shares cloth, simulation; same channel, complementary cloth-simulation-for-fabric-detail technique from a modeling (rather than sculpting) angle.

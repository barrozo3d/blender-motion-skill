---
title: Faster Alembic Playback in Blender (MDD Workflow)
source: YouTube
url: https://www.youtube.com/watch?v=H0_hfNoEv_I
author: DAMIDIGITAL
ingested: 2026-08-19
blender_version: "Not specified"
tags: [alembic, rigid-body, destruction, animation, rendering, cycles, intermediate, houdini-crossover]
extraction_status: complete
frames_dir: tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Faster Alembic Playback in Blender (MDD Workflow)

**Source:** [YouTube](https://www.youtube.com/watch?v=H0_hfNoEv_I)
**Author:** DAMIDIGITAL
**Duration:** 11m4s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello, everyone, I hope you're well.
[0:01] Today, I just have a quick tip video showing you how to optimize your Olympic imports into Blender
[0:05] and how to get them to play faster in the viewport.
[0:07] Let's get into it.
[0:08] So this workflow is only applicable for things that do not change the point count.
[0:11] So that means if you are adding points or detracting points from the scene or simulation,
[0:17] then it won't be applicable.
[0:19] So if you have a flowing water source, so like a tap turning on or a waterfall,
[0:25] you can't use this for that because of course the point count is not consistent.
[0:28] You can however use this for things like destruction simulations where the amount of points stay the same.
[0:32] So I'm going to get started and show you a quick example here.
[0:35] So I'm just going to make a scene that will be pretty slow to play back in Blender.
[0:39] And I know the so play back in Blender because I know how Blender is.
[0:43] Obviously, if you already have your scene set up, then you can skip ahead and the video will be chaptered, of course.
[0:49] So you can see exactly where to skip ahead to.
[0:51] But if you don't have your scene, I want to start from scratch.


### Example Scene Setup [0:52]
**Transcript (timestamped):**
[0:53] So I'm going to drop down a geo container.
[0:55] I'm going to go in to rename this because it's a good habit to name your nose.
[0:59] I'm going to name this example scene just because it's nice to name them.
[1:03] And I'm going to drop down a sphere.
[1:06] I'm not making any specific scene.
[1:08] I'm just making one I know will be slow to play back in Blender.
[1:10] So if you're following along, there's no secret here.
[1:13] It's just Blender is not the fastest of playing back Olympics.
[1:17] So I'm going to make a sphere and I'm going to increase the row count and the column count to something a bit higher.
[1:21] So it's purposely a bit slower to about 45, 33, just chosen arbitrarily.
[1:28] There's no reason for that.
[1:29] And then I'm going to drop down a grid so I can have an array of spheres.
[1:33] I want to have an array of spheres drop down and collide off each other.
[1:37] So I'm going to drop down a copy to points.
[1:42] And I've just dragged the grid, which you can see here.
[1:45] I turn points on.
[1:47] You can see those blue little dots are the points of the geometry.
[1:51] So I'm using these points to copy the spheres to which ends up looking like this.
[1:57] Just turn point view off.
[1:59] So grid points go into the right view, right input, which is the target points.
[2:03] And then left input is the sphere, which is the target geometry.
[2:07] Cool. So this is probably not going to be laggy enough.
[2:09] So what I'm going to do is I'm also going to drop down a mountain node,
[2:13] which is why I gave the spheres more geometry.
[2:16] So we can get a weirder surface.
[2:20] And then what I'm going to do after that is I'm going to do a copy and transform node on the grid.
[2:26] So we can increase the count basically of spheres that drop down.
[2:32] So I'm going to go ahead and increase that to three, maybe, and then translate it up by one.
[2:39] If I go to the copy of the points, you can see that I had increased that.
[2:44] I might give them a bit more clearance.
[2:45] So maybe you 1.5.
[2:47] There we go.
[2:49] And I might just copy and transform like four layers, actually.
[2:53] And then this is obviously too close to the floor.
[2:55] So I'm going to do not like transform after my mountain load.
[2:58] And I'm just going to increase the translation on the y axis.
[3:02] I had to think about it there because it's different in Houdini and Blender.
[3:06] And I'm going to increase that by like two.
[3:08] Oops.
[3:09] And I moved on the right axis.
[3:10] And that's just because I put the transform on the wrong side.
[3:12] Obviously, if we want to move all the layers, we'll have to do it on the grid side
[3:15] because that is where our points are coming from.
[3:16] So I'm going to drop that on this side and to take it off of an existing line.
[3:20] I just grab it and wiggle it, by the way, to take it off.
[3:23] So I'm going to move that and move up even more, maybe like five.
[3:27] That is 55.
[3:28] It's a bit high.
[3:30] Maybe even more, just 10.
[3:32] And then I'm going to save because you should always save.
[3:36] And then I'm going to drop down a RBD configure so we can be more specific about our collider.
[3:42] And I'm going to scroll down here to where it says collision shapes, geometry representation
[3:47] and leave it on convex hull.
[3:48] So I wanted to make a weird shape.
[3:50] You could probably get away with having some on the sphere, but the point is I'm trying
[3:53] to make a scene that is inefficient for Blender to read as an Alembic.
[3:57] So after that, I want to drop down an RBD bullet solver just because it's quite fast.
[4:04] We don't have constraints or proxy geometry, but those auto connect.
[4:07] So I'm just going to leave them.
[4:09] And then on the collision, I'm going to drop down a ground plane.
[4:14] And I do believe that these will bounce off each other, but I might just offset them to ensure it.
[4:20] So I'm going to go to the copy and transform node and I'm going to translate them a little bit on the Z axis.
[4:25] So maybe like by one or maybe point five so that they fall in between each other and don't balance.
[4:32] Cool.
[4:33] So I'm going to go ahead and press play probably a little bit laggy.
[4:35] It is indeed quite laggy.
[4:37] We're going to let that fall down to get just a bit.
[4:40] And as you can see, those all fall and collide off each other and all that good stuff.
[4:43] So I don't need to see the whole simulation.
[4:44] I'm going to drop down a file cache.
[4:47] I'm going to cache this out.
[4:49] So I'm going to name this cache falling rocks because they kind of look like rocks.
[4:54] And I'm going to make sure that is on a simulation time dependent frame range.
[4:59] And I'm going to go ahead and save the disk.
[5:00] So that's gone ahead and cached.
[5:02] I'm going to go ahead and play.
[5:03] Just to see.
[5:05] And even in Houdini is still very slow.
[5:06] So you can tell that when we bring it into blender is going to be impossible to watch this back.
[5:11] That's the ideal speed.
[5:13] So we have those golden nugget looking things falling down.
[5:17] So we're going to explore those out to blender now.
[5:19] We'll drop down a rock Olympic output.


### Alembic Output [5:21]
**Transcript (timestamped):**
[5:21] I'm going to leave it on render current frame on the first frame.
[5:24] I'm going to make sure you're on the first frame and then I'm going to rename it.
[5:29] Falling.
[5:31] Falling rocks ABC.
[5:35] If you forget the file extension on the end, it will save as just a non-descript file.
[5:40] You can just add ABC in Windows when you rename the file, but you might just do here.
[5:45] I'm going to leave all these things alone.
[5:47] I'm going to save and I'm going to click save the disk.
[5:49] And now we haven't unpacked our rocks.
[5:54] That's why I'm going to drop an unpacked node before that.
[5:57] And then I'm going to put one in there and save.
[5:59] There we go.
[6:00] I'm packing.
[6:00] I'm just going to keep it all as one piece of geometry when we import it into blender.
[6:04] So we don't have a million different pieces.
[6:05] So now if we jump over to blender, see, I have a previous example in there.


### Import Mesh To Blender [6:07]
**Transcript (timestamped):**
[6:09] Don't worry about that.
[6:11] I'm going to drop in our falling rocks in blender.
[6:14] Now you can just drag and drop before you can do it.
[6:16] But if you don't want to drag and drop, just file import.
[6:20] Alembic is the very top one.
[6:21] I'm going to drag and drop.
[6:22] You get the same settings.
[6:24] So it's going to ask me if I want to set the frame automatically.
[6:27] It will have the set frame range ticked, but our frame range is one frame.
[6:31] I'm going to untick that and leave relative path on.
[6:35] And then we have our rocks, which is no animation, which is what we want.
[6:39] And then we're going to go back to Houdini and we are going to go click on OBJ.


### MDD Export [6:41]
**Transcript (timestamped):**
[6:44] We're going to jump to the output level.
[6:48] So when you jump in here normally, there'll be nothing here.
[6:51] So I'm going to type MDD and we're going to get MDD point cache.
[6:56] We're going to drop that down.
[6:58] And in this node, we're going to change a couple of things.
[7:00] We're going to change the output.
[7:01] So I'm going to change this to falling rocks, mdd.mdd.
[7:06] The MDD is kind of redundant, but it's just like an easy to see it.
[7:09] I'm going to press save and then the soft path.
[7:12] I'm actually going to jump back out with something I should have done earlier.
[7:15] And I'm going to drop a null named out.
[7:21] And that will be my last.
[7:23] I just cut them black because I always cut my outputs black.
[7:26] If you want to do that, just click on the node you want, press C, choose your color.
[7:29] Works for any node.
[7:31] The reason that I making this null from the last edited node is so that if I make
[7:36] any changes, I don't have to then like come back.
[7:38] It's like if I put a, I don't know, an assemble or something after my unpack,
[7:44] I don't need to come back and choose, change it from unpack to assemble.
[7:47] I can just leave it on out.
[7:49] And that makes sense in a second.
[7:51] You don't understand that.
[7:52] So on the out, we're going to choose our soft path.
[7:55] I'll put it in all caps to always come up at the top.
[7:58] So there's my example scene out.
[8:01] And if I didn't have that out node, then I would be looking for the last one,
[8:05] which I think was the unpack.
[8:08] And then let's say you change it.
[8:09] Now you're going to have to look for the assemble.
[8:10] So just keep it on an out node, an output node.
[8:12] You can name it wherever you want.
[8:13] It doesn't have to be out.
[8:14] Just make sure it's in all caps.
[8:16] So now we have our MDD set up.
[8:17] We have the output file we want.
[8:18] We have our scene.
[8:21] We're going to do now is change it to render frame range.
[8:24] And we're going to save and render to disk.
[8:27] So that is finished out playing and we will be left with a limb big version
[8:33] and an MDD version.
[8:35] So I'm going to jump back into blender.


### MDD Import To Blender [8:38]
**Transcript (timestamped):**
[8:38] And here we have our static first frame.
[8:42] What we're going to do is we're going to come over to add modifier.
[8:46] So the modifier tab here, it's little wrench add modifier.
[8:48] I'm going to search MDD or sorry, and this is called mesh to form.
[8:52] So mesh cache.
[8:53] So there's mesh to form.
[8:54] Sorry.
[8:55] And there's mesh sequence cache and there's mesh cache.
[8:57] We're just going to drop down a mesh cache.
[9:00] The format automatically is MDD.
[9:02] All we need to do here is set a file path, go to where our project file is
[9:07] and choose our MDD version.
[9:09] So falling rocks, MDD.
[9:11] I'm going to select that and you can see it's now flipped it.
[9:14] I'm going to change the access mapping.
[9:15] You can just rotate that on any access you want.
[9:18] I'm going to change that to, I think is plus Z plus X.
[9:22] There we go.
[9:23] Just to correct that from Hibidini and if we press play, you can see 25 consistent
[9:29] frames and I'll give you a little side by side right here.


### Comparison [9:33]
**Transcript (timestamped):**
[9:33] So in this side by side, you can see that we have one that is very laggy around
[9:39] 10 FPS, 10 o'clock FPS and we have one that is playing a smooth 25 frames per
[9:46] second in a viewport.
[9:47] It's not causing me any lag and if you have more things in the scene, then it's
[9:51] going to be even lower.
[9:52] This is only the frame rate with just this example.
[9:55] Imagine if you had a full scene.


### Outro [9:56]
**Transcript (timestamped):**
[9:56] So that's basically it.
[9:57] It's a very quick tip.
[9:59] It's one I learned far too late into my career and I just wanted to share this
[10:04] with you now because I really couldn't figure out how people were rendering
[10:08] things in cycles.
[10:09] Obviously now I'm trying to render more and more things in comma, but if you're
[10:12] still in the stages where you prefer rendering in cycles, then this is how
[10:17] you would import destruction simulations and things like that.
[10:19] Again, the point count has to be consistent or it won't work.
[10:23] But again, first things like destruction simulations is almost completely
[10:27] necessary for you to do it this way to bring it into Blender or Cinema 4D.
[10:32] But this is specifically for Blender.
[10:33] Either way, I hope that was useful for you.
[10:35] As always, if you found this useful, I'd appreciate if you subscribed, left a
[10:39] like and left a comment.
[10:40] If you have any questions, I try to get back to them as soon as I can and I
[10:42] would just like to take a second to plug my Patreon, which we have over there.
[10:45] We have exclusive videos on the free tier.
[10:48] So you don't have to pay for all the exclusive videos, but there are exclusive
[10:50] videos on the free tier and all videos go up on the Patreon a week early,
[10:53] regardless of its paid or free.
[10:55] So please go check out the Patreon.
[10:56] We have some exciting stuff going on over there.
[10:57] I plan to have some really cool exclusives.
[11:00] So check out the Patreon and as always, have a good day.
[11:02] Take care.



---

## Captured Frames

- [1:17] tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/frame_000.jpg
- [4:33] tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/frame_001.jpg
- [8:52] tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/frame_002.jpg
- [9:14] tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/frame_003.jpg
- [9:35] tutorials/frames/faster-alembic-playback-in-blender-mdd-workflow/frame_004.jpg

---

## Structured Notes

### Core Technique
Speeding up point-cache mesh playback in Blender by exporting an **MDD point cache** (in addition to the Alembic geometry) from the DCC that ran the simulation, then driving the static Blender mesh with a **Mesh Cache** modifier instead of relying on Alembic's own (slow-to-play-back-in-viewport) sequence import — applicable only to sims with a constant point/vertex count (e.g. rigid-body destruction), not to sims that add/remove points (e.g. fluid).

### Summary
A short workflow tip video (DAMIDIGITAL) for anyone bringing external point-count-stable simulations (the example is a Houdini RBD/Bullet destruction sim) into Blender for Cycles/EEVEE rendering. About two-thirds of the runtime (roughly 0:00-8:38 of 11:04) is spent in **Houdini**, not Blender: building a deliberately viewport-heavy example scene (high-res spheres via Copy to Points on a grid, Mountain node displacement, stacked via Copy and Transform), configuring an RBD Bullet destruction sim (RBD Configure with Convex Hull collision shape, RBD Bullet Solver, a ground-plane collider), caching it with File Cache, exporting the result as an Alembic (.abc) sequence, then separately exporting the same geometry as an **MDD point cache** (via the MDD point-cache ROP at the object level, keeping a clearly-named/color-coded "OUT" null so downstream node changes don't require re-pointing the export). The **Blender-specific payoff** (the video's actual title/purpose) is short but is the real technique: import the Alembic once (first frame only, static, no animation) to get correct topology into Blender, then add a **Mesh Cache** modifier pointed at the .mdd file, correct the axis mapping for the Houdini→Blender coordinate difference (Forward/Up set to +Z/+X in the example), and press play. The side-by-side comparison shown is decisive: the Alembic-sequence version plays back around 10-13 fps in the Blender viewport, while the identical geometry driven by the MDD/Mesh Cache modifier plays a smooth, consistent 25 fps — with the gap growing worse the more objects/detail are in the scene.

### Key Steps
1. **(Houdini, for context/repro)** Build or already have a simulation whose point/vertex count never changes across the frame range — a hard requirement; sims that add or remove points (flowing water, most fluid sims) cannot use this workflow.
2. **(Houdini)** Cache the simulation (File Cache SOP) so playback is deterministic, then export the animated result as a standard **Alembic (.abc)** sequence via a Rock/Alembic Output node set to the full render frame range (Unpack the geometry first if it's still packed, to avoid a fragmented multi-piece import).
3. **(Houdini)** Separately, at the object/OUT level, add an **MDD point cache** ROP node, point its output at a clearly-named `.mdd` file, and set it to render over the full frame range too — this produces a second, lightweight per-vertex-position cache alongside the Alembic.
4. **(Blender)** Import the Alembic via File > Import > Alembic (or drag-and-drop); untick "Set Frame Range" so it doesn't force the scene to the cache's frame count, and leave Relative Path on — this brings in the correct static topology only (no animation yet).
5. **(Blender)** On that imported mesh, add a **Mesh Cache** modifier (search "Mesh Cache" in Add Modifier — not "Mesh Sequence Cache", which is the Alembic-driven variant). Set its file path to the `.mdd` file exported in step 3; format is auto-detected as MDD.
6. **(Blender)** Correct the **Axis Mapping** (Forward/Up) on the Mesh Cache modifier to account for Houdini's different up-axis convention — the video sets it to Forward +Z / Up +X to fix an initially "flipped" result.
7. Press play: the mesh now animates driven by the MDD cache, decoupled from Alembic's per-frame geometry-sequence overhead, at a dramatically higher and more consistent viewport frame rate.
8. This technique targets viewport playback speed specifically for Cycles/EEVEE workflows where you're evaluating a Houdini-sourced (or any external) point-stable simulation inside Blender rather than re-simulating it natively.

### Nodes / Settings
**Houdini side:** Copy to Points, Mountain, Copy and Transform, RBD Configure (Collision Shape: Convex Hull), RBD Bullet Solver, ground-plane collider, File Cache, Alembic Output (Rock Alembic Output), Unpack, MDD point cache ROP, Null ("OUT", output/all-caps naming convention). **Blender side:** File > Import > Alembic (Set Frame Range unticked, Relative Path on), Mesh Cache modifier (File Format: MDD, Axis Mapping Forward +Z / Up +X in this example).

### Difficulty
Beginner-to-Intermediate on the Blender side (a single modifier + import settings); the Houdini portion assumes existing familiarity with RBD/Bullet destruction setup and is shown at an intermediate pace without deep explanation.

### Blender Version
Not specified on screen or in the transcript; Mesh Cache is a long-standing core modifier, so this workflow is version-agnostic across recent Blender releases.

### Tags
alembic, rigid-body, destruction, animation, rendering, cycles, intermediate, houdini-crossover

---

## Related Tutorials
No direct match in the current blender-motion library — no other ingested tutorial covers Alembic/MDD import optimization or the Mesh Cache modifier. Readers interested in the Blender-native side of destruction simulation (as opposed to this video's import-a-Houdini-sim workflow) may want:
- How I made this bridge destruction scene in blender (`how-i-made-this-bridge-destruction-scene-in-blender.md`) — Blender-native Simulation-Nodes-driven fracture/destruction tooling, contrasted with this tutorial's "simulate elsewhere, import fast" approach.
- Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender (`superhero-landing-tutorial-02-ground-destruction-vfx-in-blender.md`) — Cell Fracture + Mantaflow, another Blender-native destruction/rigid-body pipeline.

A significant chunk of this video's runtime (the Houdini RBD sim build and the MDD export node setup, roughly 0:52-8:38) is Houdini-specific rather than Blender-specific; per this skill's cross-referencing convention, a stub pointing back to this canonical file was added to `houdini-wand/tutorials/INDEX.md`.

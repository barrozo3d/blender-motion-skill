---
title: Blender Secrets - (Long Version) Marvelous Designer-like Cloth Grabbing
source: YouTube
url: https://www.youtube.com/watch?v=1YqtY02n8iU
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (Cloth/Hook/Multires workflow, 2.9x-5.x)"
tags: [cloth, simulation, rigging, organic, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - (Long Version) Marvelous Designer-like Cloth Grabbing

**Source:** [YouTube](https://www.youtube.com/watch?v=1YqtY02n8iU)
**Author:** Blender Secrets
**Duration:** 15m12s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey friends, I mentioned later in this video that it will be very easy to make a script
[0:07] in chat.gbt that will automate a lot of the steps.
[0:11] I actually tried it and it did not take a couple of minutes, it took a couple of days,
[0:16] but still it really did work.


### Download [0:18]
**Transcript (timestamped):**
[0:19] And you can download this script, I haven't turned it into an add-on yet because I don't
[0:23] know how, I'm not a programmer.
[0:25] I guess you can download it from GitHub.
[0:28] When you extract it, you will find the script and the manual.
[0:33] So here's a little bit of explanation.
[0:35] The way you can load a script in Blender is you just open it, copy paste it and then here
[0:41] create a new text in the text editor or you can just open the text file here.


### Add Hooks [0:45]
**Transcript (timestamped):**
[0:49] Paste it, so this is all the code and then you can run it and as long as there's no error
[0:56] message, it seems to have worked.
[0:59] So now if you check the option panel with N, there are two things, add some hooks and
[1:07] remove hooks.
[1:08] And if you have your shirt selected and click on add some hooks, it will do everything.
[1:15] Set up the hooks, the vertex group, clotsim and the pin group and self-collisions and
[1:23] it will turn off gravity.
[1:25] So now when I play this, I can just have some fun with this, add some faults and when you're
[1:36] happy with that, you go to the remove hooks panel.
[1:39] You can use the middle mouse button to scroll through the option panels here and there's
[1:44] a remove hooks button.
[1:45] But very important, you need to select the shirt again and then click remove hooks.


### Add Mesh [1:52]
**Transcript (timestamped):**
[1:52] Okay, now it has removed the vertex group, the clots modifier and the empty stokes and
[1:59] you just have a mesh.
[2:09] I am going to add a as a browser and use a base mesh that I have downloaded from the
[2:20] Blender Studio and in fact, this is going to be a base mesh that is going to be included
[2:29] Blender in the future in the asset browser.
[2:33] They are going to add some base meshes, but for now you have to download them manually.
[2:38] I'll put the link in the description and this is a linked duplicate, I think.
[2:44] So I mean just press control A and make instances real.
[2:48] Otherwise we cannot do anything to the mesh and delete this empty.
[2:54] So now we have a mesh, that's great.
[2:59] Let me shade this fellow smooth.
[3:04] Let me make a shirt for him.
[3:08] In wireframe mode, deselect everything, go to circle select and just select some stuff
[3:17] on one side.
[3:22] Back to solid mode.
[3:27] You can activate circle select by pressing C and then just keep adding more to it and
[3:36] right click when you're done with it.
[3:38] Otherwise you cannot move around.
[3:41] Okay.
[3:42] If you want to remove stuff with circle select you just have to hold shift while using it.
[3:52] Okay, that looks good on one side.
[3:59] So now we're going to select mirror.
[4:03] Let the mirror as the selection, but if you click extend then it will mirror it and add
[4:07] it to the current selection.
[4:10] And we can just duplicate that with shift D and then press alt S to scale it up.
[4:22] Make sure you don't have auto merge vertices turned on because then it will just merge
[4:26] it immediately after the organic.
[4:29] So now we have a little bit of a gap and we can separate the short pressing P and using
[4:35] separate by selection.
[4:37] So if we're going to object mode now we have a short and his body.
[4:42] Let me make that a little bit more clear by turning on random.
[4:48] I think for the stimulation we probably need a little bit more geometry.
[4:54] So you can add a sub div modifier and apply it immediately.
[5:00] This should be enough I think.
[5:03] It's also important with the clotsims that you don't go too far with geometry in the
[5:07] beginning.


### Simulation [5:08]
**Transcript (timestamped):**
[5:08] Now one big problem is it's real world scale.
[5:12] It's about the average human male size and logically you would expect that that's good
[5:21] if you add a simulation.
[5:22] Here I'm adding collision to the base mesh and then I'm adding clots modifier.
[5:29] Look if we simulate this now it really won't look good because it's too small.
[5:38] So if we select all this and press S10 and enter it's 10 times too big now.
[5:46] It's an 18 meters tall dude.
[5:49] But press the spacebar and play the simulation.
[5:54] You'll see that the simulation works pretty good now.
[5:57] I recommend if your simulations don't look good just scale them up.
[6:03] That was just for demonstration.
[6:04] Let me just remove this for now.
[6:07] And first we're going to add some hooks because you cannot just grab a cloth like you could
[6:13] in Marvelous Designer for example.
[6:15] You have to add some hooks that Blender can hold on to.
[6:20] Of course I can add these on both sides but for the demonstration now I'll just add them
[6:25] on the front.
[6:26] I think that's good and we'll add this to a vertex group and click assign.
[6:35] If I deselect everything now by pressing select you can see everything that you have in that
[6:40] vertex group.
[6:42] Which is important because we have to add hooks by selecting one vertex, pressing H,
[6:48] hook to the object.
[6:51] And then I don't remember exactly which vertex I had selected so I have to use this button.
[6:58] To add all the other hooks and you cannot add them all at the same time because then
[7:01] it will just put one hook somewhere in the median point of those selected vertices.
[7:09] So we just have to do this in this stupid way.
[7:13] I guess you could very easily create a script that adds some random hooks maybe in chat
[7:22] GTP.
[7:23] Just ask it to do just that and then you don't have to do it like this.
[7:29] But I mean it only takes me a minute.
[7:33] Takes more than a minute to learn Marvelous Designer.
[7:36] Okay I think we got them all.
[7:41] Cool.
[7:42] Now back to object mode I will add a cloud modifier back.
[7:47] These quality steps and so on just really leave it alone until you are very happy with
[7:51] it if you are doing a real cloud simulation.
[8:03] Those kind of settings are just for when you are really happy with the cloud sim and then
[8:10] you are not experimenting with it anymore you can increase the quality.
[8:14] I have added a lot of frames in the simulation cache and also to the timeline so that it
[8:20] won't loop back to the beginning after 250 frames because we need to experiment with
[8:25] a bit so we need some time on the timeline.
[8:30] So now if you press this, wait one more thing.
[8:34] I forgot to add the pin group.
[8:38] So the pin group that's the vertex group that we made of those vertices that are with
[8:42] a hook now.
[8:45] And those are excluded from the simulation by using it in the pin group that way we can
[8:51] still manipulate those vertices.
[8:55] And enable self-conditions and maybe also just disable graph T to make them to keep it
[9:01] simple.
[9:03] So now if I play this.
[9:06] I can grab these in object mode and with G I can kind of move them around a bit.
[9:13] And you have to be careful.
[9:15] Just use it in a subtle way because faults can easily look bad.
[9:22] I mean especially if you just scope them from your imagination or it's best to use a reference
[9:29] of course just to find some pictures of faults or take pictures of yourself in poses so that
[9:36] you can maybe in the post that you're trying to make a sculpt of and then you have a good
[9:40] reference of what faults would really look like in clothes.
[9:44] But simulation is also a really good tool to do that.
[9:49] And we can use this as a guide later to sculpt some additional clothes there.
[10:03] So just cycle around a bit through these hooks and select them one by one and move them a
[10:09] little bit until it looks interesting.
[10:19] Of course even here it will add some faults even though I didn't have hooks there but
[10:24] because it's a clotsim it's also reacting on the back too when we're doing.
[10:30] Let me just move this one up a little bit.
[10:46] If you don't want to accidentally select the cloth itself you can just disable it in the
[10:52] other which for some reason resets the simulation.
[11:00] So then I have to undo and play.
[11:10] Okay that was not a good idea.
[11:14] Let me just quickly undo that.
[11:23] I'm just undoing it so the hooks are back in the place where they were.
[11:28] Let me just check that I didn't undo any settings because that happens sometimes in
[11:34] blender.
[11:36] Okay I'm gonna disable them right now from the start.
[11:40] Go back to first frame, press the space bar and let me do that again.
[11:55] So you see these faults are quite interesting.
[11:57] I think it would be difficult to come up with this from your imagination.
[12:05] Okay that's good enough.
[12:10] So I'll pause the simulation and I want to apply them all.
[12:23] But of course I cannot select and I'm afraid.
[12:26] Okay nothing happened.
[12:28] I was afraid I was going to make them selectable again that the clotsim would somehow disappear.
[12:34] Okay so press Ctrl A and choose visual Germany to mesh that just applies all the modifiers
[12:41] and then we have all those faults baked in.
[12:47] So we don't have to be afraid of the clotsim doing something weird.
[12:53] Nice maybe let's add a sensitive modifier at this point.
[13:01] Or actually let me add a multiverse modifier because I will be sculpting.
[13:08] The drawbush is a really good simple tool for adding faults and let me just reduce the
[13:22] strength a bit.
[13:25] Because I'm just sculpting with my mouse.
[13:30] Not recommended but when you're sculpting with your mouse of course you don't have pressure
[13:36] sensitivity so you have to kind of just set it manually.
[13:42] And I'm just being inspired now about the faults that were created by this simulation.
[13:53] Enhancing them a little bit adding a couple more faults to that.
[14:02] This will be difficult to do if you just started from zero and didn't have any simulation faults
[14:09] or reference or anything.
[14:15] You would be creating unrealistic faults really and people can tell because they're used to
[14:19] seeing clotting and faults all day long.
[14:28] If you don't like something you can just hold shift and erase it.
[14:33] Or hold control and go into the negative direction.
[14:39] Of course you have to be careful not to clip through the base mesh.
[14:45] Alright so that's how you can get some realistic looking faults using the clot simulation and
[14:54] some hooks.
[14:56] I guess we can remove this collision as well.
[15:02] Alright I hope you like it and if there's any question please just let me know in the
[15:08] comments.
[15:09] Thank you.
[15:10] Bye.



---

## Captured Frames

- [1:10] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_000.jpg
- [3:15] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_001.jpg
- [4:15] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_002.jpg
- [5:45] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_003.jpg
- [6:45] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_004.jpg
- [9:10] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_005.jpg
- [12:35] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_006.jpg
- [13:50] tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/frame_007.jpg

---

## Structured Notes

### Core Technique
Make a garment interactively grabbable like Marvelous Designer by rigging Hook modifiers onto Cloth-sim vertices (a Pin Group excluded from the simulation but still user-manipulable), scaling the whole scene up 10x for simulation stability, then baking and hand-sculpting the resulting realistic folds — including an optional custom Python script (downloadable from GitHub) that automates the repetitive hook-setup/teardown steps.

### Summary
A long, casual, unscripted walkthrough (auto-transcript contains some clear mishearings — "faults" = "folds," "clotsim" = "cloth sim," "Germany" = "Geometry," corrected throughout below). Frame 000 shows the author's custom automation script open in Blender's Text Editor (a bpy operator class defining vertex-group/hook/cloth-sim setup) next to the shirted character it targets — this script adds an "Add Hooks" / "Remove Hooks" pair of N-panel buttons that automate the entire hook-rigging process shown manually later in the video. Frame 001 shows the manual shirt-modeling stage: Circle Select (C) building up a shirt-shaped face selection on one half of a base-mesh character's torso. Frame 002 shows the completed, now-mirrored selection covering the full torso/sleeve area symmetrically. Frame 003 shows the critical scale-up step: the whole character scaled to 10/10/10 (visible in the N-panel Scale fields) to make the cloth simulation behave correctly, since Blender's cloth solver is tuned for near-real-world scale and a normal human-sized mesh sims poorly. Frame 004 shows the resulting Vertex Group weight-paint-style dot overlay on the shirt — the Pin Group used to mark which vertices are excluded from the simulation (held by hooks) versus left to simulate freely. Frame 005 shows several Empty objects (hooks) positioned around the shirt's shoulders/chest, one being moved (G) to interactively deform the cloth in real time — the actual "Marvelous-Designer-like grabbing" payoff. Frame 006 shows the Object → Apply menu with "Visual Geometry to Mesh" highlighted (Ctrl+A) — baking the cloth sim + hook deformation permanently into the mesh once the folds look good. Frame 007 shows the final hand-sculpting pass: a Multiresolution modifier added, Draw brush active (strength reduced for mouse-based sculpting without pressure sensitivity), enhancing the simulation-generated folds with additional hand-sculpted detail, visualized here with a colorful Face Sets overlay.

### Key Steps
1. **(Optional) Automate with the provided script:** download the author's Python script + manual from GitHub; open/paste it into Blender's Text Editor and run it (no errors = success). This adds "Add Hooks" and "Remove Hooks" buttons to the N-panel: with a garment selected, Add Hooks automatically sets up the vertex group, Cloth modifier, pin group, self-collisions, and disables gravity in one click; Remove Hooks (with the garment re-selected) tears all of that back down to a plain mesh again.
2. **Get a base mesh:** import/append a rigged or static human base mesh (e.g. from Blender Studio's asset library); if it's a linked duplicate, Ctrl+A → Make Instances Real so it can actually be edited, then delete the now-unneeded parent Empty. Shade Smooth the result.
3. **Model a simple garment from the body mesh:** in Wireframe mode, deselect all, use Circle Select (C, hold Shift to subtract, right-click to exit the tool) to select a shirt-shaped patch of faces on one side of the torso/arms; use Select → Mirror (with Extend enabled) to add the mirrored half to the selection; Shift+D to duplicate the selected faces, Alt+S to scale them outward along normals (create a small gap above the body's surface) — make sure Auto Merge Vertices is off first, or the duplicate will immediately re-merge with the body. Press P → Separate by Selection to split the duplicated shell into its own "shirt" object.
4. **Add simulation geometry:** cloth sims need reasonably fine geometry but not excessive density — add a Subdivision Surface modifier and apply it immediately for just enough resolution.
5. **Scale up for simulation stability:** Blender's cloth solver is tuned around real-world human scale but often still sims poorly at 1:1 — select everything and scale up (e.g. S, 10, Enter) to make the simulation behave dramatically better; scale back down after baking if needed. (This is presented as a general troubleshooting tip: "if your simulations don't look good, just scale them up.")
6. **Rig hooks manually (if not using the script):** since Blender's cloth sim can't be grabbed directly like Marvelous Designer's cloth, you must add Hook modifiers as grab handles. Create an empty Vertex Group; select one vertex at a time on the garment, press H → Hook to Object (there's no way to hook multiple vertices to independent handles simultaneously — doing so would place a single hook at their combined median point) — repeat per hook point, add each hooked vertex to the vertex group and click Assign so you can later select "everything in that group" to double check.
7. **Set up the Cloth modifier:** add a Cloth modifier to the garment; leave Quality Steps and similar settings alone while experimenting, only raising them once you're happy with the simulation and are done iterating; extend the Simulation Cache frame range and the Timeline's End frame (default 250) so you have room to experiment without looping. Set the Pin Group to the vertex group containing your hooked vertices (this excludes them from the simulation so they stay directly controllable) — this step is easy to forget. Enable Self-Collisions; the author also mentions disabling gravity here ("keep it simple" — likely so the shirt doesn't sag from gravity while you're manually posing folds via hooks) — note: the transcript mis-heard this setting name, cross-check against Cloth → Field Weights → Gravity in-app if replicating.
8. **Grab and pose folds:** in Object Mode, play the simulation, then select individual hook Empties and move them with G to interactively create folds — work subtly, since folds can easily look unnatural if overdone or purely improvised. Reference photos of real fabric folds (or photos of yourself in the target pose) give far more convincing results than sculpting from imagination. Cycle through the different hooks one at a time, nudging each until the fold pattern looks interesting; folds can appear even in un-hooked areas because the whole piece is one connected cloth simulation. (Caution flagged in the video: disabling a garment's selectability while the sim is active can reset the simulation — if that happens, undo carefully and re-verify no settings were accidentally reverted, a known Blender quirk.)
9. **Bake and refine:** once the fold pattern looks good, pause the sim and Ctrl+A → Visual Geometry to Mesh to permanently apply the Cloth modifier (and hooks) — this locks in the folds as static geometry so nothing can move or break afterward. Add a Multiresolution modifier for further hand-sculpting; the Draw brush is a simple, effective tool for adding/enhancing folds (reduce brush strength if sculpting with a mouse, since there's no pressure sensitivity to modulate it automatically) — use the existing simulation-generated folds as inspiration/guides and add complementary detail by hand. Hold Shift to erase unwanted additions, Ctrl to invert direction (push in instead of out); be careful not to sculpt through and clip the underlying body mesh. Remove the now-unneeded Collision modifier/setup from the base body mesh once finished.

### Nodes / Settings
- **Modifiers:** Subdivision Surface (applied for sim-ready density), Cloth (Pin Group, Self-Collisions, Field Weights → Gravity, Quality Steps, Cache frame range), Collision (on the base body mesh, removable after baking), Hook (per grabbed vertex, target = an Empty), Multiresolution (for post-sim hand sculpting).
- **Selection/modeling:** Circle Select (C, Shift to subtract), Select → Mirror (Extend), Shift+D (duplicate) + Alt+S (scale along normals), P → Separate by Selection, Auto Merge Vertices (must be OFF during shirt duplication).
- **Rigging:** H → Hook to Object (one vertex at a time), Vertex Group + Assign (for building the Pin Group).
- **Apply:** Ctrl+A → Visual Geometry to Mesh (bakes Cloth+Hooks permanently).
- **Sculpt:** Draw brush (Strength reduced for mouse use), Shift (erase), Ctrl (invert direction), Face Sets (used here just for visualization contrast).
- **Scale trick:** scaling the whole rig 10x before simulating for better cloth-solver stability at otherwise-real-world scale.
- **External tool:** custom author-provided Python script (GitHub, not yet packaged as an add-on) — "Add Hooks"/"Remove Hooks" N-panel operators automating steps 6-7.

### Difficulty
Advanced

### Blender Version
Not specified — Cloth modifier (Pin Group, Self-Collisions), Hook modifier, and Multiresolution workflow, consistent with modern Blender 2.9x-5.x.

### Tags
cloth, simulation, rigging, organic, advanced

---

## Related Tutorials
- [Blender Secrets - In Depth Cloth Sculpting tricks with Pose Brush](blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush.md) — shares cloth, simulation, organic, advanced; same channel, complementary sculpt-mode approach to generating realistic cloth folds (Pose brush + Cloth Simulation deformation vs. this video's Hook+Cloth-modifier grabbing).
- [Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)](blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in.md) — shares cloth, simulation, rigging; same channel, its "draped cloth with interactive hook" segment is a simpler version of this same Hook+Pin-Group technique.

---
title: Ruffled Skirts | Virtual Fashion | Blender Tutorial | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=hJ5zUTp9zCc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ruffled-skirts-virtual-fashion-blender-tutorial-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Ruffled Skirts | Virtual Fashion | Blender Tutorial | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=hJ5zUTp9zCc)
**Author:** Blender Secrets
**Duration:** 11m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ruffled-skirts-virtual-fashion-blender-tutorial-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] OK, so let's make the ruffled part of this skirt.
[0:06] I've temporarily added a female base mesh so that there's something to collide with
[0:12] for the ruffles.
[0:13] And I've added a collision.
[0:15] You can click on collision and any object with collision will interact with the clotsim.
[0:23] I don't need that to be visible, so...
[0:32] And I can just easily select this and extrude it.
[0:37] Right click to undo the transformation and then scale that up.
[0:43] Maybe let's scale it a bit more evenly.
[0:48] OK, and add an edge loop here.
[1:00] Press 3 to have face selection and then Alt-click to select the entire loop.
[1:07] I mean this loop.
[1:10] Press X and delete only faces.
[1:12] As you can see, the edges are still there.
[1:15] These are kind of like stitch threads, I guess.
[1:24] And let's add a little bit more resolution to the rest of this now.
[1:28] So when we use the clotsim, we can stitch these lines.
[1:34] And this edge will snap to here.
[1:38] But because it's too big, it will get ruffled.
[1:41] Let me just show you.
[1:44] Right away.
[1:47] That's not good.
[1:51] I have a pin group, but I'll remove it and restart.
[1:55] So I create a pin group and I will select all of the parts that I don't want to have
[2:04] simulated for now.
[2:07] Because otherwise this will just fall down.
[2:10] So I assign that.
[2:12] And just in case, I invert the selection and remove.
[2:15] Now normally if I check it in weight paint mode, yeah.
[2:19] So everything that's red will be pinned, will be in that group.
[2:24] Everything that's blue will not be.
[2:26] It's a bit strange that this is in there.
[2:33] Everything that's red is weight of one.
[2:37] Everything that's blue has a weight of zero.
[2:43] And now I'm going to use that as I'll add a clotsim.
[2:48] I was on frame 220.
[2:49] Let me go back all the way.
[2:53] So here there is a pin group.
[2:55] So you can add the vertex group to that.
[2:58] Now when we run the simulation, only this part which is not pinned will move.
[3:03] And we have to enable sewing or sewing.
[3:06] Excuse me.
[3:10] And let's have self collisions because that always looks better.
[3:13] And let's try to simulate that.
[3:17] Okay.
[3:21] So this is the result with the default settings.
[3:23] But actually Blender has all these interesting settings here.
[3:27] For example denim.
[3:30] Let's check that out.
[3:32] Always go back to the beginning of the timeline when you're doing a simulation.
[3:35] Press play.
[3:36] Okay.
[3:37] Let's stop that.
[3:42] I think that's pretty nice except there's some weird stuff going on here.
[3:49] And try one more preset and that is a leather or let's try rubber.
[3:54] In fact, rubber is a bit heavier because it's heavy.
[3:57] It will pull this stuff down.
[4:01] Start from the beginning and play.
[4:04] All right.
[4:06] So that looks nice.
[4:08] I think I'll prefer this preset.
[4:12] You can choose a frame that you think it looks the best.
[4:17] Now it looks kind of interesting here.
[4:21] Over here.
[4:25] Of course in the beginning it's all flaring out a bit.
[4:32] Maybe that's what you want.
[4:33] Something like this.
[4:34] Oh, I like this.
[4:37] Yeah.
[4:39] We can just apply this.
[4:41] Otherwise we might lose the result.
[4:44] Now you see that's just applied to the geometry.
[4:46] That's just the way it is now.
[4:49] But there's this little gap here.
[4:52] You can see there's a gap and it still has those edges.
[4:57] But if we hold shift and alt, left click on both of these edge loops, then we can right
[5:08] click and choose bridge edge loops.
[5:14] So now those are all filled.
[5:18] And to make it a little bit less abrupt, I guess we can alt left click on this and then
[5:23] control and plus to increase the selection a bit.
[5:29] And then with the vertex selection we can choose smooth vertices and then shift R to
[5:35] repeat it a few times.
[5:43] Maybe these as well.
[5:50] That looks a little bit better now.
[5:59] Of course you can add a solidify modifier.
[6:03] Make it a bit...
[6:06] Okay, it's a little subtle thickness.
[6:09] Maybe even a subdivision modifier.
[6:12] Nice.
[6:19] Let's add two layers of ruffles to this.
[6:23] Like this.
[6:27] First of all, let's do the one at the bottom.
[6:32] We can just select this edge loop like before, extrude it, scale it up.
[6:40] And maybe we can turn it into a circle.
[6:47] And doing the same.
[6:50] First let's finish this one.
[6:56] Select these faces, delete only faces.
[6:59] And then we can add some more loops.
[7:03] And then maybe here.
[7:09] Yep, I can do the same thing, extrude.
[7:16] Make it more circular.
[7:23] And delete these...
[7:27] These guys only faces.
[7:31] We need to flip the normals here.
[7:33] Shift N and flip them again.
[7:36] And now we can add some more loops.
[7:44] Now I want to hide this temporarily.
[7:49] And this too.
[7:52] So that I can select all of this and add it to the effects group.
[8:02] Okay, that looks good.
[8:04] So everything that's blue will be affected by the simulation.
[8:08] Everything in red not because we'll add it to the pin group of the cloud simulation.
[8:13] In fact, let me do that right now.
[8:17] Here in the pin group.
[8:21] We enable stowing and self-collisions.
[8:25] And as the preset, let's try out silk this time.
[8:29] Play it from the beginning of the timeline.
[8:39] Let's try another preset.
[8:43] It looks interesting, but I think the...
[8:47] The sewing force needs to be a bit higher with rubber.
[8:51] Because rubber is very heavy.
[8:55] So let's try that again.
[8:59] Okay, that looks much better.
[9:03] Let's see if we can find the most interesting frame.
[9:07] Okay, that looks much better.
[9:11] I find the most interesting frame.
[9:15] I like this.
[9:19] So I'll apply it.
[9:23] And now we have the mesh.
[9:27] I do recommend separating this again as a separate mesh.
[9:35] Pressing P, separate by selection.
[9:39] And then you can add a solidify modifier and a
[9:43] sublif modifier. It looks nice.
[9:47] Let me see, because there are a lot of ugly
[9:51] additional vertices here.
[9:59] Let me just delete all these.
[10:03] No, I should have deleted vertices.
[10:07] Now I have a big chunk missing.
[10:11] How should we do this?
[10:15] Delete vertices.
[10:19] Bridge this.
[10:23] And then just add a patch loop.
[10:27] And maybe we can relax these a bit.
[10:31] So that looks a bit better now.
[10:35] Of course in sculpt mode you can
[10:39] use the grab brush.
[10:43] And maybe pull this stuff out a bit more.
[10:47] With that border shoe.
[10:51] And you can always make it fit a bit better.
[10:55] And you can always make it fit a bit better.
[10:59] And for this we have this.
[11:03] The gap that we can fix in the same way as before.
[11:07] We just select both and then bridge edge loops.
[11:11] And we can
[11:15] increase the selection and smooth it out.
[11:19] Some.
[11:23] Some.
[11:27] Some.
[11:31] That looks better.
[11:35] And then this one can also have
[11:39] the same modifiers.
[11:43] So these are the results.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

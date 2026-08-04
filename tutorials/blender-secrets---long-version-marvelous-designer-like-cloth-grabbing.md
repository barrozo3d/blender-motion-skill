---
title: Blender Secrets - (Long Version) Marvelous Designer-like Cloth Grabbing
source: YouTube
url: https://www.youtube.com/watch?v=1YqtY02n8iU
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - (Long Version) Marvelous Designer-like Cloth Grabbing

**Source:** [YouTube](https://www.youtube.com/watch?v=1YqtY02n8iU)
**Author:** Blender Secrets
**Duration:** 15m12s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---long-version-marvelous-designer-like-cloth-grabbing <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

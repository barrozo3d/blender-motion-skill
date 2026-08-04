---
title: Cloth Tearing with Geometry Nodes in Blender 5.2 - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=nhhv9lw152A
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cloth-tearing-with-geometry-nodes-in-blender-52---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Cloth Tearing with Geometry Nodes in Blender 5.2 - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=nhhv9lw152A)
**Author:** Blender Secrets
**Duration:** 11m37s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cloth-tearing-with-geometry-nodes-in-blender-52---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### 1-minute summary [0:00]
**Transcript (timestamped):**
[0:00] To create this clod tearing simulation, first make sure you have Blender 5.2 installed.
[0:05] Add a grid and subdivide it a few times in edit mode, then try and validate it.
[0:10] Open the geometry node editor and click on new.
[0:13] Add the new Clod Dynamics node.
[0:15] Add empties at any point where you want to control the clod.
[0:18] Then add a vertex near each empty to its own vertex group.
[0:22] Drag an empty into the node editor to create an object info node.
[0:25] Add a named attribute node for the vertex group and select the group close to that empty.
[0:30] Search for a typed bundle node, choose Pin Position and then connect the nodes like this.
[0:36] Duplicate these nodes for as many empties as you have and then select the right empty and pin group in each.
[0:42] Search for a combined bundle node so you can connect everything and plug it into the effector's input.
[0:47] Now you can play the simulation and manipulate the clod with the empties.
[0:51] Turn on tearing and set it to custom so that we can control where it tears.
[0:56] Create a vertex group to control where the clod tears and then plug that into the tearing input.
[1:01] Now when we pull on the clod with the empties, it will rip apart.


### Step by step tutorial start [1:05]
**Transcript (timestamped):**
[1:06] So now that we've seen it in one minute, let's look at setting up this system step by step.
[1:12] So we're gonna get rid of this cube and I'm going to add a grid.


### The old-fashioned workflow for Cloth Hooks [1:16]
**Transcript (timestamped):**
[1:17] Grid is just a plane which already has some subdivisions and I'm going to subdivide this a couple of times
[1:24] and I'm also gonna triangulate it because, well, people say that triangulated cloth meshes look more realistic.
[1:35] So let's do it like that.
[1:36] Now typically what you would do is you would select the vertex, control H, hook to new object and you add a vertex group, call it.
[1:47] Pin one and assign it.
[1:50] And we'll just do that for each corner.
[1:57] So I have four vertex groups, one for each corner.
[2:02] And I'm gonna quickly rename these hooks because now they're just called empty and I want to call them hook one to four.
[2:09] And renaming them will make it easier to use them in the geometry notes setup later.
[2:18] So the way this would work with the old cloth modifier is we put the pin groups in the hook modifiers that were added when we pressed control H.
[2:29] And then we just collapse these to make some space and then we would add a cloth modifier.
[2:34] So not the new one, but the old one.
[2:38] And let me just open a timeline.
[2:44] And let's go to the beginning and so it falls down.
[2:53] And that's because when you use the old fashioned cloth modifier, you need to add those vertices from the various pin groups to one big pin group as well.
[3:04] And you need to add that in the cloth modifier.
[3:08] So here under shape, we need to add the pin group, which combines all those four vertices.
[3:15] And then we get this and then we can manipulate the cloth in real time.
[3:23] So that's great.
[3:24] Let's have a look at how we would do this with geometry notes instead.


### New Geometry Nodes Cloth Hook workflow [3:25]
**Transcript (timestamped):**
[3:28] So I will open a geometry notes editor.
[3:34] And the first thing we'll do, of course, is we'll remove this cloth modifier.
[3:40] So I'm just going to click on this X here to remove it.
[3:43] And I'm actually going to remove those hook modifiers as well.
[3:46] So I have no modifiers at the moment.
[3:49] I'm just going to click on new here and that adds a geometry notes modifier.
[3:55] And then what I'm going to do is I'm going to add the experimental cloth geometry notes note.
[4:04] And if we play it now, it will just fall down because it's not connected to those hooks yet.
[4:10] And so we need to add those hooks to the geometry notes setup.
[4:15] And we can do that with a object info note.
[4:17] But of course, the easiest way to do that is to just drag these guys in.
[4:22] Actually, let me just use this one for now.
[4:27] And then we also need a named attribute note.
[4:33] And this is for the pin.
[4:35] So I'm just going to select the pin one for hook one.
[4:39] And then we need to combine these two.
[4:42] And there's a couple of new combined notes.
[4:45] And we can use a combined note.
[4:46] So let's search.
[4:49] But we have this combined bundle notes, but it doesn't really have the input step we need.


### Typed Bundle node [4:55]
**Transcript (timestamped):**
[4:56] Instead, what we're going to do is use a typed bundle.
[5:03] OK, and then we're going to click here and we are going to select or search for pin position.
[5:12] And now we have what we need.
[5:14] And so from the object info, I'm going to take the location.
[5:18] And I'm going to plug it into the position here.
[5:22] And for the named attribute, I'm going to take this and I'm going to plug it into the selection.
[5:27] I guess I should probably switch them around.
[5:30] It's a bit cleaner in terms of the notes.
[5:33] So the pin group goes into the selection and the hook location goes into the position.
[5:40] And I'm just going to duplicate this a few times.
[5:43] Let me just put this here.
[5:45] Maybe I'll just move this out of the way.
[5:48] So I'm just going to duplicate this four times because we have four pins.
[5:55] And I'm just going to add the correct pins and hooks to these.
[6:07] There you go.
[6:09] Now all we need to do is combine these and then we can do that with the combined bundle notes.


### Combine Bundle node [6:10]
**Transcript (timestamped):**
[6:14] So we just drag these in.
[6:24] So now we have the four hooks and their pin groups and we are going to plug them into the effectors here.
[6:30] Let me just open this.
[6:32] So we're going to plug this into the effectors.
[6:35] And so now let's go to the beginning of the timeline.
[6:37] And now, as you can see, we can move this around.
[6:43] It's very important though that you have removed those old hook modifiers.
[6:47] Otherwise, this won't work.
[6:50] So now we can manipulate this in real time.
[6:54] And if you want, you can change the stretchiness as you can see.
[6:59] Well, that's very stretchy and bendiness.
[7:03] And that's also fun to play with.
[7:06] Maybe we'll just use a very small value for both of these.
[7:11] And you're going to set this to the shade smooth.
[7:14] And if that doesn't work, what you can always do is you can add a shade smooth note.
[7:21] Just plug it in there and now we have our smooth callout.
[7:25] And I'm just going to add some nice matcap to that just to make it a bit more visual.
[7:33] Now, what I would like to do is I would like to tear this in half.


### Tearing [7:35]
**Transcript (timestamped):**
[7:37] So let me just put this back here.
[7:43] And so what we need to do is we just need to enable tearing, simple as that.
[7:48] And tearing has a specific threshold.
[7:51] But let's just see what happens if we just take these two and we scale them away from each other on the X axis.
[7:58] And so what happened is it got torn there where the hook is connected to the cloth,
[8:04] which makes sense because that's where most of the stress would be.
[8:08] But I would like to kind of tear it in the middle here.
[8:11] So to do that, what I'm going to do is I'm just going to make sure everything is unselected in edit mode.
[8:19] And then just with the circle select, I've selected these.
[8:23] And I'm going to add that to another group.
[8:26] And by the way, we don't need this bin group anymore.
[8:28] That was only for the old fashioned callout modifier.
[8:33] So I'm just going to call this tearing group and I'm going to assign that.
[8:41] And then we're going to just plug that in with a name to attribute where I can just duplicate one of these
[8:47] and select the tearing group.
[8:49] And then we are going to have to set it to custom because now it's set to all,
[8:54] which means that all vertices or all edges can tear and that's set it to custom.
[8:59] So the tool info says all edges in a custom edge selection can tear.
[9:04] So I'm just going to plug that into the edge group there.
[9:07] That could be that we have to make a new attribute here and select some edges instead of vertices and set that attribute.
[9:15] But I think it probably works.
[9:17] Let's see.
[9:19] So let's play it and let's scale these away from each other.
[9:25] And at some point it should start tearing.
[9:27] Yes, there you go.
[9:34] So I'm not really sure yet how to avoid having all those tiny triangles.
[9:39] I'm just reset that.
[9:44] But this is already getting closer to what I want.
[9:48] So let me just full screen this so you can see the full node setup.
[9:52] So it's pretty simple, just the new cloth nodes and basically this is all you need.
[9:59] These are just extra hooks.
[10:03] But if you just want to use one hook or experiment with having one hook, you can just use this.
[10:08] So you just need a named attribute for the vertex group.
[10:13] The object info nodes for the hook, which you can just drag and drop from the outliner.
[10:18] A type.
[10:19] So let me just show that again.
[10:21] So you search for type and then you have a typed bundle.
[10:24] And then you search for the pin position and then you get this node.
[10:30] Connect them like this and then you can, if you have more hooks, you can combine them with a normal combined bundle node,
[10:36] which you can search for like this.
[10:42] And those just all plug into the effectors.
[10:44] And if you want to have a custom tearing group, then you just need another vertex group for that.
[10:50] And you need to turn on tearing.
[10:52] And that's pretty much it.
[10:54] You can also change the threshold for the tearing.
[10:57] So let's see what that does.
[10:59] If we try that, then it just takes more force to tear this apart.
[11:08] Maybe a bit too much force.
[11:10] Let me just try that with a more reasonable value like two.
[11:16] And then it will tear apart.
[11:18] So it seems that really that default value of 1.2 is the best one.
[11:23] So yeah, if you have any suggestions on how to make this work even better, please let me know in the comments.
[11:29] I'm not an expert on geometry nodes, so I am happy to learn.
[11:33] And thanks for watching all the way to the end.



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

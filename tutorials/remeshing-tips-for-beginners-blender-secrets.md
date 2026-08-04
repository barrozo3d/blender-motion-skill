---
title: Remeshing Tips for Beginners | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=3VNiWcO1QN8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/remeshing-tips-for-beginners-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Remeshing Tips for Beginners | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=3VNiWcO1QN8)
**Author:** Blender Secrets
**Duration:** 7m31s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py remeshing-tips-for-beginners-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### When to Remesh [0:00]
**Transcript (timestamped):**
[0:00] So what is remeshing and when do you use it?
[0:03] Well, let's say I'm sculpting and I use the Snakeook brush to drag out an arm for the
[0:07] sketch.
[0:09] If you look at it in edit mode you'll see that no new geometry was created, it was just
[0:14] stretched out.
[0:16] So if I try to sculpt on this stretched geometry it will not go well.
[0:20] And that is where remeshing comes in.
[0:23] Let me turn on front faces only so the brush doesn't destroy the geometry.
[0:29] Now I can sculpt on the arm that I pulled out using the Snakeook brush.
[0:34] New geometry was created so the mesh has an even distribution of quad faces.
[0:39] I'll just use the Inflate brush to add some thickness.
[0:45] And smooth it out by holding shift.
[0:48] Another reason to use remeshing is when you want to join two objects.
[0:52] If I select both while holding shift and press Ctrl J to join them, you can see that there
[0:59] are really still two separate mesh islands.
[1:03] The top of the tail object is visible inside of the cat body.
[1:07] However, when we do a foxle remesh in sculpt mode, now we can add some clay strips and
[1:13] smooth the area connecting the tail and the cat's butt.
[1:19] After some more smoothing it's a nice transition from body to tail.


### Remeshing Methods [1:25]
**Transcript (timestamped):**
[1:26] Let's look at some different methods of remeshing in Blender.
[1:29] Press R for the foxle preview.
[1:32] You can hold shift to have more precise control over the foxle size.
[1:36] Then press Ctrl R to foxle remesh.
[1:41] I'll turn on wireframe so you can see the result better.
[1:44] So this is the result.
[1:45] As you can see the remeshing has also created some kind of banding.
[1:49] For sculpting this is not really an issue, but let's see if we can get something that's
[1:53] better anyway.
[1:56] Let's try some options.
[1:57] I'll select this mesh first with Alt Q and enable fix poles and preserve volume in the
[2:03] remesh option now.
[2:05] This forces the remeshing to create better topology and preserve the shape better, but
[2:09] it takes a little bit longer.
[2:13] Press R for the foxle remesh and then Ctrl R to remesh.
[2:18] Let's have a look at the wireframe again.
[2:25] As you can see it has created more consistent quad topology.
[2:30] Let's try some more things with this third head.
[2:34] By clicking on quad in the remesh options you get this quadroflow remesh menu.
[2:42] Very often quadroflow won't work if you just try it without any preparation.
[2:46] It helps to do a foxle remesh first.
[2:49] Let's still use the fix poles and preserve volume options.
[2:54] For this time I'll go with a smaller foxle size to preserve the shape even better.
[3:00] A foxle size of 0.002 meters.
[3:04] Instead of pressing Ctrl R you can also press remesh in this panel.
[3:10] Let's try quadroflow again.
[3:14] As you can see it works this time.
[3:19] Let's check the wireframe.
[3:21] Definitely out of the three this is the best result.
[3:25] Unfortunately the left and right half are separate meshes but we can fix that.
[3:31] First select all vertices in edit mode.
[3:34] Then press M for merge and choose by distance.
[3:38] Now the halves are merged.
[3:39] As you can see 119 vertices were removed as a result.
[3:44] This is because they were overlapping in the same location.
[3:50] Looks like merging by distance didn't completely fix things.
[3:53] In the mouth and nose area there is a slight gap.
[3:56] So let's use a mirror modifier.
[3:59] And that seems to have done the trick.
[4:03] I have kept a hidden duplicate of the head in the same location.
[4:09] If I add a shrink wrap modifier to the remeshed head I can use the hidden duplicate as the
[4:14] target.
[4:15] This helps to keep the shape of the remeshed head more like the original.
[4:19] You can see the difference when I disable the modifier.
[4:23] Press Ctrl A and choose visual geometry to mesh if you want to apply both modifiers at
[4:27] once in the red order.
[4:29] So these are three methods of remeshing.
[4:32] By putting in a bit more work we get better results.


### Troubleshooting [4:36]
**Transcript (timestamped):**
[4:37] Foxhole remeshing sometimes gives a weird result.
[4:42] Like this it's certainly full of holes.
[4:46] If that happens you can use a remesh modifier instead.
[4:50] And instead of the default foxhole option set it to smooth.
[4:54] Increase the octree depth until you get a good result.
[4:59] And then apply the modifier.
[5:03] The result is quite dense.
[5:07] If you try foxhole remeshing now however it will work.
[5:12] The reason to also do a foxhole remesh after this is that you get a less dense result.
[5:19] Now let's see if we can do a quadroflow remesh on this hand.
[5:25] This is the result.
[5:29] One typical issue with things like fingers is something called spirals.
[5:35] Now this is not really an issue for sculpting.
[5:39] But if you are using remeshing to help you with retopology you would have to manually
[5:43] fix these fingers.
[5:44] Otherwise the topology is not good for rigging an animation.
[5:49] One solution for this is the paid addon quad remesher.
[5:52] Select the object and click on remesh it.
[5:57] Boom magic.
[6:01] It creates really good topology in just one click.
[6:06] And no spiraling on the fingers.
[6:10] Definitely worth getting if you are a professional 3D artist as it will save you a lot of time.
[6:16] I think it's important to mention that remeshing is not the same as retopology.
[6:22] Remeshing as we've seen is the process of recreating the mesh in the context of a sculpting
[6:26] workflow.
[6:28] Retopology is when you create a new mesh based on your sculpt which has topology that is
[6:33] suitable for a game or movie asset.
[6:36] For example rigging and animation of characters has specific requirements for edge flow for
[6:41] better deformations.
[6:43] If you want to learn more about all of this I recommend Zach Reinhardt's master 3D sculpting
[6:48] in Blender course.
[6:49] He goes over the entire workflow for manual retopology as well as discussing free and
[6:54] paid addons that help with this task.
[6:56] It's a great resource that I often use myself when I need to look up some specific sculpting
[7:00] brush information.
[7:02] I also have a playlist on YouTube with retopology tips so you can check that out as well.
[7:07] I hope this video helped you understand remeshing and the difference between remeshing and retopology.
[7:13] Thank you for watching all the way till the end and happy sculpting!



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

---
title: Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=75inBBl39es
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=75inBBl39es)
**Author:** Blender Secrets
**Duration:** 7m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vertex-groups-modifiers-and-tissue-add-on---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So I was going through my book randomly just hunting for outdated topics and updating them.
[0:06] And I found this tissue topic about the tissue add-on, which is pretty interesting and I hadn't used this add-on for years.
[0:14] So I figured I would make a updated version of it.
[0:17] And although the add-on still works pretty much the same in Blender 4.3.2, I thought it would be interesting to do a new video about it.
[0:26] And to make it a bit more interesting this time, instead of a sphere, I used these human-based meshes from the Blender Studio.
[0:33] And you can download this from the Blender demo scenes page.
[0:37] To download it, just click on this.
[0:38] And while we're downloading, we come to this page, which urges us to donate to Blender.
[0:43] It's pretty shocking that less than 0.1% of users donate to Blender.
[0:49] So definitely something to consider, even if you just pay one time.
[0:52] Once you extract the download, then you get this blend file, which contains all the assets.
[0:57] And as you can see, there are already marked as assets.
[1:01] So you don't actually need to do anything in this file.
[1:04] You don't even need to open it really.
[1:05] And all you need to do is save it in a location where you can just keep it there.
[1:12] So don't keep it on your desktop.
[1:13] Don't keep it in your downloads folder.
[1:15] Keep it in like a 3D assets folder on a hard drive somewhere.
[1:19] And then in preferences, you can set the file path.
[1:22] So under file paths, you just add wherever you keep it, and it will just add it to your asset browser from then on.
[1:30] So once you have an asset browser open, then you can just find it here.
[1:34] So you can find it in the drop down human-based meshes bundle.
[1:37] And then you can just drag and drop these assets.
[1:40] And one more thing about that, I think by default, this is set to append.
[1:45] But if not, then just choose append here and to use these assets super easy, you just drag and drop them.
[1:52] But I would recommend because now this is something that you cannot edit before you click anywhere, open this at collection panel and uncheck instance.
[2:00] Because otherwise it's just an instance and you won't be able to do anything with it.
[2:04] So let me just select this and then Alt and G to set its location.
[2:08] And then I can just close this as a browser like this.
[2:11] And then to install the tissue add-on, you go to get extensions and you just type tissue and then you just click on install.
[2:20] And after that, it will also be in the add-ons.
[2:22] And then you can find it here in the option panel, the tissue tab.
[2:27] I'm just going to add two levels of subdivision with control two.
[2:30] And then I'm just going to apply it with control A and visual geometry to mesh.
[2:35] So now we have a lot more geometry to work with, which will be interesting with the tissue add-on.
[2:40] And I'm just going to check that the scale is applied.
[2:42] And it looks like the scale is a bit different than one.
[2:45] So I'm just going to apply the scale as well.
[2:47] So I'll control A and choose scale and just click on apply.
[2:52] And let's turn on shade smooth and let's use a matte cap.
[2:56] It's a bit more interesting to look at.
[2:58] And then let's go to weight paint mode because we need to have a vertex group on this one.
[3:03] So now when I start to draw with the weight paint tool, you see that it turns red.
[3:09] And red means that the vertices here, so if I go to edit mode, you can see these vertices,
[3:15] these now have a value of one or a weight of one.
[3:19] And if I select them, then I select not just the ones that have a value of one,
[3:23] but just everything that has a value above zero in this vertex group.
[3:28] So the best way to visualize those values is with this weight paint visualization,
[3:33] which has red as one, blue as zero and green and yellow and cyan and so on as everything in between.
[3:40] To weight paint, just left click with the mouse and paint or to erase,
[3:45] you just hold control and you paint with the mouse as well.
[3:48] So that just turns it into zero value.
[3:51] And it would be nice if we can mirror this symmetrically automatically.
[3:56] So in the brush panel, go to symmetry and just click on the X here.
[4:02] And then as you can see, it will mirror that to the other side on the X axis or whatever axis that you need.
[4:09] And for some reason, I have had the experience that I had to uncheck the mirror vertex group option before it worked.
[4:16] And indeed, if I turn it off, it still mirrors the vertex group.
[4:19] So I'm not sure what that option is for.
[4:21] But anyway, it works.
[4:23] And so yeah, let's draw a strange vertex group.
[4:26] Okay, so I've unleashed my creativity on this vertex group.
[4:30] And by the way, if you want, you can also soften the border.
[4:33] So if you hold shift, just like with painting and with sculpting,
[4:38] then you kind of soften the edges.
[4:40] You kind of smooth it out.
[4:42] All right.
[4:42] So that's our vertex group painted.
[4:45] So now what we can do with this, let me just go back to object mode.
[4:49] We can add a decimate modifier to this.
[4:52] And to see better what we're doing, I will enable in the viewport overlay is the wireframe option.
[4:57] So even in object mode now, we can see the wireframe.
[5:00] And yeah, I'm just going to lower this ratio.
[5:02] And of course, now is just doing a sort of general reduction of the geometry.
[5:08] However, if I use that vertex group that we painted, so here in the vertex group,
[5:13] it's just named group by default.
[5:15] And so now it's using the vertex group that we painted as the input for where to decimate.
[5:20] And this is somewhere interesting modern art.
[5:22] Maybe somebody would like to really print this, but I think I will increase the ratio a little bit,
[5:27] maybe to something like 0.4.
[5:30] That looks pretty interesting already.
[5:32] And you can also increase and decrease the ratio of the influence.
[5:37] And so yeah, it gives us something like this.
[5:38] You can also invert the vertex group by clicking on this button here.
[5:42] So that's also something that you can experiment with.
[5:45] Maybe that's more interesting in this case.
[5:46] Let me get something like this.
[5:48] If you're happy with your result of the decimate modifier, you can apply it.
[5:52] Just click on apply here.
[5:53] And so now this is what the geometry actually looks like.
[5:56] And so now let's finally use the tissue add on to in the tissue panel here in the option panel.
[6:01] I just click on convert to jewel mesh and make sure you have the object selected.
[6:06] So click on convert to jewel mesh and it takes a couple of seconds to do some calculations.
[6:12] And then what you get is this.
[6:15] So very interesting kind of honeycomb structure.
[6:18] And yeah, to make this even more interesting, we can now add a wireframe modifier.
[6:22] And I think we need to reduce the thickness quite significantly here.
[6:26] So just reduce the thickness value.
[6:29] And in fact, you can also uncheck the option replace original.
[6:32] And that just puts the wireframe as another model on top of the original.
[6:37] So then you get something like this.
[6:38] And let me just turn off the wireframe and maybe use a more interesting madcap.
[6:44] So then you get something like this, which is some kind of weird futuristic mask, I guess.
[6:49] And yeah, you can play a bit more with the thickness.
[6:52] We still have that vertex group.
[6:54] So in fact, we could also use that here to control the thickness of these lines.
[6:59] So then you get something like this, which is also pretty cool.
[7:02] And we can also invert that vertex group again to get something like this.
[7:06] We still have this factor values.
[7:08] If you think that these lines, for example, are too thin, then you can reduce what the
[7:12] vertex group is doing by increasing this vector value like this.
[7:15] So that's just one option of the tissue add on.
[7:18] And yeah, you can see how powerful it can be to use vertex groups inside of modifiers as well.
[7:24] And definitely also check out the talks that the author of this add on did.
[7:28] They're very interesting.
[7:29] His name is Alessandro Zomperrelli.
[7:31] And he talked about the tissue add on and he does amazing things with it.
[7:35] So definitely check that out as well.
[7:37] So if you're interested to read more about this topic, you can read about it in my ebook.
[7:42] And you can also find the blend file and another version of the same topic as well.
[7:46] And you can ask questions about it if you want.
[7:49] And I will try my best to help.
[7:51] So thanks a lot for watching.
[7:52] See you later.



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

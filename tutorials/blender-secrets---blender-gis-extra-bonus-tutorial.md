---
title: Blender Secrets - Blender GIS (Extra Bonus Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=IcL7N335oCk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - Blender GIS (Extra Bonus Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=IcL7N335oCk)
**Author:** Blender Secrets
**Duration:** 6m54s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---blender-gis-extra-bonus-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, it's Jan and I wanted to go a little bit further in depth on Blender GIS, which
[0:08] is something that I made a short one minute video about a few days, weeks ago.
[0:13] And there seemed to be some confusion about whether I'd made the opening render of the
[0:24] Matterhorn Mountain with Blender GIS.
[0:27] And yes, I definitely did.
[0:30] I just probably went a little bit too fast in the video, so I'll show you now step by
[0:34] step how to make such a nice render.


### CGBoost Course [0:37]
**Transcript (timestamped):**
[0:37] And if you're interested in this kind of stuff and you want to know more in depth with a
[0:42] real video course, how to make environments in Blender, I couldn't recommend anything
[0:48] that's better than the course Martin Kleckner made over on CGBoost.
[0:52] He really spent months figuring out every single variable button you can press in Blender
[0:59] just to make the most awesome nature render.
[1:01] So I would definitely check it out.
[1:03] You can find the link in the description.


### Blender Tutorial [1:05]
**Transcript (timestamped):**
[1:07] Alrighty, so here we are in Blender and I've already put a screenshot from Google Maps
[1:12] of the Matterhorn exact location because otherwise I would never find it.
[1:16] And here we're going to the GIS menu to load the base map, which basically just loads the
[1:21] whole earth and then you can zoom in to where you want.
[1:26] So obviously the Matterhorn is in the blurry place of Europe.
[1:31] In fact, it's in Switzerland.
[1:34] I can already see it.
[1:35] It's right there.
[1:40] It looks like we are targeting you Switzerland for destruction or something from space.
[1:46] There it is.
[1:51] Now you can lock by pressing L you can lock the region that you've selected like this
[1:56] region.
[1:57] I don't want to zoom in anymore, but I do want to increase the resolution.
[2:00] So I press L to lock and then I scroll up on the mouse wheel and it will still increase
[2:05] the resolution.
[2:07] But it takes a long time.
[2:08] I've sped it up here.
[2:09] It takes forever to download.
[2:10] It can take like 20 minutes or something.
[2:14] And then you get this shiny plane and you can download the height map as well, which
[2:20] also takes a minute or five or 10.
[2:23] And you get this shiny blob of relief.
[2:27] I really recommend you embed the texture in the file and save it because otherwise if
[2:32] it crashes you lose the resolution of the terrain.
[2:36] You lose the height map, I mean.
[2:39] Here to get the most out of it, I subdefide it in edit mode.
[2:44] You really have to do that.
[2:45] Otherwise you don't have enough detail.
[2:52] Reduce the specularity and increase the roughness of that map.
[2:55] Otherwise it will look strangely shiny and I can tell you from experience that Switzerland
[3:02] is not shiny like that.
[3:05] So here I'm adding a HDRI with Gaffer add-on, which is probably the best add-on I've ever
[3:11] bought.
[3:13] And the blender is already unhappy because it's so many subdivisions.
[3:18] So I've turned on simple file.
[3:22] And I'm adding a camera, but the camera doesn't see anything because it's all too big.
[3:26] So I have to add, I have to increase the clipping and otherwise it's a massive, massive mesh
[3:36] basically.
[3:39] So I've locked the camera to view so I can move around and find a nice shot here.
[3:44] Later I will increase the height of these mountains a bit in the modifier, the displacement
[3:52] modifier because it's a bit too boring now.
[3:56] So now I'm just trying to search which one is the Matterhorn again and finding a nice
[4:03] angle with the camera.
[4:10] And changing the length of the lens a bit to make it a bit more dramatic.
[4:14] 30mm is a good camera lens length for this kind of stuff.
[4:24] So I just added an empty, although you can see it because the overlays were turned off.
[4:30] The empty will be the target for the depth of field of the camera, which is always nice,
[4:36] but in this case the mesh is just so gigantic that you can't really see the depth of field.
[4:43] So I was trying to scale it down and see if I could get a bit more blurry in this.
[4:50] And experimenting a bit more with the HDRIs.
[4:53] They're mostly from HDRI Haven, but you can just automatically download them all with


### Bonus [4:55]
**Transcript (timestamped):**
[4:58] the Gaffer add-on.
[4:59] It's really awesome.
[5:01] And this is my book.
[5:02] I was just...
[5:03] Sometimes I read my own book.
[5:05] I was just checking which picture that I used for the background.
[5:10] It's this one from textures.com.
[5:17] I downloaded it as an image on-plane with the images as planes add-on.
[5:24] I wanted to emit, of course, and just kind of line it up with the camera.
[5:29] If I were really smart, which unfortunately I'm not, I would have parented it to the camera.
[5:35] But I didn't, so later I have to move it again when I move the camera.
[5:42] Here I'm rotating this HDRI a bit and setting up some kind of camera move.
[5:50] You can actually scale keyframes in the timeline, which can be very handy.
[5:57] But Blender get crashing when I try to render it.
[5:59] So here is a quick tip.
[6:02] You can increase the scale of your camera.
[6:05] That way you can get kind of the camera fulcrum or the area which is inside the camera view.
[6:10] And then just select everything else and just delete it.
[6:22] That way you massively reduce the amount of memory you have to use and then you can actually
[6:27] render it.
[6:28] So here you go.
[6:30] This is the render shot.
[6:31] I added a little bit of rotation to the camera movement.
[6:38] So yeah, good luck with the Blender GIS.
[6:40] It was a lot of fun.
[6:41] You need some patience, but it's worth it.



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

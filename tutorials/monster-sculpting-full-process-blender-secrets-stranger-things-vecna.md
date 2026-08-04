---
title: Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna
source: YouTube
url: https://www.youtube.com/watch?v=s6GQv6eZVms
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/
frame_count: 0
frame_status: pending-selection
---

# Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna

**Source:** [YouTube](https://www.youtube.com/watch?v=s6GQv6eZVms)
**Author:** Blender Secrets
**Duration:** 21m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py monster-sculpting-full-process-blender-secrets-stranger-things-vecna <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] OK, so I have this reference image from Titan Troll Miniatures from CGTrader
[0:09] and this is just to give me some reference of the Verna monster from Stranger Things
[0:15] I'm not going to recreate it, just use it as an inspiration base
[0:20] So let me get a base mesh
[0:30] and let me join these
[0:43] set the origin to the 3D cursor
[0:47] and I just want to have the bust part so I will remove the rest
[0:52] I think I can just use a boolean
[1:00] and maybe also the arms
[1:30] and I will just symmetrize this real quick
[1:42] OK, now we can go to Scott Mode and just remesh this
[1:48] I don't need those facets
[1:53] and do a focus on remesh
[1:56] preview R and then Ctrl R
[2:00] that's pretty low, let's try that again
[2:06] you hold down shift you can change values in smaller increments
[2:14] that didn't work, so let's use a remesh modifier instead
[2:21] let's undo
[2:24] it's not undoing for some reason
[2:37] so let's use a remesh modifier then
[2:43] and apply it
[3:14] OK, now in Scott Mode I can
[3:21] use some brushes
[3:44] these areas that are problematic
[3:48] I will just smooth them out and then remesh
[3:53] because otherwise we can never get it right there
[4:02] so remeshing is taking care of those issues
[4:13] now we can just use the claystitch brush
[4:17] to add some volume, let's use symmetry for that
[4:35] this seems he doesn't really have ears
[4:39] let me just remove those I guess
[4:51] and just do a quick remesh
[5:01] it looks like when I do this it's destroying the back of the mesh
[5:06] so I will need to check
[5:12] front faces only, then that doesn't happen
[5:25] let me add a bit of volume back here
[5:37] OK, let me just file
[5:42] smooth out this seam a bit
[5:54] now to add these veins I could use a draw brush
[5:57] but instead I'm going to use another technique which is not sculpting
[6:05] I'm going to use some curves, so I'll add a curve
[6:09] a Bezier curve
[6:12] and in edit mode select all and then just delete the vertices
[6:18] so now I still have my curve selected but it doesn't have any vertices
[6:25] and as you can see in the tool panel in edit mode I have the draw tool here
[6:31] and up here you have some options
[6:35] you have cursor and surface
[6:38] so I can use that to draw on top of the surface
[6:43] it's very close to the surface so sometimes it's clipping so that's why you cannot see it very well
[6:49] but if I draw it and I add some thickness by increasing the depth value
[7:01] then I get this kind of stuff
[7:06] if we open the tool panel we get the draw tool options here
[7:11] and we can set the taper, start and values to 1
[7:16] and then when we draw a curve
[7:19] and we need to increase that
[7:23] we need to increase the depth a little bit more than
[7:28] then we get this kind of sausage with tapered ends
[7:34] like what you see in the reference image as well
[7:38] so now I can just draw those all over the place
[7:43] so let's do that
[7:53] I guess I'm making them a little bit too wavy so they should be a little bit more simple like this
[8:02] we can still adjust these later because they are curves
[8:05] so we can select these points and scale them up or move them around
[8:12] let's see what's that
[8:14] just like this
[8:17] they do overlap each other which is nice
[8:23] this is much faster than if you were to scope this
[8:45] and if you don't like something you can just press Ctrl Z and undo
[8:50] and just draw it again
[8:56] okay I think that's an evanes
[9:06] now we can adjust these a bit but actually
[9:11] they're fine, they're not perfect but it's supposed to be something organic so
[9:16] I'm not going to bother with changing it too much but if you want you can select these
[9:22] and you can rotate them
[9:28] rotate, move them
[9:32] you can scale them up
[9:35] like maybe some of these we can make them a bit fatter
[9:39] just thinner
[9:44] and the short key for that is Alt S, confusingly
[9:53] they shouldn't all be the same
[9:55] we can also just select randomly
[10:01] maybe a little bit less than this and just scale some of these down randomly
[10:07] let me invert that selection
[10:10] and reduce it and then scale some of them up
[10:14] to give it a bit more of an organic random feeling
[10:22] and now let me just select them all
[10:26] and then we can go back to the previous selection
[10:32] okay so I've joined them
[10:35] and now I can convert them all to mesh
[10:38] I hope, yep
[10:40] so now this is all one mesh
[10:44] and I can just join these two together
[10:47] and then in sculpt mode
[10:50] we can do a voxel remesh again
[10:53] and then do a voxel remesh
[10:58] and now it's a part of that mesh
[11:01] so of course now I can clean it up a bit
[11:07] and make sure it's a bit more integrated in the rest of the model
[11:16] and of course we can also add to that with the place strips brush
[11:23] looks like I still had symmetry on that's not good
[11:25] because it's a very asymmetrical model
[11:42] okay it's starting to look good
[11:45] alright
[11:49] how does that look with a mad cap?
[11:53] I guess he doesn't have a mouth anymore
[11:56] so let me add his mouth back
[11:59] let me see
[12:01] can you crease?
[12:04] I guess and
[12:06] use some smaller clay strips
[12:10] to build that up again
[12:17] and now I can add some more
[12:19] to the base
[12:28] I guess I should turn symmetry back on
[12:31] it's one of those things that's easy to forget
[12:34] for the rest I'm going to use some
[12:37] alpha textures to do the details
[12:58] and these are some
[13:01] alpha textures that I purchased
[13:04] from ArtStation
[13:09] actually let me just open a tool panel that's easier
[13:13] so what I'm doing is I just make a copy of this
[13:16] and then I click on new texture
[13:20] I have folder with all kinds of alpha textures
[13:24] and I just bought these
[13:26] these are from Nicholas Swangudow on ArtStation
[13:29] he makes really nice alpha textures
[13:35] I use the TIFF versions
[13:38] he sells both video brushes
[13:41] and also in this case the alpha textures
[13:44] which are just images black and white hide maps
[13:47] and I chose the TIFF files because it's easy to preview them
[13:50] in the browser
[13:53] so let's just start with the first one
[13:59] and we want this to be
[14:02] area plane
[14:04] mapping
[14:06] front faces only
[14:10] and I want to drag dot for the stroke
[14:13] so that we can drag it to where we want
[14:16] the falloff with a alpha texture should just be constant
[14:19] because you want to use the whole image
[14:22] we can set it up so that the rotation is random
[14:25] but let me see
[14:28] if you want to rotate something
[14:31] an alpha texture like if you don't want it to be like this
[14:34] you can always press CTRL F
[14:37] and then you can change the angle
[14:40] so for example I can
[14:43] put it above his brow or something
[14:46] and I notice that I don't have enough resolution by far
[14:49] so I am just going to add a
[14:52] multi-res modifier
[14:55] and simplify that one time
[14:58] which already gives us
[15:01] 5 million vertices so
[15:04] that's okay
[15:07] let me just quickly
[15:10] set it to shade smooth because I think that was
[15:13] not the case
[15:16] mmhmm that looks alright
[15:19] and we can change the size of the alpha
[15:22] with F radius
[15:25] that's a bit too much
[15:28] okay cool
[15:31] so now we are just going to place some
[15:34] alpha textures
[15:37] and I think I will use the random
[15:46] profile
[15:49] you can just adjust
[15:51] the intensity
[15:54] even alpha is too strong
[15:56] you can also press Shift F and just reduce
[15:59] the intensity
[16:02] like this is just a complete one
[16:05] this is just a strength of one that's obviously too much
[16:08] so you can reduce it to say 0.3ish
[16:11] and
[16:14] Of course you don't want to use the same alpha too many times because it will be very obvious.
[16:29] So let's load another texture.
[16:31] I guess you can create another alpha by clicking here and then you have all those alphas but
[16:37] in this case I'm just going to change the texture.
[16:58] I'm just going to use them all until I have something cool.
[17:02] So save sometimes, very very important.
[17:21] So these appear to all be like cut since stuff and I want to have some little bit more
[17:26] monstery alpha. So like this one. This looks like some kind of mutated monster texture.
[17:41] I don't want it to randomly rotate in this case.
[17:43] Let me reduce the strength and increase the size. That's interesting.
[18:13] I wonder if we can use this for his eyes.
[18:35] When you press ctrl z in blender sometimes it will undo the settings in the interface
[18:41] oddly enough. So we have to re-enable symmetry.
[18:47] And what's creepier if the eyes are close together.
[18:51] I guess we can always stretch them out a bit like this.
[18:58] Make him look a bit more angry.
[19:04] It looks a bit silly. I don't know. I'm not too happy with that.
[19:08] Let me see if I can find a better texture for that.
[19:24] I don't know. The eyes are not a big success I guess.
[19:31] Let's see. I think we've already got quite a lot of detail now.
[19:46] I think what we need is more veins in those creepy.
[19:53] I think we need more veiny stuff. So let me see if I can find another good
[20:00] of a texture.
[20:04] I think this one was really good. We can get a bit more mileage out of this.
[20:16] Not too strong.
[20:22] I'm just going to place lots of veins everywhere.
[20:25] Like this. Just as long as I rotate the alpha you won't really notice.
[20:33] It's the same one over and over again.
[20:37] I hope.
[20:46] He uses really good skincare products on his back but not in front.
[20:56] Maybe add a little bit more stuff in his face I guess.
[21:02] Let me have something good for this. What is this?
[21:18] If you're placing an alpha texture with drag dot like this
[21:24] and you don't like it then you want to undo it.
[21:26] Instead of pressing undo just press escape.
[21:31] That's faster because if you have to wait for undo it takes a couple of seconds.
[21:40] That's good. This is good enough.



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

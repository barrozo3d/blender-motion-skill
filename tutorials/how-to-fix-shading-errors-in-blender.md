---
title: How to fix SHADING ERRORS in Blender
source: YouTube
url: https://www.youtube.com/watch?v=EdEIUkWzYY0
author: Josh - Blender Bros
ingested: 2026-07-13
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-fix-shading-errors-in-blender/
frame_count: 0
frame_status: pending-selection
---

# How to fix SHADING ERRORS in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=EdEIUkWzYY0)
**Author:** Josh - Blender Bros
**Duration:** 13m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-fix-shading-errors-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So sometimes when you're modeling and blender, you're going to run into weird shading errors
[0:05] when you're using bullions, bevels, and things like that. So for example, I give you a really
[0:10] practical example here, then we're going to dive a bit deeper. Sometimes when you run a bevel
[0:15] like this, you might see that on the ends of the bevel, you have this weird sharp marking right here.
[0:22] Now, the ends of the bevel are what we call the holding edge. You never really want to mess,
[0:29] or dissolve out the holding edges on the bevel, right? So here you're going to see this has
[0:35] like a weird line going across it. And the reason for that is that before I added this bevel right here,
[0:42] before I added this, we actually had, if I remove this seam, we actually had a sharp marking
[0:48] attached to it. Now, just to kind of show you what sharp does, if I were to go in here and shade
[0:54] auto smooth on this cylinder, and I just selected this edge right here, and I marked it a sharp,
[1:01] this would display a physical sharp marking right there on the edge. Now, kind of the main reason
[1:08] this feature even exists in blender is for situations where the auto smooth doesn't capture the
[1:15] angle as you want. And I'll give you a really practical example here. Let's say I had this cube
[1:21] right here, and then I ran a Boolean at a very, very steep or shallow angle rather, kind of like
[1:28] this. We'll do that. And you're going to see I obviously have my shade auto smooth right here,
[1:35] but you're going to see this edge right here is not being picked up. Now, obviously I can go in,
[1:41] I can adjust the angle here, and eventually it might, you know, capture. It's a bit glitchy
[1:48] right now. I don't know what it's doing that. But, you know, eventually I have to go like super,
[1:52] super shallow on this, but let's say I had a bevel here in the back, right? If I had a bevel here
[1:58] in the back, and I had to adjust this really, really low, okay, I adjusted the auto smooth, and this
[2:06] picked up, but as a result, these are now shaded flat because the angle just isn't working together
[2:12] very well, right? You can kind of mess with that. In this case, you know, I actually got it working,
[2:18] but if this was like super, super shallow, you know, you really have to adjust that angle,
[2:24] and then it's eventually just going to mess with this area. So kind of the, you know, main reason
[2:28] blender invented this sharp mark-in to begin with is kind of for situations like this where I can
[2:34] basically go in, for example, I can keep the angle as I want. We'll apply that Boolean, but here,
[2:42] since the angle isn't being captured without affecting this side, I could actually just go in
[2:47] and simply right-click and manually mark that sharp. That's kind of the main reason that feature
[2:54] exists in the first place. That's really the only reason you would use that essentially.
[2:59] Now, back to what I was discussing before, notice these sharp edges here on the bevel, right?
[3:04] The reason that's happening is because I had a sharp marking applied, let's just add another one here.
[3:10] I had a sharp marking applied here to the bottom, right? So whenever I beveled that,
[3:16] this edge right here splits into two holding edges, one right here on the bevel,
[3:22] and then one right here on the bevel. It splits that edge into two holding edges, which is going to hold
[3:29] and kind of maintain that sharp marking. So there's two ways to fix this, three ways to fix this
[3:35] actually. You can either go to the holding edges of the bevel and clear the sharp, and that's going
[3:41] to remove that weird edge, that weird line right there. Notice if I clear the sharp, can do this
[3:47] with overlays turned off. It goes away. That's one way to do it. It's a bit slow. The other way to do it
[3:53] is to make sure there's no sharp before you add the bevel, right? So you can go in and then bevel
[3:59] that without the sharp, and it won't be there in the first place. And kind of the third way you could
[4:04] do this if you're using something like hard ops, for example, is you can actually, let me mark the sharp
[4:11] here. You don't even need to undo this manually. You can actually use a feature in hard ops, for example,
[4:17] called recalculate. If I control shift click on recalculate, it'll recalculate that sharp mark in.
[4:25] However, and I want to be very clear here, this will not work if your hard ops settings under sharp
[4:30] and in does not have sharp turned on. If this is turned off, when I recalculate it, it will only
[4:37] recalculate whatever I have turned on here. So for example, if I had a seam, it would remove that
[4:43] seam. But here, if I turn sharp on, now the angle is different because I added the bevel. So when I
[4:50] recalculate it, it'll remove that sharp because it's no longer within that angle threshold. So that's
[4:58] kind of how you can solve that problem with weird markings on your bevels and situations like
[5:04] this where you actually need a physical sharp mark in. Right? Now let's dive a little bit deeper
[5:10] here. Let's say I had a cube, we'll go ahead and just add a bevel here in the cube.
[5:18] Oops, we'll move this up a little bit and hide that. And then let's just add in a bevel modifier.
[5:24] Okay? Now you might not really see it immediately, but if I were to go into a more unforgiving
[5:30] mat cap, you're going to see that the flat area has a little bit of a shading distortion here.
[5:36] And it'll be even more obvious if I added in, for example, a bevel right here. You see that?
[5:44] See, right here, we have this weird shading error versus if I deleted it, we don't have a shading error
[5:49] at all. See that right there? It's going to be even more obvious with like a reflective one.
[5:54] You can kind of see it there. I don't know how well it's showing with YouTube's compression,
[5:59] but it should be pretty obvious that there is a shading distortion right here. Now, it made videos
[6:03] on this before, but the whole reason this is occurring has to do with vertex normal. So
[6:09] I'm going to go ahead and I'll just apply this Boolean right here. If I go into my vertex mode,
[6:15] and let me just go back to a normal mat cap, and I go to these vertex normals here,
[6:20] I actually need to apply the bevel as well so I can access that bevel geometry.
[6:26] So if I apply the bevel, you're going to see the holding edge of the bevel right here.
[6:33] I haven't selected it on the side though. The holding edge of this bevel is not 90 degrees.
[6:40] This area right here on the holding edge, these weird lines coming out. They're not 90 degrees,
[6:48] right? They look 90 degrees, but they're actually slightly bent if you zoom in. You can see
[6:54] there's a slightly bent, right? Now, what's going to happen is if I add in a weighted normal,
[6:59] if I go in here to normals and then weighted normal, this is actually going to fix the shading problem.
[7:05] I'm going to go in here and show you so you can really see it. Right there, you can see the
[7:09] shading problem. The moment I add in the weighted normal, it's gone. And that is because if I apply
[7:15] the weighted normal, and then I go back to this holding edge right here, that weighted normal forces
[7:22] those to be perfectly 90 degrees. You can see those are 90 degrees now versus before. If I
[7:28] undo that, just remove the weighted normal, these are clearly not 90 degrees. This is before,
[7:34] and then when I add in the weighted normal, this is the after, they're perfectly 90 degrees,
[7:39] so that makes the shading cleaned up. So that's another situation where you might have weird
[7:44] shading distortions or weird markings on your model. Now, a third situation has to do with curved
[7:52] surfaces. So let me add in the cylinder for this example. This is going to be way easier to
[7:56] demonstrate. I'm going to go ahead and shade that auto smooth, and I'm just going to rotate this.
[8:03] And let's just go ahead and add in a Boolean. Obviously, when you add a Boolean on a curved surface,
[8:10] like this, for example, let me double that. When I add in a Boolean on a curved surface, we have
[8:16] very, very obvious shading distortions here. It'll be a lot more obvious if I have like a reflective
[8:23] mat cap here. You see that? And then if I add in the bevel, you know, same type of idea.
[8:29] Now in this particular situation, let me apply the Boolean. So I, that's just applied.
[8:35] If I add a weighted normal, this will not fix the problem. And that's because this is not
[8:41] a flat surface. This is a curved surface, which has a completely different problem altogether.
[8:47] And the problem here simply has to do with the fact that this polygon right here is bent. If I
[8:54] duplicate this, okay, I'm going to duplicate this and just move it out. And then I'll just separate
[9:00] this by selection. This right here, obviously, this is a single face. Maybe I should duplicate,
[9:06] you know, a couple of these so you can really see it better, separate that. You're going to see,
[9:12] this is not flat. This is a bent polygon, which is causing that shading distortion. And kind of
[9:18] the best way to demonstrate this to you is if I had an a plane, add in a plane here, maybe I give it
[9:24] like just make this into an end gone, right? And then I move this up, move this down. What I
[9:31] essentially did here is I bent this polygon, which created this weird distortion. That's essentially
[9:36] what's happening here. This is nothing to do with weighted normals. That won't fix the problem.
[9:42] Here, there's really only two ways to fix it. Three ways actually. The first one is to have
[9:47] good topology to begin with. And I'll kind of show you the first example. The first way to fix this
[9:53] is to just, you know, have quads and, you know, good, good topology here essentially. So I'll kind of
[9:59] give you an example if I had a cylinder, maybe I had 16 segments here. I rotated this and I won't
[10:07] spend too much time, you know, messing with this. But say, for example, I had this, right? And then
[10:15] I just, I don't know, deleted this area out here. And then we'll just go ahead, let me fill that in.
[10:22] And then this area here, I can just do like a grid fill, right? And do a grid fill there. Now,
[10:28] if I run, you know, a sub-d on it, obviously I can get in, I can add in like isolation loops,
[10:34] things like that. But this is kind of the first way you would fix it is simply by having, you know,
[10:38] clean quad-based topology. You wouldn't have that shading distortion. The second way here,
[10:44] and the way I've always taught with a hard surface modeling workflow is to simply have more geometry
[10:51] to isolate the shading. So for example, if I just undo this all the way back,
[10:56] here before I even apply this boolean, if I just have additional geometry, right? Now when I add in
[11:05] that additional geometry here, the shading distortions are kind of isolated to these small
[11:11] end guns and triangles on the inside. So they're technically still there. They're just not as visible.
[11:17] You can kind of see it, but they're not as visible because I have way denser geometry here. So
[11:23] that's kind of the way I recommend fixing it, especially if you're just doing a rendering or
[11:27] things like that. And then the third way you can fix it, which isn't as practical, is with the data
[11:32] transfer modifier. If you want to learn that strategy, I'll put the thumbnail on the screen here.
[11:37] I show you how the data transfer modifier works in that tutorial. That's kind of the third way to
[11:42] fix it, but it's not as practical really. So there's going to be all sorts of situations where you're
[11:47] running the shading errors like weird lines on your object, shading glitches. And this simply boils
[11:54] down to whether you have markings, what your angles are set to, and how you know the booleans
[12:00] are working is it on a curved surface. Do you need a weighted normal modifier? These are little
[12:05] technical situations you need to understand. So that way when you run into these problems,
[12:11] you kind of know how to fix them. Now if you're new to blender and new to hard surface modeling,
[12:16] I would highly recommend getting our accelerator program. This is the best program on the market
[12:21] for hard surface modeling. We'll teach you our entire workflow in under two weeks, with about
[12:27] 30 to 60 minutes per day of practice. And you'll get results just like our students have done here,
[12:33] very, very quickly without wasting a ton of time on YouTube and crappy tutorials. So if you want to
[12:39] learn our full workflow from scratch, check out our hard surface accelerator program in the link
[12:45] in the top of the description. Thanks for watching and I'll see you in the next video.



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

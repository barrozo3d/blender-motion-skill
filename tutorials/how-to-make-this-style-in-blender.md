---
title: How to make this style in Blender
source: YouTube
url: https://www.youtube.com/watch?v=oAKrQboXo78
author: Bad Normals
ingested: 2026-07-16
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-make-this-style-in-blender/
frame_count: 0
frame_status: pending-selection
---

# How to make this style in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=oAKrQboXo78)
**Author:** Bad Normals
**Duration:** 14m35s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-make-this-style-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### What we do [0:00]
**Transcript (timestamped):**
[0:00] Today we're going to achieve the art style of Damong's art, the Taiwanese artist who
[0:15] knows his way around colors.
[0:17] What he does not know is that we're going to replicate his art style in blender, which
[0:21] sounded like a threat, but I like to frame it as admiration.
[0:25] I mean, really does great stuff.
[0:27] We're going to study and recreate this piece.
[0:30] The techniques are super versatile.
[0:32] You can use them for cool animations, cool graphics, and you'll learn a lot about materials
[0:37] and shaders to make such professional stuff yourself.
[0:41] Let's go.
[0:42] As you can see, the piece is made of capsules, and the fastest way to make capsules in blender


### Making a capsule [0:44]
**Transcript (timestamped):**
[0:47] is shift A, metzapol, capsule.
[0:50] You know, these capsules are actually quite friends.
[0:52] They want too much.
[0:54] So instead, a better approach is to take a cube, add a bevel modifier with a huge bevel
[0:59] amount and many segments, and scale the cube in edit mode.
[1:04] Now this is a capsule that does not bond with other capsules, and we can start putting together
[1:09] this scene.
[1:10] Now, this scene has 16 capsules placed in pairs of two, and if you're not cautious, you
[1:16] might start placing them with a good old shift D. Duplicate, and move, and duplicate,
[1:22] and move.
[1:24] So the touch is exactly on the edge, and you're like, bad normals, I don't want to do that.
[1:27] I'm tired.
[1:28] Yes, because you're not using the optimized workflow.
[1:32] I don't know if it had to be German.
[1:33] Well, the optimized workflow is to turn on snapping first.


### Quick placement [1:37]
**Transcript (timestamped):**
[1:37] So you turn on snapping in grid mode.
[1:38] You go to edit mode, you go to x-ray mode, and you enable face selection with three, and
[1:44] now you can nudge at the end and start in fixed positions on the grid.
[1:48] And you can make sure that two capsule steps are exactly touching each other.
[1:53] And if you want to now add more capsules, you just select those two.
[1:56] You duplicate the shift D to the side, and press shift R literally until you have the
[2:01] 16.
[2:02] That is so easy.
[2:03] Also, you probably want to change where the capsule's touch in the center.
[2:06] The reference, as you can see, the line is very irregular.
[2:09] It's not like a straight cut in the center.
[2:12] So you select one column, you go to edit mode, press three to select faces, all three to
[2:17] go to x-ray mode, and now you can select those two middle faces with a simple box select.
[2:23] And you can super easily move both of them up and down at the same time.
[2:27] And once you're happy, you just go out of the edit mode and repeat this with the other
[2:31] columns, so you end up with something like that.
[2:35] This is already pretty close to the reference.
[2:37] Now the question is, what do we do?
[2:39] Colors.


### Simple gradients [2:40]
**Transcript (timestamped):**
[2:40] Well, for that, we need to understand how gradients work.
[2:43] So gradients have two parts.
[2:44] They have the gray scale source, and they have the colors.
[2:49] For example, if you translate 0 to blue and 1 to red, this would be a blue-dread stripe.
[2:55] Or this would be a circle.
[2:58] Or this would be a blue-red blue circle, because the 0 is also in the end of the circle.
[3:05] Or for example, this gradient would turn into a room-looking thing.
[3:09] So the main idea is that it's just translate the certain gray scale value to a certain color,
[3:14] and all the intermediary values will be turned into a mix of those two colors.
[3:18] In Blendery, we just take, for example, a gradient texture or noise, and you add a color
[3:23] ramp.
[3:24] And it's pretty intuitive how this works.
[3:27] But with this artwork, with this situation here, we know the colors, but we don't know
[3:32] the gray scale version.
[3:33] So we need to recreate the gray scale version.
[3:36] And for that, let's first understand how the colors flow on those capsules.
[3:40] And then we can just very easily recreate the gray scale thing.
[3:44] So let's mark the colors.
[3:45] We have yellow, purple, we have blue, and we have deep blue.
[3:48] Which Apple would probably say midnight ocean.
[3:52] I'm gonna say it's deep blue.
[3:53] We've now simplified this gradient.
[3:55] To only those points, it looks like that.
[3:58] And that's a very easy gradient to replicate.
[4:00] We just need, from bottom to top, a 0 to 1 gray scale source.
[4:06] And if you map 0 to yellow, 0.25 to purple, 0.5 to bright blue, and 1 to deep blue, we get
[4:14] this gradient.
[4:15] And you actually do this in Blender.
[4:17] You just go to your material node tree and add such a setup, which takes the generated
[4:22] coordinates, which is just a 0 to 1 gradient on each axis.
[4:27] And separates only the y axis, which goes from bottom to top.
[4:32] And then you add such a color ramp that does the gray scale to color translation, as we
[4:35] just talked about.
[4:36] And you have it.
[4:37] So if you switch the mode to B's plane as well, the color transitions are much smoother
[4:42] and look just as good as the reference.
[4:44] And if you find that the colors are washed out to your liking, you can change your color
[4:48] management to Corona's PBR neutral, which makes them a bit less neutral.


### Edge bend [4:54]
**Transcript (timestamped):**
[4:54] But this is quite miles away from the reference.
[4:57] I actually want to say it is a cheap Chinese copy, but this would have been a think horrible
[5:02] on like many levels, including a political one because he comes from Taiwan.
[5:06] We're not going to do that.
[5:08] It is a known fact that this looks bad and the amongst arts version looks good.
[5:13] So how can we make it better?
[5:15] Well, the reference gradient is more sophisticated.
[5:19] It curves a bit like liquid on the edges.
[5:22] How do we do this?
[5:23] Well, if you want to change anything about how cost flow, we need to change the gray scale
[5:27] source of the gradient to give some difference for us.
[5:31] Because currently the source has absolutely no difference between the edges and the center
[5:34] of the capsule.
[5:36] And if we were to introduce the difference, the gradient would change on the edges as well.
[5:41] So let's create a gray scale gradient that differentiates between the edges and the
[5:46] center of the capsule.
[5:47] And for that, we need to know how much the surface normal of the capsule is pointing towards
[5:55] the sky.
[5:56] At the edges, it does it in a different way than in the center.
[6:00] So this gives us such a gradient that goes from minus 1 in the very bottom to 0 at the
[6:06] edge and plus 1 at the top.
[6:08] Now we don't care about the negative part too much because we are looking from the top
[6:11] anyways.
[6:12] So for us, the smallest value will be 0 on the edges to 1 in the center.
[6:18] And if we add this to our bottom to top gradients, we get colors that are curving and bending on
[6:24] the edges, which is good.
[6:26] But we don't want it to happen that much.
[6:28] So we can multiply this newly added gradient with a small value and then we can control the
[6:34] bend amount.
[6:35] So we have the gradients on the reference, we can see they are bent up, some gradients
[6:39] are bent down and we can control that with this multiply.
[6:43] As a little spice here, I also added such a setup that ensures the gray scale values are
[6:48] always between 0 to 1 because this is the range the color and node expects.
[6:54] So without it either the start or the end color would get way too dominant as we bend
[6:59] up or down.
[7:00] Even when this is happening, so I just added the setup here that takes care of it.
[7:04] So now we can add this material to all the capsules.


### Adding many materials [7:06]
**Transcript (timestamped):**
[7:08] You get a complete artwork.
[7:09] But this is a slippery slope here.
[7:12] This is a slippery slope here.
[7:14] You might pick the convenient way and go just select a new capsule, pick the gradient material,
[7:19] duplicate it, change the colors, select a new capsule, pick the gradient material, duplicate
[7:25] it, change the colors, you might do it until all the 16 ones are done.
[7:29] Short term, that's very effective, very fast.
[7:32] So now if you want to change anything for all of the capsules, like adjust the saturation
[7:38] of all the capsules, for example, or change the gray scale source system, you're cooked,
[7:44] you're not going to do that because you have to do the same edits 16 times for all of
[7:49] those capsules and unless you're into like BDSM, you're not going to do that.
[7:55] So let me show you how to make your edits linked between the capsules.
[7:59] So even though you have like 16 of them, you can do the edits and they're all linked
[8:03] and the colors are also different.
[8:05] So let's go back to the starter, only one of them has a material and you select all the
[8:11] nodes and Ctrl G, you group them.
[8:14] And you're going to be like, I know, but I know, node groups are cool, but they're like
[8:19] literally shared.
[8:21] So all the capsules will now look the same even if I make copies of the material.
[8:26] That is correct.
[8:27] But you can add parameters.
[8:29] For example, for the bend, you can add a parameter and now given every capsule as a different
[8:36] material, you can change the bend independently while the node groups content are the same
[8:42] and shared between the capsules.
[8:44] And yes, I can hear you from the back again, but normal, you can't add the color ramp
[8:48] as a parameter.
[8:50] All the colors are going to be, I think I had a voice crack though, all the colors are
[8:54] going to be the same.
[8:55] Well, do not back off.
[8:56] There is a solution.
[8:57] So go inside the node group and disconnect the color ramp.
[9:01] And instead of it adds an evaluate closure nodes and connect it there.
[9:07] Now this node is a wannabe.
[9:08] So it will be whatever you tell it to be.
[9:11] It's kind of like this plant in plants versus zombies, you just replicate whatever we tell
[9:16] it to be.
[9:17] We tell it what to be through a parameter pipe connection.
[9:22] So we add a parameter and we call it color ramp.
[9:25] And through this pipe, this wannabe will listen to your instructions and decide who
[9:30] would you pretend to be.
[9:32] We want it to be a color ramp.
[9:33] So copy the color ramp, go outside of the node group and add a closure zone.
[9:39] Connect it here into the parameter and paste in your color ramp.
[9:43] Now the evaluate closure node will be whatever is inside the closure zone.
[9:48] And that's pretty cool because now you can add materials to the capsules and change the
[9:53] ramp.
[9:54] And all the logic is still linked.
[9:56] So if you decide to add saturation node, it will affect all the capsules.
[10:00] If you want to do something before the color ramp, it also changes.
[10:03] So cool.
[10:04] I mean, blend out developers are just amazing.
[10:05] They really do such an awesome job.


### Color & Background edits [10:09]
**Transcript (timestamped):**
[10:09] So we've done some heavy technical lifting.
[10:11] Let's breathe in.
[10:12] Let's deal with some artistic stuff.
[10:14] So a little interesting thing you can see where two gradients meet.
[10:18] He has made the colors rather similar, like dark dark, light light and so on.
[10:24] So you can assume this pretty easily by just flipping the ramps and adjusting the end
[10:29] colors.
[10:30] Also the space between the gradients and around them is filled with color and glow, I
[10:34] would say.
[10:35] So you can add a plane, half a tree, the capsules and if you render with cycles, you get
[10:40] this glow.
[10:41] Now it seems that only the brighter colors emit light though and the dark ones don't do
[10:45] that that much.
[10:47] So we can do it so that for the emission shader at the end here, we create two possible
[10:53] states.
[10:54] It's one where dark colors do not glow and the other where everything is a normal
[10:59] brightness.
[11:00] What we want to see from the camera and we mix between them so that for the camera,
[11:05] we use the normal state and for every other object in the scene, we use the adjusted state.
[11:10] And this makes it possible to control the edge glow separately from what we see into
[11:15] the camera.
[11:16] That's looking pretty good already.
[11:19] I would say we have only one last thing missing here, which is adding those glass plates.


### Adding glass [11:20]
**Transcript (timestamped):**
[11:23] And I think like that's only glass, but honestly, I'm so surprised how much better this glass
[11:28] actually makes this thing look.
[11:29] I mean, you surprise at the little things in life, I guess that is it.
[11:34] We take a circle, we select the bottom parts, we move it down, we fill, extrude, add the
[11:41] bevel modifier, just move the corners and shade it auto smooth as well.
[11:46] So we got the shape and now we can add the material and to make it look like glass,
[11:50] we literally just crank up the transmission, make the color fully white and this is it.
[11:55] Now probably you will see that your capsules look very dark through the glass and it took
[12:00] me like a pretty good time and a little bit of tears, mostly just a good time to figure
[12:07] out what's happening here.
[12:09] You probably remember those two brightness states we create for our capsule material.
[12:13] Currently only the camera rays see the normal brightness we want to see.
[12:19] And when the light ray passes through the glass object, it is a transmission ray.
[12:23] So we need to make sure that in our shader setup, all the rays that are either a camera
[12:29] ray or the transmission ray will see the normal brightness version and for that we just add
[12:34] the transmission and camera ray together and we end up with the problem going away, which
[12:39] is great.


### Edge glow [12:40]
**Transcript (timestamped):**
[12:40] This is looking very close.
[12:41] There is one last thing that makes it look so good and this is the edge glow.
[12:45] So you can see there is on the edges of the capsules, if they are seen through the glass,
[12:51] the glow pretty bright.
[12:53] And we've covered every single technique to do that.
[12:56] So first let's just create the state of capsule edges that glow.
[13:02] And for that we need information about the edges.
[13:04] We already did this with the same normal node setup that we used before.
[13:08] I just copied this one over near the emission shader here and this time we don't want it
[13:13] to be white at the center and black at the edges instead of wanting to be white at the
[13:17] edges, black at the center.
[13:19] So the result is a gradient from the edges that we can adjust with the power node.
[13:24] And if you now add it to one, we get a brightness state that everything glows with a strength
[13:30] of one, but the edges glow a bit more.
[13:34] And how much more you can control with the multiply node.
[13:36] And as you remember, we want to show this only through the glass.
[13:40] So we can add a mix node to our emission strength and set the transmission rate to control
[13:46] when to show either state.
[13:48] Cool.
[13:49] Now you can duplicate the glass plates using the same placement as in the reference.


### We did it! [13:54]
**Transcript (timestamped):**
[13:54] And here it is.
[13:56] Super cool stuff.
[13:57] You can use it obviously with many different flavors like I did in the intro, doing them
[14:01] different twists.
[14:02] There is a little vault, a little crate, a little extra collection on BadRomance.com where
[14:09] you can get those three project files and also detailed explanation of the radial scene,
[14:17] which was like surprisingly complicated to figure out.
[14:19] So it's going to save you a lot of time.
[14:21] That is my pitch.
[14:22] So see you in the next one and enjoy the moment wherever you are.
[14:27] For me, it's literally the sunrise.
[14:31] See you.



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

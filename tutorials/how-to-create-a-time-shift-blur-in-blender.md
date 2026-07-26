---
title: How to Create a Time Shift Blur in Blender
source: YouTube
url: https://www.youtube.com/watch?v=TYo0Vpf13E0
author: Kai🔸
ingested: 2026-07-26
blender_version: "5.x (5.2+ for footage modifier)"
tags: [compositing, motion-design, camera, animation, procedural, advanced, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/how-to-create-a-time-shift-blur-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to Create a Time Shift Blur in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=TYo0Vpf13E0)
**Author:** Kai🔸
**Duration:** 24m39s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] A few months ago I saw Project Hail Mary in the cinema and something in that film set


### What Is the Time Shift Effect? [0:25]
**Transcript (timestamped):**
[0:26] me down a rabbit hole.
[0:27] See the film uses different aspect ratios and to make the transitions between them smoother
[0:31] the directors Phil Lord and Christopher Miller and cinematographer Greg Frazier use a time
[0:36] shift blur to blend between them.
[0:38] The film cuts between narrow flashback scenes and tall ratios in space.
[0:42] By blurring only the highlights in the image and letting them blend over the black bars
[0:46] the cut between ratios was super smooth in the film and almost invisible for me.
[0:51] Then I did some digging and once you know what to look out for you start seeing the effect
[0:54] everywhere.
[0:56] In a film camera the shutter opens, exposes a frame, closes and then the film gets pulled
[1:11] down to the next frame.
[1:12] Normally these two are in sync but if you mistime them on purpose so the film starts
[1:17] moving while the shutter is still open the bright parts of the image smear across the
[1:21] frame and that's the whole effect.
[1:23] This is basically a mechanical timing error done on purpose for artistic effect.
[1:28] But here's my favorite part.
[1:29] There's an actual piece of hardware for this.
[1:31] It's called the RE timing shift box.
[1:33] It lets the operator dial the shutter out of phase by hand which lets the operator control
[1:38] the streak length for example or the jitter.
[1:41] And that's basically what I tried to build in Blender.
[1:43] There's also a great Da Vinci version of this made by Andrew Glankfield.


### The Finished Filter in Action [1:45]
**Transcript (timestamped):**
[1:47] I linked the video down in the description.
[1:50] So what I've built is a simple effect preset that you can drag and drop from your asset
[1:54] shelf here in the compositor.
[1:56] You have full control over the highlight threshold, you can change the streak length
[2:00] and there's also a toggle that when the streak reaches one edge of the image it wraps around
[2:06] like with a real camera.
[2:07] While not realistic you have also an option to change the angle of the blur or you can
[2:11] make it symmetric so it blurs evenly from both sides of the highlight.
[2:16] But there are some more artistic controls like tint value that lets you color the streaks
[2:21] to whatever color you'd like.
[2:22] And finally there's also an option for an animated jitter like with the RE timing shift
[2:26] box that I showed earlier.
[2:28] And the effect not only works in your 3D scenes in the real time compositor.
[2:33] In newer Blender versions like in Blender 5.2 you can also add the effect non-destructively
[2:38] as a modifier to any video footage.
[2:41] Now before we start.
[2:42] This lesson is a bit long and a bit complicated but I think it's a really nice lesson in
[2:46] composting and how to work around limitations of Blender.
[2:50] So I'm going to show you how to build the whole thing step by step right now and if you
[2:54] follow along you'll end up with a working version of this.
[2:59] But if you're short on time and just like to grab it from somewhere rather than build
[3:02] the whole thing yourself I have the filter packed up neatly as an asset on my Ko-fi page
[3:06] ready to be dragged and dropped into your projects.
[3:08] The link is in the description.
[3:10] If you find it useful grabbing it there directly supports the channel.
[3:14] So with that out of the way let's start with the tutorial part.


### Directional Blur & Highlight Isolation [3:15]
**Transcript (timestamped):**
[3:17] In the Blender compositor create a compositor setup.
[3:20] Create a new empty group and hop into it with double click.
[3:24] Inside the group in the end panel name it time shift blur and set the color tag to filter.
[3:29] Inside the group add a directional blur node and increase the samples to 64.
[3:34] We can leave the node group by double clicking in an empty space here.
[3:38] Inside of our new group we need to connect it to the main node tree to see the changes
[3:41] in the viewport.
[3:42] So this directional blur node is the heart of our whole effect but it lacks in one area
[3:47] for our intent.
[3:49] It blurs the whole image so we need to find a way to only limit the effect to the brightest
[3:53] parts of our image.
[3:54] Next make a bit room here to the left and add a map range node.
[3:58] Change the from min to 0.5.
[4:00] This will isolate the highlights already.
[4:02] Then add a mix node and plug the output of the map range node in the B input of the mix
[4:06] node.
[4:07] Now duplicate the group input node of shift D and connect it to the factor.
[4:11] You can control click on the name and rename it to highlight threshold.
[4:15] Make sure that you change the A input to 1.
[4:18] Now thinking a bit into the future I'd like to have a mask input to limit the effect to
[4:22] certain parts of the image.
[4:24] To create this, after the mix node add a map node set it to multiply, duplicate the group
[4:29] input again and rename it to mask.
[4:32] In the end panel make sure the default value is 1, the min is 0 and the maximum is 1 and
[4:37] make sure you check hide value.
[4:39] If we hide the value it's being hidden here in the effect overview.
[4:43] To bring the color back to our streaks add a mix color node and change the mode to multiply.
[4:49] Mix our original image from the group input node and plug it into the A input and plug
[4:55] the output of the mix color node into the B input.
[4:58] Frame the whole thing up and name it highlight isolation.
[5:01] Now let's comp our isolated streaks over the image.


### Comping the Streaks Back In [5:04]
**Transcript (timestamped):**
[5:04] Add a mix color node and set it to add.
[5:07] Then duplicate that node and add another group input node and plug it into the A input of
[5:13] the first add node.
[5:15] Then plug the blurred image into the B input.
[5:18] Duplicate the group input node and put it into the A input of the second add node and
[5:22] set the B color to pure white.
[5:26] Duplicate first add node and then divide the first node by the second one.
[5:31] Now we have a working highlight threshold slider.
[5:35] Back in the group tie the everything a bit up by selecting our new nodes and naming them.
[5:41] Next add a lens distortion node after the directional blur node and set it to a tiny
[5:45] number like 0.01.
[5:48] This adds a little bit of chromatic aberration at the edges of our image.
[5:52] It would be a good idea to also frame this node up and name it accordingly because it


### Additional Controls [5:55]
**Transcript (timestamped):**
[5:57] will get a little bit more complex in the future believe me.
[6:01] Next I'd like to have some control over the amount and the direction outside of the group.
[6:05] So I will add a group input node.
[6:07] I will rename the direction to angle.
[6:09] Then I will duplicate the node and plug it into the amount and call it streak length.
[6:16] Right after the angle input I will add a math node and I will change its mode to subtract
[6:21] and in the number field I will type in pi divided by 2.
[6:25] This ensures that outside the group I can have a default value of 0 degrees and the streaks
[6:30] are pointing in this default position upwards or downwards like with the real effect.
[6:34] In the end panel I will quickly reorder the order of the inputs and then also frame this
[6:39] section up.
[6:40] While it might seem like unnecessary extra work to organize and name your nodes you will
[6:45] thank yourself later as your node graph grows in complexity.
[6:48] Now this is the basic effect right there.
[6:50] We have control over the highlight threshold, the streak length and the angle.
[6:54] Everything we do from here is adding more extra control and addressing one major thing.


### Image Wrapping [7:00]
**Transcript (timestamped):**
[7:00] The real effect with a real camera wraps around the image which means it comes out on the
[7:04] other end.
[7:06] Now Blender has no wrapping effect per default unfortunately but what we do have is a translate
[7:11] node.
[7:12] It lets us push the image in a certain direction and if we change the sampling from clip to
[7:16] repeat on both axes we get an infinite tiling of our image.
[7:20] So in this next section we will address this and it gets a little bit complex but bear
[7:24] with me I will break it up bit by bit and I think it's a cool lesson on how to build
[7:28] around something that Blender is currently missing.
[7:31] Now keep in mind that this is no simulation of the real effect but more of an approximation
[7:36] and a little bit of a hack on how to work around this limitation.
[7:40] Because this part repeats a lot we're going to build a few small subgroups.
[7:44] Think of it like Lego pieces that we can stamp out multiple times instead of wiring it by
[7:48] hand.
[7:49] A direction vector, a translate tab and a cascade stage.
[7:53] Then we assemble those pieces into the main blur engine that does all the streaking.
[7:57] Now to create this blur engine let's make a little bit of room here and create a new
[8:01] empty group.
[8:02] Hop into it by double clicking it and name it street blur accumulated.
[8:06] And with internal nodes I'd like to add a dot before the name.
[8:11] Inside this group let's add some new inputs.
[8:14] Change the first type to color and rename the group input to image.
[8:19] Then add another one and rename it to length and change the default to 0.1 and the min
[8:25] to 0 and the maximum to 2.
[8:26] Then add another one and rename it to angle.
[8:29] Change the subtype to angle and add another one and change the name to behavior and the
[8:34] mode to menu.
[8:36] Now let's build the direction vector node.
[8:38] This little group converts the angle and length into a pixel offset so every tab knows which


### Direction Vector Node [8:40]
**Transcript (timestamped):**
[8:44] direction to slide and how far.
[8:46] Add a math node and change the mode to cosine.
[8:49] Duplicate the node and change the mode to the sine function.
[8:52] Then duplicate the group input node and plug the angle value in the value of these two
[8:56] nodes.
[8:57] Then next add a math node and set it to multiply and multiply the cosine and the sine by the
[9:03] length of our group input.
[9:07] Right after that add a combine xyz node and combine the result of the multiply nodes into
[9:13] a vector.
[9:14] Then add a relative to pixel node and change the data type to vector and the reference
[9:19] dimension to y.
[9:20] Then duplicate the group input and feed the original image as a reference into the image
[9:24] slot of the relative to pixel node.
[9:26] Then add a separate xyz node to separate the dimensions again into x and y.
[9:31] Now we can group this part up with Ctrl G and name the group direction vector.
[9:38] This is our first internal node done so I'll duplicate it up here so we have it safe and
[9:42] ready and in the group outputs I remove the x and y.
[9:47] Next we'll build the translate tab subgroup.


### Translate Tap Node [9:48]
**Transcript (timestamped):**
[9:51] For this add two math nodes set to multiply and add a translate node.
[9:58] Connect x and y and add another group input node and connect the behavior to both extension
[10:04] slots.
[10:07] Add another group input, create a new input by connecting an empty slot to the image and
[10:12] rename it to result.
[10:15] I'm just reordering the inputs here a little bit.
[10:19] Then we can select the whole thing and group it up and name this subgroup translate tab.
[10:24] Hope back into group because we have here two important value sockets that I'd like
[10:28] to have exposed outside the group so connect them to a new input.
[10:33] With that this group is also finished and I will copy it up here.
[10:36] Next I will sort these group inputs underneath the group so we can treat it as a unit.
[10:42] Each translate tab shifts the image a little bit along the streak direction and how far


### Building the Tap Chain [10:43]
**Transcript (timestamped):**
[10:47] is set by this value.
[10:48] The plan is to make a whole row of them, each one shifted a bit further and then add them
[10:53] all together.
[10:54] Averaged out that stack of offset copies becomes the blur.
[10:59] So practically speaking we can just duplicate this whole group and add a mixed color node
[11:04] and set it to add.
[11:06] Then we can plug the first one into the A input and the second one into the B input.
[11:10] We can minimize this group and duplicate the whole thing 8 times for example and then
[11:16] connect everything together.
[11:24] Then we take the original image and put it into the result input of our translate tab
[11:30] and this in each node so we can use reroute nodes to make the whole thing a bit more readable.
[11:35] Each of these tabs needs to sit at an evenly spaced position between 0 and 1 so we take
[11:41] the index divided by n minus 1 which gives us these values for 8 tabs.
[11:46] So I quickly fill in all the values here and then we can take this add node and change
[11:55] the mode to multiply.
[11:57] Then add a math node and set it to divide and divide 1 by the amount of tabs you have.
[12:03] We do this because we added all the tabs together but that gives us 8 times too much brightness
[12:08] to turn that sum back into an average we divide by 8.
[12:12] To see what we've done add a group output node and connect the result to the image.
[12:18] Then outside the group connect the result of the multiply node to the image socket and
[12:22] connect the streak length to the length and change the behavior to repeat.
[12:27] Now connect the output of the image to the lens distortion and now you can see what's
[12:32] happening.
[12:33] The image gets pushed up step by step and it repeats over the edge.
[12:38] Next we need to mirror the angle that feeds into our streak blur group.
[12:43] For this duplicate the angle input and the subtract node, swap the value to the second
[12:48] input and type in the upper value socket pi times 1.5 and connect it into the angle input
[12:55] of the blur streak node.
[12:57] And now if we change the angle the wrap follows it.
[12:59] The streak stays continuous to any angle instead of breaking off sideways.
[13:04] What we just built was 8 tabs.
[13:06] Enough to see how it works but on a long streak you'd count individual copies.
[13:11] So here in a fast forward I'm doing the exact same thing but with 32 tabs.
[13:17] More tabs, smoother streak, simple as that.
[13:19] It's almost entirely copy-paste.
[13:21] Every tab is identical except two things.
[13:24] It's position value which still steps evenly from 0 to 1.
[13:28] I'm showing the values for 32 steps now here on screen.
[13:36] And don't forget the normalize divides by 32 not 8.
[13:40] With all 32 tabs in place the result is already much smoother but if we push the streak really
[13:45] long we can see faint stripes.
[13:47] So before the tabs we're going to add one more piece, a smooth and cascade.


### Cascade Node [13:50]
**Transcript (timestamped):**
[13:51] The idea is quite simple.
[13:52] We take the image and blend it with a slightly shifted copy of itself.
[13:56] Then we do that again with half the shift and again and again.
[14:00] Five of these halving steps should be enough to smear each tab into its neighbor.
[14:04] So those 32 copies melt together into one continuous streak.
[14:08] So let's build one of these cascade nodes.
[14:10] Add a math node and set it to subtract with the second value set to 1.
[14:15] Then duplicate this math node and set it to power and plug the subtract node into the
[14:20] exponent and set the base to 2.
[14:23] Divide this node again and set this node to multiply and plug the power node into the
[14:28] first socket and multiply by 0.001008.
[14:33] So why exactly this number and not something rounder?
[14:35] It's just one tab gap over 32.
[14:38] Five stages that we build afterwards double each time so together they cover exactly one
[14:43] gap.
[14:44] That's the whole trick.
[14:45] So next let's make some room here and copy a group input node and our direction vector
[14:51] from up here.
[14:53] Then connect the angle and the length to the direction vector and the image.
[14:57] Then duplicate the multiply node and multiply x and y together with the other multiply node.
[15:05] Then next add our good old translate node and wire it up as you can see on screen.
[15:13] Then after the translate node add a mix color node and mix the translate node with our original
[15:20] image together and set the factor to 0.5.
[15:24] Select the whole setup and group it with Ctrl G.
[15:27] Then rename this last group to .cascade.
[15:30] In the end panel we can remove this duplicate of our image slot just to make things a bit
[15:34] cleaner and connect the top image slot to the direction vector.
[15:38] And before we forget duplicate this group input one more time and connect it to the
[15:43] translate node.
[15:44] As a last step select the top value slot of this subtract node and wire it up to the
[15:49] group input.
[15:50] Change the type to integer, the default to 1, the mint to 1 and the mix to 8.
[15:55] Hope out of the group and rearrange the whole tower like we did before with the translate


### Building the Cascade Chain [15:57]
**Transcript (timestamped):**
[16:00] tab group so we can move it as a unit.
[16:03] Now copy this cascade group 5 times and wire them up.
[16:09] Then change the values to 1, 2, 3, 4 and 5.
[16:13] And when we plug it in you can see how the streaks get nicely blurred.
[16:18] One thing that we forgot in the beginning is to set some default settings to the streak
[16:21] length input so I change the default to 0.1, the minimum to 0 and the maximum to 2.
[16:28] So if we play around with the streak length the banding is now gone.
[16:32] We only want the wrap around from the streak blur.


### Limiting the Image Wrap [16:33]
**Transcript (timestamped):**
[16:34] The main streak itself should still come from the directional blur.
[16:37] So the trick is we run our accumulator twice, once on repeat and once on clip then subtract
[16:42] them.
[16:43] They're identical except at the edges so everything in the middle cancels to black.
[16:48] So duplicate our streak blur and wire it up as you can see on screen.
[17:00] Then after the streak blur nodes add a mix color node and set it to subtract.
[17:05] Tract these both from each other and set the second one to clip.
[17:10] Then after the subtract node add another mix color node and set it to add and add the directional
[17:15] blur on top.
[17:18] And set the factor to 0.72.
[17:21] This 0.72 controls how strongly we add the tail back in.
[17:24] Why not just one you ask?
[17:26] Our accumulator and the directional blur are different methods so the tail comes out a
[17:30] bit brighter than the streak.
[17:31] I found that this value matches them quite nicely.
[17:35] Wrap the whole thing up and call it edge wrap and give it a nice color again.
[17:40] And then add a switch node and set it to color.
[17:46] Connect the result of the subtract node to the true input of the switch node and set
[17:50] the false input to black and connect the switch node to the B input of the add node.
[17:55] And then connect the output of the directional blur to the A input of the add node.
[18:00] Add a new group input node and connect it to the switch input of the switch node and
[18:04] rename it to wrap around edges.
[18:06] In the end panel check the default option.
[18:14] Now we have a neat checkbox that allows us to check whether we want the wrap around edges
[18:19] or not.
[18:20] Next duplicate the directional blur node and wire it up as you can see on screen.
[18:28] Now next rename the edge wrap frame to forward and duplicate the whole thing and rename it


### Symmetric Blur [18:29]
**Transcript (timestamped):**
[18:34] to backwards.
[18:36] Now we have some loose ends here so connect everything up like you can see on screen here.
[18:42] And I guess this is the stage where many errors can happen so just double check you got everything
[18:46] before you move on.
[18:48] Then we give the streak direction the same treatment.
[18:50] We duplicate it and rename it to forward and backward.
[18:55] So in this new streak direction we need to change the math node from subtract to add
[18:59] and need to type in pi.
[19:02] Then add another math node set to subtract and subtract pi divided by 2.
[19:10] Then for the second input change the top value to pi divided by 2 as well.
[19:14] Then hook these new nodes to the new directional blur node as you can see on screen.
[19:19] Then add a mix color node and set it to mix and mix these two add nodes together with
[19:24] 0.5 to average them out.
[19:28] Then add another switch node and set it from float to color and in the true input put in
[19:34] the result of the mix node and in the false input the result of the lower add node.
[19:43] Then to control the whole thing add another group input and wire it up to the switch and
[19:48] rename it to symmetric blur.
[19:52] In the end panel I'll drag it under the angle value and just like that we get a neat checkbox
[20:00] to toggle on and off the symmetric blur.
[20:05] So with that the most complex things are now done.


### Streak Intensity [20:06]
**Transcript (timestamped):**
[20:08] Everything that comes from now on is just need to have or is for color grading.
[20:13] To control the intensity of the streaks I add a mix color node set to multiply and I
[20:20] add a new group input node and I will connect it to the color, call it streak intensity
[20:25] and in the end panel I change the type of the input from color to float and I set the
[20:32] default to 1 and the minimum to 0 and the maximum to 5.
[20:39] To keep our node a bit more user friendly we can also work with panels to hide away settings
[20:43] that we don't need that often.
[20:45] So I create one and I rename it to adjust and I will drag and drop the streak intensity
[20:50] into it.
[20:53] Next for some artistic control I think it would be cool to color the streaks directly


### Color Tint [20:54]
**Transcript (timestamped):**
[20:57] so add a mix color node set it to multiply and connect another group input node directly
[21:03] to the color and rename it tint.
[21:06] Then change the default color in the end panel to pure white and drag it into the adjust
[21:10] panel.
[21:11] So now we have a color field that we can just drag around the color and color our streaks.
[21:18] Then I would add here RGB curves node and I will drag the lower point here just a tiny
[21:24] bit down to control the falloff a bit more.
[21:26] This is just eyeballing and purely optional.
[21:29] Then frame the whole thing up and call it blend and grade.
[21:33] So next let's work on the animated chitter.


### Animated Jitter [21:35]
**Transcript (timestamped):**
[21:36] Add a new panel node and rename the panel to animated chitter.
[21:40] A cool thing that we can do is add a toggle right on the panel.
[21:44] Then inside the new panel add a few more inputs that is speed with a default of one and a
[21:49] min of zero and a maximum of 20.
[21:54] Add another one and call it amount with a default of 0.5 and a minimum of zero and a
[22:01] maximum of two.
[22:02] Add another one and call it seed and change the type to integer.
[22:10] Then next to our streak length add a scene time node and place it into the frame.
[22:14] Add a math node and set it to divide and divide the frame count by 10.
[22:21] This just makes it a bit slower.
[22:23] Then duplicate the math node and set it to multiply and here our newly created group
[22:27] inputs come into play.
[22:29] So multiply by the speed.
[22:33] Duplicate the multiply node and change it to add and add the seed.
[22:39] Then add a noise node and change it from 2D to 1D and connect the output of the add
[22:44] node to the W value.
[22:47] Add another math node and change it to subtract and whoops unhide the noise texture and connect
[22:52] the factor to the subtract value.
[22:57] Duplicate the subtract node and change it to multiply and multiply the value of the subtract
[23:02] node by our amount value.
[23:08] Then add a switch node and leave it at float and connect the animated jitter toggle to
[23:13] the switch input and the multiply to the true input and leave the false value at zero.
[23:22] Add another math node and add the streak length to it.
[23:27] Connect it like this and add another math node and set it to maximum and leave the value
[23:32] at zero.
[23:36] Back in our main node we have a checkbox and if we type in our default values and hit play
[23:41] our jitter works.
[23:45] Now one last thing I'd like to add is similar like the mask in the beginning is an option


### Isolated Streaks Output [23:46]
**Transcript (timestamped):**
[23:49] to output just the streaks.
[23:51] For that add a mixed color node, set it to add and in the input put it to pure black
[23:58] and connect the output of the curves node into the B input.
[24:02] Then connect the result to the group output and rename it to streaks.
[24:08] Now we have an option to only output the streaks which is super useful for compositing.


### Outro [24:12]
**Transcript (timestamped):**
[24:13] And that's it, that's the whole filter done.
[24:16] Congrats if you made it so far, I'm proud of you and I really hope you've learned something.
[24:21] A huge shout out to my Kofi supporters.
[24:24] Your support helps me making these tutorials and I truly appreciate it.
[24:30] Let me know in the comments if you have any questions or if there's anything specific
[24:33] that you want to see me covered in a future video.
[24:35] Thanks for watching and I'll see you in the next one.



---

## Captured Frames

- [2:10] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_000.jpg
- [4:55] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_001.jpg
- [9:31] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_002.jpg
- [11:45] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_003.jpg
- [14:30] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_004.jpg
- [17:15] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_005.jpg
- [19:15] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_006.jpg
- [23:15] tutorials/frames/how-to-create-a-time-shift-blur-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
A reusable compositor node-group asset recreating the film "time shift" / shutter-desync blur (Project Hail Mary-style): highlights are isolated, smeared with Directional Blur, and wrapped around the frame edge via a hand-built 32-tap Translate-node accumulator (Blender's compositor has no native wrap).

### Summary
Kai rebuilds the RE Timing Shift Box effect — deliberately desyncing shutter and film pull-down so highlights streak across frame — as a drag-and-drop compositor group asset with exposed controls: Highlight Threshold, Streak Length, Angle, Wrap Around Edges, Symmetric Blur, Streak Intensity, Tint, and an Animated Jitter panel, plus Mask input and a streaks-only output. The centerpiece lesson is working around Blender's missing edge-wrap: a "streak blur accumulator" built from small reusable subgroups (direction vector, translate tap, smoothing cascade) run twice (Repeat vs Clip sampling) and subtracted so only the wrapped tail survives, then added back over a normal Directional Blur. Works in the realtime compositor for 3D scenes and, in Blender 5.2+, as a non-destructive modifier on video footage.

### Key Steps
1. Create a compositor group named "Time Shift Blur" (color tag: Filter). Core: **Directional Blur** with Samples 64.
2. Highlight isolation: **Map Range** (From Min 0.5) → **Mix** (A = 1, factor = new "Highlight Threshold" input) → Multiply node with a "Mask" input (default 1, min 0, max 1, Hide Value) → **Mix Color (Multiply)** with the original image to restore streak color.
3. Comp streaks over the image with two **Mix Color (Add)** nodes (image + blur; image + pure white) divided by each other — normalizes so the threshold slider behaves.
4. Add **Lens Distortion** at 0.01 after the blur for subtle chromatic aberration.
5. Expose Angle (through Math Subtract π/2 so 0° = vertical streaks like the real effect) and Streak Length (default 0.1, min 0, max 2).
6. Edge wrap — build ".Streak Blur (Acc)" group from three Lego subgroups:
   - **.Direction Vector**: Cosine + Sine of Angle × Length → Combine XYZ → **Relative to Pixel** (Vector, reference dimension Y, original image as reference) → Separate XYZ.
   - **.Translate Tap**: two Multiply nodes × a per-tap position value → **Translate** node with both extension modes driven by a "Behavior" menu input (Repeat = infinite tiling).
   - Tap chain: 32 taps (8 to prototype), each at position index/(n−1) (e.g. 0/7…7/7 for 8), all Added together then divided by n to average. Feed the group's Behavior = Repeat.
   - **.Cascade**: blends the image with a shifted copy at factor 0.5; shift = 2^(stage−1) × 0.001008 (one tap gap ÷ 32, so 5 doubling stages exactly cover one gap). Chain 5 cascades (values 1–5) before the taps to melt the 32 copies into a continuous streak.
7. Limit the wrap: run the accumulator twice — Behavior Repeat and Clip — **Mix Color (Subtract)** them (interiors cancel, only wrapped tail remains), then **Mix Color (Add)** onto the Directional Blur at factor **0.72** (matches accumulator vs Directional Blur brightness). A **Switch (Color)** node + "Wrap Around Edges" boolean input toggles the tail (false = black).
8. Mirror the accumulator's angle with π×1.5 minus angle so the wrap follows any streak direction.
9. Symmetric blur: duplicate the whole edge-wrap + streak-direction stack as "forward"/"backward" (backward angle = +π), Mix the two at 0.5, and gate through another Switch with a "Symmetric Blur" checkbox.
10. Grading: Mix Color (Multiply) "Streak Intensity" (float 1, 0–5, in an "Adjust" panel), Mix Color (Multiply) "Tint" (default white), optional RGB Curves for falloff.
11. Animated jitter (own panel with toggle): **Scene Time** Frame ÷ 10 → × Speed (0–20) → + Seed (int) → **Noise (1D)** W input → Subtract → × Amount (0.5, 0–2) → Switch (float) → Added to Streak Length → Math Maximum 0 clamp.
12. Extra output "Streaks": final result Added onto pure black → second group output, for external compositing.

### Nodes / Settings
- Directional Blur: Samples 64; Angle offset −π/2 (default up/down); add-back factor 0.72
- Map Range From Min 0.5 (highlight threshold base); Lens Distortion 0.01 (chromatic aberration)
- Relative to Pixel: Vector, reference dimension Y — converts angle/length into pixel offset
- Translate node sampling Repeat = the wrap hack; Clip copy subtracted to isolate the tail
- 32 taps at index/31 positions, sum ÷ 32; cascade constant 0.001008 = (1/32) tap gap over 5 ×2 stages
- Jitter: frame/10 × speed + seed → 1D Noise → recentered (−0.5) × amount, max(0) clamped into streak length
- Group asset inputs: Image, Mask, Highlight Threshold, Streak Length (0.1 / 0–2), Angle, Wrap Around Edges (bool), Symmetric Blur (bool), Adjust panel (Streak Intensity 1 / 0–5, Tint white), Animated Jitter panel (toggle, Speed 1 / 0–20, Amount 0.5 / 0–2, Seed int); outputs Image + Streaks
- Finished filter is also sold as a drag-and-drop asset on the author's Ko-fi

### Difficulty
Advanced

### Blender Version
5.x (realtime compositor; 5.2+ for use as a non-destructive modifier on video footage)

### Tags
compositing, motion-design, camera, animation, procedural, advanced, blender-5x

---

## Related Tutorials
- [A FULL Blender Compositor Course!](a-full-blender-compositor-course.md) — compositor fundamentals this build assumes
- [New Compositing Effects in Blender 5.2](new-compositing-effects-in-blender-52.md) — the 5.2 compositor/modifier features this asset targets
- [Replacing Adobe After Effects with Blender (tutorial)](replacing-adobe-after-effects-with-blender-tutorial.md) — same "Blender as finishing/comp tool" workflow

---
title: How To Make Better Materials In Blender 5.2
source: YouTube
url: https://www.youtube.com/watch?v=DhSJ8gD7iyo
author: BlankFaceStudios
ingested: 2026-08-09
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-make-better-materials-in-blender-52/
frame_count: 0
frame_status: pending-selection
---

# How To Make Better Materials In Blender 5.2

**Source:** [YouTube](https://www.youtube.com/watch?v=DhSJ8gD7iyo)
**Author:** BlankFaceStudios
**Duration:** 15m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-make-better-materials-in-blender-52 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, so I have a little bit of a challenge for you.
[0:04] I want you to turn this sphere into wood.
[0:08] Now some of you out there just went and did this.
[0:16] You know who you are.
[0:17] And this, this is bad, don't do this.
[0:20] Instead, today I'm going to help you guys conquer your fears of procedural material
[0:24] making.
[0:25] Which I know looks scary, but it's actually really easy.
[0:28] We're going to go over some basic techniques together like masking and layering, the main
[0:32] nodes you should be using, and some additional tips for realism.
[0:36] And then at the end, we're going to combine it all together and make this awesome metal
[0:40] shader.
[0:43] So let's get right into it.
[0:44] Once we're inside Blender, really quick, just go to the top left corner where it says
[0:48] edit, go to preferences, add-ons, and type in Node Wrangler.
[0:52] This add-on gives tons of useful shortcuts, so make sure you have that checked.
[0:55] The shader editor works just like the viewport.
[0:57] If you want to add a new node, just press shift A. Or you can right click and go to add.
[1:02] Or you can go to the top left and press this add button.
[1:05] But I don't think anyone actually does that.
[1:07] And when you pull up the add menu, you're going to see that there's tons of nodes.
[1:11] But don't worry, I've set aside the most useful ones.
[1:13] Starting with the texture nodes.
[1:15] The noise texture is going to be your new best friend.
[1:17] It's great for mixing colors together, adding grunge and dirt, and just overall variation.
[1:22] And there's tons of settings you can use to further customize it.
[1:25] Like scale for your frequency, detail for detail, and even distortion.
[1:31] Woo!
[1:32] Second, we have Voronoi textures, my personal favorite.
[1:35] Voronoi textures are a cell-based pattern, so they're really good for skin and organic
[1:39] materials.
[1:40] If we change this F1 setting to distance the edge, we see we can start to make a cracked
[1:44] rock texture, or like reptile scales.
[1:47] And if we lower its randomness and swap from Euclidean to Chebichev, we can even make a
[1:52] tile-like pattern.
[1:53] All in one node!
[1:54] And next we have wave textures.
[1:56] They're great for creating lines and grid-like materials.
[1:59] If we distort this a bit and add some detail, we can even start to make something that looks
[2:02] kind of like wood.
[2:03] And finally we have gradients, which are really great for when we're trying to get a fade
[2:07] of a color or effect a specific area of our material.
[2:10] These work especially great with our next node, which is the color ramp.
[2:14] The color ramp allows for more control over our texture nodes.
[2:17] Here we have a basic noise texture.
[2:19] But if we drag these values on our color ramp, we begin to clamp our values and change the
[2:24] level of contrast.
[2:25] And if you want no blending at all, you can even just swap from linear to constant, and
[2:30] now you have pure black and white.
[2:32] With just these four texture nodes, they're basic controls and a color ramp, you can already
[2:36] see the hundreds of different textures and patterns that are possible.
[2:41] And once we start layering them on top of each other, we can make nearly anything we
[2:44] want.
[2:45] But before we can do that, I need to tell you guys something, and it is going to blow
[2:49] your mind.
[2:50] Are you ready?
[2:53] Colors and colors are the exact same thing.
[2:56] Let me explain.
[2:58] Right now I have a white plane, but I want to make it black.
[3:01] Now typically you would use a color node or a color ramp, or you just change this little
[3:06] box right here.
[3:07] Isn't that convenient?
[3:08] But we're not going to do that because we're cooler than everyone else.
[3:11] Instead, add a math node.
[3:13] Ooh, math scary.
[3:15] And then make both numbers zero.
[3:16] All right, now zero is a number, not a color, right?
[3:20] Yet if I plug this into my color input, it turns black.
[3:24] This zero from our math node is being sent out as a value, a single digit of data.
[3:30] However, a color is known as a vector, which is a piece of data made up of three values
[3:36] or three numbers.
[3:37] I know this is a lot of numbers, guys.
[3:39] Just hang in there.
[3:40] We can actually see if we hover over our yellow color input dot that those three values are
[3:45] assigned to RGB, or red, green, and blue.
[3:49] However, we're feeding the color only one value here when it's looking for three.
[3:54] So it's putting zero for red, green, and blue.
[3:57] Hence, we get black.
[3:58] It's the absence of all colors.
[4:00] If we crank this value to one, now it's white, the combination of all colors.
[4:05] If you wanted to target each of these channels individually, you could add a vector math node.
[4:09] So now we have three numbers.
[4:11] If I slide this first one up, we start to get red.
[4:13] So now we can target red, green, and blue individually.
[4:17] We can just the others and then make even more colors.
[4:19] Now I can hear you thinking, why would I ever make my colors this way?
[4:23] The answer is, you wouldn't.
[4:25] That would be stupid.
[4:26] Making your colors like this would be like using the add button at the top of the shader
[4:30] editor.
[4:31] It's gross.
[4:32] I've told you all of this simply as an example to show you that colors and numbers are interchangeable.
[4:38] So now let's try this in reverse.
[4:41] Here I have a mixed color node, which does exactly what you think it would.
[4:46] Right now I'm mixing red and blue, which is being controlled by this factor value.
[4:50] When our factor is at one, we have blue, and at zero, we have red.
[4:54] Now I want to make a spotted pattern with red and blue, but when I try and mix them together
[4:58] with this factor, I just get purple.
[5:01] We then need this value to sometimes be one, but also sometimes be zero.
[5:06] But that would mean this factor value would need to be two different numbers at once.
[5:11] We can't do that.
[5:13] Or can we?
[5:14] Also we know that white is one and black is zero.
[5:17] Let's just take a noise and a color ramp and plug that into our factor value.
[5:21] Now we have both red and blue.
[5:23] And this is what we call masking, where we layer or mix different elements on top of
[5:27] each other using black and white masks.
[5:30] Here's a more practical version of this.
[5:32] I have two different noises, one at a really small scale and one at a large scale.
[5:37] Same as our colors, we can use an additional noise as the factor and then get variation
[5:41] in our texture.
[5:42] This helps break up patterns, make things more realistic and just add a lot more detail.
[5:46] This stuff doesn't just only apply to color though.
[5:49] Now that we know this information anywhere you see a number, you can now control it with
[5:53] a texture instead.
[5:55] And this is really powerful.
[5:57] If we apply this noise texture setup to our roughness, we can then start to get variation
[6:02] in how reflective it is.
[6:04] Textures on roughness is really great for making things look wet or worn or even adding
[6:08] details like fingerprints.
[6:10] Now this sphere looks really detailed.
[6:12] At first you might even think, wow, that's a pretty high polysphere.
[6:16] But what if I told you it wasn't?
[6:18] Surprised?
[6:19] This is called a bump map.
[6:21] We can take our classic noise and color ramp, but now plug it into a bump node and then
[6:26] connect that to our materials normal input.
[6:29] Now we're creating the illusion of geometry detail when it's not even there.
[6:33] We can also affect things like alpha or emission with these textures to randomize transparency
[6:38] or how much the material glows.
[6:41] And that's the basics.
[6:42] See all that number stuff was important.
[6:45] Now let's put everything we just learned to the test by creating a realistic metal shader
[6:49] from scratch.
[6:52] Now I know what you guys are thinking.
[6:53] Surely he's not about to throw in a promotional segment right before the part of the video
[6:58] that we actually care about.
[7:00] Wait, is he?
[7:02] Yup.
[7:03] Did you guys know that the material made in this video is going to be available for
[7:06] download on my Patreon page?
[7:07] Well, of course you didn't.
[7:09] But now you do.
[7:10] I've got materials, blend files, early access to videos, and more all on my Patreon page
[7:15] for my three and five dollar members.
[7:17] I also have this really fun behind the scenes series where I go and show in more in depth
[7:22] look into my projects for my videos, giving insight into my process, as well as specialized
[7:27] little tutorials that you wouldn't get here on YouTube.
[7:29] I actually just released a super fun episode featuring work I did on a horror film, like
[7:34] with people and stuff.
[7:36] It's crazy.
[7:37] There will eventually be a YouTube video on that project, but if you're interested to
[7:40] learn more about it now, go check it out with the link down in the description.
[7:44] Your guys' support over there really does mean a lot to me, so thank you.
[7:51] Before we get started, it's always good to have references.
[7:54] So I just took this ice cream scoop from my kitchen, which I think has like a really
[7:58] cool like metal texture to it.
[8:00] So I'm going to take a picture of this and then drop it into Blender as an image plane
[8:04] so then I can see it while I work.
[8:06] I'm going to add in a noise texture, a color ramp, and a mix color node.
[8:10] If you press Ctrl, Shift, and then click on the color ramp, you can actually preview it
[8:14] on your object.
[8:15] With this noise previewed, I'm going to adjust the scale and make it a bit higher frequency
[8:19] to get that speckly look of the reference.
[8:21] Then I'm going to attach it to my mix color in the factor input, and then we'll make
[8:25] A and B some different colors from the image.
[8:28] But we need to break this up a little bit, so let's duplicate that noise setup and then
[8:32] make a lower scale noise to add some variation.
[8:35] Now once we have two different noises set up, let's add a new mix color node and one
[8:39] final noise to act as the factor to mix our first two together.
[8:44] Once you've got those mixed, let's plug that into our first mix color node, and now we
[8:47] have our base color.
[8:49] Okay, now we've only just started, but if we do this setup like three more times, it's
[8:54] going to get very busy in here.
[8:56] So let's organize a little bit.
[8:57] If you select all of your nodes and then press F, you can put them in like a little frame
[9:01] and label them.
[9:02] Press N and you can change the label size and even the color.
[9:06] Now looking back at the reference, there's tons of these like dark little speckles on
[9:09] this metal.
[9:10] So we're going to make another noise mask, but this time clamp the values way down to
[9:14] get these little dots.
[9:15] Then we can tack on another mix color, use that speckled noise as the factor, mix black
[9:20] or a gray with the previous setup, then change the blend mode to multiply.
[9:25] This way our speckles darken the colors underneath them.
[9:29] Now something really important that we completely forgot about, what kind of material is this?
[9:33] Oh, right, metal.
[9:35] Well wouldn't you know if we actually look on our shader, we literally have a metallic
[9:39] slider and if we just adjust that, now our metal looks more like metal.
[9:44] Who would have seen that coming?
[9:45] And now comes the fun part.
[9:47] See these scratch marks?
[9:49] How are we going to make these?
[9:51] Well a couple ways actually.
[9:53] Scratches are lines and thankfully we have a texture that's really good at making lines.
[9:59] Remember this guy?
[10:00] Let's make two of these.
[10:02] Now unlike our noise textures, we aren't going to make these different scales or frequencies,
[10:06] we want them to be turned different directions.
[10:09] So how do we rotate things?
[10:11] Click on your node and press control and T.
[10:14] Oh look, vectors.
[10:15] Hey, we know those.
[10:17] Now if we rotate on the Y axis, we can make these diagonal.
[10:21] Then we'll do the same for the other wave texture, but just the opposite direction.
[10:24] That way we'll have scratches going at different angles.
[10:27] Then let's just add a color ramp for both of these and make them really really thin.
[10:31] But they're way too perfect, so let's add some distortion.
[10:34] Now this is going to take a lot of playing around with between the distortion and the
[10:38] three different detail settings that come with the wave texture.
[10:41] After a while though, I came up with this and I think it's pretty good.
[10:45] Now if we mix these two together, they overlay and make this weird like wobbly grid pattern.
[10:51] But we want little marks, so we need to break these lines up somehow.
[10:54] Add a new mix color node, noise, and color ramp for each of the wave textures.
[10:59] Use the noise and the color ramp to create a mask to plug into the factor of the mix
[11:04] color.
[11:05] Then just make input A our scratches or the wave texture, and then make input B black.
[11:10] And now we get these little clumps of broken lines.
[11:12] The higher frequency your noise mask is, the more little scratches you get.
[11:16] Then when you mix both of these together, remember to make sure that your noise masks
[11:20] aren't identical, otherwise they'll line up like this.
[11:23] I actually just offset one of the noises with a new mapping node and then change the location.
[11:28] But even when we put this whole setup into like a frame, it still takes up a ton of space.
[11:33] So let's do something different.
[11:35] Select all the nodes and then press Ctrl and G and whoa, wait, where, where are we?
[11:41] Don't worry, everything didn't just get deleted.
[11:43] Go up to this little arrow and now you'll see that we put them in their own little node
[11:47] space.
[11:48] Nice and out of the way.
[11:49] But we can still access their output in our main shader editor.
[11:52] This is called grouping.
[11:54] Get it because G for group and yeah, you get it.
[11:57] Now let's use these scratches to affect our color.
[12:00] Add another mix color node, plug the whole main color setup into the A slot and then
[12:05] white for B. Then we'll just use our scratch output as the factor.
[12:09] And now we can see all these little scratch marks as white lines on our base color, but
[12:13] let's make it even better.
[12:15] Add a bump node, plug the scratches into the height and then make the distance something
[12:19] like .01.
[12:20] Then invert it so our scratches cut into the metal rather than like bump out like this.
[12:25] I'm also going to combine this with a couple of other bump maps like a high detail noise
[12:29] and also a low detail one.
[12:31] And now our bump has a lot more variation.
[12:33] You can combine bumps just like colors, but be wary when they mix together, they can lose
[12:39] some of their strength.
[12:40] So you may need to turn them all up a little bit.
[12:42] Then I'm just going to move all this stuff into their own little group.
[12:44] Now remember when I said there's a few ways to do the scratches?
[12:48] I wasn't super happy with the wave generated ones since we weren't able to get these longer
[12:53] scratch marks.
[12:54] So let's try something else instead.
[12:58] This time let's add a Voronoi texture.
[13:00] Change the F1 setting to distance to edge.
[13:03] Then add a color ramp and let's clamp this down and make the lines really, really thin.
[13:07] Then add some detail and some roughness to get this more imperfect scratched look.
[13:13] Then we essentially just do what we did with the wave textures.
[13:15] Make two different Voronoi's, mask them each with a black noise and then mix them together.
[13:20] Then once you're done, it should look something like this.
[13:23] This takes up a lot of space too, so I'm going to group this and then put it with the other
[13:26] one.
[13:27] I also went in and made some other random tweaks that I'm not going to show.
[13:31] Just to get it looking how I wanted, I added some lighter colors.
[13:33] I felt it was a bit too dark.
[13:35] I also added a displacement modifier with a cloud texture.
[13:38] So my sphere is a bit more imperfect looking.
[13:41] You can actually do this within the shader editor, but that'll be for another video.
[13:46] We've honestly barely scratched the surface of what can be done with procedural materials.
[13:50] There's like so many more nodes like ambient occlusion, displacement maps, subsurface scattering
[13:56] and more that we just didn't get to.
[13:59] But this was the basics, the fundamentals that you need to start building materials from
[14:03] scratch.
[14:04] But if you guys would be interested in a more advanced shader tutorial, let me know down
[14:08] in the comments.
[14:11] This is our final material.
[14:14] And while maybe in a pinch applying some stock photo you found online to your object could
[14:18] work, procedural materials just give a much higher quality and allow for so much more
[14:23] customizability.
[14:24] Anyways, hopefully you guys learned something and found this topic at least as half as interesting
[14:28] as I do.
[14:30] And if you guys followed along or made your own materials, come show them off on my Discord
[14:33] server.
[14:34] I love seeing your guys' work and I even take the best stuff from our community and I
[14:38] showcase it at the end of my videos.
[14:40] So with that said, please enjoy the work of these very talented people and I'll see
[14:45] you guys in the next one.
[14:47] Bye bye.



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

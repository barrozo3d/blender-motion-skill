---
title: New Compositing Effects in Blender 5.2!
source: YouTube
url: https://www.youtube.com/watch?v=UhlIT_-3xQM
author: Ryan King Art
ingested: 2026-07-20
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/new-compositing-effects-in-blender-52/
frame_count: 0
frame_status: pending-selection
---

# New Compositing Effects in Blender 5.2!

**Source:** [YouTube](https://www.youtube.com/watch?v=UhlIT_-3xQM)
**Author:** Ryan King Art
**Duration:** 14m35s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py new-compositing-effects-in-blender-52 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] So Blender version 5.2 is just recently released, and if you'd like to check out all the new features and updates, you can check out this page here on Blender's website, link to it will be in the video description.
[0:09] And in the new update, they've added some new compositing effects, which I'll be going over in this video.


### Defaults to GPU [0:14]
**Transcript (timestamped):**
[0:14] So in Blender 5.2, I'm just going to jump to the compositing layout, and then I'm just going to click on New to add new compositing nodes.
[0:20] Now one really nice thing about the compositor in 5.2 is it uses your GPU automatically.
[0:26] So if I just open up the side panel, let's go here to the render properties, and then I'm going to go here to performance, and then here under compositor, you can see we now have the device, and it should be set to GPU on default, you can set it to GPU if you have a GPU.
[0:39] But of course, if you don't have a GPU in your computer, you can totally just use your CPU, but the compositor works a lot faster on a GPU, so I'm definitely using that.


### Text in Compositor [0:46]
**Transcript (timestamped):**
[0:46] Now I'm just going to do a quick test render here, and then I'll jump back to the compositor.
[0:50] Now another great feature of the compositor is we now have this string to image, and the string is basically referring to text.
[0:58] So I can just drag this out to make it bigger, and I can just type something.
[1:01] So I can now just control shift select the string to image so you can see we have text in the compositor now, which is really great.
[1:08] Now what if you want to mix the text into your rendered image?
[1:11] What I can do is search for an alpha over node and drop here, and let's just preview the alpha over node, and then this string to image, I'll put it in the foreground,
[1:19] and then the render layers is going to be the background.
[1:21] Now, unfortunately, the strings to image doesn't actually have any alpha transparency, so you can't really see behind the text.
[1:27] It's just black.
[1:28] But what I can do is I can take this image and I can put it into the factor.
[1:32] And so when I do that, now you can see that it's using the black and white data.
[1:35] So the white part is going to be the text and the black part is going to be whatever's going to the background, which is going to be the render layers.
[1:42] So now I can customize the text.
[1:43] So for example, I can click here to import a font.
[1:46] And so I can just easily import a font and then I can also change the size of it.
[1:50] So let's just make the size a lot bigger.
[1:53] And then there's also some pretty easy to use settings like you can change it to the left or the middle or the right.
[1:58] And then also the vertical alignment as well.
[2:00] Now, if I drag the width down, it's going to put the text on top of each other.
[2:04] So you can now see if I just drag it down really small, you can see it's fitting each word on a line.
[2:09] But if I make the width higher, now the text can be all in one row.
[2:13] So it's definitely a pretty easy node to use.
[2:15] However, I do wish that I had some more features, maybe in the future we'll get some more updates.
[2:19] So for example, adding like a basic kind of gray background, maybe like a box around the text or adding a bit of a shadow, kind of like a shadow with a blur,
[2:26] similar to what we have in Blender's video editor.
[2:29] Those would be some nice features.
[2:30] It would also be nice if we had an alpha output so that we could just output an alpha and then mix it in with an alpha over.


### Download Assets [2:36]
**Transcript (timestamped):**
[2:36] And so we also have some new compositing effects here in the asset shelf.
[2:40] Now you are going to download some of these assets because some of these assets are in the Essentials Online Asset Library.
[2:47] If you haven't enabled the online access, you can click on Edit to go to the Preferences.
[2:51] Then you want to go down here to System and then go to Network and you want to click on the Allow Online Access.
[2:56] Now I've already downloaded all of them, but you're going to see a little cloud icon and you just want to click on the cloud icon to download it.
[3:02] And then you can use it.
[3:04] Now I'm not going to cover all of the effects because I actually have another video where I covered these other effects in Blender version 5.1
[3:10] when 5.1 was released.
[3:11] So you can check out that other video.
[3:13] Link is in the description if you want to check that out.
[3:15] But in this video, I'll just be going over the new effects in Blender version 5.2.


### Film Grain [3:19]
**Transcript (timestamped):**
[3:19] So for an example video, I'm using this video here that I used to showcase my recent sculpt.
[3:24] So the first new asset here is the Film Grain.
[3:27] So I'm just going to drop this in here so I can drag the factor up and down to control the strength of it.
[3:31] So it's pretty easy to control.
[3:33] Now there's also some different types here.
[3:34] So if you want to kind of play around with these, there's a bunch of different Film Grain effects.
[3:39] They do look pretty similar, but each one kind of is a little bit unique.
[3:42] Some of them are a little bit sharper.
[3:43] Some of them are a little bit more fuzzy.
[3:45] And then you can also turn on the animated value.
[3:47] And so this animated value is going to like generate different noise per frame.
[3:51] And so when I actually render this out, here's what the final animation looked like.


### Night Vision [3:55]
**Transcript (timestamped):**
[3:55] And the next one is a really cool one, probably one that I wouldn't use that much, but it is pretty cool.
[3:59] And that is Night Vision.
[4:01] So this kind of looks like Night Vision goggles.
[4:03] So it has this really cool almost like digital effect where there's like these little lines here.
[4:07] And kind of as I move along, you can see it's animated.
[4:10] You can also change the animation speed.
[4:11] And so when I render this out, this is what the animation looks like.
[4:14] Then there's also the exposure, which is going to kind of make it brighter.
[4:18] Then there's also this depth darken.
[4:20] So if you turn on the depth darken, you can see it's going to have a range of minimum and maximum.
[4:25] So what you can do is you can take the depth value from your rendered image
[4:28] and you can plug that into the depth pass.
[4:30] So just for an example, I added these cubes and I just put the cubes behind the sculpted character.
[4:35] You can see I'm just playing around with the minimum range and the maximum range.
[4:38] So it almost adds kind of like a misty effect or a foggy effect.
[4:41] Now this single distortion value, this is going to have kind of like those old TV lines,
[4:46] kind of making it look like it's an old distorted video.
[4:48] And there's also settings for this.
[4:50] So if I open it up, I can turn up the distortion factor.
[4:52] And now it looks like one of those old kind of distorted videos, maybe on like an old TV or like a VHS.
[4:58] There's also the distortion frequency, which is just going to scale it down.
[5:01] And so it's going to add more of them.
[5:02] Then there's also a glare value.
[5:04] So it's just going to kind of make the brighter parts of it brighter.
[5:07] So that definitely looks cool.
[5:08] And you can change the strength of it and the size and threshold.
[5:11] There's also this flicker, which you're not really going to be able to see that well.
[5:14] But you can see here's the rendered video that I rendered out and you can definitely see a flicker.
[5:17] Then there's also the degrade.
[5:19] And so the degrade is actually going to add kind of like a film grain effect.


### Depth Atmosphere [5:23]
**Transcript (timestamped):**
[5:23] Now the next effect is the depth atmosphere.
[5:25] So this is a way to create kind of like an atmospheric effect or create fog or mist.
[5:30] I do already have some tutorials on how to create fog and mist,
[5:32] but I can also use this new depth atmosphere.
[5:35] So what I did is rendered out this simple city scene here with like some city lights.
[5:39] And this is from my video on how to add fog to your scenes.
[5:42] But what I can do is I can take the depth value here on the render layers
[5:45] and I can put the depth into the depth here on the depth atmosphere.
[5:49] Now you can see there's a minimum and maximum distance value.
[5:52] So I can turn the like maximum up.
[5:54] So now you can see the fog goes back a bit farther.
[5:56] It's a bit larger.
[5:57] There's also the minimum distance.
[5:59] So if I turn this up, then the fog isn't going to start until it gets further out to the scene.
[6:03] So now you can see it doesn't look like the fog starts until about here,
[6:06] kind of halfway into the scene, or I can turn the minimum distance all the way down to zero.
[6:10] And the fog is going to start at the very starting.
[6:12] Now if I turn the maximum way down, you can see the fog is much thicker
[6:16] because it gets to the maximum amount of fog a lot quicker.
[6:19] And there's also some atmosphere settings so I can change like the thickness of it.
[6:23] There's also the interactive tint.
[6:25] And so if I turn this down, now you can see it's going to be more white.
[6:28] And so instead we can use a bit of a tint.
[6:30] So I'm going to make this like a dark blue color.
[6:32] So it looks like it's maybe a night scene or an evening scene.
[6:34] There's also the opacity.
[6:36] So if you just want to make all of the fog more invisible,
[6:39] you can just do that to kind of get rid of it.
[6:40] Now, as well as using the depth type, you can also use the mist type.
[6:44] So this is going to use Blender's mist pass.
[6:46] So what I'm going to do is open up the properties panel here
[6:49] and then I'm going to go to the search and I'm going to search for mist.
[6:52] So what you first want to do is go to the view layer
[6:55] and you want to checkmark the mist button.
[6:57] And so when you checkmark the mist button,
[6:58] now it's going to be right here on the render layer passes.
[7:02] Then what I want to do is go back here to the layout
[7:03] and I'm going to select my camera.
[7:05] And what I want to do is go to the camera settings.
[7:08] And again, I can just search for mist right up here.
[7:10] So it's easy to find.
[7:11] And under viewport display, I want to turn on mist.
[7:14] So when I turn that on, it's going to add this line here
[7:16] for the starting position of the mist
[7:18] and the ending position of the mist.
[7:21] So then the last thing that I can do is I can go here to the world properties
[7:24] and I'm searching for mist.
[7:25] So it's easy to find and you can see there is a mist pass here.
[7:28] And so there's the start and the depth.
[7:30] So the start is going to be where does it start to get misty?
[7:32] So I'll just turn this up a little bit.
[7:34] And then the depth is how far until we're going to get to 100% mist.
[7:38] So just something like that in our scene.
[7:39] Now I'll go back to the compositing layout
[7:42] and I can just control shift, select the render layers
[7:44] and I'll go down here and preview the mist.
[7:47] And if for some reason the mist pass isn't showing up here,
[7:49] even though you're previewing it,
[7:50] then that's probably because you just need to re-render the image
[7:52] with the mist pass turned on.
[7:54] So now what I can do is take the mist pass
[7:56] and put that into the mist.
[7:57] So it's going to use that black and white data to create the mist.
[8:00] Now what if you want to change the depth of the mist?
[8:03] Well to do that you need to go here to the world properties
[8:05] and go to the mist pass and then you can change the depth here.
[8:08] But you can see it's not really updating.
[8:10] That's because I just need to re-render the image.
[8:12] So I'll just turn this way down and then just hit F12 again to render.
[8:15] And it's rendered and you can see now I updated.
[8:18] So now you can see those street lights are kind of fading away a lot faster.
[8:21] Now what I could also do is search for a color ramp
[8:23] and put it between the mist and the depth atmosphere.
[8:25] So then I could drag these values around
[8:27] and so you can see that's going to make it more sharp or less sharp.
[8:30] So if I make it darker, the mist is going to be more invisible.
[8:34] But if I make it lighter, it's going to be a lot more visible.


### Dithering [8:37]
**Transcript (timestamped):**
[8:37] Alright, so the next compositing effect is the dithering.
[8:40] So let's just drop the dithering right here.
[8:41] And so the dithering is basically like a pixel art effect.
[8:45] So if I zoom in really close here,
[8:46] you can see it kind of is turning into pixel art
[8:48] and I can change the intensity.
[8:50] So if I just turn the intensity way down,
[8:52] you can't really see it that well,
[8:53] but it still looks a little bit pixelated.
[8:55] It's kind of making these kind of like shadow shapes.
[8:58] If I turn the intensity way up,
[8:59] you can clearly see that there's a lot of pixels.
[9:02] And then you can also change the type.
[9:04] So I'm just going to hold down the control key
[9:05] and switch between the different types.
[9:07] There's just some different methods for that pixel effect.
[9:10] And then I can change the pixelate value.
[9:12] So if I turn this way up, now you can see it's very pixelated.
[9:15] And when I was prepping for this tutorial and trying these all out,
[9:18] as soon as I saw this,
[9:19] I immediately thought of that one painting in Minecraft
[9:22] where there's like that like bus sculpture
[9:24] and it's all pixelated
[9:25] because the Minecraft paintings are all pixelated.
[9:27] I did sculpt this character in Blender.
[9:29] And if you want to check out the time lapse video,
[9:31] the link will be in the description.
[9:32] And then I can change the color amount.
[9:34] So if I turn this way down, it's going to be really sharp
[9:36] and have all these like really strong colors
[9:38] where I can turn it up and it will look much more
[9:40] like the original image,
[9:42] but it just has kind of some pixels
[9:43] if you zoom in really close.


### Paint Filter [9:45]
**Transcript (timestamped):**
[9:45] Now the next one is the paint filter.
[9:47] So I'm just going to drop the paint filter here.
[9:49] It basically makes your image look like it was hand painted.
[9:52] And I think it looks really good
[9:53] on my Michelangelo David sculpture
[9:55] because I'm making this look like it's supposed to be
[9:57] like a real life marble sculpture,
[9:59] but then it kind of looks like a painting.
[10:01] So just kind of gives it more of that traditional feel.
[10:04] Now there's a bunch of different types here.
[10:05] So there's watercolor, which I think looks the best.
[10:07] There's also oil paint.
[10:09] So that's pretty cool.
[10:10] Looks similar, but a little bit different.
[10:12] There's also this digital geometric,
[10:14] which doesn't look quite like a traditional painting
[10:17] because it is a little bit sharp.
[10:18] And if you change the type to custom,
[10:20] you can see now there's this stroke texture.
[10:22] So you could actually take some like existing image texture
[10:24] or something and you can actually plug it up
[10:26] to the stroke texture.
[10:28] So if I take this brick displacement image
[10:30] and plug that into the stroke texture,
[10:32] you can kind of start to see it looks like a brick pattern.
[10:34] Let's change it back to the watercolor
[10:36] because that's my favorite one.
[10:37] So you can see if I make the size larger,
[10:39] those blotchy bits are going to be a lot bigger.
[10:42] If I turn the size to like a really small size, like a five,
[10:45] now you can see it's going to be really small
[10:46] and I kind of have to zoom into the edges to see it.
[10:48] So it's almost like a detail level
[10:50] and it's changing the size of the splotches.
[10:52] So maybe just like something like a 40,
[10:54] that might even be a little bit too big.
[10:56] Maybe I'll just go with like a 20.
[10:57] Then there's also the simplification.
[10:59] So if I turn up the simplification,
[11:01] you can see it just looks a bit more smooth.
[11:03] It also has kind of like a little kind of circular pattern,
[11:05] but it looks quite a bit more smooth
[11:07] or I can turn the simplification way down.
[11:09] And you can see there's lots more areas
[11:11] which are kind of popping out.
[11:12] It looks just a little bit more messy,
[11:13] especially on the corners.
[11:15] And then there's the accidental colors.
[11:17] So if I turn this way up,
[11:18] you can see it's adding all these like blotchy colors
[11:20] or I can turn it way down
[11:21] and it's just going to use the original colors.
[11:23] Then there's the pooling effect
[11:24] which is going to add like little splotches and blobs.
[11:27] So it's almost like it's giving it imperfections.
[11:30] Then there's the sharpness.
[11:32] So clearly that's very sharp
[11:34] or I can turn this way down.
[11:35] And it's going to be pretty blurred.
[11:36] So I think somewhere in the middle looks pretty good
[11:38] because if it's too sharp,
[11:39] it just doesn't really look like an actual painting.
[11:42] It's too clear.
[11:42] So definitely somewhere in the middle looks pretty good.
[11:44] I actually think the default looks pretty good.
[11:46] And then you can change a seed.
[11:48] So that's just going to randomize the painting.
[11:50] And then to give it a little bit of a canvas-y texture,
[11:53] I can turn up this edge breakup.
[11:54] You can see we're kind of getting this like oval dots pattern.
[11:58] And I can also turn the scale down
[11:59] just to make it like really small.
[12:00] But it almost now looks like it's actually on
[12:03] like a canvas that you would paint on.
[12:05] There's also some other material settings you can change.
[12:07] So you can change it to like paper.
[12:09] So now it kind of looks like
[12:10] it's been painted on some rough paper.
[12:12] I can also just use none.
[12:13] Or I can also use this custom type.
[12:15] And so I could plug up some kind of texture
[12:17] to this custom type.
[12:18] So I'm just going to add back in that brick displacement.
[12:20] And let's just plug the image up to the texture.
[12:23] But if I turn up the edge breakup,
[12:24] now you can kind of start to see that brick pattern.
[12:26] And I also rendered the animation.
[12:28] So here is what the paint filter looks like
[12:30] when you render an animation.


### Rim 2d [12:31]
**Transcript (timestamped):**
[12:32] And the last one that I'll be going over in this video
[12:34] is the rim 2D.
[12:35] So I'll just drop the rim 2D here.
[12:37] So this here is the project files
[12:38] from my Mace Windows sculpt.
[12:40] I do have a time-lapse video if you want to check that out.
[12:42] Now this rim 2D is basically going to create
[12:44] like a colored outline on the edge of your object.
[12:47] Now this isn't going to work
[12:48] if you don't render it with a transparent background.
[12:50] So you need to make sure you have a transparent background
[12:53] and then render that out with the transparency
[12:55] and then it will put it on the edge.
[12:56] So now what I can do is change like the factor
[12:59] to make it more bright or less bright.
[13:00] And then I can also change the rim color.
[13:02] So I can just change that to maybe like a purple color.
[13:04] And now it kind of looks like a strong rim light.
[13:06] There's also the blend type if you want to change that.
[13:09] And then there's the lighting intensity
[13:10] so I can make it brighter.
[13:12] And if I do make it brighter now
[13:13] the bloom is kind of affecting it more.
[13:15] I can also blur it a little bit.
[13:16] So if I just blur it,
[13:17] it's not really going to blur this edge
[13:19] because that had the transparency
[13:20] but it's going to blur this edge here.
[13:22] Then there's also this light wrap
[13:24] and this is going to increase the spilling kind of
[13:26] along the edges.
[13:27] So it's kind of going to just pull out that edge.
[13:30] Then you can also transform it.
[13:31] So if you do want to move it around
[13:32] you can just change the offset.
[13:33] So I could just like drag it over to the side a little bit
[13:36] maybe drag it down.
[13:37] So I probably wouldn't use that often
[13:39] but for stylized rendering it could be pretty useful.


### Other Effects [13:41]
**Transcript (timestamped):**
[13:42] Now there's actually three other compositing effects
[13:44] which were added to Blender 5.2
[13:46] and that is the normal mask, the position mask
[13:50] and also the exposure visualization.
[13:53] Now I tried to look these up online.
[13:54] I went to the Blender manual and the documentation
[13:57] and tried to search for it.
[13:58] I even watched a bunch of videos on YouTube
[14:00] about the Blender 5.2 new features
[14:02] and no one seems to be talking about it.
[14:04] So if you guys know of any articles or videos
[14:06] or anything that explain these
[14:08] you can definitely let me know in the comments
[14:10] but I even looked in the Blender manual
[14:11] and usually the Blender manual has a page
[14:13] for pretty much everything in Blender
[14:15] but I couldn't find anything about this
[14:16] in the Blender 5.2 manual.


### Closing [14:18]
**Transcript (timestamped):**
[14:18] And if you are a beginner to compositing
[14:20] and you'd like to learn all the basics of compositing
[14:22] then I do have a compositing for beginners tutorial
[14:24] which you can check out.
[14:25] I also have a playlist where I post new Blender updates
[14:28] and feature videos.
[14:29] So you can also check that out right up here on the history.
[14:32] So if you found this helpful and thank you for watching.



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

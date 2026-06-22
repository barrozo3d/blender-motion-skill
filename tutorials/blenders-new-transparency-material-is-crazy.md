---
title: Blender's NEW Transparency Material is CRAZY!
source: YouTube
url: https://www.youtube.com/watch?v=U2I8YDrO5Jc
author: SouthernShotty
ingested: 2026-06-22
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blenders-new-transparency-material-is-crazy/
frame_count: 0
---

# Blender's NEW Transparency Material is CRAZY!

**Source:** [YouTube](https://www.youtube.com/watch?v=U2I8YDrO5Jc)
**Author:** SouthernShotty
**Duration:** 10m28s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### A Small Feature With Big Impact [0:00]
**Transcript:** Blender 5.2 adds an awesome new feature to the principal BSDF node called Thinwalls,  which makes certain types of transparent materials much easier to pull off.  It improves things like paper transparency, creating thin film-like materials like bubbles,  it makes it much easier for light passing through foliage to create more realistic environmental  renders, and it even fixes the infamous dark glass effect problem people have in Blender.  Where when you try and light through something like a glass window,  you will lose a ton of light energy in the glass itself will almost appear dark.  But the greatest part of all of this new feature is that not only does it approve everything  visually and make the process simpler, it also renders quicker.  So before we get started, I want to say thank you to the sponsor of this video, which is Storyblocks,  and let's dive in and get started. Now at the end of the video, I'm going to show you how to use  it to make this cool effect right here. But first we're going to go through some of the boring  settings and then I'm going to show it in some practical examples. If you're feeling impatient,  feel free to skip ahead to the end of the video. No...


### Getting Started [1:02]
**Transcript:** give you an idea of how the settings work with it. So here we have a simple scene. We have a plane  here with a sphere behind it and a sunlight pointing right at it. So if I turn this on in the  render mode, you can see that you can't see the light at all unless if I rotate around. So it's  snapping back here into front view. If I wanted to make this object transparent, let's say for example,  add some subdivision surface, I would turn the weight all the way up to one. However, you can see  we're not seeing our object at all. And that's because Blender currently struggles with doing one  sided planes for any type of transmissive values. So the solution in the past was to come over here  at a solidify modifier. And suddenly it would start behaving normally. However, the problem with this  is this gets a bit cumbersome to add solidify to everything. It also doubles your geometry  crown for any object you have the supply to. And in some instances, when you have very complex  objects, it might also become problematic and break the look of your object overall by having  things fight together in Z fight. But this is why the thin wall is so great. So I can kick off the  solidify modifier ...


### Understanding the Settings [2:46]
**Transcript:** setting here, which by default is set to zero. But if I set this all the way to negative one,  you'll notice that it disappears. And that's because it's determining what direction the thin wall  is projecting from. So since we have a light coming from this side over here, it's trying to  project from in here and not getting anything. So if I turn this all the way to one, it would instead  instead of splitting the difference, shift everything so that it detected all the light coming from  this side. Now this is subsurface scattering, but this also works on transmissions as well,  making it perfect for glass. So now that we understand how the settings work, let's go ahead and  take a look at some various materials we could apply it to. Let's take a minute to talk about our  sponsor story blocks, which has been a really great resource to the channel. And what makes story  blocks different is that it's 100% human-made stock media library built specifically for creators  by creators. It's all there to help you save time. For example, using these templates on this video  for CTA for my personal favorite, dragging in textures into blender to use for grunge maps or for  background images i...


### Thin Film Effects [4:53]
**Transcript:** create really thin films, for example, such as a bubble. So here you can see I have a glass sphere.  You're just sitting in front of a Suzanne. You can see how that is coming across as very thick  glass. It's viewing the entire object as one solid piece of glass. But if I check on thin wall here,  it's only going to take a look at the faces and render it that way instead. And now you can see how  we're getting a cool bubble effect. You could even make this a little bit better by adding a small  thin film on top of it and feeding some color into there. You can also pair this with other of  glass effects. For example, this iridescent glass shader that I have a tutorial for for some  pretty cool results. So next up here, I want to show how we can use this thin wall to get better  foliage renders. I downloaded this blender demo file from the website. The artist is listed


### Better Foliage Renders [5:40]
**Transcript:** over here. Now, the artist had a pretty complex leaf setup. I've simplified it down to here.  And I also want to point out that they've already double-sided the leaves. So if you zoom in on the  leaves, they have two sides to get kind of a better render with the default system. But let's take  look at the render that is output from this. So if I come over here, you can see that with the  normal render, we get much darker shaded leaves. And we're rendered at 26.3 seconds. If we come up  here, the only thing I did is check on thin wall. You see how much more light is naturally passing  through the leaves. And we saved over two seconds on render time. Now, if these leaves weren't  double-sided, we can end up saving even more render time. Now, two seconds may not seem like a lot,  but we are getting better results for less render time. And if you didn't double-side the leaves,  you could save even more render time. And then now imagine that you have a whole force to  trees in your scene. And that time can really stack up to be saving you minutes per frame. Let's


### The Glass Problem [6:35]
**Transcript:** take a look here at this famous classroom demo scene and how thin walls can be used to make better  windows and glass renders. So over here, we have a giant window. But the thing is there's actually  no glass there. Instead, there's just a giant emission plane. I can't be certain why the original  creator made it this way, but my assumption is that glass would just end up causing issues.  So let's turn on a big glass plane there. And you can see immediately how it starts to cut down  the lighting in the scene there. And this is Blender's infamous dark glass problem. So when you have  that one-sided glass and Blender, what it does is it ends up not calculating the light properly,  and it ends up eating way more light energy than it should. And as you can see here, it is  dramatically cutting down the lighting in the scene. However, with our new thin wall, we can come  over here, turn on thin wall, and you can see how we immediately gain that lighting back.  But still get some reflections in our windows that are now visible here. If I zoom in,  you can see that we're getting actual glass and reflections. Thin wall also works great for paper  rendering. And I was going to set up a pap...


### Creative Example [7:47]
**Transcript:** on paper renders. I'm going to show you how I kind of created that horror film look where it's  pressed up against a frosted glass. You can see here, I even have some simple animation on it as  well as the character comes in. First, I'm going to show you the geometry setup. It's just a simple  plane here with two pieces extruded. And then I applied a black material to those pieces just to  create a little bit of contrast. Back here, I just have a simple human model. And I just did this  really crappy shape key animation to make them look like they're coming in closer. But the lighting  setup, I have a few lights up front just to highlight the bump pattern on the plane. And then I have  a sunlight pointing at the back of our character and a area light too. The interesting thing is that  if you turn off the sunlight, you can actually get a really spooky looking kind of blurred out version  with just the area light. Since it's a big soft light, it ends up projecting soft strados.  So let's take a look at the material setup here. So I opted to use the transmission instead of  the subsurface because I was going for a glass look. And then all I did is import some grunge  textures, which ...


### Final Thoughts [10:19]
**Transcript:** interest. I'm really excited to see what the community creates with this thin wall material.  Let me know what you think about the tutorial in the comments below. I will be putting this project  file on my Patreon if you'd like to check it out.



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

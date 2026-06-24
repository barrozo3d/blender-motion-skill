---
title: Blender's NEW Transparency Material is CRAZY!
source: YouTube
url: https://www.youtube.com/watch?v=U2I8YDrO5Jc
author: SouthernShotty
ingested: 2026-06-23
blender_version: "5.2"
tags: [materials, shaders, rendering, lighting, glass, organic, intermediate, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/blenders-new-transparency-material-is-crazy/
frame_count: 8
---

# Blender's NEW Transparency Material is CRAZY!

**Source:** [YouTube](https://www.youtube.com/watch?v=U2I8YDrO5Jc)
**Author:** SouthernShotty
**Duration:** 10m28s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### A Small Feature With Big Impact [0:00]
**Transcript:** Blender 5.2 adds an awesome new feature to the principal BSDF node called Thinwalls,  which makes certain types of transparent materials much easier to pull off.  It improves things like paper transparency, creating thin film-like materials like bubbles,  it makes it much easier for light passing through foliage to create more realistic environmental  renders, and it even fixes the infamous dark glass effect problem people have in Blender.  Where when you try and light through something like a glass window,  you will lose a ton of light energy in the glass itself will almost appear dark.  But the greatest part of all of this new feature is that not only does it approve everything  visually and make the process simpler, it also renders quicker.  So before we get started, I want to say thank you to the sponsor of this video, which is Storyblocks,  and let's dive in and get started. Now at the end of the video, I'm going to show you how to use  it to make this cool effect right here. But first we're going to go through some of the boring  settings and then I'm going to show it in some practical examples. If you're feeling impatient,  feel free to skip ahead to the end of the video. Now before we dive into some of the cooler  visual examples, let's just show where the thin wall is and how to activate it. I'm also going to

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_000.jpg

### Getting Started [1:02]
**Transcript:** give you an idea of how the settings work with it. So here we have a simple scene. We have a plane  here with a sphere behind it and a sunlight pointing right at it. So if I turn this on in the  render mode, you can see that you can't see the light at all unless if I rotate around. So it's  snapping back here into front view. If I wanted to make this object transparent, let's say for example,  add some subdivision surface, I would turn the weight all the way up to one. However, you can see  we're not seeing our object at all. And that's because Blender currently struggles with doing one  sided planes for any type of transmissive values. So the solution in the past was to come over here  at a solidify modifier. And suddenly it would start behaving normally. However, the problem with this  is this gets a bit cumbersome to add solidify to everything. It also doubles your geometry  crown for any object you have the supply to. And in some instances, when you have very complex  objects, it might also become problematic and break the look of your object overall by having  things fight together in Z fight. But this is why the thin wall is so great. So I can kick off the  solidify modifier and just instead check on the thin wall option. And now we are seeing this as a  thin wall and our object is passing through. Now, you might be noticing that this doesn't look orange.  And that's because subsurface scattering is generally used for skin. So we have these default  radius values and scales here. And what this is doing is trying to determine what it's like when you  pass through something like wax or skin to offset the color slightly. Since we've checked on thin  wall, Blender now knows that we are not trying to create a big waxy or organic substance. And instead,  it just deletes this. So if you wanted that orange look, you would just go up here and manually add it  into the diffuse color. But let's look at the other settings down here too. Down here, we have this

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_001.jpg

### Understanding the Settings [2:46]
**Transcript:** setting here, which by default is set to zero. But if I set this all the way to negative one,  you'll notice that it disappears. And that's because it's determining what direction the thin wall  is projecting from. So since we have a light coming from this side over here, it's trying to  project from in here and not getting anything. So if I turn this all the way to one, it would instead  instead of splitting the difference, shift everything so that it detected all the light coming from  this side. Now this is subsurface scattering, but this also works on transmissions as well,  making it perfect for glass. So now that we understand how the settings work, let's go ahead and  take a look at some various materials we could apply it to. Let's take a minute to talk about our  sponsor story blocks, which has been a really great resource to the channel. And what makes story  blocks different is that it's 100% human-made stock media library built specifically for creators  by creators. It's all there to help you save time. For example, using these templates on this video  for CTA for my personal favorite, dragging in textures into blender to use for grunge maps or for  background images in fill. I also love that there's smoke and fire assets, which I can mix into my scene  for an easy effect. And there's a lot of other great content on the sides such as sound effects and  things, which I can use to mix into my videos and my animations. I also love that they have a good  selection of things like aerial shots, which is really nice to mix into your edits for your short  films to add a bit of a high budget look. There really is just a ton of variety and content on this  site that's incredibly useful no matter what project you're working on. I also really appreciate  how simple the licensing model is, making it super easy to know what you can and can't do with  the files that you've downloaded. It's also nice knowing that everything you're downloading is  supporting a real artist. It's also pre-licensed, meaning that you won't get flagged when you upload it  to channels like YouTube for copyright flags. Now, if you're a creator and you'd like to get access  to all this content, they're offering 15% off any annual plan for a limited time. And that  discount is only available through my link, which you will find here on the screen and down in the  description below. But that being said, let's dive back into the tutorial. It can also be used to

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_002.jpg

### Thin Film Effects [4:53]
**Transcript:** create really thin films, for example, such as a bubble. So here you can see I have a glass sphere.  You're just sitting in front of a Suzanne. You can see how that is coming across as very thick  glass. It's viewing the entire object as one solid piece of glass. But if I check on thin wall here,  it's only going to take a look at the faces and render it that way instead. And now you can see how  we're getting a cool bubble effect. You could even make this a little bit better by adding a small  thin film on top of it and feeding some color into there. You can also pair this with other of  glass effects. For example, this iridescent glass shader that I have a tutorial for for some  pretty cool results. So next up here, I want to show how we can use this thin wall to get better  foliage renders. I downloaded this blender demo file from the website. The artist is listed

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_003.jpg

### Better Foliage Renders [5:40]
**Transcript:** over here. Now, the artist had a pretty complex leaf setup. I've simplified it down to here.  And I also want to point out that they've already double-sided the leaves. So if you zoom in on the  leaves, they have two sides to get kind of a better render with the default system. But let's take  look at the render that is output from this. So if I come over here, you can see that with the  normal render, we get much darker shaded leaves. And we're rendered at 26.3 seconds. If we come up  here, the only thing I did is check on thin wall. You see how much more light is naturally passing  through the leaves. And we saved over two seconds on render time. Now, if these leaves weren't  double-sided, we can end up saving even more render time. Now, two seconds may not seem like a lot,  but we are getting better results for less render time. And if you didn't double-side the leaves,  you could save even more render time. And then now imagine that you have a whole force to  trees in your scene. And that time can really stack up to be saving you minutes per frame. Let's

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_004.jpg

### The Glass Problem [6:35]
**Transcript:** take a look here at this famous classroom demo scene and how thin walls can be used to make better  windows and glass renders. So over here, we have a giant window. But the thing is there's actually  no glass there. Instead, there's just a giant emission plane. I can't be certain why the original  creator made it this way, but my assumption is that glass would just end up causing issues.  So let's turn on a big glass plane there. And you can see immediately how it starts to cut down  the lighting in the scene there. And this is Blender's infamous dark glass problem. So when you have  that one-sided glass and Blender, what it does is it ends up not calculating the light properly,  and it ends up eating way more light energy than it should. And as you can see here, it is  dramatically cutting down the lighting in the scene. However, with our new thin wall, we can come  over here, turn on thin wall, and you can see how we immediately gain that lighting back.  But still get some reflections in our windows that are now visible here. If I zoom in,  you can see that we're getting actual glass and reflections. Thin wall also works great for paper  rendering. And I was going to set up a paper scene here, but Christopher 3D already made an awesome  video as well. And here he has this really cool receipt scene showing off how well thin wall works

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_005.jpg

### Creative Example [7:47]
**Transcript:** on paper renders. I'm going to show you how I kind of created that horror film look where it's  pressed up against a frosted glass. You can see here, I even have some simple animation on it as  well as the character comes in. First, I'm going to show you the geometry setup. It's just a simple  plane here with two pieces extruded. And then I applied a black material to those pieces just to  create a little bit of contrast. Back here, I just have a simple human model. And I just did this  really crappy shape key animation to make them look like they're coming in closer. But the lighting  setup, I have a few lights up front just to highlight the bump pattern on the plane. And then I have  a sunlight pointing at the back of our character and a area light too. The interesting thing is that  if you turn off the sunlight, you can actually get a really spooky looking kind of blurred out version  with just the area light. Since it's a big soft light, it ends up projecting soft strados.  So let's take a look at the material setup here. So I opted to use the transmission instead of  the subsurface because I was going for a glass look. And then all I did is import some grunge  textures, which you can do from great resources like story blocks and combine them together. So here,  I have one noise texture plugged into a color ramp. Now let's see what that looks like. You can  see how that's just a simple stretched out noise texture. Here, I have a bigger noise texture.  And then all I've done is multiply those on top of each other to create this simple base texture.  Then after that, what I did is take some simple grunge maps here and multiply them on top of this  tan color to give us a little bit of a look like that. And then I did a second grunge texture. You  can see how this one's kind of adding some scratches. I plugged those into a color ramp to make it  black and white. Multiply that on top of the base noise back here. And then I plugged all of that  into the roughness value for a bump normal here and a roughness as well. Then I took the original  color that I had up here, which was this nice warm color and plugged that into the base color.  Combined, that gives me this kind of blurry scratched out glass look. Then for my lights,  I just went ahead and added a tiny bit of color into each of these. You can see that the back  lights are actually a little bit warmer. And then for the front lights here, I tried to mix in  some pale colors, which ends up giving us a few splashes. So if I grab all three of these lights here  and hide those, you can see how much they're bringing the scene to life by creating a little bit of  bounce light on the bump map we have here and highlighting the roughness there. You can also see  that by adding a little bit of pale color here at the top, we just get a little bit more visual

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_006.jpg

### Final Thoughts [10:19]
**Transcript:** interest. I'm really excited to see what the community creates with this thin wall material.  Let me know what you think about the tutorial in the comments below. I will be putting this project  file on my Patreon if you'd like to check it out.

**Frame:** tutorials\frames\blenders-new-transparency-material-is-crazy\frame_007.jpg


---

## Structured Notes

### Core Technique
Blender 5.2's new **Thin Walls** option on the Principled BSDF — treats a single-sided mesh face as an infinitely thin shell for transmission/subsurface light transport, replacing the old Solidify-modifier workaround for one-sided transparent/translucent surfaces, fixing Blender's "dark glass" light-loss bug, and rendering faster.

### Summary
Explains why Blender previously needed a Solidify modifier on any one-sided plane used with transmissive/SSS materials (Blender couldn't correctly compute transmission through a single-sided face), and why that workaround was costly: doubled geometry, occasional Z-fighting on complex objects. Thin Wall (Principled BSDF) removes the need for Solidify entirely — toggling it on makes the renderer treat the face itself as a thin shell. With Thin Wall enabled, Subsurface Scattering's default skin-like radius/scale offset is automatically disabled (since "thin wall" implies you're not modeling a thick waxy/organic volume) — diffuse color must be added back manually if a tinted look is wanted. A direction parameter (default 0, range -1 to 1) controls which side of the thin shell the light is treated as entering from — works for both Subsurface and Transmission, important for matching the actual light direction in a scene. Demonstrated use cases: (1) bubble/thin-film glass — a "thick glass sphere" look becomes a true hollow bubble shell when Thin Wall is enabled, since Blender renders per-face rather than as one solid volume; combinable with iridescent glass shaders for extra realism. (2) Foliage — double-sided leaf geometry renders measurably faster (~2+ seconds saved in the demo) and noticeably brighter/more naturally backlit with Thin Wall on vs. off, with even more savings possible on non-double-sided leaves. (3) The classic "dark glass" bug — a one-sided glass plane in Blender's classroom demo scene visibly eats scene light when added normally; enabling Thin Wall restores correct light transmission while keeping visible reflections, fixing the long-standing one-sided-transmission light-loss problem. (4) Paper rendering (referenced via another creator's video, not demonstrated in depth here). (5) A creative "frosted glass horror" effect: a bump-mapped Transmission material (chosen over Subsurface for a glass rather than skin look) built from layered, multiplied Noise Textures and grunge-map textures (Color Ramp → multiply chains) feeding Roughness/Bump/Base Color, viewed through a plane with extruded black-material cutout shapes and a softly shape-keyed human figure behind it for a "pressed against frosted glass" silhouette effect; warm/cool colored area + sun lights add bounce-light interest on the bump pattern.

### Key Steps
1. Enable **Thin Wall** on the Principled BSDF (Subsurface or Transmission section) instead of adding a Solidify modifier to a one-sided plane/mesh that needs to transmit or scatter light.
2. Note Subsurface's default radius/scale skin-tint behavior disables automatically with Thin Wall on; re-add a tint manually via Diffuse/Base Color if wanted.
3. Tune the Thin Wall **direction** value (-1 to 1, default 0) to match which side of the surface your key light is actually coming from, for both Subsurface and Transmission use.
4. For bubble/thin-film glass: apply a standard glass material with Thin Wall enabled on a closed sphere — it renders as a hollow shell instead of solid glass; optionally layer a thin-film color pass on top, or combine with an iridescent glass shader.
5. For foliage: enable Thin Wall on leaf materials (works with or without double-sided leaf geometry) for both better light transmission look and faster render times.
6. For fixing dark/light-eating one-sided glass (e.g. windows modeled as a single plane): enable Thin Wall on the glass material to restore correct light transmission while preserving reflections.
7. Frosted-glass creative effect: use Transmission (not Subsurface) for a glass rather than organic look; build a grunge/scratch texture from 2+ Noise Textures (different scale/stretch) multiplied together as a base, then 1–2 grunge-map image textures multiplied on top (one through a Color Ramp for black/white scratch detail), feeding the combined result into Roughness, a Bump/Normal input, and tinting via Base Color; build foreground silhouette geometry (a plane with extruded, black-materialed cutout shapes) and a softly shape-key-animated figure behind the glass; light with a front area light (highlights the bump pattern) and a rear sunlight/area light (rim/silhouette on the figure), tinting front and back lights with slightly different pale/warm colors for visual interest and bounce light.

### Nodes / Settings
Principled BSDF: **Thin Wall** checkbox (Subsurface and Transmission sections), direction parameter (-1 to 1). Solidify modifier (the old workaround Thin Wall replaces). Shader Editor for the frosted-glass effect: Noise Texture (×2, different scale/stretch, multiplied together), Image Texture (grunge maps) → Color Ramp (for B/W scratch masks) → Mix/Multiply chains feeding Roughness, Bump/Normal, Base Color. Lighting: Sun light, Area lights (front + rear, tinted colors).

### Difficulty
Beginner to Intermediate — toggling Thin Wall itself is trivial, but building the layered grunge-texture frosted-glass material requires moderate Shader Editor fluency.

### Blender Version
5.2 (Thin Wall on the Principled BSDF is explicitly a new 5.2 feature).

### Tags
#materials #shaders #rendering #lighting #glass #organic #intermediate #blender-5x

---

## Related Tutorials
- `blender-new-cloth-simulator-changes-everything.md` — same author (SouthernShotty), similar "new Blender 5.x feature deep-dive" format
- `you-should-make-glass-animations-in-blender-51.md` — shares glass material territory

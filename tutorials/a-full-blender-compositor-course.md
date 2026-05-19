---
title: A FULL Blender Compositor Course!
source: YouTube
url: https://www.youtube.com/watch?v=_7N7emOvDko
author: SharpWind
ingested: 2026-05-19
blender_version: "4.5"
tags: [compositing, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/a-full-blender-compositor-course/
frame_count: 0
---

# A FULL Blender Compositor Course!

**Source:** [YouTube](https://www.youtube.com/watch?v=_7N7emOvDko)
**Author:** SharpWind
**Duration:** 42m19s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** What is the Blender Compositor?  In short, it's all of the post-processing you do after you've already rendered the image.  And it's all of these noodles that happen between this box and this box.  And today I'll show you how it all works.  How's it going? My name's Sharp and I'm making a library of all the content about everything Blender related so you can find it all in one place.  And today my Discord community has voted for the Blender Compositor.  If you like Blender, you're now legally obligated to subscribe.


### Theory & Setup [0:23]
**Transcript:** So Blender's Compositor is based on nodes, unlike some popular software that are based on layers.  And that's a good thing, because you can reuse nodes and wire them in any way you want and organize them better and layers are scoops!  Sorry, we'll use layers at work.  I reckon that if you want to learn how to use the Compositor, it's first best to learn how nodes work.  And I know that a lot of you guys know this already, but without a good foundation, all of your buildings collapse, so suck it up!  Since Compositoring usually comes at the end of the production, I'm gonna assume that you have an entire scene already set up.  If you don't, I've got plenty of tutorials on how to do that, shameless self-plug, or you can make something really simple.  Like this will be enough for the purpose of teaching you how to use the Compositor.  I'm gonna use this.  If you click on the Compositor tab up here, you'll get this interface with the timeline down below and the Compositor window up top.  To start Compositing, you'll click this Use Nodes box, which will give you these nodes.  We'll start with this node, which is our rendered image, so anything we got from hitting the Render button in our...


### Practical Compositing [5:49]
**Transcript:** What I'll usually do when I'm compositing is have a little setup like this.  It feels like much, but trust me, it's rather simple.  Conveying simple instruction in the form of nodes can sometimes look more complicated than it actually is,  but I'm here to teach you how to logic works so this is less scary.  So once again, we start with our rendered image, that's usually the base.  In the first step I like to do is adding some glare.  A glare usually takes the brightest parts of our image, then blurs them and then adds them onto the image.  And for this we have a simple glare node.  I'll just plop the Sonntima noodle when you can see all the effects.  In version 4.5 you have three outputs on the node.  One is the full image, one is only the glare, and one is only the highlighted parts which generate that glare.  You can use all of these different outputs for different compositing needs.  Here you can change the type of the glare and the quality.  Higher quality usually looks more realistic, but it computes slower.  In the highlight section you get to pick the threshold and the smoothness, and to show you this I'll switch to my highlights output.  The threshold determines how bright ...


### Render Layers [21:58]
**Transcript:** Starting first with render layers.  You can actually separate different parts of your scene  into completely different layers,  having disconnected from each other,  and then composite them together.  This is a very powerful tool,  and I've talked about it in my life footage CGI video,  but I'll recap it here very quickly.  In the top right corner here,  you can create or view different render layers.  And once you're inside one of those layers,  you can choose which of your collections  will be visible in it or not.  Let's make this make sense  by opening this little test scene.  We've got a glowing cylinder, a plastic monkey,  a metal ball, and a checkered floor.  Each of these elements are in their respective collection,  but I've also put the lights  in a separate collection as well.  I'll begin by renaming the current render layer  I'm in into scene.  This will include everything,  and it's like my main one.  Then I'll use this icon here,  where I can either make a completely new render layer,  make one that has the same settings as this one,  or create a completely blank one.  Let's make a completely new one  and call it floor.  You can see and select your layers in this drop...


### Render Passes [28:43]
**Transcript:** In our scene,  if we open the View Layer Properties panel  because we're in cycles,  we have all of this amazing data over here.  E-D also gives you some,  but cycles is much, much more advanced.  The ones up here include data,  where the combined pass is the final image  you always see whenever you render anything.  Here we also got our Mist Pass and ZPass,  which we've reduced before.  We know what these are now,  but you can also extract position,  normal and vector data,  and even UV data,  letting you re-texture things in compositing.  Yes, that is possible.  You can change the textures of things after the fact.  Compositing is powerful.  As well as grease-pansel data, denoising data,  even stuff like object or material index  so we can mask individual objects or materials.  Up here,  you can also exclude this layer from being rendered  or only rendered this layer.  And down here is what we're interested in right now.  These are your render passes that include light information.  You've got direct, indirect and color information  for the diffuse pass,  glossy pass, transmission pass,  the volume doesn't have the color info,  and finally you've got a mission,  environment light...


### Professional Setup [32:51]
**Transcript:** I was actually pretty happy when compositing with Voter  for this video because I'm a huge nerd  and that's basically what compositing is.  And now I get to unleash all that nerdness onto you guys.  So I'll just stick with the scene  that includes all the different render passes  so I can use it to its full potential.  So for this scene,  I won't be needing any render layers  because there's not too many things in here.  Plus there's not a profound foreground and background  that you want to be separated.  So everything is gonna be on one layer.  I also won't be needing any of the databases up here,  except maybe the denoiser pass  because I can still render less samples  and get away with that.  Yeah, let's check this one on.  And for the light passes,  we're gonna need almost all of them.  So diffuse direct indirect in color  because we have rough surfaces  and half rough surfaces in here.  Then glossy direct indirect in color passes  because we have reflective  and half reflective surfaces in here.  Transmission direct in direct in color  because we have transmissive surfaces.  You know, this thing volume direct and indirect  because there's no color,  but we still have a volume...



---

## Structured Notes

### Core Technique
Comprehensive Blender Compositor course: node fundamentals, Glare, color correction, Render Layers for scene separation, Render Passes for multi-pass compositing (diffuse/glossy/transmission/volume/emission separate), and a full professional multi-pass composite setup.

### Summary
42-minute full compositor course by SharpWind. Starts with compositor fundamentals (Use Nodes, Render Layers node, Composite/Viewer outputs), covers practical effects (Glare — Bloom, Streaks, Fog Glow), color correction nodes, Mist/Z-depth passes, Render Layers for separating scene elements, and culminates in a professional multi-pass composite using light passes (diffuse direct/indirect/color, glossy, transmission, volume, emission) for full control over every light contribution. Blender 4.5 Glare node has 3 outputs.

### Key Steps
1. **Setup** — open Compositor tab; tick Use Nodes; Render Layers node (source) + Composite node (destination) + Viewer node (preview)
2. **Basic Glare** — Shift+A → Glare node between Render Layers and Composite; Type: Bloom (Fog Glow / Streaks also available); Threshold = brightness cutoff; Smoothness; 3 outputs in B4.5: full image, glare only, highlights only
3. **Color Correction** — Hue Saturation Value, Bright/Contrast, Color Balance (lift/gamma/gain or slope/offset/power), Curves node
4. **Z-depth / Mist** — enable Mist pass in View Layer Properties; use in Compositor with Map Range + Mix nodes for depth of field or fog gradient
5. **Render Layers** — create multiple View Layers (top-right icon in 3D viewport); assign collections to be Visible or Indirect Only per layer; render all layers in one render; in Compositor: multiple Render Layers nodes, one per layer; composite together with Alpha Over
6. **Render Passes** — View Layer Properties → Passes: enable Diffuse Direct, Diffuse Indirect, Diffuse Color, Glossy Direct, Glossy Indirect, Glossy Color, Transmission Direct, Transmission Indirect, Volume Direct, Volume Indirect, Emission; each becomes a socket on the Render Layers node
7. **Multi-pass composite** — in Compositor: take Diffuse Direct + Diffuse Indirect → Add → Multiply by Diffuse Color → diffuse beauty; repeat for Glossy, Transmission; Add all beauty passes + Emission + Volume → final image; now adjust each light type independently
8. **Denoiser pass** — enable in View Layer → Denoising Data; plug into Denoise node in compositor; allows fewer render samples with denoising applied per pass

### Nodes / Settings
- Glare: Type Bloom (also Streaks, Fog Glow, Ghost); Quality High; Threshold 1.0; B4.5: 3 outputs
- Mist Pass: enable in View Layer → Passes → Data; pair with Map Range for fog effect
- Render Layers node: Image output = combined; additional sockets per enabled pass
- Multi-pass formula: `(DiffDirect + DiffIndirect) × DiffColor = diffuse beauty`
- Alpha Over: blends render layers with correct alpha; Z-Combine for depth-sorted layers
- Denoise node: Image input + Denoising Albedo + Denoising Normal → denoised output
- Blender 4.5: Glare node updated with new output sockets

### Difficulty
Intermediate

### Blender Version
4.5

### Tags
compositing, rendering, intermediate

---

## Related Tutorials
- [[add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2]] — multi-pass compositing in ACES workflow
- [[photorealistic-renders-in-blender]] — photorealism pipeline that ends in compositor finishing
- [[i-recreated-movie-scene-in-blender-nuke-complete-tutorial]] — professional VFX compositing pipeline

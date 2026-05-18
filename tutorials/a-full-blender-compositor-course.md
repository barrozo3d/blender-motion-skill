---
title: A FULL Blender Compositor Course!
source: YouTube
url: https://www.youtube.com/watch?v=_7N7emOvDko
author: SharpWind
ingested: 2026-05-18
blender_version: "4.5"
tags: ["compositing", "rendering", "materials", "shaders", "beginner", "intermediate"]
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
Complete Blender Compositor workflow from scratch — Use Nodes setup, glare, render layers for scene separation, and multi-pass compositing with diffuse/glossy/transmission/emission render passes for full professional control.

### Summary
SharpWind covers the full Blender Compositor pipeline in 42 minutes. Starts with node basics and the Use Nodes toggle, progresses through practical compositing (glare, blur, color grading), then covers render layers for compositing separate objects independently, and finally multi-pass rendering (diffuse/glossy/transmission/volume/emission passes) for maximum post-production control. Blender 4.5 node interface shown.

### Key Steps
1. Open **Compositor** tab → check **Use Nodes** → Render Result node + Composite node appear
2. Add **Node Wrangler** addon → Ctrl+Shift+Click any node to preview it with a Viewer node
3. Add **Glare node** after Render Result → Type: Fog Glow / Streaks / Ghosts; Quality: High; Threshold and Smoothness in Highlight section; Blender 4.5 has 3 outputs (full / glare only / highlights only)
4. Add **Render Layers**: top-right corner of viewport → new layer icon → rename → assign Collections to Visible/Hidden per layer → composite layers back together with Mix/Add nodes
5. Enable **Render Passes** in View Layer Properties → Data: Mist, Z; Light: Diffuse Direct/Indirect/Color, Glossy Direct/Indirect/Color, Transmission, Volume, Emission; Denoising
6. In Compositor: **Render Layers node** exposes all enabled passes as outputs → wire passes into separate correction chains → recombine with Add nodes
7. Professional setup: enable Denoiser pass → render at lower samples → denoise in compositor; separate Diffuse/Glossy for independent color correction
8. Use **Color Balance**, **Hue Saturation Value**, **Curves** nodes for per-pass grading

### Nodes / Settings
- Render Result node — the base rendered image input
- Composite node — final output; required for compositing to take effect
- Viewer node — Ctrl+Shift+Click via Node Wrangler for live preview
- Glare node — Type: Fog Glow / Streaks / Ghosts; Quality: High/Medium/Low; Threshold: 0.5–1.0; Blender 4.5: 3 separate outputs
- Render Layers node — exposes all enabled passes; one per render layer
- View Layer Properties — Light Passes: Diffuse Direct/Indirect/Color, Glossy D/I/C, Transmission D/I/C, Volume D/I, Emission; Denoising
- Mix node (Add mode) — recombines light passes into final image
- Color Balance node — per-pass color grading
- Curves node — contrast and color control per channel

### Difficulty
Beginner / Intermediate

### Blender Version
4.5

### Tags
#compositing #rendering #materials #shaders #beginner #intermediate

---

## Related Tutorials
[PENDING EXTRACTION]

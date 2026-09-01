---
title: 3 Easy steps to make Realistic Materials
source: YouTube
url: https://www.youtube.com/watch?v=hAWLqRpzK6I
author: Jamie Dunbar
ingested: 2026-07-18
blender_version: "Blender 5.0.0 -- observed in frame_000"
tags: [materials, shaders, procedural, rendering, cycles, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/3-easy-steps-to-make-realistic-materials/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 3 Easy steps to make Realistic Materials

**Source:** [YouTube](https://www.youtube.com/watch?v=hAWLqRpzK6I)
**Author:** Jamie Dunbar
**Duration:** 12m20s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### How materials tell a story [0:00]
**Transcript (timestamped):**
[0:00] Nothing in the real world is ever perfect.
[0:03] All objects have scratches, rust, dirt, and other imperfections.
[0:08] Over time, these imperfections build up in specific ways,
[0:11] and it's these imperfections that help tell a story.
[0:14] If you want your audience to immediately get a feel for the worlds that you're creating,
[0:19] the objects in your worlds need to reflect that story.
[0:23] In this video, I'll show you the three most common types of imperfections and how to create them,
[0:28] but all the objects in your renders can contribute to the story you're trying to tell.
[0:32] For this tutorial, I'm going to be using what's known as a shader ball.
[0:35] It's a unique type of 3D model that specifically has a lot of curved surfaces and bevel edges to test your materials on.
[0:42] This shader ball was designed by Tetsurin, but they've made it freely available,
[0:46] so you can download this model and the final material from my Gumro page.


### Base materials [0:50]
**Transcript (timestamped):**
[0:50] Link in the description.
[0:51] Let's start by setting up the base materials we'll be working with.
[0:54] For this tutorial, we'll keep it relatively simple and use a metal material as the base
[0:58] and put a coat of paint over the top of it.
[1:00] All of the procedural nodes that we'll create later will be used to chip away at the paint,
[1:04] revealing the metal underneath.
[1:06] But keep in mind that you can layer any number of materials over the top of each other
[1:09] to create even more complex results.
[1:12] Slide open a new window, change it to the shader editor,
[1:15] select the shader ball, and click New to create the first material node.
[1:19] Since I know we'll want a metal and paint material,
[1:22] we'll immediately duplicate this principled shader and move it up.
[1:25] The metal material will be very simple here, since we won't really see that much of it in the end.
[1:30] Just turn the metallic to one, lower the base color to a light grey,
[1:34] and adjust the roughness to suit.
[1:36] We'll see a little more of the paint material, so I want to add a little more variety in the color.


### Node Wrangler [1:40]
**Transcript (timestamped):**
[1:41] You'll notice a lot in this tutorial that I use a few keyboard shortcuts.
[1:44] These shortcuts come as part of the node wrinkle I add on,
[1:47] which for some reason still isn't enabled by default.
[1:50] If it's not already enabled, go to your Edit, Preferences menu,
[1:54] go to the Add-ons tab and search for Node,
[1:57] and make sure that the node wrangler add-on is enabled.
[2:00] You can now use the shortcut Control Shift and left-click on a node to preview it in the viewport.
[2:05] Add a Noise texture, a Color ramp, and a Mix Color node.
[2:09] Plug the Noise into the Color ramp and the Color ramp into the factor of the Mix node.
[2:14] So you can see the results really clearly.
[2:16] I'm going to add two wildly different colors into the A and B slots.
[2:20] If we preview this, you can see that we're getting both of these colors mixing together randomly.
[2:24] You can adjust both the Noise texture and the Color ramp to suit your material now.
[2:29] Personally, I always push the black and white values on the ramp closer together to create more contrast,
[2:34] and increase the scale, detail, and roughness of the Noise texture.
[2:38] Odds are, you don't actually want these two colors to be this extreme,
[2:41] so I'm going to go with an orange color and make one slightly lighter and the other slightly darker.
[2:46] If you connect the Mix Color into your Material base color,
[2:49] you'll now see that the Paint layer has a bit of variation,
[2:52] which adds a nice healthy dose of realism to your objects.
[2:55] Adjust the roughness to determine what kind of paint this is.
[2:58] Lower the roughness if you want shiny paint.
[3:00] In my case, I know that the metal underneath is going to be quite shiny,
[3:03] so I'm going to go with a more matte finish to the paint to add some additional contrast.
[3:08] We can now add a Mixed Shader and connect both the paint and metal materials to it.
[3:12] Using the Factor allows us to slide back and forth between them,
[3:15] but what we really want is to add some imperfection details into this Factor
[3:19] so that we can make it look like the paint is being chipped away by nature.
[3:22] The edges of objects can take quite a beating. They get dropped, bumped, chipped,
[3:27] and over time, all of these imperfections building to what's known as Edgeware.
[3:31] Now, trying to hand paint every single edge on an object could be an overwhelming task.
[3:36] Fortunately, Blender has some building tools to help us create these procedurally,
[3:40] so you'll only ever need to create this setup once to be able to reuse it over and over again.


### Edge wear [3:45]
**Transcript (timestamped):**
[3:45] There's a few different setups that can create Edgeware,
[3:47] and sometimes one method will give better results depending on the model.
[3:51] If you're using cycles, you'll be able to use any of these methods.
[3:54] If you're using EV, the Bevel node and the Pointiness nodes won't work.
[3:58] I'll be using cycles in this video, so I can show all of them to you,
[4:01] but just keep in mind that you'll want to use the Ambient Occlusion method if you're using EV.
[4:06] For this model, the Bevel node setup has given me the best results, so let's set one up.
[4:10] Create two Bevel nodes, a Mixed Color, and a Color Ram.
[4:14] Plug the two Bevel nodes into the Mix node and the Mix into the Ram.
[4:18] Set the Mix node to Difference and set the Factor to 1.
[4:21] Set the Ram to Constant and drag the white value almost all the way back to the black.
[4:26] The Position value should be really low, something around 0.01.
[4:30] This setup works by comparing the two Bevel nodes and finding the difference between them.
[4:34] So set the lower Bevel node radius to 0 and the top one to a very small value, something like 0.002 gives me good results.
[4:42] This is a great start, but the edges are extremely clean.
[4:45] We want to roughen them up a bit so the damage looks a lot more random.
[4:49] Create a Noise texture and another Color Ram.
[4:51] Get used to creating Color Ramps. We're going to be making a lot of them.
[4:54] You can mix the Bevel setup and the Noise together using a Mixed Color node,
[4:58] making sure to set it to Multiply and cranking the Factor all the way up.
[5:01] Turn up the Scale, Detail and Roughness on the Noise texture and plug it into the Color Ram.
[5:06] I like to add a bit more contrast so I'll drag both the black and white values more towards the centre of the Ram.
[5:11] Feel free to adjust the Noise and Color Ramps to determine just how much you want to eat away at these edges.
[5:16] If we plug this Mixed node into the Factor on the Mixed Shader,
[5:19] we can now see that our final shader is starting to take shape,
[5:22] with the paint looking like it's being chipped away to the reveal the metal underneath.
[5:26] Feel free to experiment with both the Ambient Occlusion and the Pointiness setups as well.
[5:30] I found that the Bevel setup works really well for objects with lots of sharp edges.
[5:34] The Ambient Occlusion works better for surfaces with more curves,
[5:38] and the Pointiness setup is best suited for organic models such as high polysculps.
[5:42] I often use this method to extract extra details such as scales or wrinkles.
[5:47] And of course you can mix any of these together to create even more complex results.
[5:51] But to keep it simple, I'm going to stick with the Bevel setup for this tutorial.


### Scratches [5:55]
**Transcript (timestamped):**
[5:56] The Edgeware is looking really nice, but now I want to break up these larger surfaces.
[6:00] These larger areas are more exposed than the tight little edges,
[6:03] and as such they're more likely to have other objects drag across them.
[6:07] So let's add some procedural scratches to simulate this.
[6:10] Creating a cracked surface is really easy to do in Blender.
[6:13] Just create a Veronai texture, and set the second drop down to Distance to Edge.
[6:18] I'm also going to add some mapping nodes to the Vector, which will help us in a moment.
[6:23] The shortcut to add these is Control-T.
[6:25] Use the Object slot, which gives us a few more cracks to play with.
[6:29] In this case I want our cracks to be white to mix back into our Edgeware later,
[6:32] so it creates a color ramp, flip the colors, and drag the black value back down really low,
[6:37] something around 0.01.
[6:39] This looks good, but there's a lot of cracks.
[6:42] We want to mask away some of these so that we're left with only a handful.
[6:46] The best way I found to do this is to duplicate the Veronai texture,
[6:49] and set the type back to the default, which is F1.
[6:53] Because the Veronais are using the same scale, and therefore a very similar mathematical model,
[6:58] this second Veronai is a kind of smoothed out version of our cracks.
[7:02] If you add another color ramp and crush the values closer together,
[7:05] you can really see how the cracks line up to the smoothed version of our circular shapes.
[7:10] If we now take both of these ramps and multiply them together with a mixed color node,
[7:14] we can use the second texture to slowly cut out some of our cracks, and they'll align perfectly.
[7:19] Now to make sure that both of these Veronais stay in sync,
[7:22] it may be worth adding a simple value node and plugging it into both scale slots,
[7:26] set the value to somewhere around 10.
[7:28] Finally, as good as these cracks are looking, I'd like to add a little more randomness to their shape.
[7:33] We can do this by plugging just about any random value into the mapping node.
[7:37] In this case I'm going to use a Musgrave texture and plug the height into either the location,
[7:41] or the rotation, either we'll work, as it's just kind of adding some randomness into the equation.
[7:46] If you want even more randomness, you can plug it into both.
[7:49] We now have some nice scratches which we can mix back into the edgeware from earlier,
[7:53] so add another mixed node and set it to add to combine these masks.
[7:57] Plug this new mask into the factor on the mixed shader to see both the edgeware and the cracks.
[8:02] Now if your cracks are a little difficult to see, you can go back and adjust the color ramps to make them a little thicker.
[8:07] I've also found this is a really good time to add a bump node, as this really helps bring out the cracks.
[8:12] So add a bump node and plug the edgeware and cracks mix into the height of the bump,
[8:17] and the normal into the normal of the metal material.
[8:20] On a bump node, the white values make the surface look raised, while the black values push it into the surface.
[8:25] Now at the moment that means that our cracks are actually pushing up,
[8:28] so hit the invert button on the bump node to flip this and push the cracks and edgeware down into the surface.
[8:35] You can then adjust the strength to determine how deep you want the scratches to be, around .2 seems to be a good value here.


### Random damage [8:40]
**Transcript (timestamped):**
[8:41] This is all looking great, but I want to add one last layer of completely random damage across everything.
[8:47] This is really simple after everything else that we've done.
[8:50] Just create a noise texture and add a color ramp, plug them together and adjust the settings for some random black and white values.
[8:56] Add a final mixed node set to add and join this random noise with the edgeware and scratches that we've already created.
[9:03] Plug this final value into the mix shader as well as the bump and see the final results come to life.
[9:09] That finishes off our procedural metal material with edgeware, scratches and random damage,
[9:14] but there's one last procedural trick that I'd like to leave you with.
[9:17] Let's add some dirt to this sucker.
[9:20] Before adding dirt, let's quickly clean up this mess of nodes a little bit using some frames.
[9:24] I'll create a frame for the edgeware, the cracks, the damage and the color setups.
[9:30] Grab all the nodes and drag them into the frame.
[9:33] The frame will automatically resize to fit all the nodes.
[9:36] You can also name these frames and increase the label size to make them easier to read.
[9:40] There, that's much easier to understand.


### Dirt [9:42]
**Transcript (timestamped):**
[9:43] I want the dirt to start at the bottom of the model, almost as if it's been sitting on the ground accumulating gunk,
[9:48] then slowly fade out as we get higher and higher up the model.
[9:52] For this, we'll want to use a gradient texture.
[9:55] Add a texture coordinates and a mapping node using the control T shortcut and set the coordinates to object.
[10:01] Keep in mind that this setting relies on the values in your objects transforms,
[10:05] so make sure that your model is in the center of the world and apply the transforms to ensure all these values are set back to default.
[10:11] This should give you a nice gradient going straight through the middle of your model.
[10:14] But it's rotated the wrong way, so let's flip that around using the y rotation on the mapping node.
[10:19] Set this to negative 90.
[10:21] You can then use the x location to move the gradient up and down the object.
[10:26] As per usual, I want to create a color ramp at the end of this setup to further control the contrast.
[10:31] I'm going to set this to constant and bring the white value down.
[10:34] This is great, we've now got a dirt line that we can play with, but I want to roughen it up and randomize it a bit.
[10:40] So create another noise texture with a color ramp and join them together and adjust both to your liking.
[10:46] What I really want now is to find a way of blending between the objects mapping here and this new randomness that we've created.
[10:52] So create another mix node and plug the color ramp into the top and the mapping node into the bottom.
[10:57] Set the mix node to add and crank the factor all the way up.
[11:00] We'll then plug this random mapping back into the gradient texture, which will still give us that dirt line, but it's now roughened up.
[11:07] Let's put this hole set up into its own frame labelled dirt.
[11:11] We can now use this new mask that we've created to layer a new color on top of our paint material.
[11:17] Duplicate the mix color node with the original paint colors and plug the old colors into the top slot and add a brown color to the bottom slot.
[11:24] And then we can use our new mask as the factor.
[11:27] This will add dirt colors on top of the paint.
[11:29] And to add to the effect, we can plug this dirt mask into a bump node and plug that into the normal slot of our paint material.
[11:36] This will raise the dirt layer slightly, making it look like the dirt is on top.
[11:41] And this here is our final shader.
[11:43] Don't forget that you can download this model and the procedural material from my Gumroad page.
[11:48] Now feel free to try your new material out on a bunch of different objects and take joy in knowing that, because it's a procedural material, you'll never have to hand paint these imperfections again.
[11:58] As I mentioned earlier, some of these nodes, such as the pointiness node or the bevel nodes, don't work in EV.
[12:04] However, you can bake them out into texture images, which does allow EV to render them.
[12:08] So, if you'd like to learn how to do that, jump on over to this next video.



---

## Captured Frames

- [2:20] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_000.jpg
- [4:26] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_001.jpg
- [5:19] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_002.jpg
- [6:53] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_003.jpg
- [7:14] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_004.jpg
- [8:30] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_005.jpg
- [10:31] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_006.jpg
- [11:27] tutorials/frames/3-easy-steps-to-make-realistic-materials/frame_007.jpg

---

## Structured Notes

### Core Technique
Fully procedural wear shader — paint over metal chipped away by three stacked masks (bevel-difference edge wear, masked Voronoi scratches, noise damage) plus a gradient-based dirt layer, built once and reusable on any model.

### Summary
Jamie Dunbar builds a story-telling material on a shader ball (Tetsurin's free model). Two Principled BSDFs (shiny grey metal; matte orange paint with Noise→ColorRamp→Mix color variation) are combined with a Mix Shader whose factor is a procedural imperfection mask. Edge wear = difference of two Bevel nodes (radius 0 vs 0.002) through a Constant ramp at ~0.01, roughened by multiplying a contrasty noise. Scratches = Voronoi Distance-to-Edge masked by a duplicate Voronoi F1 (same scale via a shared Value node ≈10) with a Musgrave feeding the Mapping for randomness. Random damage = noise + ramp. All masks Add-combined into the Mix Shader factor and an inverted Bump (strength ~0.2) on the metal. Dirt = object-space Gradient Texture (Y-rot −90) roughened by adding noise into the mapping, layered as a brown tint over the paint colors with its own bump. Bevel/Pointiness don't work in EEVEE — use the AO method or bake to textures.

### Key Steps
1. Base: duplicate Principled BSDF — metal (Metallic 1, light grey, roughness to taste) + paint (matte). Paint color variation: `Noise Texture` → `Color Ramp` (push stops together for contrast) → `Mix Color` factor between two orange tones → Base Color.
2. Combine with `Mix Shader`; the whole tutorial builds its Factor mask. (Node Wrangler: Ctrl+Shift+click previews any node.)
3. **Edge wear (Bevel method)**: two `Bevel` nodes → `Mix Color (Difference, Fac 1)` → `Color Ramp (Constant, white pos ≈0.01)`. Bevel radii: 0 and 0.002. Roughen: `Noise` (high scale/detail/roughness) → `Color Ramp` → `Mix Color (Multiply, Fac 1)` with the bevel mask.
4. Method choice: Bevel = sharp-edged hard surface; **Ambient Occlusion = the EEVEE-safe option** and curved surfaces; Pointiness = organic sculpts (also good for extracting scales/wrinkles). Mixable.
5. **Scratches**: `Voronoi` → Distance to Edge → `Color Ramp` (flipped, black ≈0.01, white cracks); duplicate Voronoi set to F1 + crushed `Color Ramp` as a mask; `Mix Color (Multiply)` — the F1 cells cut out cracks that align perfectly. Shared `Value` (≈10) → both Voronoi scales. Randomize: `Musgrave` height → Mapping location and/or rotation (Ctrl+T for mapping chain, Object coords).
6. Combine: `Mix Color (Add)` edge wear + scratches → Mix Shader factor; `Bump` node — mask into Height, **Invert on** (cracks push in), Strength ≈0.2 → metal's Normal.
7. **Random damage**: `Noise` + `Color Ramp` → `Mix Color (Add)` with the rest → factor + bump.
8. Organize in named Frames (edge wear / cracks / damage / color).
9. **Dirt**: Ctrl+T mapping on `Gradient Texture`, coords **Object** (center object + apply transforms first!), Mapping Y-rotation −90, X-location slides the dirt line; `Color Ramp (Constant)`. Roughen: noise+ramp `Mix (Add, Fac 1)` into the *mapping vector* feeding the gradient. Use as factor of a duplicated paint-color Mix with a brown tone, plus its own `Bump` into the paint's Normal (dirt sits on top).
10. EEVEE: bake Bevel/Pointiness masks to image textures.

### Nodes / Settings
- `Bevel` ×2 (0 / 0.002) + `Mix (Difference)` + `Color Ramp (Constant, 0.01)` — edge wear
- `Voronoi (Distance to Edge)` + `Voronoi (F1)` mask, shared `Value` scale ≈10, `Musgrave` → Mapping — scratches
- `Bump` — Invert, Strength 0.2, masks into Height
- `Gradient Texture` + Object coords + Mapping (rot Y −90) — dirt line
- `Mix Color` modes used: Difference, Multiply, Add; `Mix Shader` for material blend
- Node Wrangler: Ctrl+Shift+click preview, Ctrl+T mapping
- Cycles-only: Bevel, Pointiness; EEVEE-safe: AO (or bake)

### Difficulty
Intermediate

### Blender Version
Not specified — modern UI; Cycles required for the Bevel/Pointiness methods (AO or baking for EEVEE).

### Tags
#materials #shaders #procedural #rendering #cycles #intermediate

---

## Related Tutorials
- [Perfect Textures in Blender - Works Every Time](perfect-textures-in-blender---works-every-time.md) — image-based counterpart of the same wear philosophy (AO edge wear, environment blending)
- [Doing Surface Imperfections Right | Vray, Cycles, Arnold](doing-surface-imperfections-right-vray-cycles-arnold.md) — shares #materials #shaders; roughness-map realism
- [The Easiest Way to Texture in Blender (Adaptive, No UV Unwrapping)](the-easiest-way-to-texture-in-blender-adaptive-no-uv-unwrapping.md) — shares #materials; PBR quick setup

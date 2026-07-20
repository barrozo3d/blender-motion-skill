---
title: Blender 5.2 Health Potion Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=NrK9FjcNBJA
author: Polygon Runway
ingested: 2026-07-20
blender_version: "5.2"
tags: [materials, shaders, procedural, glass, product-viz, lighting, hdri, compositing, rendering, cycles, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-52-health-potion-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender 5.2 Health Potion Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=NrK9FjcNBJA)
**Author:** Polygon Runway
**Duration:** 18m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's create this fantasy health potion scene and look at some of the cool features of Blender 5.2.
[0:06] And if you just started Blender and you need some help with the tutorials,
[0:09] also check out my free starter course. The link is in the description. You just sign up on my
[0:13] website. It's 100% free. It takes 1 to 2 hours to complete and then you will have so much easier
[0:19] time going forward. And with the new Blender scene open, let's just select the light and the cube
[0:23] here. Press X delete and I'll start with the shape for potion. So let's appreciate
[0:28] and let's create a cylinder. Now let's tap into the remote and let's press S then shift Z to
[0:33] scale it down a little bit like this. So we lock the Z axis out and do something like that.
[0:40] Now let's also make this a little bit smaller. Let's look from the front by pressing 1 on an
[0:45] iPad and now press S to scale it down and I'm looking around like 10 to 20 cm just like this.
[0:53] You can see the squares right here and if you tap out and press N for the side panel, you can see
[0:58] the size right here on the Z axis. And also to note, I scaled it in the edit mode. So the scale is
[1:03] one. This is really important to maintain. Now let's zoom in a little bit and let's tap into the
[1:09] edit mode. Alt click the bottom loop and let's press Ctrl B to battle and let's increase
[1:16] number of cuts to something more smooth and let's press C so we don't overlap this and it's
[1:22] nicely clamped at the bottom. And finally here let's select everything at the top press X
[1:26] and delete faces. Press Ctrl R to create a loop right here and one more here where we can scale this
[1:34] down. Finally, Alt click this, make it a little bit larger. Okay, this looks fine. So before we do
[1:39] anything else, let's look from the front and let's prepare some of the other geometry. So this is
[1:43] the file right here. Now we'll need the liquid. So we'll just reuse some of the geometry. Let me
[1:49] collapse the side panel and enable X-ray view and just select everything here. Press Shift D to
[1:54] duplicate and just right click to release it and press P and separate the selection that was
[1:58] separated into a new object. So let's tap out, let's call this liquid. And finally, let's create a
[2:04] cork. So we can just reuse some of the geometry here. So tap into the remote, Alt click this
[2:10] press Shift D and as to make it smaller. And now press P and enter to separate this as well.
[2:16] Let's select this edge tab in and let's look from the front. We can just select all press G
[2:21] and Z and move it down here. Let's make it smaller, press F to fill and E to extrude.
[2:28] And let's scale it up a little bit like this. And finally, we can push this up. So we can make
[2:33] this angle a little bit sharper here like something like this and maybe push the whole thing up
[2:40] tiny bit. Okay, now let's tap out and let's select the liquid here. We can call this the cork.
[2:46] Now with the liquid, I want to close this up. So tap into the remote, select this, make it a little
[2:52] bit lower. So G and Z and press F to fill. And let's press Ctrl B to bevel. And let's create
[2:58] bevel like this and we can reduce the number of cuts with the mouse wheel to something like this.
[3:03] And just so it's better shaded, let's press Ctrl R and increase the number of cuts to create
[3:08] some more geometry there. And you can now tap out and let's add some subdivision.
[3:16] I think one level will be fine right click. Shade this smooth and now select this one here.
[3:22] And let's tap into the remote. Let's create a few more cuts here as well.
[3:28] And finally one more near the top. And now let's add a solidify.
[3:35] And we'll need to go and we'll need to go outside here.
[3:38] Just like this. And now let's add that subdivision surface again.
[3:46] Right click and shade smooth. And finally select this one, add some bevel. So we have some
[3:51] supporting loops. Increase number of segments. And let's reduce the amount. Something really
[3:56] small like 0.002. And add that subdivision and shade smooth. Now if we talk about the x-ray
[4:04] back, this is basically what we have here. Now we can make this a little bit larger.
[4:08] So it better touches the sides there. Finally let's select everything, hold shift,
[4:13] select the file, press Ctrl P and parent. So we can move this as one object. And let's look from
[4:18] the front, press G, then Z and move it up here. And let's press shift A and add a plane that will
[4:24] serve as a background for us. And finally one more thing I want to reuse some of this geometry
[4:28] to create the label. So let's select the file, tap into the remote. Let's toggle x-ray again.
[4:34] Let's look from the side here. And we'll just select a few of these faces like that.
[4:40] You can see it goes to the other side because we are in the x-ray. And now let's just press shift D
[4:45] to duplicate right click to least P and separate. And now if you type out, let's just select this.
[4:50] Let's call this label. And I will remove the solidify of course here. Tapping to the edit mode.
[4:57] Select all and press Alt S to make this larger. So it wraps around like this. Looks okay. And now
[5:03] I will use the shrink wrap modifier. So let's type out. Let's toggle the x-ray and let's go ahead
[5:08] and add the shrink wrap modifier. It's in the form category right here. And let's just pick the file.
[5:17] And we need to set some offsets. Something really really small. So 0.001 should be enough.
[5:24] Maybe it's even too large. So 0.01. Okay. Just a little bit of that offset. And finally,
[5:33] if this radius looks too sharp, we can add few supporting loops with control R right here in the
[5:39] edit mode. If you're busy and you want to learn as quickly as possible with steady progression,
[5:44] also check out my other courses where you will learn everything from simple,
[5:47] locally designed all the way to full character illustration, textured environments,
[5:51] and with the latest one full car modeling and animation. So if you're interested,
[5:55] please check out the link in the description. And let's now take care of the materials. So let's
[5:59] expand this and let's use the UV editor. And finally, let's make this larger. And let's switch
[6:07] this to shader editor. And in the render settings, let's switch to cycles. All enable GPU and the
[6:13] noisy and switch my render the noisy to GPU and reduce the samples. Now if you preview this,
[6:20] this will be too dark. So let's pershift A and let's add an area light, press G, then Z and move
[6:26] it up here. We can make it a little bit smaller and let's push this higher and let's reduce the
[6:32] strength. This will be like a main fill light. There'll be enough for now. And now let's select the
[6:39] vial and in the materials, let's create a new one. Let's call this glass. And let's just increase
[6:46] the transmission all the way to one. And let's make this a little bit brighter here. And let's
[6:53] reduce the roughness. Of course, the roughness is never uniform like this. And if you want to make
[6:58] this look a little bit better here in the shader editor, just pershift A, search for noise.
[7:04] And you can hold control shift and click this to preview. If you have the node Wrangler add-on
[7:09] active, you just go to preferences and search for Wrangler in the add-ons and activate it by
[7:15] clicking checkbox. And right here, this is a little bit too stretched. So we can press control T.
[7:20] Again, this will work only if you have the Wrangler on and switch these to object mapping just
[7:25] like that. And finally, we can play with the scale. And we can pershift A and search for amp at the
[7:33] color ramp and compress this a little bit to make nice smudges. And we can of course increase the
[7:40] detail. So it looks like this. Finally, let's flip this. I want this part to be dark because
[7:48] that will be glossy. And this should be just a tiny bit brighter to give this a little bit more
[7:55] roughness. And if you now plug this to the roughness. And here to the surface, let's unplug the
[8:02] metallic. It's not visible right now and there is some artifacts here, but that's because the
[8:07] liquid object right here in the vial is the same size. So we can tap into the remote.
[8:14] Now let's toggle the exterior so we can see what's happening there. And we can press old S and
[8:19] just a tiny bit make it smaller. So it doesn't overlap there. Now if you select this and look from
[8:26] the bottom where there's some reflection, you can now adjust the roughness. You can see how
[8:34] there will be a little bit of that rough surface here and there. And that's exactly what we'll give,
[8:40] you know, the glass a little bit of character. And now let's select this part right here and let's
[8:45] just give this some color for now. We can leave it like this. And let's select the liquid here.
[8:52] And let's give it a glass material and duplicate it here. Let's call this liquid.
[8:58] And here we can just remove all of this setup and leave the roughness at zero.
[9:03] But let's change the IOR2133. And finally let's change the color to something red or whatever color
[9:13] you want to pick. And now let's select the label and we can take advantage of some of the new
[9:18] asset libraries in Blender. If you go here and switch this to asset browser for a second
[9:24] and here you can pick the essentials which are libraries that come shipped with Blender currently.
[9:30] They're not downloaded yet. So if you, for example, check the materials. You can see some of them
[9:35] have this cloud icon that means that you can download them and use them. And there's a super
[9:40] cool paper texture that you can just drag and drop here. It's not very visible here. And there's
[9:46] another issue you cannot do anything here, you know, adjust the roughness or anything. But if you go
[9:52] here, you can see there's this library icon. So you need to click that so you unpack this and attach
[9:58] it from the S library. And now if you select the paper note, you can tab it and then you will
[10:04] see the true setup of the texture. But again, as you can see, you cannot do anything. But if you now
[10:10] tab out and select that group here on the side, if you don't have it here, hit N. You can see there's
[10:17] another icon like this. So you can click it. And now if you go inside, you can change whatever you
[10:22] want here. This of course wasn't really necessary, but I wanted to show you how you can work with some
[10:26] of these materials. And there's one new important setting here in the Principles shader in Bender
[10:31] 5.2. And that's the tin wall. If you uncheck it, you will see this behaves normally. Let's actually
[10:37] uncheck the scene lights and scene world for a second. So it's a little bit brighter. You can see
[10:42] this is the material. And if you tab out now, you can adjust the wrinkles and the bumpiness of it.
[10:50] And of course, the roughness, which is really, really cool and finally, some color. So let's make
[10:58] it brighter. And I think the bumpiness doesn't need to be so strong. And finally, if you tab in, let's
[11:06] keep this enabled because it will be really important. Now, I will show you the difference. If you now
[11:11] pre-shift A and add a light, let's add a point light, press Gdn Z and move it towards the middle of the
[11:16] vial. Let's now enable scene lights and world back. You'll see this is what you get. I get this
[11:23] nicely lit liquid inside, which is exactly what I want to do. So I'll hold shift and select the
[11:30] vial, press Ctrl P and parent. And now, of course, the roughness is visible a little bit better. So
[11:34] let's maybe reduce it a little bit like this. And also, let's make the vial a little bit darker.
[11:42] So it's not so transparent like this. And finally, you can see what the tin wall does with the light
[11:49] behind. If I go back here and disable this, this is basically a solid object. And now with the
[11:55] tin wall, it has, it's like natural translucent sea without ever touching the transmission here.
[12:01] So very cool feature. I really like this. And I will definitely play with this a little bit more.
[12:06] There are already tons of great examples out there. And now we can add some AGRI. So we have the
[12:12] world section here in the essentials. And we can, for example, choose the forest and just drop it
[12:17] into the scene to have some nice lighting. Of course, this is a little bit too strong. So in the
[12:21] shader editor, let's switch to world. And again, we'll need to detach this from the data. And now we
[12:28] can do something like 0.1. So it's just a nice subtle lighting that will give us great reflections
[12:37] on the glass there. Finally, let's add some texture to the ground as well. Because they will give
[12:42] us the full information how the light will actually behave. Because right now this is white. And there's
[12:47] a lot of reflected light. So you can either choose something from the materials here, something like
[12:53] tiles or whatever you want. I have the polyhaven library here and I have my favorite wooden texture.
[13:01] Already picked. And it's the rough wood right here. It looks really great. It has a lot of
[13:05] character. And here with the polyhaven add-on, I can fix the texture scale. So it's nicely mapped
[13:13] to the scale of my scene. And finally, we can better see how this will look and how the light is
[13:19] actually reflecting in our scene. And let's now switch this to UV editor. Select the label tab
[13:25] into the edit mode. And right here, I'll go back to the object. And I will attach this texture
[13:30] into the description. And you can then just grab it here and drop it into the scene. And first,
[13:37] let's just connect it here. So we better see how it looks. And now tab into the edit mode and we'll
[13:42] unwrap this. So, pursue an unwrapped angle based. As you can see, it doesn't fit. So we'll need to press
[13:49] R and 90 degrees here. And let's scale it down a little bit and scale on the ZXs. Okay, maybe we can
[13:58] even make it a little bit larger. So it better fits inside. And now let's just multiply this over
[14:06] the color. So I'll push it A, add a mix color now. So search for mix, mix color, drop it here. I'll
[14:13] unplug this so I can choose this color right here. Press Ctrl C. I'll plug this right here and
[14:20] Ctrl V, the color right there. And plug this back. And now I will switch the mix to multiply.
[14:27] And you can play with the factor if you want to make this a little bit more faded. And maybe
[14:31] let's go a little bit brighter like this. And finally, let's select the point light. And we can
[14:38] play with the color. We can give this, you know, like a Scarlet color. So it works a little bit
[14:43] better with the theme. And we can also reduce the strength tiny bit. But yeah, there's your potion.
[14:50] Finally, let's check our scene. We additionally need to parent the label. So I'll parent it to the
[14:56] vial and just drop it on the ground here like this. Then of course, you can just right click,
[15:04] select your archi and Alt D to duplicate the whole thing to the side like this. Rotate it.
[15:14] But from this one, I will remove the point light. Now you can see how nicely looks the paper.
[15:20] And how different it is when you have the light there with the tin wall. And when there is no
[15:26] light coming from behind. So let's select this again. I will select your archi, Alt D to duplicate and
[15:34] just rotate it somewhere here. And maybe just create an overlap like this. Okay, let me look from
[15:41] the side. Okay, let's hit zero on an umpette for a camera view. Let's select the camera. Press G
[15:49] then Z twice to go closer. And I'll press N, enable camera to view and just use my viewport controls
[15:59] to position this. We can collapse the UV editor. Okay, I really like it. And finally, let's duplicate
[16:13] this light, press Shift D and bring it lower. Like this, let's make it smaller and just move it
[16:20] back here. So we create a little bit of that backlight here. And of course, let's make it much
[16:26] weaker. And if you don't want to render everything here, press Ctrl B and just limit the render
[16:33] bounds. And finally, let's switch this to compositor and enable compositing. Let's set it to always.
[16:41] And let's create a new compositing node. And finally, let's push A and we'll add a bloom. So let's
[16:47] search for bloom. Drop it right here. And let's play with the strength. We can do something like five
[16:53] here and adjust the threshold like this. And of course, there are these cool presets here that you
[17:02] can use. Some of them are new. You can see they are actually in that cloud essentials library.
[17:09] So you can play around with these different nodes. I really like the aberration, which will kind
[17:15] of give this distortion. But I really like to go soft on this. And we need is another one that's super
[17:23] useful. But again, don't go too crazy with it. Finally, let's look at the camera and enable depth of
[17:30] field. Just the focus distance. So we actually see our objects. They're really close. So we'll need to
[17:38] go something like this. If you really want to see just enable limits here. And then you can adjust
[17:44] the cross until it kind of crosses through the label there. Something like this. And finally,
[17:51] in the render settings, color management, you can switch the transformation, play with the exposure
[17:58] and gamma to get more cinematic look. Maybe play with the curves a little bit.
[18:09] Okay. Maybe 1.3. Oh, yeah, I like this one. Quite a lot. So does the quick help ocean scene in
[18:19] Bender 5.2. And I really hope you liked it. And YouTube says a lot of you who watch are not
[18:24] subscribed. So please, if you want me to keep making these hit that subscribe, it will really help me.
[18:29] Thank you so much for watching and have a wonderful day.



---

## Captured Frames

- [0:22] tutorials/frames/blender-52-health-potion-tutorial/frame_000.jpg
- [1:09] tutorials/frames/blender-52-health-potion-tutorial/frame_001.jpg
- [6:39] tutorials/frames/blender-52-health-potion-tutorial/frame_002.jpg
- [7:33] tutorials/frames/blender-52-health-potion-tutorial/frame_003.jpg
- [9:03] tutorials/frames/blender-52-health-potion-tutorial/frame_004.jpg
- [11:16] tutorials/frames/blender-52-health-potion-tutorial/frame_005.jpg
- [16:47] tutorials/frames/blender-52-health-potion-tutorial/frame_006.jpg
- [18:09] tutorials/frames/blender-52-health-potion-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Full small-prop scene build in Blender 5.2: hard-surface glass-bottle modeling from a single cylinder, procedural smudged glass/liquid shaders, the new Thin Wall Principled BSDF option for backlit translucency, essentials asset-library materials/HDRIs, and a compositor finishing pass (Bloom, DOF, color curves).

### Summary
Polygon Runway builds a fantasy "health potion" vial start-to-finish: modeling the bottle, liquid, cork, and label from one duplicated cylinder base; shading glass and red liquid with noise-driven roughness variation; using Blender 5.2's new Thin Wall BSDF setting to get a naturally translucent label/paper look and backlit liquid glow from an internal point light; texturing the ground and label with essentials/Polyhaven assets; and finishing with Bloom, depth of field, and color-curve grading in the compositor.

### Key Steps
1. **Base shape**: delete default cube, add a Cylinder, scale down (S, Shift+Z to lock Z), scale again in front ortho view to ~10-20cm; note the mesh scale must stay at 1 (scale applied in Edit Mode, not Object Mode).
2. **Bevel + cleanup**: Alt-click bottom edge loop, Ctrl+B to bevel with more segments, delete top faces, Ctrl+R to add loop cuts, scale down the neck opening.
3. **Duplicate-and-separate workflow**: reuse the same cylinder geometry via Shift+D (duplicate) + P (separate) to derive the liquid, the cork, and later the paper label from the vial mesh — rather than modeling each from scratch.
4. **Cork**: from a duplicated slice, extrude (E), fill (F), bevel, and push/shape into a stopper; parent everything with Ctrl+P once positioned.
5. **Liquid + vial mesh cleanup**: fill top with F, bevel, add Ctrl+R support loops, Subdivision Surface modifier (1 level) + Shade Smooth, then Solidify on the vial with a small Bevel (~0.002) and another Subdivision Surface.
6. **Glass shader**: Cycles render, Transmission = 1, low Roughness driven by a Noise Texture → Mapping (Object coords, Ctrl+T Node Wrangler to auto-wire) → Color Ramp (compressed/inverted for smudges) into Roughness — never a flat roughness value for realistic glass.
7. **Liquid shader**: duplicate the glass material, zero out roughness, set IOR ≈ 2.133, change Base Color to red (or desired liquid color).
8. **Label material & Thin Wall**: apply an Essentials-library paper material (unpack via the library/"make local" icon to edit params), then use the new Blender 5.2 **Thin Wall** checkbox on the Principled BSDF for one-sided translucency without a Solidify modifier — demoed by toggling it with scene lights off/on to show wrinkle/bump/roughness/color response.
9. **Interior backlight**: add a Point Light inside the vial (parented to it) to sell backlit liquid glow through the Thin Wall label/vial; reduce vial roughness slightly and darken it so it isn't too transparent.
10. **Environment**: drop an Essentials-library "Forest" world HDRI, detach from library data, reduce strength (~0.1) for subtle reflections; add a Polyhaven wood-plank ground texture with fixed UV scale via the Polyhaven add-on.
11. **Label UV + tint**: UV-unwrap the label (Angle Based), rotate/scale to fit, then Mix Color (Multiply) the paper texture over a chosen tint color, feeding the result into Base Color.
12. **Duplication + camera**: parent label to vial, use Alt+D (linked duplicate) to place a second/third bottle, rotate for composition, switch to camera view (Numpad 0) with "camera to view" for framing; limit render bounds with Ctrl+B while iterating.
13. **Compositor finishing**: enable "Use Nodes" compositing, add a Bloom node (Strength ≈5, tuned Threshold; check the essentials cloud presets), enable camera Depth of Field with a Focus Distance dialed to the label, and grade in Color Management via a Curves adjustment (~1.3 contrast lift) for a cinematic look.

### Nodes / Settings
- **Shader Editor (Glass):** Principled BSDF — Transmission 1.0, Metallic unplugged, Roughness ← Color Ramp ← Mapping (Object) ← Noise Texture (Ctrl+T auto-wire via Node Wrangler add-on).
- **Shader Editor (Liquid):** Principled BSDF — Roughness 0, IOR 2.133, Base Color = red.
- **Shader Editor (Label):** Essentials paper material (unpacked/local) + Principled BSDF **Thin Wall** enabled; Mix Color node set to Multiply blending the paper texture with a picked tint color, feeding Base Color.
- **World Shader:** Essentials "Forest" HDRI, Strength ≈ 0.1, detached from library data.
- **Modifiers:** Bevel, Subdivision Surface (1 level) + Shade Smooth, Solidify (vial shell).
- **Lights:** one Area Light as main fill (lowered strength), one Point Light inside the vial (parented) for interior backlight/glow, later duplicated and dimmed for rim/backlight on the ground composition.
- **Compositor:** Use Nodes → Bloom (Strength ≈5, custom Threshold, essentials presets available incl. Aberration), Camera Depth of Field (Focus Distance targeting the label).
- **Color Management:** Curves node, gamma/exposure tweak, ~1.3 contrast adjustment for cinematic grade.
- **Render:** Cycles, GPU + OptiX/GPU denoising enabled, reduced sample count.

### Difficulty
Intermediate

### Blender Version
Blender 5.2 (Thin Wall Principled BSDF option, Essentials asset library are 5.2-specific features)

### Tags
materials, shaders, procedural, glass, product-viz, lighting, hdri, compositing, rendering, cycles, thin-wall, blender-5x, intermediate

---

## Related Tutorials
- [THIN WALL, the incredible new Principled BSDF feature in Blender 5.2](thin-wall-the-incredible-new-principled-bsdf-feature-in-blender-52.md) — deep dive on the same Thin Wall BSDF feature used here for the label/liquid translucency.
- [Blender's NEW Transparency Material is CRAZY!](blenders-new-transparency-material-is-crazy.md) — more Thin Wall use cases (bubbles, foliage, frosted glass).
- [Realistic Product Lighting In Blender](realistic-product-lighting-in-blender.md) — glass product lighting techniques (Area Lights, emission planes) applicable to the vial/liquid shading here.
- [Brand New Material Assets in Blender 5.2 LTS](brand-new-material-assets-in-blender-52-lts.md) — same Essentials asset-library material workflow used for the paper label.
- [Photoreal Skies In Blender 5.0](photoreal-skies-in-blender-50.md) — HDRI + world-strength lighting approach similar to the Forest HDRI setup here.

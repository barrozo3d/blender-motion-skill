---
title: My New Favorite Lighting Trick in Blender!
source: YouTube
url: https://www.youtube.com/watch?v=1-Cj4mtdCMc
author: Curtis Holt
ingested: 2026-06-25
blender_version: "Blender 4.x"
tags: [lighting, cycles, vfx, technique, emission, ray-visibility, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/my-new-favorite-lighting-trick-in-blender/
frame_count: 0
---

# My New Favorite Lighting Trick in Blender!

**Source:** [YouTube](https://www.youtube.com/watch?v=1-Cj4mtdCMc)
**Author:** Curtis Holt
**Duration:** 8m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Alright, everyone. I've got something pretty cool to show you. So, as a part of my new animated production I'm working on, called Project Fold, of which the production files are available on Patreon. I have recently just done some new lighting tests, relating to laser-like lighting. So, just showing you some animation tests here on the screen now. You can see we're like lines of inconsistent laser-like passing over an object. Some of the laser-like has bleed away from the actual main line, whereas other parts don't actually have bleed, they're actually just blocking light. It's a really interesting technique. It's something that I've sort of come up with myself. I know that a lot of people have done laser lighting and blender with a variety of methods. Some using area lights, some using the new kind of raycast projection. I'm doing a more physical way of doing it, where it's literally just intersecting objects with the statue in this case, which is a CC0 model from No-3D or AT on Sketchfab. I know that before I explain it, I will get people asking, why didn't you use this method? Why didn't you use this method? Because that always happens whenever I share a technique that I'm playing with. Someone always goes, hey, it would be easier if you did it this way. It might just be easy to show you. So, okay, this file is available on my Patreon for the Silver Tier members under the June 2026 production files badge. You see that it's animated. So, we've got a camera, we can watch it happen. And if you look in the viewport, you'll be able to see what's happening here. We have intersecting objects with the statue. There are other things moving in the scene. There's basically a pivot object, which has different light objects and the camera attached to it. And we can see how it changes as it progresses. Okay, so there's a couple of extra light objects on top and there's a volume cube as well, which just helps to diffuse the lighting in the space. That's what gives it that cinematic look. If you look back in the camera, there's a bit of light diffusion again in the background there. And there's also some bloom, just keeping it that bit of an ethereal look. So, the laser light objects themselves, if I go to laser objects in the collection, if I select one like, let's do laser blue to open side. Now, if I move my face, you'll see down in the viewport, it's actually an extremely thin cube. Inside of that cube is a another cube. It's going to be quite hard to show if I actually show it on the viewport, because it's so thin. So, let's go all for graphic quickly. So, there's an outer shell to the cube, and then there's an inner shell. And the inner shell has a misive light kind of bouncing inside of itself inwards. And the outer shell is just a casing to prevent light from leaving. Although in the case of this blue object, the side panel has been removed from the cube, which is what allows it to bleed light downwards, but we can see the effect of the inner shell being the stronger line along the top there. Okay? So, there's a bit of tricky setup going on with it, but that's basically the principle. Now, other objects like the red one do not have the side open, so the red light is not bleeding outwards from the side of it. If I was to remove one of these side faces, it would look like this. Let me see if we get the red light bleeding. So, creatively, I'm choosing to leave it. Now, in terms of like ray visibility, every ray visibility option is disabled, except for diffuse. You can optionally add glossy or volume scanner if you want it for creative effect. I'm leaving them off. Now, however, since the object is not visible to the camera, it is still physically present, which means it is visible to the other light sources in the scene. Now, this is slightly problematic if I want it to blend the light bleeding together. So, this is actually just a side effect of how the path tracing works in cycles, but I thought I could use it for creative effect. So, we've got the blue light bleeding down, then we've got the red laser object, which is also blocking the blue light bleed. So, it's almost acting like a subtractive laser source, which is removing the light bleed. Do you see that there? Now, this is a really kind of tricky and finicky method of lighting, but when I saw this, I thought, you know what? Kind of unique. I like it. So, you can get this really oddly specific lighting thing here, where I've got a second blue laser source, which is pointing downwards in the body, then I've got the red blocking the upper blue light source. So, you can almost get these areas of subtractive light, and we can control exactly how the boundaries look. Now, the reason why I'm interested in this method, rather than a different method of doing laser lighting, is because there are some very specific things I want to explore in regards to hiding information in light. Now, I don't know if I'll actually, you know, probably use this for my animated shorts, but it may be a bit easier to visualize here. Right, so I've got a sphere, and I've got one of these light sources. So, again, it looks like a plane, but it's not. It's a cube that's being flattened to a very thin whip, and the whip is the equivalent of the kind of thickness of that laser line you want to put on an object. Like I said, there's an inside hull as well. So, the inside cube is looking inward, so it's projecting light inwards, and the outside one is to block the light. Now, here's a representation of what we could see on the inside shape. So, notice here, it may be difficult to see. This is the red line providing the laser light around the sphere. Again, if I remove one of the side panels, the light will bleed out, so we can also see that there. So, we effectively have a procedural noise pattern being applied to the laser light object. So, the interesting thing about this is in theory, you know, we can move this back and forth on the object through the inside side, and we're taking little bits of that noise data and using it as intersecting light on the object. Now, this is not the same material, but for example, you can see that I can change the noise presence there. So, if I did the equivalent on the red one, you can see that I can make more of it or less of it present. Or if there's less present, then I could, you know, change the scale of the noise texture to make it a bit more noisy around the edge. So, you understand the principle here. What it's actually doing is the major planes inside of that, the very thin cube, are projecting this noise texture. So, as they intersect with an object, you're getting like the light rim lighting up the surface on that object. Now, what this allows for is something quite interesting, let me put the face back on. So, I could do like multiple layers of the laser around an object. And again, depending on the thickness of the object, you'll be getting like slightly different slice positions of that texture. Well, let's say, for example, that some of the objects are loud for light to bleed out of them, but some didn't, you could get something like this. So, you can have some of that texture projecting, and then it stops, and then some projects, and then it stops, and then you could animate that. So, something is like passing through those light phases. Now, I'm just showing a noise texture here, but you could replace that with anything, for example, codified information, and if you're creative of it, and again, the actual material of the object, you're projecting the lion, will affect this, then you could have specific patterns or information presenting on the object that's facing through the light. So, it's a really kind of oddly specific way of doing a laser-type lighting, but I find it way interesting. And going further than this, we're using planes here, but you don't have to. So, imagine like overlapping shapes of outside holes, that have an inside hole, with the emissive lighting in them, and then those shapes pass through other objects. And so, in this way, it becomes interesting, because you could almost think about it like a high-dimensional shape projecting light information onto a lower-dimensional shape, right? Interesting. Something that'll be a little bit tricky to do with just area lights or just shader recasting. So, it's a bit non-traditional, but it's just something I'm experimenting with. And like I said, this file is available on the Patreon. Production file was June 2026. You're looking for the file 8 laser shapes.plend. The 8, by the way, is just an indicator, like an ID on my computer. It doesn't actually mean there are eight objects in there. It's just a numerical way of me categorizing experiments. So, more things would be added, like, if more production files get made throughout June. So, again, silver team members, that's about $5. You can also sign up to free to the Patreon to get informed of monthly updates for what I'm doing. And all of my other products are available on here for the $10 tier, except for a couple of generators, I think, so I need to be collected and added. So, yeah, I just thought you might find that technique interesting. Again, we can just have a quick look at a low-rayer's animation here of it. So, again, you can imagine that as the light is scanning over the object, at the moment it's just a noise pattern, but we could actually give it any kind of visual input, which informs how the highlights will form around an object. So, while it's being used here artistically, you could use it very specifically on specific shapes of objects to get certain information across visually. And I just think that looks really cool. So, yeah, hopefully you found that interesting. Have a great day, and I'll see you next time.



---

## Structured Notes

### Core Technique
Physical "laser slice" lighting using extremely thin cubes: each laser object is a flattened cube with an inner emissive shell (faces pointing inward) and an outer blocking shell; where the object intersects scene geometry it projects rim light with the pattern of the emissive material — subtractive effect created by solid outer shells blocking bleed from other lasers.

### Summary
Curtis Holt (Project Fold) demonstrates a physical laser-style lighting method that avoids area lights or shader raycasting. Each laser object is two nested geometry pieces: (1) an inner cube with faces pointing inward, carrying an emissive material that can include any noise/procedural texture; (2) an outer cube with all faces intact to trap the light inside. Where the thin object physically intersects scene geometry in Cycles path tracing, the emissive material creates a rim-light effect along the intersection line. The intersection "slices" a cross-section of the noise texture, so as the laser moves through an object it samples different 2D slices of the 3D noise → produces animated light information. Removing one side face from the outer cube allows light to bleed downward. Ray visibility: all disabled except Diffuse (invisible to camera but still casts light). A second laser with fully intact outer shell can BLOCK the bleed from the first laser, creating subtractive areas. Volume cube adds diffusion/atmosphere. Production file available on Patreon (file 8 laser shapes.blend, June 2026).

### Key Steps
1. **Create thin cube:** Add cube → scale to very thin slab (matches desired laser line thickness). This is the laser object.
2. **Add inner hull:** Duplicate cube slightly smaller, flip normals so faces point inward. Assign Emission material with emissive pattern (noise texture, procedural, or solid color).
3. **Outer hull material:** Assign solid material to outer cube. Leave all faces intact to block light escape. Only normals-outward (standard).
4. **Light bleed option:** In Edit Mode, delete one side face from outer cube → light bleeds out that open side.
5. **Ray visibility:** Object Properties → Visibility → Ray Visibility → uncheck Camera, Shadow, everything EXCEPT Diffuse. Object is invisible to camera but emits light physically.
6. **Subtractive effect:** A second laser object with intact outer shell (no open face) blocks light bleed from another laser → creates dark bands in the bleed area.
7. **Emissive material with noise:** In inner cube shader — Noise Texture (any scale) → mix into Emission Color or Emission Strength. As laser intersects the mesh, Cycles path tracing projects the 2D cross-section of that 3D noise onto the surface.
8. **Volume atmosphere:** Add a volume cube (Volume Scatter shader, very low density) in scene for diffusion and atmosphere.
9. **Compositing:** Add Bloom/Glare for ethereal look.
10. **Animate:** Move/rotate the laser objects across the scene. The intersection line tracks the surface automatically.

### Nodes / Settings
- Inner cube: normals flipped (Alt+N → Flip), Emission material, emissive texture = Noise/Procedural
- Outer cube: standard normals, opaque material (acts as light blocker)
- Remove side face: Edit Mode → select face → X → Face delete = creates bleed opening
- Ray Visibility: Camera OFF, Shadow OFF, Diffuse ON (only). Optional: Glossy ON or Volume Scatter ON for creative bleed
- Volume cube: Volume Scatter (density ~0.01) for scene atmosphere
- Cycles path tracing required (physical light intersection)
- Bloom: compositor Glare node

### Difficulty
Intermediate — conceptually unique; setup is relatively simple but the physics interaction requires Cycles and understanding of ray visibility

### Blender Version
Blender 4.x (standard Cycles + ray visibility setup)

### Tags
#lighting #cycles #vfx #technique #emission #ray-visibility #intermediate

---

## Related Tutorials
- `fundamentals-of-lighting-in-blender.md` — core Cycles lighting theory
- `how-i-made-realistic-storm-clouds-in-blender.md` — Light Linking for isolating lights
- `how-to-make-cyberpunk-scenes-in-blender.md` — neon/emissive lighting setups
- `tutorial-how-to-make-a-volumetric-projector-in-blender-45.md` — volumetric light projection companion

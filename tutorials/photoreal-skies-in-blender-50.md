---
title: Photoreal Skies In Blender 5.0
source: YouTube
url: https://www.youtube.com/watch?v=nXubB9krxVI
author: Extra 3d
ingested: 2026-07-18
blender_version: "Blender 5.0"
tags: [lighting, hdri, volume, materials, shaders, rendering, blender-5x, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/photoreal-skies-in-blender-50/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Photoreal Skies In Blender 5.0

**Source:** [YouTube](https://www.youtube.com/watch?v=nXubB9krxVI)
**Author:** Extra 3d
**Duration:** 5m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Have you ever had this problem where you're setting up a scene? Everything looks good, but
[0:21] the background just feels dead? You want something cinematic, especially for an evening
[0:25] or night shot, but you can't use volumetrics because that's going to increase render time
[0:30] and slow everything down. And at the same time, you can't even use the traditional method
[0:35] of adding a 2D image on a plane because the camera is animated and the illusion completely
[0:40] breaks the moment the camera starts moving. I ran into this exact issue while working
[0:45] on this scene, and after trying a bunch of different methods, I found a really simple
[0:49] solution that looks realistic, works perfectly with camera animation, and doesn't affect
[0:54] your render time. And the best part is, it's completely free. So stick around because
[0:59] this is going to save you a lot of time in your future projects.
[1:03] Let's start with the evening shot. So this shot is pretty dark and it really needs something
[1:07] beautiful in the background. The default sky texture is just not enough, and honestly
[1:12] my laptop will divorce me if I use volumetric clouds. So I started looking for better
[1:17] options, and that's when I realised that we can just use HDRIs. Now before you say you
[1:22] already know about it, wait there is more to it. The problem with using high dynamic range
[1:27] images is that almost all of them have buildings, trees or some kind of obstacles. And second
[1:33] of all, these do a very bad job at lighting your scene. But I have figured it out, and to
[1:38] solve the first problem, we are just going to use skies with no obstacles, which are basically
[1:43] called pure skies. Now Polyhaven gives some pure sky options, which are great, but after
[1:48] doing a bit more research, I found this amazing collection of pure skies that are completely
[1:52] free. The link is in description. Head over to the HDRI section and add those in the
[1:58] cart that you like. When done, just check out. Download it, and then in Blender, open the
[2:04] Shader Editor and switch to the World tab. Select the background node, press Control plus
[2:10] T, and load your HDRI. Just make sure no triangular is enabled for this to work. Otherwise
[2:16] you'll have to set it up manually. Once that's done, you'll instantly get a really nice
[2:21] and clean background. You can also use the pure skies that Polyhaven provides. Just
[2:26] download the HDR format and choose a higher quality than 8K resolution.
[2:34] There are also HDR eyes that can work for the night time if you keep the strength low.
[2:38] I've already made a complete video on outdoor lighting in Blender, so you can check that
[2:43] out as well. By the way, the ocean you're seeing here is from this video, and all of my
[2:47] project files are available on my Patreon, so definitely check it out.
[2:52] Now for the other scene, I used a daytime HDRI. The only issue with that is, it doesn't
[2:57] like the scene very well on its own. Like most of you guys, I ended up using a sunlight
[3:02] to do the heavy lifting. If you already have a daytime setup with the Sky Texture, and
[3:06] you want to light the scene with that while showing the HDRI in the background, the first
[3:11] thing you need to do is make sure the sun rotation of the Sky Texture matches the HDRI direction.
[3:17] After that, you can mix them using a Mix Shader. Add a light path node and connect the
[3:21] camera ray into the factor. If you get the other way around, just switch the sockets.
[3:26] Obviously, you're not going to get perfect lighting right away, but here are a few tips
[3:30] that really help. First, make sure to use volume metrics. Add a cube and scale it so it properly
[3:37] covers your entire scene. Go into the Shader Editor, add a principled volume shader, and
[3:42] plug it into the volume socket. Keep the density very low and increase the anisotropy to
[3:48] around 0.7. This alone adds a lot of depth. The second tip is to use light blocking. Unlike
[3:56] lighting a product or a character where we can easily control which areas the light affects,
[4:01] outdoor scenes are a bit different because light comes from all directions. And the first
[4:06] rule of lighting is to make sure the light doesn't come from the back of the camera. To
[4:10] reduce that, we can use light blocking. Just add a big plane, rotate it, and place it behind
[4:15] the camera. Create a dark, diffuse material for it, with max roughness. If it gets annoying
[4:21] or visible, go to the object data properties. Under visibility, uncheck camera, and change
[4:27] the viewport display to bounds. The third tip is to use cloud shadows. You can do this
[4:33] in a similar way by placing a big plane between the sun and your scene. But this time go
[4:38] into the shader editor and create a basic material. Add a noise texture with a colour ramp
[4:43] and plug that into the alpha. Play around with it until you get something interesting. These
[4:49] are the settings that worked best for this scene. By the way, as a new year gift, this
[4:54] entire project file is completely free on my Patreon, so definitely grab it. And if you
[4:59] want to support the channel you can get the membership, which gives you access to almost
[5:03] all of my project files. Links are in the description. I also use this fake fog technique
[5:09] that I talked about in another video. It adds an extra sense of depth and atmosphere.
[5:14] It's basically just an emission shader plugged into the volume socket, with a bluish colour
[5:19] and very low strength. And finally in the compositing stage, I use the cinematic compositor,
[5:27] which is going to get an update very soon to keep an eye out for that as well. Link is
[5:31] in the description.



---

## Captured Frames

- [2:10] tutorials/frames/photoreal-skies-in-blender-50/frame_000.jpg
- [2:21] tutorials/frames/photoreal-skies-in-blender-50/frame_001.jpg
- [3:17] tutorials/frames/photoreal-skies-in-blender-50/frame_002.jpg
- [3:42] tutorials/frames/photoreal-skies-in-blender-50/frame_003.jpg
- [4:15] tutorials/frames/photoreal-skies-in-blender-50/frame_004.jpg
- [4:43] tutorials/frames/photoreal-skies-in-blender-50/frame_005.jpg

---

## Structured Notes

### Core Technique
Cinematic, animation-safe sky backgrounds without volumetric render cost: pure-sky HDRIs for the backdrop, mixed with a Sky Texture for lighting via a Light Path (camera ray) Mix Shader, plus cheap depth tricks (thin volume cube, light-blocking plane, cloud-shadow plane, fake emission fog).

### Summary
Extra 3d solves the "dead background" problem for animated cameras in Blender 5.0. Regular HDRIs contain buildings/trees and light scenes poorly, so use **pure skies** (Polyhaven's pure-sky HDRs at >8K, or the linked free collection). For daytime: keep the Sky Texture as the light source (match its Sun Rotation to the HDRI direction) and show the HDRI only to the camera by mixing World shaders with a `Light Path → Is Camera Ray` factor. Depth tips: a scene-covering cube with near-zero-density Principled Volume at anisotropy ~0.7; a dark max-roughness plane behind the camera as a light blocker (camera visibility off, viewport display Bounds); a noise-texture-alpha plane between sun and scene for cloud shadows; and "fake fog" — an Emission shader (bluish, very low strength) in the volume socket.

### Key Steps
1. Get pure-sky HDRIs (no obstacles): Polyhaven pure skies (HDR format, >8K) or the free collection linked in the description.
2. World setup: Shader Editor → World tab → select Background node → **Ctrl+T** (Node Wrangler) → load HDRI.
3. Evening shots: pure sky alone works; night: keep HDRI strength low.
4. Daytime with Sky Texture lighting: match Sky Texture **Sun Rotation** to the HDRI's sun direction (demo: Sun Size 0.545°, Sun Elevation 36°, Sun Rotation 185°, Sun Disc + Multiple Scattering on, low strength ~0.1) → `Mix Shader` between Sky Texture background and HDRI background, factor = `Light Path` **Is Camera Ray** (swap sockets if inverted): camera sees HDRI, lighting comes from Sky Texture.
5. Depth: cube covering the scene → `Principled Volume` into Volume socket, very low density, **Anisotropy ≈ 0.7**.
6. Light block: big plane behind the camera, dark diffuse, max roughness; Object Data → Visibility → uncheck Camera; Viewport Display → Bounds.
7. Cloud shadows: big plane between sun and scene; `Noise Texture` → `Color Ramp` → Alpha of a basic material.
8. Fake fog: `Emission` shader (bluish, very low strength) into the Volume socket.
9. Composite with a cinematic compositor setup.

### Nodes / Settings
- World: `Background` × 2 + `Mix Shader` + `Light Path (Is Camera Ray)`
- `Sky Texture` — Sun Size 0.545°, Elevation 36°, Rotation 185° (match HDRI), Sun Disc, Multiple Scattering, Strength 0.1
- `Principled Volume` — density ≈ 0, Anisotropy 0.7 (cube)
- `Emission` → Volume socket (fake fog, bluish, low strength)
- `Noise Texture` + `Color Ramp` → Alpha (cloud-shadow plane)
- Object visibility: Camera off, display as Bounds
- Node Wrangler Ctrl+T; Polyhaven pure skies >8K HDR

### Difficulty
Beginner–Intermediate

### Blender Version
Blender 5.0

### Tags
#lighting #hdri #volume #materials #shaders #rendering #blender-5x #beginner #intermediate

---

## Related Tutorials
- [3 Easy Lighting Setups | Blender Tutorial](3-easy-lighting-setups-blender-tutorial.md) — shares #lighting #hdri #volume
- [Photoreal Volumetrics in Blender](photoreal-volumetrics-in-blender.md) — the full-volumetric counterpart when render budget allows

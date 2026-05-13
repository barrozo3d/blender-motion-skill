---
title: Art Stream #27: Nodes, nodes, nodes! [Blender / Geometry Nodes]
source: YouTube
url: https://www.youtube.com/live/7FdfSKOkzXg
author: Midge "Mantissa" Sinnaeve
ingested: 2026-05-13
blender_version: Not specified
tags: [geometry-nodes, particles, volume, procedural, abstract, intermediate, advanced]
---

# Art Stream #27: Nodes, nodes, nodes! [Blender / Geometry Nodes]

**Source:** [YouTube](https://www.youtube.com/live/7FdfSKOkzXg)
**Author:** Midge "Mantissa" Sinnaeve
**Ingested:** 2026-05-13

---

## Description

Come to our conference: https://denoised.net

The stream will stay up as an archive for those can't make it!

Go listen to our EP! https://open.spotify.com/artist/75VNDP9SUFELIRIcvztV5m

PC specs because people always ask: Core Ultra 7 265K, 96GB RAM, RTX 3090

For more of my stuff find me here:

Website: https://mantissa.xyz/
Mastodon: https://mastodon.art/@mantissa
Bluesky: https://bsky.app/profile/mantissa.bsky.social
Instagram: https://www.instagram.com/mantissa.xyz
X: https://www.x.com/t

---

## Raw Content (for analysis)

Kind: captions Language: en Hello. How are you all doing tonight? Hope you're well. Start a little bit early, but see if we can pick some music to listen to. Hope you're all doing well. Uh if there's any issues with any audio or video or whatever, just let me know. As always, it has been a while and I've used OBS for other things, so I have to like reset up every single time. Um, let's see. Music, music, music. Uh, I have a fan on in the background, by the way. So, if that is annoying, let me know. It'll turn it off. Can't wait to see what you're cooking. Yeah. Well, hopefully I'll have some cool stuff. I've kind of been on a bit of a roll lately, so I want to share that while it's all fresh in my head messing with geometry nodes, obviously. But had a bit of a break through and some fun with like textures and 3D and stuff. So, it's nice. Let's see. What are we picking while we're waiting? Actually, I was jamming on this the other day. So, let's go here and let's start start here. Actually, this is the song I really want to hear. So, let's start here and then by the end we'll get there. That is very loud. Cool. Well, thank you at for letting me know. Nice. All right, I think I'm good to go. Let's close this. Yes. Yes. All right. So, uh, Houdini stuff. No, mostly Blender lately. Um, to Houdini, not for a really stupid reason, actually. Um, I switched over to different Linux distro year ago. I think I switched over to Arch to use Wayand and all the new stuff with um, just to see what it's like. And I really ended up liking it and stuck with it. And, um, Houdini doesn't work on Wayland yet. I can switch back back to X11 if I want to, but um yeah, then I have to switch between and it's just annoying. So, I just ended up doing more geometry nodes. But I will say the stuff that I did last year with it um has kind of inspired what I'm going to get into today. Uh so, I sort of found a way to do it in geometry nodes as well. But I'm already just chatting without really doing anything. So, let's start uh at the beginning. So, I was on a bit of a mission to figure out if I could make a nebula and then I did I did some last year in Houdini, which was fun. And now I've gotten to a really fun simple way of doing them in Blender. So, let's start with volume cube and distribute some points in there. And really, this is the base of everything. So, let's type distribute points and volume. There we go. Let's start with a density of a th00and maybe. So, if you're just going to display stuff with noise, um, and I'll show you. Let's do a noise texture. And if at any point I'm like going way too fast or something, just let me know. Um, and I'll slow down a little bit. But I've been in the zone with these lately, so it's fun. Um, so if you just throw an offset in the noise texture, if I make this a bit smaller, you can see you get a nebula. But uh let's say we want to push this out further to get like more tendrils. You might want to scale this vector. So the noise texture is giving us basically threedimensional vectors to offset the position in which is really nice. Um and if you untick normalize then you get them in all directions and it works really well. Um but if you just scale this up then you'll see you don't really get a nebula. Even if we put this up to like 10,000, um, you never really get that nebula feeling. And the trick to it, I found, is by, um, basically repeating it, which sounds really simple when you think about it. Let's see if we repeat here. Throw it in there, throw it in here, and then repeat a few times and bring the scale down a little bit. uh down or oh, I don't know. We'll see. We repeat it a few times and you'll see you'll get more like a nebula type thing. And the fun thing is you can really prototype this live and it just adjusts which is awesome. So you can mess with the scale. See a smaller scale can give you like tighter sort of strings and a larger scale then you need less iterations and you get like bigger nebulas and stuff. Um let's set it to 4D and just play with this. So you see if you start playing with it here, you can just kind of live scroll through it and look for an interesting shape. And that's like a lot of fun already, you know. It's cool. Now, let's see. Let's actually set the radius of the points to be a bit smaller. And now you're totally getting Nebula vibes. And the thing is the only downside of doing it this way, I think, is you're tempted to push the density up and up and up and up. Um, and it kind of works, but at some point you it just gets too much. Like this starts getting a little funky and it's always going to be kind of a point nebula. Now, I've tried to then uh convert this to a volume and then get the volume and then maybe you could smooth it out. like you go all kinds of crazy with it, but I don't think it's going to do this high of a density. So, let's try it like that. I'll try it, but I hope it doesn't crash. So, let me save this first. Uh, projects or we going to throw that in here. Let's do five. There we go. Um, but I haven't really gotten this to work yet. So, let's see. or no, it's points to volume. Yeah. So, the radius needs to be a bit smaller. And then what I was thinking about is if we just mess with the size here, you can kind of get something up the density. Uh, and then let's do volume to mesh. Volume to mesh. There we are. and you can create sort of a nebula, but again, the lower you go, the more like blobby this gets. So, um, let's see if we set this radius down. We set the file size back up to 0.1. No, it's fine. See? And then, uh, set position. Then we're going to blur that out. So I take the position and then you got the blur attribute and that basically creates a smooth um for the positions of the mesh which is really nice. Uh there we go. And then we just basically have a smooth. So now you could get something that looks kind of nebulike. Let's see. The problem is if we increase this down. No, sorry that's not what I meant to d

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/art-stream-27-nodes-nodes-nodes-blender-geometry-nodes.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Live art stream exploring procedural nebula creation in Geometry Nodes by distributing points in a Volume Cube and using iterated/repeated noise texture offsets to generate organic space nebula shapes.

### Key Steps
1. Start with a Volume Cube node; add a Distribute Points in Volume node with a density of ~1000 to scatter points.
2. Add a Noise Texture node; connect its output as a position offset via a Set Position node to displace the point cloud.
3. Uncheck Normalize on the Noise Texture to get offsets in all directions for more natural spread.
4. To get nebula tendrils, scale the noise vector before input; simple scaling alone doesn't produce nebula feel even at high scales.
5. Use a Repeat Zone (loop) on the noise offset: run the noise offset through multiple iterations (repeat a few times) and reduce scale — this creates layered, tendril-like nebula formations.
6. Switch the noise to 4D mode; scrub the W value to explore different nebula shapes in real time.
7. Reduce the point radius to achieve finer nebula texture.
8. Experiment with converting points to volume (Points to Volume node) then back to mesh (Volume to Mesh node) for a smoother blob-like nebula.
9. Use Set Position followed by a Blur Attribute node to smooth out the resulting mesh positions for a soft nebula surface.
10. Iterate on scale, repeat count, and W value interactively for real-time design exploration.

### Blender Nodes / Settings
- Volume Cube node
- Distribute Points in Volume node (Density: ~1000)
- Noise Texture node (4D mode, Normalize unchecked, W value for variation)
- Set Position node
- Repeat Zone (loop iterations for layered noise)
- Points to Volume node
- Volume to Mesh node
- Blur Attribute node (smoothing mesh positions)
- Point radius adjustment

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#geometry-nodes #particles #volume #procedural #abstract #intermediate #advanced

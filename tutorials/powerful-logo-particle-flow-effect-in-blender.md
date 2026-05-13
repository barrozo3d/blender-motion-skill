---
title: Powerful Logo Particle Flow Effect in Blender
source: YouTube
url: https://youtu.be/TTGcr-45jCE
author: Ducky 3D
ingested: 2026-05-13
blender_version: Not specified
tags: [geometry-nodes, particles, particles-reveal, animation, logo-animation, typography, materials, shaders, motion-design, intermediate]
---

# Powerful Logo Particle Flow Effect in Blender

**Source:** [YouTube](https://youtu.be/TTGcr-45jCE)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this blender motion graphic tutorial we will be taking logos and text, converting them into hundreds of particles, and then displacing and animating the particles. We will be using geometry nodes to create the effect and the materials will be driven by noise textures.

These tutorials are part of a new series where we are looking at using blender like it is Photoshop or after effects. Putting images, logos, and text to make interesting effects. In a way replacing the need for some of those af

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going, guys? So, today we are going to be creating this in Blender. It's really cool and it is part of the series I'm doing here on YouTube about using Blender like it's Photoshop, like it's After Effects, and creating text effects, things on images. And this is a really cool one. First, we'll use the text tool, pick a font, get our text to say whatever we want it to, and then we can head into geometry nodes and distribute some points on that text. After that, it's pretty easy. We'll just do a small set of noise textures to displace it and then get some of the parts to displace and some of the parts to not displace so we can still read the text but get this really interesting displacement. After that, we will just use the noise texture to shade the particles and we'll be totally done. Here on YouTube, I have several other tutorials in this theme about using Blender like it's Photoshop, like it's After Effects, and running images and logos and text through it to make some cool stuff. So, check out the playlist below for more tutorials in this theme. And over on Patreon, I have a couple exclusive tutorials in this series, so you can learn even more stuff. Check out all that. And it's the end of the year, so you can get a discount on annual memberships now through January. All that linked in the description. With that being said, let's learn how to make this effect. All right. So, let's start out in the text tool. So, we're going to hit shift A, click on text. Now, you don't have to use text. You can actually use anything you want. You noticed that you may have noticed in the thumbnail, uh, there's the Blender logo. So, you can use the Blender logo, like import an SVG, uh use literally any piece of geometry. I'm just using text because uh that's the theme here for this series. And you can do it with text. You can do with anything. And the text is editable, which is really cool. Um so, with that being said, I'm just going to type in all caps L return. And then I'm going to go here to the text tool. And then in the font, I'm going to go ahead and pick uh a nice serif sans serif. Sarif right down here, I'm going to get the character spacing. Oops, no, sorry, the line spacing a little bit better. I'm going to scale this up. And then also here on the alignment, we'll do center and middle. [snorts] And then I'm going to scale it up pretty big. And I'm hittr a apply scale. uh scaling it up is going to affect the distribution of points. So, your scene will probably look a little different than mine because I didn't scale this at exact measurements, but this is not an exact tutorial. You'll get the idea. Um, now that we have our text ready to go, I'm going to open up uh the geometry nodes tab. I'm going to just make my scene the way I like it. Also, I'm going to go over to the shading tab um and make my scene the way I like it to, which that isn't working. There we go. Uh so, should this be my system defaults? Yes. Do I always forget to do it? Yes. Um back to geometry nodes. So, let's go ahead and put some points on this scene so we can get something looking really cool. So, I'm going to click new in geometry nodes. And first we're going to need to get a distribute points on faces. Plug that there. And then once you bring up that density, you'll start to see uh whatever geometry you put it on, it start to be readable. Um then we'll need to get a set point radius node and then you can bring the points down. Now on mine, my radius was my ending radius is 0.00.00009. That's really small. The thing about this effect is the smaller your points and the more dense you have points. So the more points and the smaller they are, the better this effect will look. Um because it starts to look like dust. That's kind of the idea here. So, the more dustlike your scene looks, uh, the better your glow is going to look, the better the color is going to smooth out it. Everything benefits from it being denser and the points being smaller. Uh, so it's really going to be a give and take of what you are willing to put your computer through. Um, but I'm going to give myself 10,000 on uh the density. Now, that does not mean I have 10,000 particles. That's just the density number. Um, I don't know how many particles I have. It's a lot. So, now that we have this, we can go ahead and get a set position node and start to displace these particles around. So, we're going to use a I'm going to hit shift A and search noise texture. And make sure that you uncheck normalize and use color. If you use factor, it's not going to displace the particles on all axes. It's only it's going to basically do it on like a diagonal because it's combining all the normals. normals, the the axes basically. So, plug that into offset and you're going to get this. I have found this specific effect uh looks really good if you bring your roughness up a little bit. Again, you want it to be very dustlike and then um leaving everything else default. I think we this is all editable later. So, now we have this. What I want to do is figure out how to get only portions of the text to have this effect on it. Um, and then we're going to get a vector math node and set that to scale. And that is going to uh decide how strong this effect is going to be. [snorts] Uh, again, so I want some of the text to be this, some of the text to be that. How do we do that? That is going to be with a mix vector node. So now what I want to do is create a use a texture to go some portions of this text to look like that, some to look like that. And if you have a little bit of experience with things like that, it's going to be with the factor slot. So we need to get another noise texture and we need to get a RGB curves node. And I'm just going to go ahead and flip the curves. Plug color into color. Make sure you click. Actually, I'll show you why you need to do that. So, if we do this, it's it kind of looks like we're back. If you click on normalize, 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/powerful-logo-particle-flow-effect-in-blender.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Converting text or logos into a dusty particle flow effect in Blender using Geometry Nodes' Distribute Points on Faces, then selectively displacing portions of the point cloud with two Noise Textures and Mix Vector, so parts remain readable while others disperse dramatically.

### Key Steps
1. Add a Text object (Shift+A > Text); type text in Edit Mode; set font, line spacing, center alignment; apply Scale (Ctrl+A) — scale affects point distribution density.
2. In Geometry Nodes on the Text object: add Distribute Points on Faces node (Density: 10,000+); add Set Point Radius node (Radius: ~0.00009) — smaller radius looks more dustlike and enables better glow.
3. Add Set Position node; connect a Noise Texture (Normalize: off, Color output not Factor) to the Offset socket for 3D displacement in all axes.
4. Adjust Roughness up on the Noise Texture for a more dusty appearance.
5. Add a Vector Math (Scale) node to control displacement strength globally.
6. For selective displacement: add a second Noise Texture → RGB Curves node (invert/flip the curve); use its output as the Factor socket of a Mix Vector node between zero displacement and full displacement.
7. Connect the Mix Vector output to the Offset socket — now some regions stay intact (readable text) while others flow away.
8. Animate the overall displacement scale or the second Noise Texture's W value over time for animated reveal/dispersion.
9. For shading: in the material, use a Noise Texture connected to a Color Ramp to color the particles procedurally (hot core, cool edges, etc.).
10. Apply an Emission or Point shader material for a glowing particle look; render in Cycles or Eevee.

### Blender Nodes / Settings
- Distribute Points on Faces node (Density: 10,000+)
- Set Point Radius node (Radius: ~0.00009)
- Set Position node
- Noise Texture node x2 (Normalize: off, Color output; Roughness: high)
- Vector Math: Scale (displacement strength)
- Mix Vector node (Factor = second noise output for selective displacement)
- RGB Curves node (invert for mask)
- Noise Texture in material (particle color)
- Color Ramp node (color gradient)
- Emission shader

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#geometry-nodes #particles #particles-reveal #animation #logo-animation #typography #materials #shaders #motion-design #intermediate

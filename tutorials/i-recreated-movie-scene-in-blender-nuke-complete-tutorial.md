---
title: I Recreated movie scene in Blender & Nuke | Complete  Tutorial
source: YouTube
url: https://youtu.be/iW6WF8guDMY
author: MISSING PIXEL VFX
ingested: 2026-05-13
blender_version: Not specified
tags: [rendering, compositing, animation, camera, lighting, materials, intermediate, advanced]
---

# I Recreated movie scene in Blender & Nuke | Complete  Tutorial

**Source:** [YouTube](https://youtu.be/iW6WF8guDMY)
**Author:** MISSING PIXEL VFX
**Ingested:** 2026-05-13

---

## Description

In this video, I break down how I recreated an iconic shot inspired by Kong: Skull Island using Blender and Nuke.

This cinematic VFX shot combines live-action style composition with CG elements, focusing on realistic lighting, atmosphere, and seamless integration. I’ll walk you through my workflow—from scene setup in Blender to final compositing in Nuke—while sharing simple techniques to enhance realism and depth.

This is not just a technical tutorial, but a creative approach to making your CG

---

## Raw Content (for analysis)

Kind: captions Language: en Hello friends, welcome back. Today we are going to recreate this shot in Blender and Nuke and I'm going to use all the free assets and I will also provide the renders and the project file. With that you can learn something new. Before I start this video, I want to say something first. Thanks a lot everyone. Last week my channel crossed 4,000 subscribers. I know this number sounds very less, but for me it's another step towards the success, so I'm really happy with that. They love me. Let's go and start it. First we'll download all the assets we need. I'll go to Sketchfab. I'll search for Kong. And we have this element. This is really good for this shot. I'm going to download this as a face because it's not heavy. I think this is only 6 MB, so I'll just download it. And we'll also search for helicopters. I'll type Apache. This is really good model and I'm going to use this one, too. Download and this time I'm going to download this as GLTF because the face is too heavy. So I think this is going to work here. Once I download the assets, I will bring them into Blender and check if the texture and everything is working fine. And if not, I'll just fix it and then I'm going to use it for further steps. So I have this model here. In reference, we don't see this armor on the character's hand, so I'm going to delete that one. First I will hide the fur. And then select the object and hit tab or edit. And select all the vertices and press P on the keyboard. And by loose parts. So we have separate parts for the character now. And I will just select the body, press H so we can hide that and also I'll select these extra parts from the mouth of the face and hit H so we can just hide them. Select all the armor and then delete. And then press Alt H, we get all the rest of the object back in the viewport. Now go to the lighting view and check the material or the textures for the shot for the model. Let's bring in the shaders tab as well. And shaders. First we'll fix the fur. I think I'll just hit this cross button and open it again and press the path. And I will select fur, open. And also for the normals, just hit this and I'll bring that. fur alpha So, now we have fur and fur alpha, but we need to do some little more fixes like I don't want this much bright. I'll make it darker. Somewhat like that. And if I take a close look from here, let's do a basic lighting first. Like that and you can see more. I'll take a color ramp. Add it here and slightly bring this white point still here so we can see these kind of fur. This is an image texture, so we see it like that. It's not actually fur. They're projected some images, which is really good for this kind of shot. I'll keep it somewhat like this. I will select the body this time and just hit this cross button and I'll just bring the body texture, which is the show and bring it. Alt D and bring it here and connect it this to base color. And then this normal, I think this is going to be different one. Let's fix that, too. Yeah. And that's fine, but I'm going to I think this is okay. This is normal. Yeah, that's okay. That's fine. Okay. So, now the texture is done for the shot. Like it's a very basic simple texture they have assigned and this is going to work for the shot because the character is mostly silhouette and we don't need any details and I think this is going to work. So, select everything and press Ctrl J to make it one. And likewise, we can bring the uh helicopter and make the um texture fix. And same thing I did for the helicopter, I just brought it in and uh applied all the textures and I did one more extra thing to that. Like I kept this blade in separate control and this one is separate control and whole body is one because when I do the animation, I want to give some rotation to the blades, so we can do that easily. And I took an empty and applied this helicopter to that, so whenever we just move, we have this like whole body is moving with that. And we also have the separate control for the blades. And the next thing is animating the character. I can use Mixamo for that. So, I got this character into Mixamo and I will type in stand up. Okay, so we have this animation. Okay, this is good for the shot. I'm going to do some changes in the parameters. Like, first thing I'll just override it like I'll make it very slow. We can do it in Blender itself, but we can just see how it looks. And then the arm space, I'll just make it bit more so that we feel that character is bit angry or something like that with that arm space. I think this is roughly matching with the shot we have as a reference. I can download it now. I'll download it as a BX 30 FPS and just keep everything as is. So, I brought that character into Blender again, uh the animated character, and we'll see what we can do. First thing we need to set the scale. For the scale, I'm going to keep this character around like just move this helicopter first. I don't want this into the scene. I'll make it big enough to like roughly around 80 m. So, let's take a measure tool and see how that how big that will be. Oh, that will be super big. I'll just keep it up to like 80 or 81 m. I'll select the model and just make it big. Go to the timeline and yeah, we choose this frame where he's already standing and then we can make the height. Maybe this is fine. So, 80 m is some somewhere around here. All right, keep it that. So, this is this height scale that I'm using. And the speed is too fast like I just want to make it bit slow, but we'll see it with the camera. So, next thing I'll bring in the camera first and I'll just remove this helicopter this side. We don't want this to see it. I'll just grab camera. Camera I'm going to keep it away from the character like almost 700 m because I'm going to use long lens. So, So, somewhere around this point. Select the camera and bring it in here and check the measures again. Not yet. Okay, some way somewhere around there. And I'll make the 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Complete VFX pipeline tutorial recreating a Kong: Skull Island-style cinematic shot in Blender and Nuke using free Sketchfab assets, Mixamo animation retargeting, large-scale scene setup with a 700m camera-to-subject distance, and final compositing in Nuke.

### Key Steps
1. Download free assets from Sketchfab: Kong model (FBX, ~6MB) and Apache helicopter (GLTF); import into Blender and fix textures (fur alpha, body texture, normal maps).
2. Fix Kong model: hide fur; Tab into Edit Mode; P > By Loose Parts to separate; delete armor pieces; Alt+H to restore; fix fur texture Color Ramp to darken slightly.
3. Connect helicopter blade as separate object with an Empty parent for independent blade rotation control (animated rotation for spinning blades).
4. Animate Kong in Mixamo: upload character, search "stand up" animation; adjust arm space parameter; download at 30FPS (BVH).
5. Import animated character back into Blender; scale Kong to ~80m tall (use Measure tool to verify).
6. Position camera ~700m from character (long lens = cinematic telephoto compression); set up camera framing.
7. Set up scene lighting: atmospheric fog/volume, dramatic backlit mood to create silhouette effect (character mostly silhouette, minimal texture detail needed).
8. Set up helicopter flight path animation with keyframes.
9. Render in Blender with multi-pass render outputs (diffuse, specular, shadow passes) for Nuke compositing.
10. Composite in Nuke: assemble passes, add atmospheric effects, color grade for cinematic Kong: Skull Island feel.

### Blender Nodes / Settings
- Image Texture nodes (fur, body, normal map textures)
- Color Ramp node (fur darkening)
- Empty parent (helicopter blade rotation control)
- Measure tool (80m character scale verification)
- Volume Scatter (atmospheric fog)
- Camera: long lens (~300–400mm equivalent for telephoto compression)
- Mixamo: animation retargeting, arm space parameter
- Multi-pass rendering for Nuke compositing
- Ctrl+J (join meshes)

### Difficulty
Advanced

### Blender Version
Not specified

### Tags
#rendering #compositing #animation #camera #lighting #materials #intermediate #advanced

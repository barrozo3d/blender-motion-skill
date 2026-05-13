---
title: Blender Tutorial - Eternals Gold Wireframe Animation
source: YouTube
url: https://youtu.be/WmldjCv9P84?si=8OfevIgZN31ZV4_A
author: Blender Made Easy
ingested: 2026-05-13
blender_version: any
tags: [animation motion-design logo-animation curves svg wireframe brand-video beginner intermediate]
---

# Blender Tutorial - Eternals Gold Wireframe Animation

**Source:** [YouTube](https://youtu.be/WmldjCv9P84?si=8OfevIgZN31ZV4_A)
**Author:** Blender Made Easy
**Ingested:** 2026-05-13

---

## Description

In this Blender tutorial we will be recreating the Eternals gold wireframe animation! It's not an exact 1 to 1 but it still looks pretty cool. 
For Blend files check out - https://www.patreon.com/c/BlenderMadeEasy
Logo - https://www.blender.org/about/logo/

Subscribe for more Blender Tutorials! youtube.com/blendermadeeasy?sub_confirmation=1

Come join the Discord! - https://discord.gg/2YcMjXK

Download Blender - www.blender.org

Come follow me on social media!
Skillshare Page - https://www.skill

---

## Raw Content (for analysis)

Kind: captions Language: en hello everyone and welcome to another blender made easy tutorial today I'll be learning how to create this gold wireframe build animation in blender I got this idea from the new Marvel film eternals from this scene right here where the weapon creates itself I thought it looked pretty cool so I decided to recreate this effect in blender using any curve object you are able to create this for this animation I used a single vertex and I basically traced out the sword and then converted it to a curve to keep things simple I'm going to be using the blender logo for this tutorial fortunately for us the blender logo actually has an option for us to download it as an SVG I will link this page in the description once you have it you can jump over into blender and then import it in by going over to file down to import and then selecting the SVG once you import it in it's very very small so make sure you select everything by box selecting it and then scaling the entire thing up we're going to scale it up pretty big and then place it in the middle of our scene we don't really need the extra objects so select the extra parts of the logo and delete them because you're not going to need them we only really want the main part of the logo now that we have the logo in our scena let's go over the curve settings and I'm going to talk about how to create this effect to make things simple let's select both of these and press contrl J to join them together as one curve object next over in the fill mode we don't really need it we don't need a face so switch it over to none right there if we open up up the geometry tab we can give it some thickness by changing the depth right here you'll notice though if I drag it up just slightly it creates a huge amount of bevel even though the value is so small well the reason for that is because we scaled everything up really big so make sure you press crl a and apply the scale next if we go into edit mode and press a to select everything and open up the properties tab by hitting n you're going to notice the mean radius is set to 284 that means it's going to multiply the depth by that value that's not going to look very good and that's why it's scaling everything so big so make sure you set the mean radius down to a value of one and now the depth should actually work correctly so if we drag this up you're going to see it's actually working properly the next step is to clean up our curve you'll notice that there's some parts of the curve that have these weird shading issues and the reason that's happening is because there are two vertices right on top of each other if we go into Edom mode we can select the One X and then delete that vertex that will fix the issue go around the curve and make sure you do that for every single part that has that weird issue now let's talk about how to animate the build effect and that is done by using the start and end in the mapping section over here in the geometry panel at the moment if we drag this up you can see it's not working and that's because our curve is a complete Loop we need to add in a hole in the middle of our curve you might think to go into edit mode and then delete one of the vertices but you're going to notice that it doesn't create a hole it's still right there it's a complete Loop instead what you need to do is select two vertices then press X and delete the segments not the vertices delete the segments and that will create a hole in the middle from there select one of the parts and then just fill out the hole so we'll select right there press e to extrude and drag it down until it's right in the same position just like that now what happens is if we drag up the start you're going to see that this is the effect that we're getting we can actually animate this value and it will create the build effect we need to do that exact same thing for the inner circles so go into Edom mode and delete two of the segments so select two of them X and delete the segments then grab them and move them into place keep in mind wherever you create this hole that is where the build animation is going to start so if you want your animation to start building at this point then create a hole right there but if you want it to start building over here create a hole right here on this curve to actually get the build effect we need to animate the end value if we drag this down you're going to notice that it starts to create this effect but there are two problems one problem is I don't want it to go in this direction I want it to go in the opposite direction and and another problem is I don't want these to go in the same direction I want one to go this way and the other one to go this way so to fix that you can go into edit mode we'll select the outer logo right here and then we'll select the inner logo and press crl L and then to switch the Direction all you have to do is right click and then click on switch Direction so let's animate this value I'm going to bring the end frame all the way down to zero and then add in a key frame right on that side we're going to jump all the way to frame 200 and drag the end all the way up to a value of one and then add in another key frame let's take a look at this by restarting our animation and playing it and this is the effect that we're getting now let's talk about the mapping start and end values these are how the mapping is going to affect the animation with it set to resolution what it's going to do is it's going to take the geometry of your object and base the end value on that for example if we scroll up to this part of our logo and then we scroll forward a little bit you're going to see at this point if we go into edit mode there's a big chunk that is missing a lot of geometry so this part is going to go very fast and then play it you can see this part's slow this part's fast and then it becomes slow again because there is more geometry that is because the end is set to resolution

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/blender-tutorial-eternals-gold-wireframe-animation.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Animate a curve-based wireframe "build" effect by animating the Geometry > Mapping > Start/End values on a curve object — creating a self-drawing line animation inspired by the Eternals weapon construction scene.

### Key Steps
1. Import SVG logo: File → Import → SVG; box-select all and scale up significantly
2. Select the curve → Ctrl+J to join into one curve object
3. In curve properties → Fill Mode: None (removes face fill)
4. Open Geometry tab → set Depth for wire thickness
5. Ctrl+A → Apply Scale (critical — large scale causes huge bevel values)
6. Edit Mode → press A → open N panel → reset Mean Radius to 1.0
7. To create the build gap: select two adjacent vertices → X → Delete Segments (NOT vertices)
8. Extrude one vertex back to close the gap at the correct starting point
9. Keyframe Geometry > Mapping > End: value 0 at frame 0, value 1 at frame 200
10. To reverse direction: Edit Mode → select curve → right-click → Switch Direction
11. For separate inner/outer curves to build in opposite directions: select inner with Ctrl+L → Switch Direction

### Blender Nodes / Settings
- Curve Properties → Geometry → Depth: controls wire thickness
- Curve Properties → Geometry → Mapping → **Start / End**: animate these for the build effect
- Fill Mode: **None** (in curve Shape section)
- Mean Radius: reset to **1.0** in Edit Mode (N panel) after applying scale
- Mapping mode: Resolution vs Uniform — Resolution makes speed proportional to geometry density

### Difficulty
Beginner/Intermediate — no shader nodes; pure curve and animation workflow

### Blender Version
Any (tested with a version showing the Eternals film era, ~3.x)

### Tags
animation motion-design logo-animation curves svg wireframe brand-video beginner intermediate build-animation self-drawing draw-on eternals

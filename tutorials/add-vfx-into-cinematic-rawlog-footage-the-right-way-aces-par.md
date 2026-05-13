---
title: Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1
source: YouTube
url: https://youtu.be/aJF2sAjRsy0?si=sF4GyRUcpJzAkv37
author: InLightVFX
ingested: 2026-05-13
blender_version: any
tags: [compositing rendering color-management aces vfx theory intermediate advanced]
---

# Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1

**Source:** [YouTube](https://youtu.be/aJF2sAjRsy0?si=sF4GyRUcpJzAkv37)
**Author:** InLightVFX
**Ingested:** 2026-05-13

---

## Description

Get the free super cool poster: https://gumroad.com/l/XUOQrK
Part 2: https://www.youtube.com/watch?v=LssHxDCM7H4
To support more tutorials like this: https://patreon.com/inlightvfx

RAW and LOG footage is known for creating that cinematic look we all strive for, but it often looks very flat right out of the camera. So how do we add VFX to flat-looking footage? Join me as we utilize ACES, a color workflow within Blender and Davinci Resolve, to do just this. With all the necessary software being 1

---

## Raw Content (for analysis)

Kind: captions Language: en as you progress as a vfx artist at some point you'll probably work with log or raw footage this footage looks flat out of the camera which leads to high quality cinematic images the cameras that can shoot this type of footage keep getting more affordable and more popular so how do we add vfx into flat log or raw footage the answer is aces aces is a free color management pipeline now what that means will make more sense as we go on but basically asus enables artists to easily incorporate vfx into high quality log and raw footage asus is quickly becoming the industry standard workflow it's being adopted not only by big studios but also independent artists like you and me and it's for all these reasons and more that i think you should learn aces one of the main things aces does is handle the color gamut and gamma of our footage in this video we'll learn all about what this means in part two we'll look at the ace's workflow using davinci resolve and blender but for now if you don't understand color gamut and gamma join me and let's dive in for this video i created this poster that goes over these concepts so make sure to download it and follow along linked in the description first up color gamut we use the term color gamut when talking about color spaces now what the heck is a color space well if we look up color space on google we'll see most of the images are of this chart this chart was actually created in 1931 but as you can see it's still widely used today to visualize color spaces let's break this chart down first there's this whole color region you see here this represents all the possible colors that the average human eye can see out in nature as such we call this the visible color space and the boundary of this space is labeled as the gamut of human vision so we can think of gamut as meaning the total range or boundary of a certain color space cameras capture images and video by representing the real world with a subset of colors from a certain color space display devices then represent these images using a color space that could be the same or different these different color spaces used for capturing and displaying images can be mapped onto our diagram with triangles we use a triangle to mark the color gamut or range of a color space all the colors inside the triangle gamut are the ones able to be captured or displayed so how does all of this apply to aces well part of aces includes the main asus color space which is called aces 2065 1 and as you can see the gamut of this color space encompasses the entire visible spectrum of light this is why asus is so powerful remember when i said that aces is able to handle the color gamut of whatever footage we throw at it well here's what i mean because the aces color gamut is so huge aces is able to use footage filmed in a variety of smaller gamuts and transform that footage into the ace's color space and this is super helpful for artists because we can just focus on doing vfx in aces and never again have to worry about what type of footage we're handed now it's not exactly that simple but it is really nice so now we understand color gamut which mainly deals with color and describing a certain range of colors if gamete describes color gamma we can think of as having to do with brightness and luminance let's look at a different graph to understand now don't freak out you've seen this type of graph before with rgb curves our x-axis will represent luminance input level so 0 on the x-axis means complete black and 1 means complete white the y-axis will represent the output values let's draw a straight line represented by the function y equals x now gamma is actually just a value and this value is taken as the exponent of our input this gamma value is part of what is called a gamma transfer function if we set the gamma value to 1 then our line here stays the same our input luminance values are not changed by the gamma function this is called a linear gamma or more specifically a linear transfer function with a linear transfer function if we add two luminance inputs say 0.25 plus 0.25 we get an expected output of 0.5 two times as luminous the math works as expected if we set the gamma value to 0.5 or 1.5 we'll see that our line becomes a curve this is what we call a non-linear gamma curve or non-linear transfer function we can see that if we have an input of 0.25 we get 0.5 on output if we then add 0.25 we get 0.7 so math from input to output with non-linear transfer functions is a little weird now in nature in the real world light waves interact in a linear relationship if you double the luminance input of a light source we get double the output blender in most 3d software is set up to use linear calculations by default when rendering and compositing let me show you why this is helpful we have a scene here with two lights on either side of the cube and the world shader set to black i can render the scene with both lights on and get this image or i can render an image with just one light on and a second image with the other light on and if i add these two images together in compositing you'll see it looks exactly like the image with both lights on the reason this math works so well is because we're using linear light calculations which again is how light works in the real world this is also why multi-pass compositing is possible which is the technique i've shown in other videos so now let's talk about humans our eyes perceive brightness from the world around us non-linearly let me provide an example to explain this say you're in a completely dark room and then you light a candle your eyes perceive a big change in brightness but if we're in a bright environment and we light the candle our eyes see very little change to the brightness of the environment even though the change in luminance the candle is the same as you can see our eyes are more sensitive to changes in brightness of darker shades so we say that our eyes perc

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-par.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Conceptual foundation for the ACES color pipeline: understanding color gamut, gamma transfer functions (linear vs non-linear), and why ACES 2065-1 is the ideal working color space for VFX compositing into RAW/LOG footage.

### Key Steps
1. Understand color gamut: the range of colors a camera or display can capture/show, represented as a triangle on the CIE 1931 chromaticity diagram
2. Understand that ACES 2065-1 color space encompasses the entire human visible spectrum — larger than any camera or display gamut
3. Understand linear gamma: Blender uses linear light math by default (doubling input = doubling output), matching real-world light physics
4. Understand non-linear gamma: human eyes perceive brightness non-linearly (more sensitive to dark changes); displays apply gamma encoding to compensate
5. Understand why linear compositing enables multi-pass rendering (separate render passes add correctly in linear space)
6. LOG/RAW footage uses non-linear gamma encoding to preserve dynamic range — must be transformed into ACES linear space before VFX work
7. ACES IDT (Input Device Transform) handles converting any footage type into ACES 2065-1
8. Note: practical workflow is in Part 2 — this video is pure theory

### Blender Nodes / Settings
- No specific nodes — this is a theory/conceptual video
- Key concept: Blender renders in linear light by default → correct for multi-pass compositing
- Follow-up: see ACES Part 2 for the actual Blender/DaVinci Resolve setup

### Difficulty
Intermediate — requires understanding of color theory; essential before tackling RAW/LOG VFX work

### Blender Version
Any (color theory is version-agnostic)

### Tags
compositing rendering color-management aces vfx theory intermediate advanced log raw color-gamut gamma linear workflow

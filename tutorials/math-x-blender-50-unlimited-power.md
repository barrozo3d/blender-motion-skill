---
title: Math x Blender 5.0 = UNLIMITED POWER!
source: YouTube
url: https://youtu.be/EvWAcSA86fw
author: MTR Animation
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Math x Blender 5.0 = UNLIMITED POWER!

**Source:** [YouTube](https://youtu.be/EvWAcSA86fw)
**Author:** MTR Animation
**Ingested:** 2026-05-13

---

## Description

📖 Use the code "MATH" to get 25% off The Big Nodebook!!!
https://mtranimationgumroad.gumroad.com/l/thebignodebook/MATH

Use this link if you want to become an affiliate:
https://mtranimationgumroad.gumroad.com/affiliates

In this tutorial, we are creating an Apollonian Gasket by applying lots of complex mathematical equations in Blender 5.0! These equations will be implemented all procedurally using the Repeat Zone, For Each Element Zone, and tons of Math Nodes using the latest version of Geomet

---

## Raw Content (for analysis)

Kind: captions Language: en [music] This is the appalonian gasket. It's a mathematical phenomenon that starts with just three circles and repeatedly adds new circles in the gaps between them. And at first this might seem like a simple process until you look at the complex mathematics behind this. And that complexity is exactly what inspired me to recreate this structure using Blender's geometry notes. So let me show you how that is done. And in this tutorial we are going to use a lot of complex formulas. And if we would add those formulas in one by one, note by note, then this tutorial is going to take like hours. And to be honest, I don't think that's really needed. So, I did some pre-work. So, if you go into the link in description, there you will find a Blender file which contains node groups that already implement the formulas that we're going to use. So, download that and open it up. And then we can get started. And as always, what we're going to start off with is clicking on the cube and create a new geometry nodes for this. And we're going to remove the group input because we do not need the default cube. And also, let's actually remove this light. And let's move the camera a bit to the side. We don't really need it for now. And the thing that we want to create first is we want to create the structure of one circle that goes like this. One big circle and then we want to create two smaller circles just like this in between it. And this we are going to create with three points. So if we do an points node and this is going to be the bigger point and these smaller points we want that to be two other point nodes. The reason why we don't just put the count to three over here is because I want to have specific control over the position and the radius of each point that we're adding in. So, let's join these points together with an join geometry nodes. Let's connect them all like so. And like so. And let's connect it like this. And the first thing that I want to do is change the radius of the bigger point. This radius should become two. And then for the other two points, what we want to do is make it that the radius of these points is also dependent on the radius of the bigger point. So let's do that. Let's make it procedural by adding in a value note which we set on two. And let's connect it like this. And we want that the radius of this point is half of the radius of the bigger point. So let's do a math node which we set on multiply. Let's multiply this by 0.5 and connect it like so. The next thing that I want to do is change the X position of this point so that it is always like this in the corner of the other point. So first of all I want to have control over the separate X Y and Z sockets. So let's do an combine XYZ node. And now this X value you see that that needs to become a value of one. And you remember okay this is a value of two and this is a value of one. So basically what we need to do is subtracting the radius of the smaller point from the radius of the bigger point with an M note set to subtract and then subtract from the bigger one. Subtract the smaller one. And that's going to be our X location. And then if you change the size of the smaller point, you see it's always in the corner of the bigger point, which is perfect. Let's make it like this. And now what I want is that the third point is going to fill this gap over here. And that we are going to do by first giving it the right radius. And the radius of this third point is basically the radius of this smaller point subtracted from the radius of the bigger point. So if we do another subtract node and we subtract from the bigger point we subtract the second point then you will see if we connect that it is correct because if we put it like so it fits perfectly in between. But now we also need to make this X position procedurally dependent on the other two. So if we do another combine XYZ node, then this X position, you see that that needs to become minus.6. And to get to that value, we are going to do the exact same thing as we did for the second point. So we're going to subtract the radius of this third point from the radius of this bigger point. So if we do another subtract note and we subtract from the bigger point, we subtract the radius of the earth point and that's going to be the x position. Then you see uh it's on the wrong side and that's logical of course. So let's flip it to the other side by doing an math node set to multiply. And let's multiply this by minus1 and then you will see it's always in the correct way which is perfect. Let's set this on 0.5 for now so that it is perfectly aligned in the middle. And just to make this tutorial look a little bit better, let's do an instance on points node and also an curve circle to instance circles on these points. And the scale of these instances should be dependent on the radius of the points. And then you see we have perfectly created that shape that I showed you earlier. The next thing that we're going to do is adding in a fourth circle in between the gaps of the other three circles. And that we are going to do in three steps. Step one is of course add that fourth circle in geometry notes. And the second step is to determine what should be the radius of this new point. And then the third step is to determine the position of that point. But let's start with the radius. And the radius we are going to determine that with these formulas. So you see the radius of this new circle is 1 / K. K is the curvature that this new circle should have. And to calculate the curvature of this new circle, we need this bigger formula over here. You see K4 is the curvature of the new circle. But then you see we also need K1, K2 and K3. And those are the curvatures of this [clears throat] circle and this circle and this circle. And to calculate the curvature of those three circles, we need this formula. So let's calculate the curvature of those circles first. And we're going to do that b

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/math-x-blender-50-unlimited-power.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Blender Nodes / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced]

### Tags
[To be added]

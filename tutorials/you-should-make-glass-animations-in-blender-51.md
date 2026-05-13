---
title: You Should Make Glass Animations in Blender 5.1
source: YouTube
url: https://youtu.be/vemW4ceygRg
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# You Should Make Glass Animations in Blender 5.1

**Source:** [YouTube](https://youtu.be/vemW4ceygRg)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

Making 3D glass Motion graphics can be one of the most satisfying ways to make some cool animations in blender. Today I will show you my workflow with 6 Glass animated wallpapers. I will talk about why i picked the shapes, the materials and my render settings. 
----------------------------------
Animation 1 - https://www.patreon.com/posts/glass-disks-156985765?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link
----
Animation 2 - https://www.patreon

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going, guys? Today, I'm going to talk about six separate glass animations with the goal that you can walk away from this video and be able to make so many more of your own glass really beautiful stylized animations. So, I'm going to go over my thought process, like why did I pick certain shapes, material settings, tips and tricks, and I'm going to talk about some render settings as well. Now, before we jump into it, these three animations that I'm going to be talking in the video, they are currently available as tutorials here on YouTube, and I will link those in the description. And these animations are exclusively available on Patreon, but I still will be breaking them down here in this video. So, if you want to check any of these full tutorials out, they are available. If you want to join the Patreon, there is a ton of exclusive content, project files, and tutorials, and breakdowns. So, if you want to check that out, that is going to be linked in the description. And you can get a discount if you subscribe annually. So, all of these tutorials, except for the wires one, have a single thing in common. We're using glass objects in combination with smooth emissive textures, and the glass objects are going to bend the texture and make a really cool effect. There are no lights, the textures are the light. The trick with all of these is pairing the right texture with the right object and making something really cool. All right, so let's look at this first one. It's my favorite one of the bunch. The glass objects here act like a magnifying glass for the material beneath it. Now, it's pretty easy to make a grid of interlocking spheres. You first get an array modifier to go one direction, and then you get a second array modifier to go the opposite direction, and then you just take the settings and offset them. In kind of a rare moment for this YouTube channel, you don't need geometry nodes for this at all, and it makes something really cool pretty quick. Now, for the emissive material at on the bottom, at first I tried out a noise texture and with the W animation, and it was really cool, especially if you scale up the texture. I didn't really love the movement. Now, then I took that grid and I tried out a wave texture at a really large scale. This is kind of my hack for making animatable gradients. You just take a wave texture, and now you have a gradient. I liked how it how the gradient kind of bended around the spheres, especially with just a straight up and down one. It looks really cool. Now, this whole thing got a lot cooler when I added a high value to the distortion, played with the phase offset, and it just looked really cool. It had the same speed and cadence of the straight line, but had a little bit more variation and unpredictability to this whole animation. Now, keep in mind, the smaller you make the scale, the better this is going to look to a point. So, like this is a large scale, doesn't really look that good. So, if you bring it down to like .7, it looks really good. But if you bring it down to like .1, you're going to get way bigger, which this might be something you're looking for, but I want more variation. .7 for me looked really good and really beautiful. Last thing I'll say about these is one thing that makes these really beautiful is as the texture animates in, you get this interesting movement. So, the texture's traveling this direction on the object, but you still get you could see as it's traveling outward, you get some some highlights right here. So, you get to appreciate the whole object as it's kind of bending around the object, and I just think it's really beautiful. And then you get kind of that secondary motion with some of these reflections, and it all is just really nice. This next one is a ribbed glass, and originally I tried to just use a wave texture to displace the glass, but I didn't like how the sharp edges showed up. I really felt like I was fighting the texture, and the references I was looking at, this didn't match it. It just wasn't up to the quality that I wanted it to be. The thing that's going to make or break this ribbed glass is going to be bevel and thickness of the glass object that's in front of the emissive texture. So, having a much thicker object like this with a soft with a full bevel modifier on it is really going to make this look a lot better. And then, of course, all it needs is an array modifier. Now, this one looks best with a noise texture and a color ramp, and you can get something really cool right off the gate. But smoothing it out makes it look a lot better. So, if you take a color ramp, switch it over to B-spline, but you still get some gray. You're going to need three nodes, two of them set to black, so that you can control the dark point, and you get something really, really cool. Also, within the mapping, if you also squish the texture to complement the ribs of the glass, you're going to get something really, really beautiful. And also recommend a little bit of distortion on the noise, then go ahead and just add whatever color you want in there, and really, really fast, you can get something very beautiful and very elegant. I would bring the detail down to zero, just keep a classic noise texture with a really smooth color ramp, and if you animate the W, it looks incredibly beautiful. Now, this one's a good example of being really intentional about where the emissive material is in relation to the glass. How close is it? If I take the plane and just put it right in the middle of the glass, it's going to look like this. And then as I move it further beneath the glass, you're going to get more of these really beautiful spots. So, right where it's dark, you're going to see it bend up and down in those spots where it's black. But what happens is if you bring it too far down, it gets too much it gets really muddy, and it just kind of is really over stimulating to the eye. So, if I bring it bac

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/you-should-make-glass-animations-in-blender-51.md and extract:
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

---
title: A FULL Blender Compositor Course!
source: YouTube
url: https://youtu.be/_7N7emOvDko
author: SharpWind
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# A FULL Blender Compositor Course!

**Source:** [YouTube](https://youtu.be/_7N7emOvDko)
**Author:** SharpWind
**Ingested:** 2026-05-13

---

## Description

I'll teach you how to use Blender's compositor system to it's full extend! If you're just starting out, or dabbing into the hardcore areas, this video covers the entire spectre!
Never miss a video! ► https://bit.ly/2CGmgK1
#blender #tutorial #compositing 

► Discord Server: https://discord.gg/EJhEysM
► Instagram: https://www.instagram.com/sharpwind_official/
► Twitter (X): https://x.com/just_sharpwind

How Blending modes work (timestamped): https://youtu.be/G3fWEcbuAqQ?si=p7-bory4LhFYP0Bp&t=408


---

## Raw Content (for analysis)

Kind: captions Language: en What is the Blender compositor? In short, it's all of the post-processing you do after you've already rendered the image. And it's all of these noodles that happen between this box and this box. And today, I'll show you how it all works. How's it going? My name is Sharp, and I'm making a library of all the content about everything Blender related, so you can find it all in one place. And today, my Discord community has voted for the Blender compositor. If you like Blender, you're now legally obligated to subscribe. So, Blender's compositor is based on nodes, unlike some popular software that are based on layers. And that's a good thing because you can reuse nodes and wire them in any way you want and organize them better. And layers are stupid. Sorry, we use layers at work. I reckon if you want to learn how to use the compositor, it's first best to learn how nodes work. And I know that a lot of you guys know this already, but without a good foundation, all of your buildings collapse. So, suck it up. Since compositing usually comes at the end of the production, I'm going to assume that you have an entire scene already set up. If you don't, I've got plenty of tutorials on how to do that. Shameless self-plug. Or you can make something really simple. Like this will be enough for the purpose of teaching you how to use the compositor. I'm going to use this. If you click on the compositor tab up here, you'll get this interface with the timeline down below and the compositor window up top. To start compositing, you will click this use nodes box, which will give you these nodes. We'll start with this node, which is our rendered image. So, anything we got from hitting the render button in our 3D scene, uh the result is in here in this box. And this noodle goes all the way here to this box which is our final output. So whatever goes in here will be the final result. This box is just the viewer. So you can see it. The output is here. Now between this noodle path I can do whatever I want and it's going to affect my image. And there's a bunch of pre-made boxes to perform certain operations. These boxes are called nodes. As a demonstration I can press shift A or use this drop-own add menu and locate the node that I want to use. Let's say for example brightness and contrast. With shift A. You can also use a search function and I like to use it all the time cuz it's easier. Just find the node however you want. This node, as the name suggests, performs an operation which can either add or remove brightness and or contrast to whatever comes into this input over here. So, by placing it here, I'm just going to insert it into my noodle. Basically, our rendered image looking like this is going into the input. Then, we can tweak the parameters in this node which is going to change it and then spit out the changed output. The brightness and contrast node, for example, can increase the overall image's brightness by adding overall value to the image or add contrast by taking the middle brightness point and pushing all the values away from it. I know the scale is tipped to one side as due to Blender's color transform, and that's way too much to get into this video. It shouldn't make a difference for you unless you're a colorist. Don't worry about it. But we can't really see these changes unless we've rendered our image first. That's why I like to make a certain setup whenever I work. If you have the node wrangler add-on enabled, which you always should, that's the law, you can control, shift, and click on any node just like in the shader editor, and it will create a viewer node, letting you see the result of the note that you clicked on. So, you can preview what every individual node does. But by default, it's going to show in the background here, and I don't like that. So, what I like to do is I like to click on this backdrop, which will make it disappear, and then split this window in half, change this one into the UV editor, and as a display, choose the viewer node. So whatever's coming into the viewer node will be shown in the UV editor here. Now we have our composite results separate from our node tree and we can see all the changes we make in real time. So when I slide the brightness and contrast values, you can instantly see what they do. But that's far from the end of node magic. You see the brightness and contrast values. They have inputs, meaning we can plug non-uniform values into them and they will affect different parts of our image in different ways. Now, the brightness and contrast node isn't really the best example for what I'm about to show you, but the node is pretty obvious in what it does. So, I'm going to stick with this example. Let's say that I take another output from our rendered result by click and dragging from this output, drop it in the middle of nowhere and search for color ramp. You could also just have added this manually and connected everything manually. I don't think that's something I have to explain. If I control shiftclick this note to preview it, you can see it turned everything into a grayscale. We can move these handles to clamp it or change their colors and whatnot. It's the same as in the shader editor. We now have a black and white version of our render. And in Blender's terms, black equals zero. So all of these parts on the image that are black are going to have the value of zero in these places. And white is equal to one. So all of the bright parts are going to be one. All these gray values are just a fraction from 0 to one. So you have all the values. It's like a grayscale. You get it? If I were to plug the output of our color ramp into the brightness input of our brightness and contrast node, it will give these parts of the image a value of zero, meaning nothing's going to change, and all of these parts a value of one. So, it's like only giving a brightness value of one to only these parts of the image. Now, it's hard to see because the bri

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/a-full-blender-compositor-course.md and extract:
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

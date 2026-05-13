---
title: Fundamentals of Lighting in Blender
source: YouTube
url: https://youtu.be/ENnEYoUpFfU
author: Blender Guru
ingested: 2026-05-13
blender_version: Not specified
tags: [lighting, rendering, cycles, hdri, beginner]
---

# Fundamentals of Lighting in Blender

**Source:** [YouTube](https://youtu.be/ENnEYoUpFfU)
**Author:** Blender Guru
**Ingested:** 2026-05-13

---

## Description

Discover the fundamentals of lighting in Blender.

Join the Blender Guru Academy: https://academy.blenderguru.com/join

Download the Starting 3D Model: https://drive.google.com/file/d/10XimqZ8ZytpuIB1ZIaMSBs66nQ9NytO_/view?usp=sharing

Poliigon Addon: https://www.poliigon.com/blender

=== Chapter Marks ✂️===
0:00 Intro
0:58 Positioning
5:12 Staging
11:11 Falloff
18:12 Size
24:57 Color
27:06 Polish

===Follow me🫰===

Twitter: https://twitter.com/andrewpprice
Instagram: http://instagram.com/andrew

---

## Raw Content (for analysis)

Kind: captions Language: en Lighting is one of the highest leverage skills that artists can learn because it can multiply the impact of everything else you've already done. Often the same number of lights but in a different arrangement can completely transform an audience's reaction to the same image. And when you look across history, you'll see that the artists that learned to use lighting effectively created some of the most iconic memorable artworks. And in the modern era, lighting is a futurep proof skill in the age of AI because it's a skill that relies mostly on your judgment to best service the story. But before you can light large scale fun environments like this one, you need to understand what lights actually do. So in this video, we are going to be lighting this simple sci-fi crate as you learn about the fundamentals of lighting, which is positioning, fall-off, size, and color. And if you're watching this on YouTube, this is actually a free lesson from my Blender Guru Beginners Academy, which you can learn more about by clicking up there or by clicking the link in the description. So, after downloading the blend in the attachment, you should open it up and see this. And then, if you went to the rendered view mode at the top there, you should see your crate. But why can you see your crate? Because we actually haven't got any lamps in our scene at the moment. So, why can we see our crate? Because if this was in space, you couldn't see something if there was no sunlight. So why is this? It is because this color here is gray and that's actually adding light into it's called like environment light. So generally you don't want this cuz you want to be able to control the lighting um and not just have it blasted from uh all directions, which is what we've got here. So firstly, you go to your world tab over here and then you either change the color to black or what I do, I just set the strength to zero. And now lights out. we now have to rely entirely on the the lights that we add to the scene. So, I'm actually going to split my view. So, I'm going to go to the top, right click, and say vertical split. And then on the left hand side, this is going to be my rendered view mode. And then on the right hand side, it will be my 3D viewport. So, I can uh manipulate things. So, we need to add in a lamp so that we can see things. So, shift A. And the lamp we're going to use is just your bog standard typical point lamp, which is uh if you don't know, omniirectional. So, it's casting light from all directions like a basically a hovering orb of light uh anywhere we put it or or a light bulb. I guess it's another uh maybe more familiar uh light source. Uh anyway, with this, let's just crank it up a little bit so that we can see it. And let's uh let's move it around. Now, a big mistake a lot of beginners get into is they go like, "Huh, look, I got like all this shadow and I can't even see the other side of this." So, I'm going to create another lamp. I'm going to put it over there. And then, well, I've still got shadow along the front there. So, I'm going to create like another lamp. I'm going to position it about there. And look, I got this big ugly shadow there. So, I might as well put another one there. And then it just ends up looking terrible. But the reason this looks terrible isn't because there's too many lamps. It's because there's no shadow. Shadow is actually vitally important for the human brain to understand the form of what it is you are looking at. To give you an example, um if I was to uh have just a sun lamp, right, just blasting sun from the top down, looking at the uh the um the the crate there, and I went into top view and I I had a look at this. It's really actually impossible to understand what the shape of this object that we're looking at is like I modeled this thing and I don't even know if this is a protrusion or an intrusion, right? The these little uh these little cutouts here, is it going up or is it going down? It's impossible because we have no shadow. Whereas, if you were to just rotate this sun lamp ever so slightly, you can see how much easier it is to understand what we're looking at, right? So, shadow is your friend. Embrace shadow. You do want shadow in your scene. Don't try to hide it. It is vitally important. So, uh yeah, don't don't remove it. However, having said that, there is a big difference between shadow and so much shadow that you can't see anything, which is what we've got on this side of my crate. I've got all this detail and decals and stickers and things that you can't see, and I want the viewer to be able to see that. So, to solve this, you need to have a separate light source, but just not so bright that it's confusing the eye as to uh what the shape of the object is. So, I'm going to take my little lamp here, and I'm going to hit shift D to duplicate it, and I'm going to just move it somewhere to the right hand side so that it's casting light, you know, onto our on this this side of the box there. Now, with the same strength as this one, right? They've both got a strength of 460 there. You can see that it's it's that problem. It's it's it's so much light that it's it's making it a little bit difficult for the eye to understand the form. So, all we need to do is just drop it. Right now, what's the amount? There's no exact amount. I remember growing up there was like these textbooks on like 3D and it was like, oh, it should be like half the value of the the the key light source. I think that's just like bogus. Doesn't need to be that. It's just go go go go go by your eye, right? You still want to see that there is obviously shadow on this hand side, but obviously not so dark that I can't see anything. So, I just make it a little bit brighter than that so that I can still see there's something there, but it's clearly in uh in shadow. Now, so far I've been looking at the crate from this angle, this sort of 3/4 view. That's what they call it. Um, but 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/fundamentals-of-lighting-in-blender.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Teaching the four core fundamentals of Blender lighting — positioning, fall-off, size, and color — using a sci-fi crate as a practical example, demonstrating how each property affects shadow, form readability, mood, and overall render quality.

### Key Steps
1. Set the World Background strength to 0 (World Properties > Surface > Strength: 0) to remove ambient environment light and start with pure darkness.
2. Split the viewport: left side Rendered view, right side 3D Viewport for simultaneous manipulation and preview.
3. Add a Point lamp (Shift+A > Light > Point); increase strength to see the crate; position as the key light (primary directional source).
4. Avoid adding multiple equal-strength lights from all sides — this kills shadows; instead, embrace shadows as essential for form reading.
5. Add a fill light (Shift+D duplicate the key light; move to opposite side); reduce its strength significantly (much less than key) so the viewer can still see shadow detail but not be blinded.
6. Understand fall-off (Inverse Square falloff by default): light diminishes with distance squared; closer lights illuminate more intensely; use this to control the drama.
7. Understand light size: small radius = hard crisp shadows; large radius = soft shadows; adjust Light Radius in light properties.
8. Consider light color: cool-colored fill vs. warm key light creates visual contrast and mood; use the Color picker in light properties.
9. Always evaluate lighting from the final camera angle (Numpad 0) as perspective completely changes the light's perceived impact.
10. "Polish" phase: fine-tune strength, position, and color to serve the story and direct the viewer's eye.

### Blender Nodes / Settings
- World Properties > Surface > Strength: 0 (remove ambient)
- Point Light (omnidirectional, Strength, Radius, Color)
- Sun Light (directional, rotation controls shadow direction)
- Area Light (large soft source)
- Light Radius (shadow softness: 0 = crisp, high = soft)
- Light Color (warm/cool contrast for mood)
- Rendered view mode

### Difficulty
Beginner

### Blender Version
Not specified

### Tags
#lighting #rendering #cycles #hdri #beginner

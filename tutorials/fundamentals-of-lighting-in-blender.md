---
title: Fundamentals of Lighting in Blender
source: YouTube
url: https://www.youtube.com/watch?v=ENnEYoUpFfU
author: Blender Guru
ingested: 2026-05-19
blender_version: "4.x"
tags: [lighting, beginner, cycles, rendering]
extraction_status: complete
frames_dir: tutorials/frames/fundamentals-of-lighting-in-blender/
frame_count: 0
---

# Fundamentals of Lighting in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=ENnEYoUpFfU)
**Author:** Blender Guru
**Duration:** 43m25s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Lighting is one of the highest leverage skills that artists can learn because it can multiply the impact of everything else you've already done.  Often, the same number of lights but in a different arrangement can completely transform an audience's reaction to the same image.  And when you look across history, you'll see that the artists that learn to use lighting effectively created some of the most iconic, memorable artworks.  And in the modern era, lighting is a future-proof skill in the age of AI because it's a skill that relies mostly on your judgment to best service the story.  But before you can light large-scale fun environments like this one, you need to understand what lights actually do.  So in this video, we are going to be lighting this simple sci-fi crate as you learn about the fundamentals of lighting, which is positioning, fall off, size, and color.  And if you're watching this on YouTube, this is actually a free lesson from my Blender Guru Beginners Academy, which you can learn more about by clicking up there or by clicking the link in the description.


### Positioning [0:58]
**Transcript:** So after downloading the dot blend in the attachment, you should open it up and see this. And then if you went to the rendered view mode at the top there, you should see your crate.  But why can you see your crate? Because we actually haven't got any lamps in our scene at the moment. So why can we see our crate? Because if this was in space, you couldn't see something if there was no sunlight.  So why is this? It is because this color here is gray and that's actually adding light into it's called like environment light.  So generally you don't want this because you want to be able to control the lighting and not just have it blasted from all directions, which is what we've got here.  So firstly, you go to your world tab over here and then you either change the color to black or what I do, I just set the strength to zero. And now lights out, we now have to rely entirely on the lights that we add to the scene.  So I'm actually going to split my view. So I'm going to go to the top right click and save vertical split. And then on the left hand side, this is going to be my rendered view mode. And then on the right hand side, it will be my 3d viewport so I can manipulate things.  So we n...


### Staging [5:12]
**Transcript:** Now so far I've been looking at the create from this angle this sort of three quarter view. That's what they call it.  But what if I wanted to like change the angle and look at it from a completely different angle.  Well, it completely changes right this now looks like flash photography that horrible flat lighting because lighting is view dependent.  It only works for a specific view, which is why you generally don't start lighting an object until you know for sure where the camera is going to be once the camera is locked in, that's when you start lighting.  Now I wanted to for the sake of engagement for a video. I wanted to jump straight into the lighting, but it makes sense to lock down the view so that you know exactly where the lighting needs to be before you continue.  So I'm going to create a new camera. So shift a I'm going to hit camera and I'll just move this up a little bit. If you want to view through the camera view, that is number pad zero, of course.  And a lot of people already have experienced this and you might already know the solution, but for those who don't, yeah, when you're in this view here, if you try to like orbit, right, you click the orbit thing like mid...


### Falloff [11:11]
**Transcript:** Okay, now back to the challenge of lighting and I want you to ignore the position and I should just forget forget this light here and just look at this single light source and have a look at the intensity of the light and how look at like what you think might be not great about what we have going on here as it relates to intensity and some of the astute observers that are watching right now might notice that you know what this side of my crate here feels like.  A little brighter than this side of the crate here right and this is called fall off right as light increases from the distance of a light source right so from here to to across here it is losing intensity and it's something that like children understand the closer you stand to a light bulb the brighter it is going to appear.  But what a lot of artists don't understand is how severe this fall off actually is and why this is such a useful storytelling tool okay so I'll tell you what the answer is in a second here but I want you to have a guess at what you think is the the fall off okay so having a look here we've got the light sources here we have let's say this this single face right which is like this one over here hitting ...


### Size [18:12]
**Transcript:** important traits we've talked about the position of the light we've talked about the fall off of the light I wanted to introduce you to  two more the first is the size of the light and then the color of the light so firstly the size of the light and you can  change the size of a light we're going to your lamp settings where they lamp selected and then changing this radius value here  and you'll notice that as you increase it right the the lamp gets this like a circle that appears around it and then it does something to the render right and the really a  stoop people that that that know what what's going on will notice that this is changing the the softness of the shadow right so as I increase it you can see it this  shadow is becoming feathered and and soft and as you increase it further and further it becomes kind of like an overcast day  and this is kind of where a lot of like beginners kind of stop because they're going to like I mean like it must a big deal like what what is this really changing and what am I supposed to do here right what what how am I supposed to use this  effectively as an artist it doesn't appear to be really doing much well believe it or not it's actually ...


### Color [24:57]
**Transcript:** right do I want to feel make it feel like it's grounded in the real world and that the light is  coming from nature or from incandescent or fire or something like that that's where I'm thinking of  these values here alternatively if I don't want it to feel like that and I want it to feel like  it's part of an urban scene like a street scene or a club scene or anything like that that is when  I would use the color value because then I have full control over the colors and I can introduce a color  that you would never see in nature you're never going to see purple light in nature someone's  going to prove me wrong I'm sure but you will never see this right like there's just certain colors  that you just don't see as light sources are in in nature but yeah that's where you can play with it  here so this is a sci-fi crate right so it would actually make sense in this case for me to use  a light source that I'm not going to find in in nature I'm not going to find on like the Kelvin  scale here so I'm going to use something that's like a little bit bluer maybe like that  and that's just going to help tell part of the story that this is like hey this is a sci-fi crate  in a you know made ...


### Polish [27:06]
**Transcript:** know we want this to look as best as we can we want to have a little bit of fun I'm going to show  you now some of the other changes that I would make to this box to the the setup of this box  to try to render this as best as we possibly can if we if we were just doing like a single  model render like this like for something to post on art staging and you portfolio to show off a  model what is the best way that I could possibly show this to maximize the likelihood that somebody's  going to click on it and you know actually appreciate it right so what are some changes that I  might make well one even though we're showing a model just by itself on a plane like this it doesn't  hurt and it's really low low effort to just throw a texture that relates to the object onto the  surrounding plane here so this plane here it's just black right but this is a sci-fi box right  do what we dragged in a real sci-fi box and carefully positioned it for like a studio lighting  why not just make this look like concrete right it's a really tiny simple thing but it just adds  to the story of the asset that we're doing so simple way to do this I'm just going to be using  the polygon add-on which you can ...



---

## Structured Notes

### Core Technique
Four fundamentals of lighting — Positioning, Falloff (inverse square law), Size (shadow softness), and Color — taught through lighting a sci-fi crate in Cycles; emphasises locking camera before starting to light and using a contextual ground texture for storytelling.

### Summary
43-minute Blender Guru lighting fundamentals course (free excerpt from his Beginners Academy). Covers the four pillars of lighting through practical application: (1) Positioning — where to place lights relative to camera for drama; (2) Falloff — inverse square law means doubling the distance quarters the intensity, a powerful storytelling tool; (3) Size — larger light = softer shadows, recreates overcast vs. sunny; (4) Color — Kelvin scale for natural light vs. creative color for sci-fi/stylised. Emphasises staging (lock camera first) and polish (use contextual textures on ground).

### Key Steps
1. **World to black** — World Properties → Strength = 0 (removes environment light); now you control 100% of the light
2. **Lock camera first** — Shift+A → Camera; Numpad 0 (camera view); N-panel → View → Lock Camera to View; position camera; lock it; THEN start lighting
3. **Positioning** — add Area/Point/Sun lights; position relative to subject AND camera; lighting is view-dependent — same setup looks different from different angles
4. **Falloff** — inverse square law: light intensity ∝ 1/distance²; practical: move a light 2× further away = ¼ the intensity; use this to control how much of the scene is lit — close lights = dramatic falloff, distant (sun) = even falloff
5. **Size** — Area Light Radius: small = sharp hard shadows (sunny day); large = soft shadows (overcast); Size parameter on Point Light for same effect; larger size = more realistic but slower render
6. **Color** — two approaches: Kelvin scale (warm 2700K candle to cool 10000K sky) for natural light; free Color picker for stylised/sci-fi; color contrast between key and fill adds visual interest (warm key + cool fill)
7. **Polish** — add a matching ground texture (concrete, metal, sci-fi floor) to tell the story of where the object is; low-effort but high-impact; use free Poliigon texture

### Nodes / Settings
- World: Strength = 0 for full lighting control
- Area Light: Size (shadow softness); Shape (Square/Rectangle/Disk)
- Point Light: Radius (shadow softness); Falloff: default is Inverse Square (physically accurate)
- Sun Light: Angle (shadow softness, 0.526° = real sun); no falloff (infinite distance)
- Spot Light: Spot Size (cone angle); Blend (cone edge softness)
- Color: Light Data → Color; or enter Kelvin value
- Lock Camera to View: N-panel → View tab (in 3D viewport)

### Difficulty
Beginner

### Blender Version
4.x

### Tags
lighting, beginner, cycles, rendering

---

## Related Tutorials
- [[3-easy-lighting-setups-blender-tutorial]] — three practical lighting setups building on these fundamentals
- [[realistic-product-lighting-in-blender]] — product lighting applying these principles
- [[the-key-to-realism-in-blender-or-3d]] — broader realism including lighting strategy

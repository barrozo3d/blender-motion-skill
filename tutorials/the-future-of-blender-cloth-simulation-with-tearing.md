---
title: The FUTURE of Blender Cloth Simulation (with Tearing!)
source: YouTube
url: https://www.youtube.com/watch?v=6hn12BWufTs
author: CGDive (Blender Rigging Tuts)
ingested: 2026-07-01
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-future-of-blender-cloth-simulation-with-tearing/
frame_count: 6
---

# The FUTURE of Blender Cloth Simulation (with Tearing!)

**Source:** [YouTube](https://www.youtube.com/watch?v=6hn12BWufTs)
**Author:** CGDive (Blender Rigging Tuts)
**Duration:** 12m28s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Into [0:00]
**Transcript:** I just found out that there is a new experimental cloth simulation in Blender 5.2 Alpha.  And that got me very excited. Like, are we getting modern physics simulations? Finally.  So this is very new to me, but I managed to get it to work really easily, even with my basic  geometry node skills. So it's not at all difficult to use. And my first impressions are that performance  looks really good, but more important than performance, simulation stability is a lot better  than the old cloth system. Things that would have definitely exploded or collapsed before  now just work. And the new system also has dynamic cloth tearing out of the box. And I mean really  dynamic. You don't need to pre-cut the cloth or anything like that. You just need to apply force  and the cloth will tear automatically. So in this video, I'll show you how it works. But first,

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_000.jpg

### How to get the new cloth [0:52]
**Transcript:** here is how to get access to it. You can go to blender.org, download, scroll down to go experimental,  click on this button. And you can download blender 5.2 for your operating system. Once you have

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_001.jpg

### How to enable the new cloth [1:08]
**Transcript:** 5.2 Alpha, go to edit preferences, experimental, and to enable this feature, I need to enable  a couple of these. And I'm not sure which ones they are. The geometry nodes here, dynamics is one  of them, I think. But I'm not sure which the other ones are. So I'll just enable everything.  Okay, and now if I go to geometry nodes, create a new geometry node tree, and search for cloth,  I should have the cloth dynamics group. Okay, and if I just plug it in here for the cube and press play,  the cube will start falling because it is now a cloth object. Now I'll start over.

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_002.jpg

### How it works [1:51]
**Transcript:** And let me create a little standard scene that you see in cloth simulation tutorials. I'll have  a floor. And Suzanne is collision objects. And a subdivided plane is my cloth object.  Okay, now let's go to geometry nodes. So I'll create a new geometry node tree,  and add the cloth dynamics. Now this will start falling, but it won't collide because we haven't  set this up as colliders. Here, by the way, huge thanks to Blender essay. I found out about this  new feature through his posts on X, and he also posted some images of the setup, which helped me  figure things out. Okay, so how do we make the ground and the monkey collision objects?  First, I'll name my objects, and then select the collision objects, and move them to a new collection,  call it collision, and now I'll drag and drop the collision collection into the node tree.  Next, I'll press Shift A, and search for collider. And there are two of those, but you should choose  geometry collider inside the geometry node tree. Now I can connect this collection into the geometry  collider. And to make it take effect, we have to connect it into the effectors. But this is a bundle.  So you can drag a new model from here, and search for combine, combine bundle. And you can plug  the bundle into the effectors. The reason this is done so is if I had another collider here,  this is just an example, but I could connect it over here, and now I can have multiple objects or  multiple collections being regarded as effectors or as collision. So now if I play the animation,  this should already work. Right, let me give more subdivisions to this cloth.  Currently it does struggle with very thin objects. I'll show you some ways to improve this.  Under solver, we have sub steps and constraint steps, which control the quality of the simulation,  so I can increase those. Interestingly, that also changes the behavior of the cloth.  At least right now it seems to make it stiffer. But in here we have sliders to control the behavior  of the cloth. And unlike the old system, the names are very clear. We have bandiness.  You know, right now our cloth is very stiff like leather. Bandiness should make it softer.  Like this. And stretching is might be easier to show if I don't have the ground, so I'll delete it.  And this is the default stretchiness. If I increase it,  the cloth should stretch more. That is not exactly what happens, but you know, it's a work in  progress. Under structure, we have something called collision radius. So if I increase this,  that should help with some of these penetrations. Also the geometry friction on the collider help  with that a little bit in my experiments. Yeah, that definitely helps. So something else that we  often want to do with cloth is pinning. So that is also very easy to do here. I'll go to edit mode.  And let's select a bunch of vertices over here and press control G assigned to new group.  That will just create a new vertex group called group. So now to enable the group, I can drop  this pin group input and plug it into the group input. And that will create a new property for me,  which I can control. And here it automatically found my pin group. I'm not sure if that should  happen. If it's in this state for you, you can click this button to switch to group selection  and find your pin vertex group.  Right, and choose it from here.  So now we have pinning just like we know it from the old system. I can go to weight paint and smooth it.  So that's pinning. So we've already uncovered a lot of the features here. Let's see some that we  haven't used so far. Invert pinning group will do exactly as it says. Basically this part,  the active part should become simulated and the black part will become not simulated.  At least that is what should happen. But for some reason nothing happens. I'm not sure why.  Anyway, this should simply invert the pinned group. And I think it worked for me earlier,  but right now it isn't, but I'm sure it will be fixed.  Dumping is a common parameter in simulations. It just makes the simulation slower and smoother.  So if I set it to a higher value, the simulation will be a lot slower.  Next we have gravity. It is set to a realistic value. You can tweak it, but in most cases you don't  need to. Next we have tearing, which I'll show you in a second. And effectors are the collision  objects, but also forces. So let me recreate the setup that Blender essay showed on Twitter.  So we have something called simulation force. And I'm going to plug it in here.  And now if I just give it a value on the x-axis for example, it will act like very simple force,  which forces the cloth to go towards the positive x direction. But to make it more interesting,  I'll literally just copy the setup from Blender essay. And that gives us a more natural wind effect  with some sort of oscillation or turbulence. Okay, and if you play with the values, you can get  different wind effects. Okay, here I'm in a new scene and I have this fear as the cloth object.  And again, I've set up my collision and I just wanted to show how when I have a closed object,  it is automatically treated as a soft body of sorts. Of course, depending on your settings,  it might collapse. But when stiffness is high, it doesn't. So let's check out the tearing now.

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_003.jpg

### Tearing [8:50]
**Transcript:** First I'm going to go to weight paint and paint up here and smooth the group. That will automatically  create a new group. So let's create the property so that we can use this group.  I'll enable stretchiness and bendiness.  And you'll see how the parts of the cloth that are not pinned start to stretch towards the ground.  Now if I enable tearing, and let's increase the threshold a little bit,  as soon as the cloth stretches above a certain threshold, it will tear. It will tear automatically.  So here's another scene, basically the same setup we have this plane as the cloth. And this is a  collider here. So now if I play the animation, I can basically in real time affect this cloth.  But if I enable tearing, then things get interesting.  I just need to apply enough force and that will tear the cloth. This is so cool and this is just  an experimental build. I'm definitely looking forward to what this will become when the system is  finalized. By the way, here is another example of the new cloth system that I found on YouTube.  It is by Bradley animation. And they've created a system in which the tearing is activated by drawing  lines. Okay, in the beginning I mentioned stability. And here is what I mean. This is not a new system.

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_004.jpg

### Improved Stability [10:35]
**Transcript:** This is the old system. And this is a test I was doing very recently. Basically I have this  cloth object. It has some shrinking applied, which means that it will become smaller. And then there is  collision object of a similar shape below it. And when we simulate, here is what happens.  First of all, the simulation is very slow.  And the simulated object totally loses the collision. Okay, this is completely unusable.  Now I have the exact same objects and the exact same animation. And I try to recreate it with  the new system. And the only thing that's different is this little simulation. This basically shrinks  the monkey for the first couple of frames. And if I play it with the default settings,  you'll see that it's actually kind of worse than the old system. But if I just enable this  deforming sitting, things change dramatically. Overall simulation speed is a lot faster. And most  importantly, our simulated object did not explode or collapse. By the way, if I enable tearing here,  we might get very cool results because the cloth will keep shrinking and eventually it will reach  a point where it needs to tear. So cool. I hope you enjoyed this video. Please like, subscribe,  and I'll try to keep informing you about cool Blender updates like this.

**Frame:** tutorials\frames\the-future-of-blender-cloth-simulation-with-tearing\frame_005.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

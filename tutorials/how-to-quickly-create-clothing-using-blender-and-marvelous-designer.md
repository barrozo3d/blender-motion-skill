---
title: How to Quickly Create Clothing using Blender and Marvelous Designer
source: YouTube
url: https://www.youtube.com/watch?v=Rp1G9mIBskI
author: Martin Klekner
ingested: 2026-07-20
blender_version: "2.8 RC"
tags: [cloth, organic, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to Quickly Create Clothing using Blender and Marvelous Designer

**Source:** [YouTube](https://www.youtube.com/watch?v=Rp1G9mIBskI)
**Author:** Martin Klekner
**Duration:** 22m20s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hello friends, Martin here and welcome to this new tutorial on my channel.
[0:03] This time another one of the character creation tutorials.
[0:07] And in it I will actually introduce you to this awesome tool called Marvelous Designer
[0:12] in which you can create your own CG clothing in a matter of minutes.
[0:16] So let's get to it!
[0:20] As mentioned, we'll be using Marvelous Designer, this awesome tool that completely revolutionized making CG clothing.
[0:28] I've always been afraid of sculpting clothes because I know how much I suck at it.
[0:33] But with this software, complex shapes and cloth simulation is now a question of just a few clicks
[0:39] and a few simple tucks on digital fabric.
[0:43] Well, don't take my word for it, just watch this tutorial and you'll see for yourself.


### Blender 2.8 RC [0:48]
**Transcript (timestamped):**
[0:50] And look here at what version of Blender I'm using.
[0:53] That's right, it's the release candidate version that just came out.
[0:57] With this beautiful splash screen from the awesome open movie Spring.
[1:01] So exciting to finally see the final version of Blender 2.8 might actually become a reality.
[1:07] Speaking of which, now is really the best time to start with Blender.


### CGBoost Launch Pad Course [1:11]
**Transcript (timestamped):**
[1:11] And there's really no better way than to try the new Blender Launchpad course by Zach Reinhardt
[1:17] who now under the banner of his new platform CGBoost just released this comprehensive introduction to Blender 2.8.
[1:25] And I mean, it's aimed at beginners, but I tried a course myself and I must say I'm learning something new in every chapter.
[1:33] So I guess I'm not so advanced after all.
[1:36] But yeah, big shout out to Zach for finishing this epic course.
[1:40] I really can't recommend it enough.
[1:43] And if you want to get it, just click on the link in the description below.


### Preparing the character in Blender [1:47]
**Transcript (timestamped):**
[1:50] But now to the actual tutorial.
[1:52] First things first, if you haven't watched my How to Quickly Add Animated Characters Using Adobe Fuse,
[1:58] definitely do that because it's sort of a prequel to today's tutorial.
[2:03] In it, I show you how to create your own characters using the Adobe Fuse software,
[2:08] which is free for everyone in its current beta stage.
[2:12] And I don't really think it will get out of this beta stage anytime soon.
[2:16] So either head out to the tutorial or simply use your own animated character.
[2:21] Very quickly, here you can see me importing the character from Fuse and Mixamo.
[2:25] This one is in Colleta format and you may actually want to check that your armature doesn't have any rotation or scaling.
[2:32] So that's why I hit Ctrl A here and apply both scale and rotation.
[2:38] Every time I want to create a garment in Marvel's Designer, which is supposed to conform to some pose character is making,
[2:46] the first step I do is adding a T-pose to the animation.
[2:50] The reason is we want to first create a clothing when the character is in its neutral pose
[2:55] and only then start animating it with the garment on.
[2:59] So that's why here I immediately go to the pose mode, select all my bones with A and switch to graph editor.
[3:07] Here I select all my keyframes and push them to the right forward in time.
[3:12] You can hit G and lock your axis on X to lock the movement of your keys only to the right.
[3:19] And let's push them so that the actual animation starts at round frame 30 or so.
[3:24] Then go back to frame 1 and here click on pose, clear transform and all.
[3:31] And in the 3D viewport hit I and choose available to add a keyframe for all your selected bones.
[3:38] This way we have keyed their position and rotation at the same time.
[3:42] Now when you scrub through your timeline you can see that the pose linearly transforms from the T-pose to our animation.
[3:49] Here I also delete other keyframes that I don't need in this case since I want this pose right here to be the end pose.
[3:57] Something you can do as well before exporting to Marvel's Designer is to bake your keyframes.
[4:03] For that just go to pose, animation and bake action where you just choose your end frame, in my case it's 59.
[4:11] Click OK and voila all your frames are baked so that there is a keyframe on each frame of your animation.
[4:18] Now all you have to do is to select the whole hierarchy of your armature here and export it as FBX.
[4:26] Just check selected objects here and that's it.
[4:30] Now switch to Marvel's Designer to create our clothing.


### Marvelous Designer Intro [4:33]
**Transcript (timestamped):**
[4:34] What I really like about Marvel's Designer is the fact that you actually need to know only a very little to start messing around with some basic clothing and cloth simulation.
[4:45] So on the left you have this 3D viewport where we are going to be adjusting our garment by various hand and pin tools.
[4:54] By the way to move around in the viewport just hold down Alt and left click to rotate, middle mouse button to pan around and to zoom in and out just hold down right mouse button.
[5:07] Here on the right in the 2D pattern window we create pieces of our clothing and stitch them together.
[5:13] I will not go too deep on purpose here so let's just follow along and at the end of it you'll have enough knowledge about this software to make your own pieces of clothing.
[5:23] First off of course let's import our character.
[5:26] So here in import dialog choose FBX and find the model we've exported from Blender.
[5:32] You'll be asked various stuff here in the import tab but let's ignore everything now except for this autoscale option. Check that one.
[5:41] With that click OK and your character or rather an avatar, how it's called here in Marvel's Designer will be imported.
[5:49] On this character we'll be pinning pieces of clothing but first off let's jump up here into the animation mode and check whether we have our animation imported as well.
[5:59] Good it's here so let's get back to simulation mode.
[6:03] So as mentioned we'll be creating this basic garment, this is actually a piece of clothing called Hitton and over it we'll make this cloak in Ancient Greece it was called Klamis.
[6:14] Let's start with the Hitton.


### Making the Chiton Pattern [6:16]
**Transcript (timestamped):**
[6:17] For that let's focus on this window on the right where we'll create our patterns.
[6:22] Marvel's Designer actually works the same way as if you were cutting and sewing together a real piece of clothing.
[6:29] So you always have various shapes of fabric and by defining their shape and connecting their sides and corners together you form a garment.
[6:38] In our case let's not make it too difficult so let's just click on this rectangle tool here and drag it over the silhouette of our model like this.
[6:48] This way you've created your first piece of fabric and it immediately appears here as you can see.
[6:55] We can start playing with the shape of this fabric so let's hit this edit pattern tool and drag this bottom corner up like this.
[7:04] You can see that the shape changes in the 3D viewport as well.
[7:08] Now I don't want this piece to be just a rectangle I want the shape to taper a bit up here around the neck.
[7:14] So what we can do is hit this add point icon here and with it add two new points here.
[7:23] Now you can grab the points and push them closer together like this and also with the add point tool add two points up here as well.
[7:32] I want to have here a little curved hole made for the neck so grab another tool this one is called edit curvature.
[7:39] You can activate it with the C key and drag this segment down like this.
[7:44] Cool now we have our basic shape more or less done.


### Mirroring the Cihton Pattern [7:49]
**Transcript (timestamped):**
[7:52] Of course now we have created just the front part of our hiton.
[7:56] Now what we want to do is symmetrically copy this front part and mirror it over to the back.
[8:01] Fortunately Marvelous Designer has a tool that does just that.
[8:05] So just right click on your piece of clothing and click symmetric pattern.
[8:10] A mirrored copy is now created.
[8:13] Now I remember that in the beginning I had a hard time wrapping my head around the fact that I create some pattern here in the 2D pattern window
[8:21] and it is also created in the 3D viewport but when I start moving it here it doesn't move in the viewport.
[8:28] Think of it like a UV editor where if you move an island it doesn't move the geometry either.
[8:34] So here on the right side we create shapes and these stage as the same all the way
[8:39] and now here on the left we simulate those shapes and watch all the physics happen which I will show you in a moment.
[8:47] So after you symmetrized your pattern go into the 3D viewport, click on this new piece of fabric
[8:53] and with your manipulator push it behind the character like this.
[9:00] By the way I have my manipulator set to a world settings so they do not rotate along with your camera
[9:07] which is unbelievably stupid if you ask me so if you encounter this
[9:12] know that you have to switch to world coordinates up here in the preferences and gizmo option.


### Simulation and Sewing the Chiton [9:19]
**Transcript (timestamped):**
[9:21] Awesome with that done time to fire up the magic.
[9:24] In this case it's called simulate the magical simulate button of Marvelous Designer.
[9:29] Yes if you hit this button or the keyboard shortcut space bar well in this case stuff just falls down
[9:36] but that's just because we haven't connected any of our fabric parts together so that it hits the body and sticks to it.
[9:43] So first of all hit space bar again to stop the simulation and then hit CTRL Z to return it to the default state.
[9:51] By the way any time I activate the simulation mode this icon will glow yellow like this.
[9:58] Now let's go back to the 2D pattern window and hit this segment suing button.
[10:05] This will allow us to connect our two parts together and just like it says it will stitch them together along the edges.
[10:13] I want to have an open segment here for the hands to go through but I want to connect the sides of the hit on so that they wrap around the body.
[10:23] So with the segment suing tool keyboard shortcut N by the way just click here on this top part of the segment here and then on this part
[10:31] and connecting lines like these should appear.
[10:35] Do the same thing on the other side and now if you hit space bar to simulate well something's definitely happening.
[10:42] Stuff is connecting midair but it's still not sticking to the body because we haven't connected it up here.
[10:49] Again N for suing tool and connect these two edges on both sides.
[10:54] Be sure you are clicking on the same side of the edges not across because then your stitching might get crossed and create a mess.
[11:02] Let's see what happens now hit space bar and I always want to make this sound when the parts connect together.
[11:09] Sorry.
[11:11] Anyway we can do better here so disable the simulation mode with space bar hit control Z and let's add one little thing that will bring everything together
[11:21] and that is an internal polygon line.
[11:24] I know it doesn't sound too exciting but bear with me.
[11:28] Just click on both sides of this pattern here around the waist area and by the way since we've created our pattern symmetrically
[11:35] it automatically draws the line on the other side too.
[11:39] Now this line by itself doesn't do much but if you check this elastic button here
[11:46] well that's a different story.
[11:48] This elastic option basically brings the cloth together as if there was some sort of rubber band.
[11:54] The idea is that later I will put a belt on this waist so that this folded bit will be hidden beneath it.
[12:01] Let's just quickly raise the strength and lower the ratio here which makes the effect a bit stronger.


### Manually Adjusting the Cloth [12:07]
**Transcript (timestamped):**
[12:10] Now one thing that we can also do with the simulate mode active is with your regular select tool
[12:16] which you can activate by hitting Q is to manually play around with the fabric.
[12:21] You basically can grab it, push it where you want it, the whole thing will simulate and you can experiment like this however you want.
[12:28] This is what makes Marvel's designers so much fun.
[12:31] This ability to quickly stretch and tuck your folds in any place.
[12:35] I also lowered the ratio of the elastic line a bit more to about 15 and I decided to select the line,
[12:42] hit CTRL C, CTRL V and paste a duplicate of it a little lower.
[12:47] This way I created a bigger shrunk area around the waist which gives me more space for the future belt.
[12:54] Of course you can also create a belt in Marvel's designer but this tutorial is supposed to be basic so let's just keep things simple.
[13:03] A bit of further pushing and pulling in the simulation mode here and also one awesome thing about Marvel's
[13:09] is that even after you've simmed your garment you can still change the shape of the pattern.
[13:14] So you're free to go back here, hit the edit pattern button, hotkey Z by the way and change the shape however you want.
[13:33] What I also decided to do was to narrow down this neck part as well.
[13:38] Simply drag your points around then hit spacebar and stuff will re-simulate.
[13:44] And anytime you think the clothing needs some manual help don't hesitate to go in and fluff it like this.
[13:50] That's what this software is all about.
[13:53] One thing you can do too to change the behavior of the fabric is to go to this fabric menu up here,


### Changing the Fabric Type [13:56]
**Transcript (timestamped):**
[14:00] click on the fabric one and scroll down until you find this menu.
[14:05] Here you can pick from all sorts of fabric types so let's change ours to linen for example since in Ancient Greece they used it a lot.
[14:14] And you can see that when we hit simulate the clothing readjusts itself, the behavior of linen is slightly different now.
[14:22] You can of course experiment with the settings here manually as well so yeah do that.
[14:32] Now to actually have our hit on animated along with our character all you have to do is switch to this animation tab


### Animating and Pinning [14:34]
**Transcript (timestamped):**
[14:39] and hit this red camera button here and all you have to do is just wait for the software to compute the result.
[14:49] Easy peasy and you can of course then just go to simulation tab, hit spacebar and adjust your clothing further with the move tool.
[15:01] One thing you can see though is that the fabric has a habit of reading the text.
[15:06] One thing you can see though is that the fabric has a habit of returning to its original shape.
[15:11] I really wanted to stick to this concrete spot on the shoulder since that's how men in Ancient Greece wore their sleeves.
[15:18] So let's introduce another tool, this one called pin.
[15:22] For the pin to be usable you basically shape the clothing to your desired shape for example like this then immediately stop the simulation with spacebar and click on the pin tool.
[15:34] Now just select a few polygons you want to stay pinned and here we go they won't budge an inch now.
[15:42] Just repeat the process, fold your fabric however you want it, stop the simulation, pin polygons where you want them and then simulate again.
[15:53] If you don't like the way you pin your polygons you can always use the pin tool again, hold down control and select the polygons you already pinned and they will get deselected.
[16:08] You can then play around with your fabric some more, pin some new polygons and stick them to the place you've chosen.
[16:15] Now let's use this pin option to create a cloak or clemence for our character.


### Making the Cloak [16:19]
**Transcript (timestamped):**
[16:26] This is very easy but as surely you know any character with cloak is immediately 100% cooler.
[16:34] So yeah it's very very handy.
[16:36] It's pretty much like falling leaves or birds in the sky that make your shots always much more epic which is something I talk about extensively in my new course making a short film teaser in Blender.
[16:48] So don't forget to check that one out if you want to make your own Eevee scenes and videos.
[16:55] Now simply create a new rectangular shape.
[17:00] Let's quickly move it behind the character.
[17:06] Make it narrow up here and then in the 3D viewport pin the two corners of it.
[17:15] And the thing is now that the polygons are pinned if you hit spacebar for the simulation mode you can move them around however you want.
[17:22] So our goal now is to move them both on the neck of our avatar.
[17:28] So just move them around, pull on the fabric if needed and play with it until you get a shape you like.
[17:36] I'll actually speed up my clumsy process a bit here.
[17:45] It's so satisfying to watch right? I love the way the fabric moves and simulates in 3D space.
[17:53] What you can do at this point if you want to change the behavior of your cloaks fabric is to create a second fabric type in this window here.
[18:01] Select the clemence and change the type down here.
[18:07] Then in the fabric two settings use for example this silk preset or other wool presets anything you like really.
[18:17] And you can see the behavior of the fabric changing with the different presets you choose.
[18:24] In the end I went with the wool coat weight preset.
[18:31] At one point I then edited the shape of the pattern a bit more, made it longer and also trimmed it up here.


### Finalizing the Cloak [18:33]
**Transcript (timestamped):**
[18:39] Then I just continued the process of pushing the two pinned polygons and pulling on the fabric until I was satisfied with the result.
[18:48] One additional note here, any edge of your garment pattern can be made elastic.
[18:53] Just select it with the edit pattern tool shortcut Z and activate the elastic option here.
[18:59] And then again increase the strength and lower the ratio.
[19:03] Now some more pushing and pulling and let's get this fabric out of the hand of our character.
[19:10] That's very important and you can push it behind the character like this.


### Adding Pressure and Exporting [19:33]
**Transcript (timestamped):**
[19:34] One thing you can do to maybe simulate a bit of wind or a force pushing the fabric is to use this pressure option here.
[19:45] However, well don't go overboard with it or you'll end up like this.
[19:52] If you manage to completely mess up your garment you can always go here and hit reset 3D arrangement.
[19:58] But it's not really necessary here. Just pull on the fabric and get it back to the previous shape.
[20:07] And with the pressure set to negative one it's actually as if very low force pushed it away from the body.
[20:13] So it behaves a bit more floaty now.
[20:28] Cool, the very last thing we'll do here is to hit this remesh button.
[20:32] It actually does quite a decent job of creating a nice looking rectangular topology instead of a total mess of triangles.
[20:40] Now just shift select all the parts of your garment, hit file, export and obj select it.
[20:48] And you can safely ignore everything now. The only concern might be the scale of the thing and we will adjust that in blender quite easily.


### Importing into Blender [20:57]
**Transcript (timestamped):**
[20:59] So back to blender now. Here simply import your obj.
[21:08] If it's a different size scale it to its place. 0.1 worked for me.
[21:15] Now to improve the look you can smooth the normals.
[21:19] Hit ctrl 2 for smoothing the geometry and also with proportional editing activated by hitting O.
[21:25] Push and pull various areas where the geometry might protrude.
[21:30] Also before adding textures you can lay out the UVs which are however pretty much laid out for you from Marvel's designer.
[21:38] So just select the regions and pack them.
[21:43] Here I actually went in, textured the garment in substance painter very quickly, added some belt and little accessories.
[21:51] But that's a topic for another time.
[21:55] So my friends I hope I've picked your interest and introduced you to the wonderful tool called Marvel's designer in a quick and easy way.
[22:04] And as you can probably tell by the huge amount of icons and menus we haven't covered this tool is much more complex than what I've shown you here.
[22:13] So yeah can't recommend it enough. But that's quite enough for today. See you next time and Martin out.



---

## Captured Frames

- [2:59] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_000.jpg
- [6:38] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_001.jpg
- [7:39] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_002.jpg
- [10:31] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_003.jpg
- [12:21] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_004.jpg
- [17:06] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_005.jpg
- [20:32] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_006.jpg
- [21:19] tutorials/frames/how-to-quickly-create-clothing-using-blender-and-marvelous-designer/frame_007.jpg

---

## Structured Notes

### Core Technique
A Blender <-> Marvelous Designer round-trip pipeline for building simulated cloth garments (an Ancient-Greek chiton and cloak) on a rigged character: pose the character in Blender for export, pattern and simulate the cloth in Marvelous Designer, then reimport the finished garment mesh into Blender for cleanup.

### Summary
Martin Klekner shows the full external-cloth-sim workflow used for character garments before Blender had its own robust cloth tools. In Blender, an Adobe Fuse/Mixamo character's animation is shifted forward so frame 1 holds a clean T-pose, then keyframes are baked and the armature exported as FBX. In Marvelous Designer, the character imports as an "avatar"; flat 2D rectangular fabric patterns are drawn, edited (add points, edit curvature for a neckline), mirrored to the back, and stitched together with the Segment Sewing tool before running the cloth simulation so the fabric drapes and sticks to the body. Internal elastic lines gather the waist, the Pin tool locks fabric to specific spots (e.g. a shoulder clasp for the cloak), and fabric presets (linen, wool, silk) change drape behavior. After remeshing to clean quad topology, the garment exports as OBJ and comes back into Blender for scale correction, smoothing, and proportional-editing touch-ups before texturing (in Substance Painter, only briefly mentioned).

### Key Steps
1. **Prep the character pose in Blender**: apply scale/rotation on the imported armature (Ctrl+A), enter Pose Mode, select all bones (A), and in the Graph Editor select all keyframes and slide them forward in time (G, X to lock the X/time axis) so the timeline's frame 1 is free.
2. **Create a clean T-pose at frame 1**: go to frame 1, Pose > Clear Transform > All, then in the viewport press I > Available to key only the properties already keyed (location + rotation) for all selected bones — this linearly blends from the T-pose into the start of the original animation as you scrub forward.
3. **Bake and export**: delete any now-unneeded keyframes, then Pose > Animation > Bake Action (set the end frame to the animation's last frame) to get a keyframe on every frame; select the full armature hierarchy and File > Export > FBX with "Selected Objects" checked.
4. **Import into Marvelous Designer**: File > Import > FBX, enable the Autoscale option on import so the character avatar comes in at the correct real-world scale; check the Animation tab to confirm the baked animation imported, then return to Simulation mode.
5. **Pattern the chiton**: in the 2D Pattern window, use the Rectangle tool to draw a fabric panel over the character's silhouette; refine it with the Edit Pattern tool (drag points/edges), the Add Point tool (insert new corner points), and the Edit Curvature tool (hotkey C, drag a segment to create a curved neckline).
6. **Mirror and position**: right-click the pattern piece > Symmetric Pattern to mirror it into a back panel; in the 3D viewport, grab the new piece and push it behind the character (switch the manipulator/gizmo to World coordinates in Preferences > Gizmo if it's rotating with the camera, which is undesired).
7. **Stitch with Segment Sewing**: hotkey N (Segment Sewing tool), click one edge segment then its matching segment on the other pattern piece to connect them — leave openings for the arms, stitch the sides so the fabric wraps the torso, and stitch the shoulder seams; press Spacebar to Simulate (icon glows yellow while active) and Ctrl+Z / Spacebar to stop and reset.
8. **Gather the waist with an Internal Line + Elastic**: click both sides of the pattern near the waist to add an Internal Polygon Line (auto-mirrors since the pattern was created symmetrically), enable its Elastic option, then raise Strength and lower Ratio to cinch the fabric like a drawstring/future belt line.
9. **Manually sculpt drape**: with simulation running, use the Select tool (hotkey Q) to grab and tuck fabric folds directly in the 3D viewport — the sim reacts live; pattern shapes can still be edited after simulating via the Edit Pattern tool (hotkey Z).
10. **Change fabric behavior**: Fabric menu > pick a preset (e.g. Linen) to change drape/stiffness characteristics; re-run Simulate to see the new behavior, or hand-tune the underlying cloth parameters.
11. **Bake the garment to the animation**: switch to the Animation tab and click the (red camera) "Freeze"/simulate-to-animation button, wait for it to compute cloth motion across all baked frames, then return to Simulation mode to spot-fix with the move tool.
12. **Pin fabric for the cloak**: draw a new rectangular pattern for the cloak (Klamis), position it behind the character, and Pin its two top corners (Pin tool) so they can be dragged to a fixed spot (e.g. the shoulder clasp) without the simulation pulling them back to the pattern's rest shape; Ctrl+click a pinned polygon with the Pin tool to unpin it. Assign the cloak its own Fabric Type (e.g. wool coat weight or silk preset) independent of the chiton.
13. **Optional pressure/wind and cleanup**: the Pressure parameter (e.g. -1) simulates a light outward force for a floatier drape; Reset 3D Arrangement recovers from an over-messed simulation; finish with the Remesh button for clean quad-ish topology instead of dense simulation triangles.
14. **Export and reimport**: select all garment pattern pieces, File > Export > OBJ (ignore most options except scale, which is corrected in Blender); back in Blender, import the OBJ, rescale if needed (0.1 worked for this file), Ctrl+2 (or Shade Smooth) to smooth normals, and use Proportional Editing (O) to push/pull any protruding geometry; UVs come pre-laid-out from Marvelous Designer, so just select regions and pack islands before texturing.

### Nodes / Settings
- **Blender (pre-export)**: Ctrl+A (Apply Scale/Rotation on armature), Pose Mode > select-all (A), Graph Editor keyframe shift (G, X), Pose > Clear Transform > All, I > Available (partial keyframe insert), Pose > Animation > Bake Action, File > Export > FBX (Selected Objects checked).
- **Marvelous Designer 2D Pattern tools**: Rectangle, Edit Pattern (drag points/edges), Add Point, Edit Curvature (hotkey C), Symmetric Pattern (right-click context menu), Segment Sewing (hotkey N), Internal Polygon Line + Elastic (Strength/Ratio sliders), Pin tool (Ctrl+click to unpin).
- **Marvelous Designer 3D viewport**: Simulate toggle (Spacebar), Select/move tool (hotkey Q) for live fabric manipulation, Reset 3D Arrangement, Remesh button, Pressure parameter (negative values = outward force).
- **Fabric menu**: per-pattern-piece Fabric Type presets (e.g. Linen, Silk, Wool Coat Weight) controlling drape stiffness/weight.
- **Animation tab**: bake/compute button (freezes the cloth sim across the full baked FBX animation) so the garment follows the character's motion.
- **Export**: File > Export > OBJ (garment pieces selected).
- **Blender (post-import)**: Import OBJ, manual scale correction (e.g. 0.1), Ctrl+2 / Shade Smooth for normal smoothing, Proportional Editing (O) for spot mesh fixes, UV Editor to select/pack the Marvelous-Designer-generated UV islands.

### Difficulty
Intermediate

### Blender Version
Blender 2.8 (Release Candidate) for the Blender side; Marvelous Designer (version not specified) for the garment patterning/simulation.

### Tags
cloth, organic, animation, intermediate

---

## Related Tutorials
- [Master Blender Sculpting: Every Brush Explained](master-blender-sculpting-every-brush-explained.md) — shares the cloth/organic/intermediate focus; its cloth-simulation sculpt brush family (Drag/Expand/Bend/Twist Cloth) is a native-Blender alternative to the external Marvelous Designer draping shown here.
- [Realistic Cloth Physics in Blender – Full Tutorial](realistic-cloth-physics-in-blender-full-tutorial.md) — covers the same garment-draping goal using Blender's native Cloth modifier instead of Marvelous Designer, useful as a no-external-software comparison.
- [Blender NEW Cloth Simulator changes EVERYTHING!](blender-new-cloth-simulator-changes-everything.md) — modern (5.2) native alternative to this tutorial's external MD pipeline, covering pinning, tearing, and organic cloth behavior directly inside Blender's Geometry Nodes cloth system.

---
title: How to make awesome Topology Animation | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=m7dccc-J9aQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.2.0 -- observed in frame_000"
tags: [animation, rigging, camera, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to make awesome Topology Animation | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=m7dccc-J9aQ)
**Author:** Blender Secrets
**Duration:** 19m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey friends, a lot of people seemed to like this animation, so I figured out to make a
[0:16] little tutorial about it.
[0:19] It's actually pretty simple, once you figure out the steps that you need to do.
[0:24] Let me just play it, so you can see that it's actually playing in real time.
[0:28] This is all happening in real time.
[0:30] I'm just playing like the viewport.
[0:34] It's very light, so it's almost 100 frames per second.
[0:37] And if I press zero, I go out of the camera, and you can see I can just rotate around this
[0:42] while it's all happening.
[0:43] And please don't look at the back of the hand, because there are triangles.
[0:47] But yeah, you can't really tell, but it's actually if I stop playing.
[0:56] If I just scrub through the timeline like this, if you keep your eye here on the outliner,
[1:02] you'll see it keeps switching to the next cube, because on four, five, six, seven, and
[1:14] you can actually, you can't keyframe animate the viewport visibility, but you can keyframe
[1:20] animate this icon.
[1:23] I don't know what it's supposed to be.
[1:27] Globally disabled in viewports icon.
[1:30] So you can turn that on here, and then you can animate it simply by hovering over it
[1:35] and pressing I.
[1:38] So you can enable or disable it and then press I, and then you will set a keyframe for that.
[1:44] And so that's how you animate the visibility of all these different cubes.
[1:47] And really, if we just go back to the first one, now the first cube is selected here.
[1:56] And as you can see, it only has some keyframes on the timeline.
[2:01] And in the shape keys here, scrubbing between these two keyframes, and you can see that the
[2:08] value of the shape key is changing.
[2:10] And you can see that the edge is moving from the very edge to the middle of the box.
[2:18] And then when we go a little bit further, it switches to the next box.
[2:21] And it also just has one shape key, which goes from this to this.
[2:29] And then if we go a bit further, we have another shape key, and that's the one that just flattens
[2:33] the hand.
[2:37] And then there's this shape key, which just says this box has one shape key to change
[2:42] the shape of this flattened hand and so on.
[2:49] It's all very simple because shape keys can't add geometry.
[2:54] So all you can do is you can start with the geometry you want to end up with.
[2:59] And then you just make a shape key for when the geometry is hidden.
[3:05] Even here, those extruded fingers are still there, but they're just, I don't know if I
[3:10] can show you.
[3:11] They're just very close to these vertices.
[3:15] So the way you can do that is just, you just select one of the first two, and just press
[3:24] double G, and then you just slide it.
[3:28] So double G, and you have to make sure you go in the right direction.
[3:33] So now it looks like there are no vertices there, but actually they are there.
[3:41] And so every step is just one shape key that adds, actually that hides some geometry that
[3:53] is in that next stage.
[3:58] And so it goes through this whole list.
[4:01] And the fun thing is, yeah, you can play it back and you can see it all move and you can
[4:06] add a camera.
[4:18] And at the very end, there is a rigged hand.
[4:26] So by the time we're in a cube 22.
[4:30] I guess I have to enable the metric here.
[4:33] I guess you have to select the metric to be able to go to post mode.
[4:37] So yeah, this one is just able to animate this one hand.
[4:43] All the previous hands didn't have an armature.
[4:46] And this hand, I just added a metric.
[4:54] You have the Rigify Metrics.
[4:57] And as you know, you now have to enable Rigify.
[5:01] I guess you can still enable Rigify in the add-ons.
[5:07] But some things like Rigify, Skinify, for example, that's an extension now.
[5:17] But Rigify, if you enable that in add-ons, then you can just add like a human and then
[5:24] you can just delete all the bones that you don't need.
[5:27] That's a very easy way to get some good hand bones.
[5:38] And the camera loops.
[5:41] I just hand animated the camera as best I could just by locking it to view.
[5:51] I can just click on the camera to view.
[5:57] And then you can just hold down the middle mouse button and rotate the camera and just
[6:05] press I to the key frame.
[6:07] So that's how I did the initial camera animation.
[6:13] And then I added a few more key frames in between to make the animation a little bit
[6:17] better.
[6:18] But then in the end, I added the camera shakeify add-on from Ian Ubert, where you just add
[6:27] it by clicking on plus.
[6:31] And then you can choose one of these.
[6:33] You can just increase how much it wobbles and stuff.
[6:40] And it really adds a lot.
[6:42] Like if you remove this, it's just kind of a boring linear camera movement.
[6:48] And yeah, what else can I tell you about this?
[6:50] It's pretty simple, but let's just make one.
[6:55] So let's say we have this cube and we want to insert and then extrude and insert and
[7:02] extrude inwards or something.
[7:04] And we want to do this as an animation.
[7:08] So what we can do, we can work backwards from what we have, or we can just start with
[7:16] a new one.
[7:18] And we can already start on the first cube with the inset.
[7:22] So let me just turn on the wireframe so we can always see what we're doing even in object
[7:28] mode.
[7:30] So add a shape key, add another shape key, set it to one.
[7:37] And then you just, in this case, I can just scale this up or let me see how can I do this.
[7:43] Yeah, also by pressing double G.
[7:49] And then if I go back to object mode, I can now control, I don't know if you can see it,
[7:54] but I can now control that inset with a shape key.
[8:03] And instead of adding more shape keys and getting super confused, I am just going to
[8:06] duplicate this guy and I'm going to hide the first one.
[8:12] So now I just have this one.
[8:15] And I don't want to keep these shape keys.
[8:17] I want to apply them and do that by pressing control A and going to visual geometry to
[8:22] mesh.
[8:24] And I'm not setting any keyframes of animation just yet.
[8:29] So for the next stage, we want to extrude this.
[8:33] And I haven't set any shape keys yet.
[8:34] I'm just working on the geometry.
[8:38] And now a shape keys, set the second one to one.
[8:44] And then this, I'm just going to press double G until it's there.
[8:49] So now in object mode, I have this next stage.
[8:56] So let's continue, duplicate it with shift T, hide this one.
[9:00] So now I have only this one.
[9:04] First of all, we'll apply the shape keys, visual geometry to mesh.
[9:08] And then let's see, we can inset this again.
[9:14] Shape key for that, set it to one, edit it, dot G.
[9:20] Now we have this next one.
[9:23] So I have this new one, I'll apply the geometry.
[9:28] Maybe we can just extrude inwards.
[9:34] As shape keys set to one.
[9:37] And let's see, move it with double G.
[9:42] So now we have the shape key to make this whole.
[9:45] So we have this, we have this.
[9:50] We have this.
[9:57] So now we are going to animate these.
[10:00] And we will need to have this icon enabled.
[10:04] And first of all, let's just enable the visibility of all of these.
[10:08] I'll show you why in a minute.
[10:10] And I'll also open a dope sheet.
[10:14] And here you have some buttons only show selected.
[10:19] We will disable that.
[10:20] And here is only show errors.
[10:23] Let's see, show hidden.
[10:25] This way all of the keyframes will be visible of all the objects, which is convenient sometimes.
[10:31] So, well, let me just turn this off for a bit.
[10:36] Let's play.
[10:37] So about here, after 33, let's say after 30 frames,
[10:43] we want to have this end result.
[10:46] I am going to press I over this value field here.
[10:51] And then if we go back to zero or let's hit 10, then we set the value to one.
[10:58] So now we've keyframe animated the movement.
[11:08] And as soon as this value is a one,
[11:11] I will switch to another cube.
[11:13] So I will set a keyframe or the visibility of this
[11:18] and the invisibility of the next one.
[11:23] And then I will go to the next frame,
[11:26] pressing the right arrow key on the keyboard.
[11:30] Let me just enable the viewport visibility here.
[11:33] And then I will make this physical press I to keyframe it, make this one invisible, press I to keyframe it.
[11:40] So now there's what's called a Texas switch between these two cubes.
[11:46] On frame 30, their previous box is visible.
[11:49] And on frame 31, the next one is visible.
[11:53] And so we need to select the next one in the outliner here.
[11:57] And let's check.
[11:59] Okay, so we can set a keyframe for the value one.
[12:02] And then let's just go a bit further on the timeline.
[12:08] And set keyframe value to zero.
[12:13] So this is what we have so far.
[12:18] And as soon as this is fully extruded, we can do the same thing where we just set keyframes for the visibility of this one and the next one.
[12:26] Then on the timeline, go forward one frame.
[12:29] Be careful that you don't press back or forward here because that this messes up your outliner.
[12:35] Just hover the mouse over the timeline or the dope sheet.
[12:41] You can see why I have the dope sheet open.
[12:43] You can see all the keyframes and on the timeline for some reason, there's just no keyframes.
[12:47] I don't know what the reason is behind that.
[12:49] But anyway, next keyframe, we will make that one invisible and the next one visible.
[12:56] So it switches between box one.
[12:59] Oops.
[13:00] It switches between box one and two.
[13:04] And so we select the box two.
[13:07] And let me see.
[13:09] Yeah.
[13:10] We need to set a keyframe for that.
[13:12] Go forward a bit.
[13:14] Set a keyframe for that.
[13:17] Inset.
[13:18] So now we have that in set.
[13:21] And we can again animate the visibility in the outliner.
[13:32] So now we can go from box two to three and select box three.
[13:37] And we need to first have this keyframe value and then a bit later have the whole like this.
[13:45] Okay.
[13:46] So let me just set the length to 120 frames.
[13:54] I prefer to set this to 60 frames per second because it's really smooth.
[13:59] And if we play it now, it'll play back way too fast.
[14:02] So what we can do is put the cursor here in the beginning of the timeline, press A to select all of the keys and then scale from there.
[14:11] You can hold shift to have a bit more control.
[14:18] Okay.
[14:19] That's a bit more reasonable.
[14:20] So we just make it 240 frames.
[14:27] So now we get this.
[14:37] So that's the basic principle of hardworks.
[14:40] To add a camera, let's see, just lock the camera to view.
[14:47] Then we can hold shift and middle mouse button to pan or middle mouse button to rotate.
[14:56] And we can just set the keyframe representing I, then go for the time and maybe just get a bit closer to this.
[15:08] Set another keyframe and maybe another keyframe.
[15:15] So what do we have?
[15:16] Nothing.
[15:17] And why is that?
[15:19] I guess because I hadn't selected my camera.
[15:21] So I've no idea what I was setting keyframes for, but you know, there you go.
[15:25] So press I and rotate the camera bit, press I again.
[15:41] It's zoom in on that.
[15:46] So we get something like this.
[15:49] And you have to know that you set these keyframes, you have to compensate a bit for this wild movement.
[15:56] So you have to go to these in between frames and just clean that up a bit.
[16:09] Here it still goes too far to the left.
[16:18] It's not really easy to animate noise camera movement, but I have a good trick for that.
[16:24] And I'll show you in a bit.
[16:33] So okay, that's already more passable.
[16:36] And as you can see, it really moves very fast.
[16:41] So I'm thinking about maybe making it a bit longer, maybe twice as long.
[16:47] So I'm just gonna select all of these and scale them.
[16:53] Let's see what that's like.
[16:55] Yeah, that's much better.
[17:02] And there's some wobble here.
[17:16] Okay, good enough.
[17:18] And then we go to the camera tab and we use the camera shake file at all.
[17:24] And camera shake file, you can just download it from GitHub.
[17:28] I will share the link in the description.
[17:30] It's just something made by Ian Ebert and a friend of his.
[17:34] And it's based on tracked camera shots from real life.
[17:39] So just click on plus.
[17:42] And let's just see what that does.
[17:43] So it adds a lot of camera shake, but you can reduce the influence.
[17:57] And diminish the effect of it.
[18:00] Or you can try a different one.
[18:07] And somehow this really makes the camera move a lot better, I think.
[18:14] If you want to loop it.
[18:16] So in my previous hand animation, I had it loop so that the hands are placed by a box and then it starts over again.
[18:24] But you need to make sure that you have the starting camera keyframe and that you duplicate it at the end.
[18:33] And also that you keyframe animate the influence to go down to zero because otherwise the shaking won't match up with the beginning of the loop.
[18:41] So you can also just hear, like if at the end, if you want to keyframe animation.
[18:46] Here, if you want to the influence to go from this to zero, you just do that.
[18:53] So here, the influence at the end goes to zero.
[18:56] And then in the beginning, you also have it at zero.
[18:59] And then it gradually ramps up.
[19:01] So the keyframe for that.
[19:03] That way there won't be a visible jump when the video loops.
[19:07] So yeah, that's how we do it.
[19:10] I don't think there's anything else I can add to this.
[19:13] But if you have any questions, please put them in the comments and I'll try my best to answer.
[19:19] Thanks for watching.



---

## Captured Frames

- [0:28] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_000.jpg
- [1:23] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_001.jpg
- [2:01] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_002.jpg
- [7:22] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_003.jpg
- [8:03] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_004.jpg
- [10:43] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_005.jpg
- [13:54] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_006.jpg
- [18:00] tutorials/frames/how-to-make-awesome-topology-animation-blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
A "topology reveal" animation built from a chain of separate objects (one per modeling stage), each holding a single Shape Key that morphs a hidden final-geometry detail into view; keyframing each object's viewport-visibility icon in lockstep with its Shape Key value creates a seamless illusion of one continuously-evolving mesh — finished off with a hand-animated, Camera Shakify-enhanced camera fly-through.

### Summary
Frame 000 shows the technique's real-time payback: a simple ridged box shape mid-scrub in the Dope Sheet, with many objects listed in the Outliner (right) each carrying dense keyframe rows — confirming many separate objects drive the illusion. Frame 001 shows a later stage of the same sequence — a hand/glove-like shape with articulated finger-like extrusions, still using the same object-swap+shape-key system, Dope Sheet visible below with keyframes for camera and multiple cube objects. Frame 002 shows the starting point of the from-scratch demo: a plain selected cube with the Item panel open showing Vertices/Edges/Faces/Triangles counts. Frame 003 shows an Inset operation applied to the cube's top face (the small inset square highlighted), the first geometry change that will be "hidden" behind a shape key. Frame 004 shows the Shape Keys panel with a "Key 1" shape key added and set to Relative, Value field visible at the bottom-right — the mechanism for storing an geometry-reveal state per object. Frame 005 shows the object back at its base (un-keyed) cube shape with the Shape Keys panel still open and a Timeline below, right before extruding/inset work continues on the geometry. Frame 006 shows a further-along stage: a stepped cube-on-cube form with an inset recess on top, Dope Sheet showing accumulated keyframes and an "Enter" hint near Output settings, illustrating render-length/output setup partway through the tutorial. Frame 007 shows the finished camera setup: an isometric view of the stepped cube form with the Camera Shakify panel open in the sidebar (Style dropdown, Influence, Scale, Manual Timing fields) — the add-on used to give the hand-animated camera a natural, tracked-shot-like wobble.

### Key Steps
**Understanding the illusion (analysis of the original animation, ~0:00-6:50):**
1. The animation is not one continuously-modeled mesh — it's a sequence of separate cube objects, one per "modeling stage," stacked in the same location. You cannot keyframe an object's viewport visibility (the eye icon) directly, but you *can* keyframe the "Globally disabled in viewports" icon: enable it, hover over the icon, press I to set a keyframe, toggle it, press I again — this is what makes each object appear/disappear at the right moment.
2. Each object carries exactly one Shape Key that animates from a starting shape to a target shape (e.g. an edge sliding from the boundary to the middle, or a form flattening). Since Shape Keys can only *move* existing vertices, not add new geometry, the trick is to always start modeling with the *end* geometry already present, then hide the "future" detail by sliding its vertices (G,G — double-tap G to slide along the surface) very close to neighboring vertices so it's visually imperceptible until revealed.
3. The full sequence is just many of these single-shape-key objects handed off to each other via synchronized visibility keyframes, right up to a final stage with a rigged hand (Rigify human metarig with unneeded bones deleted, or the separate Rigify-adjacent "Skinify" extension for skinning).
4. The camera move was hand-animated by locking the camera to the viewport view, orbiting/panning with the middle mouse button between keyframes (I to key), then finished with the free **Camera Shakify** add-on (by Ian Hubert) for a naturalistic tracked-shot wobble — installed from GitHub, added via the "+" button in the camera's sidebar panel, with adjustable Influence/intensity per shake style.

**Building one stage from scratch (~6:50 onward):**
1. Enable Wireframe display (so geometry stays visible even in Object Mode) and start with a base cube.
2. Model only as far as the *next* stage requires (e.g. Inset a face), add a Shape Key, set its Value to 1, then in Edit Mode use double-G to slide the newly-inset geometry back until it's hidden/flush with its neighbors again — this "shape key = 1" state now represents the un-revealed look, while returning the Shape Key's Value to 0 reveals the inset.
3. Once satisfied, go back to Object Mode; the inset is now controllable purely via the Shape Key slider.
4. Duplicate (Shift+D) this object for the *next* stage and hide the original — don't keep stacking more Shape Keys on one object, since that gets confusing fast. On the duplicate, apply the existing Shape Key permanently via Ctrl+A > Visual Geometry to Mesh (this also clears the Shape Key stack) before modeling the next detail (e.g. Extrude) and repeating the add-Shape-Key / double-G-hide / duplicate cycle.
5. **Animating the sequence:** open a Dope Sheet, disable "Only Show Selected" and enable "Show Hidden" so every object's keyframes stay visible regardless of selection — critical for orchestrating many objects at once. For each stage: set a keyframe (I) on the current object's Shape Key Value at 0 on an early frame, then a keyframe at Value 1 roughly 30 frames later; at the frame where Value reaches 1, set a visibility keyframe (I over the "globally disabled" icon) making the current object invisible and the next object visible in the same frame, then advance one frame (right arrow — hover over the Timeline/Dope Sheet first, not other panels, to avoid corrupting the Outliner selection) and set the opposite visibility keyframes there for a clean cross-fade/swap; repeat down the whole chain of objects.
6. **Timing/pacing:** set project frame rate to 60 fps for smoothness; if the whole sequence plays too fast, put the playhead at frame 0, select all keyframes in the Dope Sheet (A) and scale them (S, hold Shift for finer control) to stretch the timing uniformly — the author stretched a shorter take out to 240 frames this way.
7. **Camera animation:** lock the camera to the current view (View menu), then Shift+middle-mouse to pan / middle-mouse to rotate between keyframes, pressing I on the camera to key each pose — expect wild/jerky results at first and plan to go back and manually clean up in-between frames. Add Camera Shakify afterward via "+" in its panel, tune Influence to taste, and try different shake style presets.
8. **Looping the camera shake cleanly:** duplicate the starting camera keyframe at the very end of the timeline, and keyframe the Camera Shakify Influence value down to 0 at both the very start and very end of the loop, ramping up from 0 shortly after the start — otherwise the shake pattern will visibly jump/desync where the loop repeats.

### Nodes / Settings
- **Animation:** Shape Keys (Basis + one "Key 1" per object, Value 0-1 keyframed), Object visibility keyframing via the "Globally disabled in viewports" icon (not the standard eye-icon visibility, which can't be keyframed), Dope Sheet filters (Only Show Selected off, Show Hidden on).
- **Rigging (final stage only):** Rigify metarig (Human preset, prune to just hand bones) or the separate Skinify extension for auto-skinning.
- **Add-ons:** Camera Shakify (free, by Ian Hubert, GitHub-installed) — Style presets, Influence, Scale, Manual Timing.
- **Modeling combo per stage:** Inset (I) / Extrude (E) on the target detail, double-G (G,G) vertex/edge slide to visually hide the new geometry, Ctrl+A > Visual Geometry to Mesh (bake/clear Shape Keys before the next duplicate).
- **Timing:** 60 fps project setting, Dope Sheet select-all (A) + Scale (S, Shift for precision) to retime a whole keyframe range at once.

### Difficulty
Intermediate

### Blender Version
Not specified — the video notes Skinify is "an extension now" separate from Rigify, and uses the Camera Shakify add-on; consistent with a recent Blender 4.x/5.x release.

### Tags
animation, rigging, camera, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library cover shape-key-driven "topology reveal" object-swap animation or the Camera Shakify add-on yet.

---
title: Combining Ragdoll physics with Motion Capture animation | Rokoko Smartsuit 2 | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=d16IOajUwIc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/
frame_count: 0
frame_status: pending-selection
---

# Combining Ragdoll physics with Motion Capture animation | Rokoko Smartsuit 2 | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=d16IOajUwIc)
**Author:** Blender Secrets
**Duration:** 11m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] For a while now I've been trying to find an easy-to-use method for combining ragdoll physics with mockup animation, for example for getting up after a fall. With, shall we say, limited success.
[0:13] The reason I kept failing was because I was trying to make everything really complex, trying to do everything with one rig.
[0:21] By simplifying things as much as possible, I was finally able to mix ragdoll and mockup animation.
[0:28] A big thank you to Rococo for making this video possible.
[0:32] First you'll need a ragdoll that has rotation constraints, so that its arms and legs don't move in impossible angles. I've described in previous videos how to make this kind of ragdoll.
[0:42] But since I've already made it and fine-tuned the constraints, you can skip all that work and just download it from my website.
[0:49] Note that the hitboxes have to be set to start deactivated. That way the physics simulation starts only after they're hit by another object.
[0:57] As a side note, the rigidbody connection empties have to be parented to the hitboxes, so that the connection works well. But don't worry, this has already been taken care of in my ragdoll file.
[1:07] Then record some mockup actions for your scene.
[1:10] If you need some special kicks or actions that you're not able to do or you don't have a mockup suit, the Rococo app has a motion library of performances that you can choose from, including some free ones.
[1:21] In case your character still needs to be rigged, I recommend doing this online in the free Mixamo AutoRigger.
[1:26] Make sure that you download it in a t-pose and check automatic bone rotation when importing the file.
[1:32] As you can see, the auto-rigged character is now in a t-pose compared to the kind of t-pose it was in before. This will help a lot with properly retargeting the animation.
[1:42] I like to set the armature to in-front and to display as sticks.
[1:46] Import the fbx file of the mockup animation and use the free Rococo add-on to retarget it to your characters.
[1:54] I highly recommend renaming the armatures in advance. That will avoid confusion during the retargeting process.
[2:00] Pick the source and target armatures. Click on build bone list.
[2:05] Check the bone list for any mistakes and then click on retarget animation. You can delete the source armature.
[2:13] In this video I'm using the animation layers add-on.
[2:17] It's a commercial add-on and if you want a free alternative, I did make a couple of videos that you can check out.
[2:23] I recommend getting this add-on if you often do animation in Blender.
[2:26] To use it, first enable it, then add a new layer. Turn on auto-keying and add some adjustment keys.
[2:33] And that's all. It's very easy to use add-on and it really makes animating in Blender much more fun.
[2:39] Just remember to turn off auto-keying at the end.
[2:44] Append the ragdoll from my ragdoll-planned file.
[2:47] Open the collections folder inside of the file and append the ragdoll collection.
[2:54] Go to frame 1.
[2:57] Go to the point where your character has to do a stunt.
[3:00] Move it to roughly overlap the character.
[3:03] Parent a passive rigidbody, set to animated, to the bone of whichever body part first collides with the ragdoll.
[3:10] Here I'm moving the 3D cursor to the selected bone.
[3:15] Then any object added, like a cube, will be in that location.
[3:20] Scale it down.
[3:23] Turn the cube into a rigidbody.
[3:26] Set it to passive and check animated.
[3:29] Hold shift and select the cube and then the armature in object mode.
[3:33] Then go to post mode.
[3:35] Parent the cube to the bone by pressing Ctrl P and choosing bone.
[3:39] The passive rigidbody cube now follows the foot.
[3:43] Now bake the rigidbody cache.
[3:46] The floor needs to be a passive rigidbody object.
[3:50] Instead of parroting a passive rigidbody to the kicking foot,
[3:53] you could also use a separate animated passive rigidbody object.
[3:57] That way you have more control over the speed and the movement.
[4:01] Once you've got something that you're happy with, select all the hitboxes while holding shift.
[4:07] Then bake the simulation to keyframes.
[4:12] Now we have the rigidbody cache baked to keyframes.
[4:15] This way we can't accidentally lose the rigidbody animation.
[4:19] You can now hide or delete that cube.
[4:21] One issue that we need to fix is that the rigidbody animation starts too early.
[4:27] Select all the hitboxes in the Ractal Collection.
[4:32] Then move all the keyframes, a couple of frames forward, in time.
[4:35] You can move the keys by pressing G.
[4:38] Now the impact looks better.
[4:43] Unhide the hidden character and create a new animation layer.
[4:48] Rename the new layer stunt for clarity.
[4:51] Go to post mode. Make sure that auto-keying is enabled.
[4:55] Select all the bonds and set a location and rotation keyframe just before the impact.
[5:00] Then move forward in time a few keyframes and post a character to match the Ractal.
[5:08] The poses don't have to perfectly match the Ractal as long as it looks okay.
[5:18] After finishing one pose, go forward in time a few frames and do the next one.
[5:33] To make things easier to see, select all the hitboxes.
[5:36] Then while holding Alt, check the in-front option.
[5:40] And while still holding Alt, set the display as to higher frame.
[5:47] Whenever you have bonds that are in a really weird pose, you can select them and then press Alt and R to reset their location.
[6:01] You don't even really need to set that many keyframes.
[6:04] You can set more keyframes to accurately follow the Ractal, but I find that a small amount of keys already looks fine.
[6:10] It depends on how realistic or stylized you want the results to be.
[6:15] Finally, add Mocap for the part after the Ractal animation, when the character gets back up.
[6:21] I recommend importing the Mocap FBX in a fresh planter file that has your character in it.
[6:26] Then retarget the animation as you've done before.
[6:30] You can delete keyframes that you don't need.
[6:35] Because of the physical difference between this character and myself, there's some clipping of the hands into the body.
[6:42] To adjust this, you can open the Graph Editor window and then in post mode select the bone that you want to adjust.
[6:49] Press the Home key if you don't see any of these keys in the Graph Editor.
[6:53] Double-click on one of the rotation channels.
[6:57] Then move the keys up or down on the Y-axis by pressing G and Y.
[7:02] This way you can make some quick adjustments.
[7:06] Open a dope sheet window and set it to Action Editor.
[7:09] Then name this action appropriately.
[7:14] Then save the file with a clear name.
[7:18] Back in our main file, open a non-linear animation window.
[7:24] Click this button to see only the animation of the selected object.
[7:29] Append the action from the other file.
[7:39] Select the top layer in the non-linear animation editor.
[7:43] Add a new track.
[7:46] Select the new track and press Shift A.
[7:50] Then choose the Getting Up action.
[7:54] Find the right point to start the action and press Y to split it.
[7:59] Then you can delete the part that you don't need.
[8:03] Set a blend-in value of one frame.
[8:09] We need to move this action forward in time.
[8:14] It looks like it should start around frame 400.
[8:17] As you can see, the Getting Up action starts in a very different location.
[8:22] Normally it would be easy to solve this by simply moving the root bone and setting keyframes for that.
[8:28] Unfortunately, Mixamo Rigs mysteriously don't have root bones.
[8:32] However, we can still kind of add a root bone ourselves.
[8:35] In Edit Mode, extrude a bone.
[8:37] In this case, I extruded it from the hip bone.
[8:41] Name it the root bone.
[8:44] Select the hips bone and parent that to the root bone.
[8:48] Now we can use this improvised root bone to change location and rotation of the character with some keyframes.
[8:54] Add a new animation layer.
[8:58] Select the root bone in Post Mode.
[9:00] Go to the last frame of the ragdoll animation and set a location rotation keyframe.
[9:06] Then go to the next frame and position the armature where it should be.
[9:12] I recommend using auto-keying for this so you can quickly iterate and find the right pose.
[9:18] Press back and forth to toggle the previous and next frame and compare visually where it should be.
[9:24] Now that the position is solved, there's still some ugly movement where the next action suddenly begins.
[9:30] Before we fix that, let's give a proper name to this animation layer.
[9:38] Create a new animation layer.
[9:43] On the last frame of the ragdoll animation,
[9:45] we can create a new animation layer.
[9:48] We can also create a new animation layer.
[9:51] On the last frame of the ragdoll animation,
[9:54] select all the bones except the root and set a location rotation keyframe manually.
[10:00] Go forward or view frames and set another location rotation keyframe.
[10:05] Copy the pose of the last frame of the ragdoll animation with Ctrl C.
[10:10] Go one frame forward and paste the pose with Ctrl V.
[10:14] Set a location rotation keyframe so that the pose is recorded.
[10:18] Now we need to move the armature back to the right location.
[10:22] I recommend turning on auto-keying for this.
[10:27] Like before, fine tune by visual comparison while toggling back and forth between those two frames.
[10:37] When that's done, don't forget to turn off auto-keying.
[10:48] Now the ragdoll end position blends to the getting up action.
[10:54] The blend is too fast, so we'll need to move that last keyframe.
[11:03] That looks better.
[11:05] Using this technique, we can create many seamless animations with virtual stunts.
[11:11] One last tip, if you run into these kind of shenanigans
[11:14] where the ragdoll explodes all over the place when you move it,
[11:17] one thing you can do is just temporarily remove the rigidbody world.
[11:23] Then you can move the ragdoll and add the rigidbody world back when you're done.
[11:30] Check my mocha playlist for more motion capture related videos
[11:33] or click the link to go to my website and download the ragdoll file.



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

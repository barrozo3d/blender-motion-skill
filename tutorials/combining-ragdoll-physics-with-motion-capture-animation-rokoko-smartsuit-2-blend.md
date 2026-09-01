---
title: Combining Ragdoll physics with Motion Capture animation | Rokoko Smartsuit 2 | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=d16IOajUwIc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.6.0 -- observed in frame_000"
tags: [rigid-body, simulation, animation, rigging, expert]
extraction_status: complete
frames_dir: tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Combining Ragdoll physics with Motion Capture animation | Rokoko Smartsuit 2 | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=d16IOajUwIc)
**Author:** Blender Secrets
**Duration:** 11m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:45] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_000.jpg
- [1:35] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_001.jpg
- [2:05] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_002.jpg
- [3:20] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_003.jpg
- [4:35] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_004.jpg
- [5:05] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_005.jpg
- [7:55] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_006.jpg
- [10:50] tutorials/frames/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend/frame_007.jpg

---

## Structured Notes

### Core Technique
Seamlessly blend Rigidbody ragdoll physics (for an impact/stunt/fall) with Rokoko motion-capture animation (for the walk-in and get-up), by treating the three phases as separate NLA-blended animation layers/actions rather than trying to force one unified rig to do everything — including an improvised "root bone" workaround for Mixamo rigs (which lack one) so the ragdoll's end position can be reconciled with the mocap's world-space starting point.

### Summary
Frame 000 shows the ragdoll setup being physically tested in isolation: a falling cylinder about to strike a cube collider, with a small humanoid ragdoll already knocked down nearby — confirming the pre-built ragdoll (with rotation-constrained joints) the author distributes for download. Frame 001 shows the Mixamo Auto-Rigger comparison: "Original" vs. "Auto-rigged" T-pose side by side, illustrating why re-downloading in T-pose with Automatic Bone Rotation matters for clean retargeting. Frame 002 shows the Rokoko Retargeting add-on's UI mid-process: a mocap skeleton, a small ragdoll rig, and the target character all visible together, with Source/Target armature dropdowns and a "Build Bone List" / retarget panel open. Frame 003 shows a hitbox cube with "In Front" display revealing the character's stick-figure armature bones through it, plus the Rigidbody World panel (Steps Per Frame, Solver Iterations, Split Impulse) in the sidebar. Frame 004 shows the ragdoll mid-stunt: the character's real mesh (pink) next to its blue ragdoll hitbox proxy, captured mid-fall/kick with visible physics deformation. Frame 005 shows a further stage of the same stunt, the ragdoll now airborne/tumbling next to the character's posed mesh — this is the hand-posed "Stunt" animation layer being fit to match the ragdoll sim's silhouette. Frame 006 shows the Non-Linear Animation editor with a "Getting Up" action strip (orange, selected) above two other layers, positioned in the 3D viewport where the character (small figure) stands separate from the ragdoll's resting pose. Frame 007 shows the same NLA strip now highlighted green (active/selected) with its blend-in region visible as a small triangular fade at the strip's start — the final blend-tuning stage.

### Key Steps
1. **Prepare a constrained ragdoll:** use (or download the author's pre-built) ragdoll rig with rotation constraints on each joint so limbs can't bend into impossible angles; hitboxes must be set to start **deactivated** so physics only kicks in once something else collides with them; rigidbody Connection Empties must be parented to their hitboxes for the joint constraints to actually work (already handled in the provided file).
2. **Record or source mocap:** capture motion with a Rokoko Smartsuit, or use Rokoko's motion library (including free entries) for actions you can't perform yourself.
3. **Rig the target character (if needed):** use the free Mixamo Auto-Rigger; download in T-pose with Automatic Bone Rotation checked on import — this produces a cleaner T-pose than the source mesh's original pose and is important for accurate retargeting later. Set the armature's Viewport Display to In Front + Sticks for clarity while working.
4. **Retarget mocap onto the character:** import the mocap FBX; rename both armatures beforehand to avoid confusion; use the free Rokoko Retargeting add-on — pick Source and Target armatures, click Build Bone List, review it for mistakes, then click Retarget Animation; delete the now-unneeded source armature afterward.
5. **(Optional) Use the Animation Layers add-on** (commercial; free alternatives exist per the author's other videos) for easier iterative posing: enable a new layer, turn on Auto-Keying, add adjustment keys, then remember to turn Auto-Keying back off when done.
6. **Set up the stunt/impact trigger:** append the ragdoll collection from the separate ragdoll file; go to the frame where the stunt should occur, move the ragdoll to roughly overlap the character. Snap the 3D cursor to the relevant bone (e.g. the foot that makes contact), add a small cube there (Shift+S or cursor-to-selected style workflow), scale it down, make it a Rigidbody set to Passive + Animated, then in Pose Mode select the cube then the armature and Ctrl+P → Bone to parent the cube to that bone — the passive rigidbody cube now follows the kicking foot and can trigger the ragdoll on contact. (Alternative: use a separately-animated passive rigidbody object instead of parenting to a bone, for more control over impact speed/timing.) The floor also needs to be a passive rigidbody collider.
7. **Bake the physics:** once satisfied, select all hitboxes and Bake the Rigidbody simulation to keyframes — this locks the ragdoll animation in permanently so it can't be lost or accidentally re-simulated; the trigger cube can then be hidden or deleted. If the ragdoll's reaction starts too early, select all hitboxes in the Ragdoll Collection and press G to shift all their keyframes forward in time together.
8. **Hand-pose a "Stunt" layer to bridge the mesh to the ragdoll:** unhide the real character, create a new animation layer named "Stunt"; in Pose Mode with Auto-Keying on, set a Location+Rotation keyframe on all bones just before impact, then step forward a few frames at a time, posing the character to roughly match the ragdoll's silhouette at each point (poses don't need to match exactly — "good enough" reads fine). Use Alt+click on In Front / Display As Wire toggles to apply the setting to all selected hitboxes at once for easier visual comparison; Alt+R resets a bone's rotation if it ends up in a broken pose. Fewer, well-chosen keyframes are often enough — density depends on how realistic vs. stylized the result should look.
9. **Add the "getting up" mocap for after the fall:** import that mocap FBX into a fresh file containing just the character, retarget as before, delete unneeded keyframes, and fix any clipping (e.g. hands into torso, from body-proportion mismatch with the original mocap performer) via the Graph Editor — select the bone, press Home to frame all its keys, double-click a rotation channel, then G, Y to nudge keys up/down on that channel. Rename the resulting action clearly in the Dope Sheet's Action Editor, and save that file separately.
10. **Blend the ragdoll end-pose into the "Getting Up" mocap via NLA:** back in the main file, open a Non-Linear Animation editor (optionally isolate to the selected object's tracks); append the "Getting Up" action from the other file; select the top NLA track, add a new track, Shift+A to add that action as a strip; trim its start with Y (split) and delete the unneeded portion; set a short Blend In value (e.g. 1 frame) and move the whole strip to roughly where it should start (e.g. ~frame 400).
11. **Fix root-bone-less Mixamo rigs:** Mixamo rigs don't ship with a root bone, which makes it hard to reposition the character in world space for a clean handoff between the ragdoll end pose and the mocap's own starting location. Fix: in Edit Mode, extrude a new bone from the hips, name it "root," then parent the hips bone to it — this improvised root bone can now be keyframed for Location/Rotation to reposition the whole character.
12. **Match the "Getting Up" clip's start position to the ragdoll's end position:** add a new animation layer; select the root bone in Pose Mode, set a Location+Rotation keyframe on the last frame of the ragdoll animation, then move forward a frame and reposition the armature to match visually (Auto-Keying on for fast iteration, toggling back and forth between the two frames to compare). Rename the layer clearly.
13. **Smooth the pose transition at the exact handoff point:** add another new animation layer; on the ragdoll's last frame, select all bones except root and manually set a Location+Rotation keyframe; step forward, set another keyframe; copy the last ragdoll-frame pose (Ctrl+C), paste it one frame later (Ctrl+V), and key that too so the pose is properly recorded; then move the armature back to the correct location with Auto-Keying, fine-tuning by toggling between the two frames — don't forget to disable Auto-Keying afterward. Adjust the final keyframe's timing/position if the resulting blend feels too abrupt.
14. **Troubleshooting tip:** if moving the ragdoll causes it to "explode" chaotically, temporarily remove the Rigidbody World, reposition the ragdoll, then re-add the Rigidbody World afterward.

### Nodes / Settings
- **Physics:** Rigidbody (Hitboxes: start Deactivated; Passive + Animated for trigger objects and the floor; Connection Empties parented to hitboxes for constraints), Rigidbody World (Steps Per Frame, Solver Iterations, Split Impulse), Bake to Keyframes.
- **Rigging/Retargeting:** Mixamo Auto-Rigger (T-pose download, Automatic Bone Rotation), Rokoko Retargeting add-on (Source/Target armature, Build Bone List, Retarget Animation), Ctrl+P → Bone (parent object to a specific bone).
- **Animation tools:** Animation Layers add-on (commercial; new layer, Auto-Keying, adjustment keys), Non-Linear Animation editor (tracks, strips, Y to split, Blend In value, isolate-selected-object toggle), Graph Editor (Home to frame keys, double-click channel, G+Y to nudge), Dope Sheet → Action Editor (renaming actions).
- **Pose tools:** Ctrl+C / Ctrl+V (copy/paste pose), Alt+R (reset bone rotation), Alt-click toggles (apply a display setting to all selected bones/hitboxes at once), improvised root bone (extruded from hips, hips reparented to it) for Mixamo rigs lacking one natively.
- **Viewport:** In Front display + Sticks (armature visibility through geometry).

### Difficulty
Expert

### Blender Version
Not specified — Rigidbody/NLA/Graph Editor workflow with the Rokoko Retargeting and (commercial) Animation Layers add-ons, consistent with modern Blender 2.9x-4.x.

### Tags
rigid-body, simulation, animation, rigging, expert

---

## Related Tutorials
- [Blender Tutorial - Control Physics Sims with Geometry Nodes (Beginner Friendly)](blender-tutorial-control-physics-sims-with-geometry-nodes-be.md) — shares rigid-body, simulation, animation; different domain (Geometry Nodes physics control) but directly relevant rigid-body-simulation fundamentals.
- [Blender Secrets - In Depth Cloth Sculpting tricks with Pose Brush](blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush.md) — shares simulation, rigging; same channel, complementary character-animation-plus-simulation technique.

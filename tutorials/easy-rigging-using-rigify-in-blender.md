---
title: Easy Rigging Using RIGIFY in Blender
source: YouTube
url: https://www.youtube.com/watch?v=RdTuAY23vzk
author: Grant Abbitt (Gabbitt)
ingested: 2026-07-20
blender_version: "4.3"
tags: [rigging, animation, beginner, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/easy-rigging-using-rigify-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Easy Rigging Using RIGIFY in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=RdTuAY23vzk)
**Author:** Grant Abbitt (Gabbitt)
**Duration:** 15m0s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Introduction & Overview [0:00]
**Transcript (timestamped):**
[0:00] In this video, I'm going to show you how you can rig your character using the Rigify add-on that ships with Blender,
[0:05] and it's a relatively easy process.
[0:07] This is a continuation of the tutorial for making low-poly, PlayStation-style characters.
[0:12] If you want to download this character to follow along, then check the links in the description,
[0:16] and you can find the previous tutorials there as well.
[0:19] And if you like my content, then there's lots of links to similar courses, which are more detailed and methodical,
[0:24] especially my animation course, if you want to animate your character.
[0:28] So let's rig our character.
[0:29] So we've got our basic character here, and the first thing I need to do is add my Rigify rig.


### Adding the Rigify Armature (Meta-Rig) [0:30]
**Transcript (timestamped):**
[0:34] Now, notice that my 3D cursor is up the top here, so it's best to have it in the world center,
[0:40] assuming that your character is also in the world center.
[0:43] So I'll press Shift S that will bring up my cursor pie menu, and I can bring the cursor to world origin just here.
[0:50] So you can see it in the middle there.
[0:51] Now, before adding the Rigify rig, you need to enable the add-on.
[0:55] You go up to Edit, Preferences, Under Add-ons.
[0:58] You should be able to search for Rigify here and just tick it to enable it.
[1:02] Once that's ticked, you can close this down, and when you press Shift-A to add,
[1:06] all go up to the Add menu up here.
[1:08] Under Armature, you should see some extra armatures.
[1:11] So we've got the Rigify MetaRigs just here, and the Human one is what we want to add.
[1:16] There are some other ones.
[1:17] There's some animals as well, which are very useful, and there's some basic ones just to give you a really basic rig.
[1:22] But the Human one up here is the one we want, so I can add that in, and you should see it add in like this.
[1:27] So we want to resize it to our character.


### Matching the Bones to the Character Mesh (Scaling/Positioning) [1:30]
**Transcript (timestamped):**
[1:30] Now, it's best to do this in Edit mode, but I'll show you what happens if you do it in Object mode.
[1:34] So I'll go to Front View with one of my numpad, or you can use the Cartesian coordinates up here.
[1:39] I can scale it up so it roughly matches my character somewhere around about there.
[1:45] Now, remember I did that in Object mode.
[1:46] That's important for later on.
[1:48] It's also tricky to see the bones.
[1:50] You can come down to the Object Data Properties here.
[1:52] I'll just bring up this menu.
[1:54] And under Viewport Display, we can turn on In Front so we can always see our bones from whatever angle we are.
[2:00] Go back to Front View though, and now I want to match up my rig to my character.
[2:04] So I'll go to Edit mode.
[2:05] So that's Edit mode up here.
[2:06] And it's really helpful to turn on the X Symmetry before you start modifying the shape.
[2:11] So I'll turn that on there.
[2:12] And now I can start moving my bones into position.
[2:15] Something that's quite useful if I zoom into the arm and move my 3D cursor now to the shoulder bone up here.
[2:20] I can press the Period key.
[2:22] That brings up my Transform Pivot Point menu.
[2:24] You can also find that in the middle here.
[2:26] And I'll change it to 3D cursor.
[2:27] The default is the median point just there.
[2:30] But I'll change it to 3D cursor.
[2:31] Now if I select these bones and press R to rotate, it will rotate around that 3D cursor, which is quite helpful.
[2:37] The Period key on your keyboard is the shortcut for that.
[2:40] And you do often want to change between bounding box center or median point to the 3D cursor.
[2:45] So I'll go back to the median point, select my end bones here for the hand and pull them into position.
[2:51] Elbow needs a little bit of adjusting there.
[2:52] And that's great.
[2:53] Let's go to Side View now.
[2:54] I'll bring the elbow back.
[2:55] I'll bring the shoulder back.
[2:57] And again, I'll select the hand and move that into position.
[3:01] Now for a low poly character like this that has joint fingers, I can remove some of these fingers.
[3:06] You do need to be a bit careful in Rigify which bones you remove because it can cause problems when generating the full rig.
[3:13] I'm going to keep this middle set here.
[3:16] So I'll go from this hand bone here down to the bottom here by holding down control and delete bones.
[3:21] Same for this one and same for this one.
[3:25] You must make sure you get the hand bone as well, which is the one at the top as well as all the finger bones.
[3:30] So I'll select these ones and move them across slightly and positioning the fingers can be quite awkward.
[3:35] So I'd have to go to Front View, line them up, Side View and line them up.
[3:39] What's a bit easier is if we turn snapping on and the snapping mode, if we change it to volume,
[3:43] that will snap to the center of the volume of any object.
[3:46] So if I press G to grab, move that into the end there, you can see right in the middle because it's snapped to the middle of this point in the object.
[3:53] So I'll just move these into position.
[3:55] So G to grab and be careful of that.
[3:58] If I just left click on this and move it, it disconnects that bone.
[4:01] We don't want that.
[4:02] That's really important to keep these connected.
[4:03] So box select those and move those into position.
[4:07] I'll just move these around now.
[4:09] These might look like they're jumping all over the place.
[4:11] So this is the end finger.
[4:13] This is actually the hand bone so that can come back in here.
[4:16] And this one is the start of the thumb just there.
[4:18] So that makes a little bit more sense now and I'll move this one into here and this one up there.
[4:23] So there's my hand bone in position for this character.
[4:25] If you've got fingers, then you can actually set them up with all the finger bones.
[4:29] And because I've got X symmetry on, that's happening on the other side.
[4:32] So let's set up the legs now.
[4:34] We'll start with Side View and just bring them back.
[4:36] So G them wide.
[4:37] So I'll turn snapping off at this point.
[4:38] We don't need it on anymore.
[4:39] G them wide and move the ankle bone to position the knee bone into position.
[4:43] Move these ones forwards for the toes.
[4:46] This bone here needs to go right to the bottom corner just there.
[4:49] And in front view, I'll obviously move these across.
[4:51] So G the next with those cross.
[4:52] This bone needs to be as wide as your foot because that's the foot roll as it's called.
[4:57] And then these need to move into position.
[5:00] And these ones as well.
[5:01] Okay, so we're almost there.
[5:02] We have got this big problem and big mess of the face just here though.
[5:06] My character hasn't got any facial animations.
[5:08] So I can again, delete all these.
[5:10] So all the ones at the front, make sure you don't get the head bone here.
[5:13] So I'll delete those and the ears just here, delete those.
[5:17] And there is an extra bone just in here.
[5:19] You can't see it.
[5:20] If I alt click on this, you can see there's face.
[5:23] And we need to get rid of that face bone as well.
[5:25] Otherwise we'll get some errors when we generate the rig.
[5:28] I'll just select this one to this one and G them wide with that back slightly.
[5:31] Oh, that's another one where it's connected.
[5:33] So just be careful of that.
[5:34] Make sure we select that as well.
[5:36] G them wide.
[5:37] Any bones that are connected like that, you need to make sure they stay connected.
[5:40] Otherwise, again, you'll have problems when you generate the rig.
[5:42] So you can see it's all looking like it's in place at the moment.
[5:46] Just have a good look around and I think we're there.
[5:49] Okay, so it's all working.
[5:51] It's a really good idea to save at this point.
[5:53] So I'm going to quickly save by work.
[5:55] So now I need to generate my actual rig that I'm going to use that has all the extra controllers.


### Generating the Final Rig [6:00]
**Transcript (timestamped):**
[6:00] But before I do that, remember, if I go back to object mode and press N on my keyboard
[6:04] and go to item, remember I scaled my rig in object mode.
[6:08] So the scale isn't quite set to one.
[6:10] That means if I go to my object data properties, scroll down to the generate rig button.
[6:14] If I generate it now, you can see that the rig is slightly undersized.
[6:19] That's its original position.
[6:20] So I'll undo that and I need to apply this scale.
[6:24] I can press control A to set or apply the scale and you can see that change to one.
[6:29] Now when I scroll down and go to generate rig, it generates the rig of the right size.


### Parenting the Mesh (Automatic Weights) [6:30]
**Transcript (timestamped):**
[6:33] So if I go back to my outliner up here and I'll just scroll down to the bottom, you can see there are now two rigs.
[6:39] The meta rig, that's the original that I moved my bones into position and my new rig,
[6:43] which is the actual one with all the cool controllers.
[6:46] So the meta rig, I can actually hide.
[6:48] So I'll hide that.
[6:49] You can actually delete it even.
[6:50] And the rig here is the one that I want to use.
[6:53] So now I can select all my objects.
[6:54] If you've got a single character, you just select your character and then the rig has to be selected last.
[7:00] So that's the active object.
[7:02] That's the one we're parenting to.
[7:03] I can now press control P and you can find that menu up in object, parent,
[7:08] and then there is with automatic weights just there.
[7:11] That's the one we want.
[7:12] That means the weight painting will be set up for us.
[7:14] And now I should be able to select my rig, go into pose mode and select one of my bones.
[7:19] I'll talk about what they do in a second and press R to rotate and you can see it's hooked up.
[7:23] But there's a slight problem that the leg is moving with the arm here.
[7:26] I'll right click to cancel that movement and just check some other areas.
[7:29] So down here and the right leg is moving a bit with the left leg here.


### Testing the Rig & Fixing Weights [7:30]
**Transcript (timestamped):**
[7:32] So there's a little bit of weight painting issues that we need to tidy up.
[7:36] But before I do, let's just explain what the different bones are.
[7:39] First of all, I'll scroll down and under the viewport display, I'll turn on in front so we can see them all.
[7:43] There's lots of different colors of bones on your rig.
[7:46] The purple one is the root bone.
[7:47] So there's only one of those and that will move around your whole character.
[7:50] The orange ones are for fingers and you can actually press S to scale to scale your fingers in like this.
[7:55] And of course, R to rotate and even G to grab if you want to stretch your hand around.
[8:00] The green and the red are IK and FK.
[8:04] The red being IK, which stands for Inverse Kinematics and you control that by the end bone of the sequence.
[8:10] So this is controlling the entire arm up to the shoulder there.
[8:13] And if I select that IK bone at the end, that's what it defaults to.
[8:18] I can actually switch this with that bone selected.
[8:20] I can switch across to FK and you can see that moving position.
[8:24] And now I can select the green bones and press R to rotate those and you can see them moving around with forward kinematics.
[8:30] And that's controlled almost in the reverse direction.
[8:33] So the top bone is controlling the ones below it.
[8:36] I'll go back to the IK though.
[8:38] So that's the IK and FK slider just there.
[8:40] Generally speaking, most people have FK for the arms and IK for the legs, but that one's for another tutorial.
[8:46] In the IK, you've got this bone as well, which you can press G to grab and move it around and distort it.
[8:51] Or R to rotate to change the elbow position.
[8:54] And the same is true for the legs.
[8:55] You can rotate that for the knee position and the end here, you can move the character around.
[9:00] The blue bones in here are tweak bones, they're known as.
[9:03] I hardly use these, but you can sometimes tweak your animation slightly just by moving those around.
[9:08] Down at the bottom here, we've got some more red bones, which is the foot roll.
[9:11] If I roll that, you can roll the ankle like so.
[9:14] And this is the up and down.
[9:15] And it's great clever because it actually keeps the toes on the ground.
[9:20] So it's very good for walk cycles.
[9:21] And then you've got the yellow bones, which is the core in the middle, just here.
[9:25] So that's a quick, brief rundown of the bones.
[9:27] Now we need to fix the weights.
[9:30] Now, in order to weight paint, we need to be able to see the bones that are actually connected to the specific parts of our character.
[9:37] But these are actually just control bones moving those deformed bones as they're known around.
[9:42] What we need to do is scroll up to our bone collections here and I'll open this up.
[9:47] So that's relatively wide.
[9:48] So we can see all our bone collections.
[9:50] And you'll notice these special bones down the bottom here, the deformed bones are the ones we need to use for weight painting.
[9:56] So I'll select that.
[9:57] And I'll actually just for now hide the rest of them.
[9:59] So there's the deformed bones.


### Cleaning Up Bone Layers/Final Touches [10:00]
**Transcript (timestamped):**
[10:01] And like I say, that's what we need to weight paint to.
[10:03] Now, in order to go to weight painting, we need to go back to object mode.
[10:06] You need to have your rig selected first.
[10:08] And if your character is one object, then you select the entire character.
[10:11] Or if it's several objects, you select the specific one you want to change the weights for.
[10:16] Then with that as the active object, you go into weight painting.
[10:19] Now, currently I have no bone selected.
[10:21] So this is blue for cold is not attached to any bone.
[10:25] If I select a bone with alt left click, you can see that this head here has no attachment to that bone.
[10:31] But as I come a bit closer, you can see that this bone has a bit of influence on this neck here.
[10:37] And as I go through, you can see that this bit here is fully influenced by this bone.
[10:41] But the chin is influenced a little bit by this bone.
[10:45] And you can change your bones by alt left click.
[10:47] So what we need to do is remove any influence of this bone here and make sure that this bone here has all the influence of the chin.
[10:54] To do that, we paint.
[10:56] So currently the ink coming out of our brush is a weight of one.
[11:01] So if I start painting, it will paint a weight of one and the strength of this brush is one.
[11:05] Now, it's important to understand that the weight is set to one.
[11:08] So if I change the strength here, it just means if I resize my brush with F that I'm painting
[11:13] and it will slowly change across to red.
[11:16] But if I change the weight to zero, it will slowly start painting towards zero.
[11:20] So the strength is different to the weight.
[11:22] And the easiest way is to have your weight set to one and paint the weight in.
[11:27] Weird, let's say a strength of something like 0.7, let's say,
[11:30] and you can slowly paint these things in if you want to gradually change it.
[11:33] Now, I'm going to undo the changes there because there's a slight nuance about blender.
[11:38] I mentioned that this bone here, alt left clicking on that bone will select it,
[11:41] has some influence on the chin.
[11:43] And so does this bone.
[11:45] But painting the red in this area will not remove the influence of this bone.
[11:49] In order to remove it, we need to go across the tool, options and auto normalize.
[11:54] Normalize means it's got a maximum of one.
[11:56] That means when I start painting here, it will remove any other influence of any other bones.
[12:01] So I can paint in here until it goes red.
[12:03] And now when I press alt left click on this, you can see that it's cold for this bone.
[12:08] There's a little bit of influence up there.
[12:09] So I'll just alt left click on this one and paint.
[12:11] Now I did neglect to say that you can turn on the X axis symmetry.
[12:15] So you only need to paint on one side, but my object is mirrored.
[12:18] So there was no need for me to do that.
[12:20] I'll just paint this all in.
[12:21] So we've now got the head just being influenced by this bone.
[12:24] So if I go back to object mode, choose my armature and let's bring up the face bones just there.
[12:30] Oh, actually, they're torso bones aren't they?
[12:31] I deleted the face.
[12:32] You'll see the torso bones there.
[12:34] And it's actually the head bone here is actually part of the torso.
[12:37] And if I rotate this now, you can see the chin is no longer attached to the other parts of the neck,
[12:42] or in fact, the torso of this character.
[12:45] So you need to go through.
[12:46] I'll just hide the torso bone there.
[12:48] And we don't need the face bones at all.
[12:50] So you need to go through your character, painting the different parts to the correct bones.
[12:54] So let's do the torso next.
[12:56] So I need to go to object mode for my rig.
[12:58] I can press control tab to go across to object mode, choose the torso last.
[13:02] So that's now the active object control tab and across to weight paint.
[13:06] I can now move in and alt left click on different bones and see the influence.
[13:11] And I think that all looks okay.
[13:13] I think the main problem I was having was with the legs when I was moving those,
[13:17] when I was moving the arm, some of the leg was moving.
[13:19] And when I moved the leg, some of the opposite leg was moving.
[13:22] So let's go to the leg object and change that.
[13:25] So I need to move to that new object.
[13:26] Unfortunately, there's no quick way to jump to a different object.
[13:30] It's fine if your character is all one object, you don't have to worry.
[13:32] But in my case, they're all separate objects.
[13:34] So I need to go back into object mode, make sure that the rig is selected first.
[13:37] The object I want to weight paint last control tab across to weight paint.
[13:41] And you can select either of these two bones and start weight painting.
[13:44] So I'll have a weight of one and a strength of one now and start painting across here.
[13:51] And painting across here and with the auto normalize that should get rid of any other
[13:56] influence from other objects.
[13:58] And because these are mirrored, it should have the same effect on the other side all going well.
[14:03] I'll just quickly do the calf bone and then we'll check whether that's working.
[14:05] So back to object mode, rig first, the lower leg or the calves,
[14:09] second control tab, cross to weight paint, alt left click to select that bone and paint.
[14:16] And then we can go into object mode, choose the rig and into pose mode to control tab and
[14:20] pose mode.
[14:21] We can hide the deform bones at this point and then bring back the other bones.
[14:26] We don't need the face bones.
[14:27] And then I can select my character to grab and you can see it's only influencing
[14:32] this leg now and let's check the other leg is working and that's working well.
[14:36] Now the very last thing is, and I forgot to mention this, you can actually highlight
[14:39] one particular bone with the star.
[14:41] I forgot all about that functionality and you can turn the star off.
[14:44] So that's a much quicker way.
[14:45] We can see our deform bones much quicker that way and then turn them off like so.
[14:49] So now you've rigged your character, you're all ready to go and start animating and posing
[14:54] and doing all sorts of funny things.
[14:55] As always, if you've got any questions, then comment below.
[14:57] Thanks for watching and I'll see you next time.



---

## Captured Frames

- [1:22] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_000.jpg
- [1:39] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_001.jpg
- [4:16] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_002.jpg
- [6:14] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_003.jpg
- [6:43] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_004.jpg
- [8:04] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_005.jpg
- [9:21] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_006.jpg
- [11:56] tutorials/frames/easy-rigging-using-rigify-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
End-to-end character rigging with Blender's built-in Rigify add-on: fitting a Human meta-rig to a low-poly character mesh, generating the final control rig, binding the mesh with Automatic Weights, and hand-correcting weight-paint bleed between separate mesh objects.

### Summary
Grant Abbitt rigs a low-poly PlayStation-style character (from his earlier modeling tutorials) using Rigify. He adds the Human meta-rig armature, scales and repositions its bones in Edit Mode to match the character (deleting unused face/finger bones for the low-poly design), generates the final control rig, parents the mesh to it with Automatic Weights, then tests it in Pose Mode. Because the character is built from several separate mesh objects, some bones bleed influence across unrelated body parts (e.g. rotating an arm also moves a leg); he fixes this per-object in Weight Paint mode using Alt+Click bone selection and the Auto Normalize option so painting one bone's influence to 1.0 correctly zeroes out competing bones.

### Key Steps
1. **Prep**: enable the Rigify add-on (Edit > Preferences > Add-ons, search "Rigify"), snap the 3D cursor to world origin (Shift+S), then Shift+A > Armature > Human (Meta-Rig) — found under the Rigify Meta-Rigs submenu alongside Animals and Basic Human/Quadruped rigs.
2. **Scale to character**: in Object Mode, scale the whole meta-rig up to roughly match the character's size in Front Orthographic view; enable "In Front" under Object Data Properties > Viewport Display so bones stay visible through the mesh from any angle.
3. **Match bones in Edit Mode**: enable X-Axis Mirror before moving bones so edits apply to both sides at once; use Period (.) to switch the Transform Pivot Point to 3D Cursor for rotating around a specific joint, and toggle Snap-to-Volume (magnet icon) so grabbed bone tips snap to the center of nearby mesh geometry — much faster than eyeballing Front/Side views.
4. **Delete unused bones**: for a low-poly/no-finger-detail character, Ctrl+select down a finger chain and delete, making sure to also remove the topmost hand-adjacent bone; likewise delete the Face bone group (including a hidden extra "face" bone found via Alt+Click) since the character has no facial rig — leaving unused connected bones in place causes errors when generating the rig. Always verify bones that must stay parent-connected didn't get disconnected by an accidental plain-click-drag.
5. **Apply scale before generating**: back in Object Mode, press Ctrl+A > Scale on the meta-rig (since it was scaled in Object Mode, not Edit Mode) — generating the rig without this produces an undersized result; Object Data Properties > N-panel > Item tab confirms Scale reads 1.0 once applied.
6. **Generate Rig**: Object Data Properties > Rigify panel > Generate Rig button creates a second, separate armature object with all the animation controllers; the original meta-rig can be hidden or deleted afterward.
7. **Bind mesh to rig**: select all character mesh objects, select the generated rig last (making it the active object), Ctrl+P > Parent > With Automatic Weights to auto-generate vertex groups and weights.
8. **Test & read bone colors**: enter Pose Mode on the rig — purple = single root bone (moves the whole character), orange = finger controls (S to scale, R to rotate, G to grab/stretch), red = IK chain controls (end bone drives Inverse Kinematics up the chain; an IK/FK slider on the selected IK bone switches to green FK bones, which rotate top-down instead), blue = tweak bones (fine per-segment adjustment), red foot-roll bones near the ankle (roll for heel/toe rotation, keeps toes planted — key for walk cycles), yellow = core/torso control in the middle.
9. **Fix weight-paint bleed**: switch to the Deform bone collection (bottom of the Bone Collections panel) since those are the actual deforming bones, not the visible control bones; enter Weight Paint mode (rig selected first, target mesh object selected last/active) and Alt+Click a bone to preview its current influence (blue = 0, red = 1).
10. **Paint corrections with Auto Normalize**: enable Tool > Options > Auto Normalize so painting weight 1.0 onto one bone automatically zeroes competing bone influences on the same vertex (painting red without it leaves other bones' influence intact); use Weight = 1.0 with full Strength = 1.0 for hard reassignment, or a lower Strength (e.g. ~0.7) to gradually blend a value. Repeat per separate mesh object (torso, each leg, calves, etc.) since Blender has no quick "jump to next object" shortcut — go back to Object Mode, reselect rig then the next mesh object, Ctrl+Tab into Weight Paint again.
11. **Cleanup**: use the bone-collection "star" icon to quickly isolate/solo one collection (e.g. Deform bones) instead of manually toggling visibility for each layer.

### Nodes / Settings
- **Add menu**: Armature > Rigify Meta-Rigs > Human (also Animals and Basic Human/Basic Quadruped variants available).
- **Object Data Properties > Viewport Display**: In Front (enabled) to see bones through mesh geometry.
- **Transform Pivot Point**: 3D Cursor (via Period key) for joint-centered rotation; Median Point is the default.
- **Snapping**: Snap Target = Volume, for snapping bone tips to the center of nearby mesh geometry.
- **Object Data Properties > Rigify panel**: Generate Rig button (creates the second, poseable rig object from the meta-rig).
- **Ctrl+P parenting menu**: With Automatic Weights (binds mesh to armature with auto-generated vertex groups).
- **Bone Collections panel**: Face / Face (Primary) / Face (Secondary) / Torso / Torso (Tweak) / Deform, etc. — Deform collection holds the actual skinning bones used for weight painting, separate from the visible control-bone layers.
- **Pose Mode**: IK/FK slider property on the IK end-bone (per limb); bone color coding — purple (root), orange (fingers), red (IK + foot roll), green (FK), blue (tweak), yellow (torso/core).
- **Weight Paint > Tool > Options**: Auto Normalize (checkbox) — critical for correctly zeroing competing bone weights; Weight and Strength are separate sliders (Weight = target value painted toward, Strength = per-stroke opacity).

### Difficulty
Intermediate

### Blender Version
Blender 4.3 (continuation of the author's low-poly PlayStation-style character series)

### Tags
rigging, animation, beginner, intermediate, blender-4x

---

## Related Tutorials
- [Blender 5.1's NEW Rigging Tool is INSANE!](blender-51s-new-rigging-tool-is-insane.md) — builds directly on a Rigify-rigged character (golem), extending it with Geometry Nodes-driven procedural deformers via the Bone Info node.
- [Mastering Blender's Graph Editor](mastering-blenders-graph-editor.md) — the natural next step after rigging: animating and refining motion on the controls generated here via F-curves and interpolation.
- [Create a Walk Cycle animation in Blender](create-a-walk-cycle-animation-in-blender.md) — uses a Rigify-style mannequin rig's IK/FK and foot-roll controls (as explained here) to block a full walk cycle.
- [Your Guide to Mechanical Rigging in Blender (Robot Arm Tutorial)](your-guide-to-mechanical-rigging-in-blender-robot-arm-tutorial.md) — contrasting IK rigging approach (manual bone-chain constraints) for hard-surface/mechanical rigs vs. this video's Rigify auto-rig workflow for organic characters.
- [The COMPLETE BLENDER 3D Animation COURSE](the-complete-blender-3d-animation-course-5-hours-blender-b3d-animation.md) — covers armature rigging and IK constraints as part of a full beginner animation pipeline, complementary to this focused Rigify walkthrough.

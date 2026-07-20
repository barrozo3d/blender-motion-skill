---
title: Create a Walk Cycle animation in Blender
source: YouTube
url: https://www.youtube.com/watch?v=SLh3hUIxv1s
author: Pierrick Picaut
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/create-a-walk-cycle-animation-in-blender/
frame_count: 0
frame_status: pending-selection
---

# Create a Walk Cycle animation in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=SLh3hUIxv1s)
**Author:** Pierrick Picaut
**Duration:** 19m5s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py create-a-walk-cycle-animation-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, this is Pierre-Rick from P2Design, a new version of Blender just released today
[0:05] and I thought that would be nice to make a little animation with it.
[0:09] In this video we'll do this simple work cycle.
[0:13] If you're a beginner, it's a great exercise to practice and warm up, focusing on the most
[0:18] important poses without the struggle of the graph editor.
[0:23] Pause the video and capture the following references and let's get started.


### Free rig [0:48]
**Transcript (timestamped):**
[0:48] To follow along you can get any of my character rig for free or if you want to support my
[0:53] work you can pay $15.
[0:56] You will find a page with the different characters rig, the first one are the mannequins rig
[1:01] we're gonna use.
[1:02] You will find what we need under rig download.
[1:05] There are two zipped files and I advise you to use the latest one called P2M Library 5x.
[1:13] Want to download the zipped file and zip it in a dedicated folder.
[1:17] The zip file includes the four different rigs along with some asset libraries information.


### Character’s library [1:22]
**Transcript (timestamped):**
[1:23] You can link the characters you want to work with directly or we can add it to our asset
[1:29] library.
[1:30] Go to edit, preferences and file path.
[1:33] You should find a tab called asset libraries in which we can load our new rigs.
[1:38] I've done that before obviously so I will remove them so that we start the same way.
[1:43] On the right hand side of the panel you will find the plus button just click it.
[1:48] It opens a file browser, just go to the folder you unzipped the characters in.
[1:53] You can confirm by clicking on the add asset library.
[1:56] A new asset library has been created named after the folder we selected.
[2:01] Let's make some space and remove everything in the 3D view.
[2:05] We can create a new window and open the asset browser.
[2:09] The asset browser is generally overcrowded but we can filter to only display the library
[2:15] we just loaded.
[2:17] Here you will find a folder per character.
[2:20] We will use the regular character.
[2:22] You can find zip folder to filter between the rig and the post library.


### Linking the character [2:27]
**Transcript (timestamped):**
[2:27] To make sure we properly link our character in the import setting option we'll use link.
[2:34] From there we can simply drag and drop our character rig directly into our blender scene.
[2:39] It works exactly as if we linked the character in the scene.
[2:43] To expose our character rig we need to right click on its collection, go to library override,
[2:50] make selected and content.


### Getting started [2:52]
**Transcript (timestamped):**
[2:52] We can now select our character rig, press control tab to enter post mode.
[2:57] In the bottom right corner of your 3D view you should have a little arrow.
[3:01] Click it to open the post library.
[3:04] From there we can filter the posties by only enabling the regular character posties.
[3:09] A new tab for our regular character just appear in which we can find his dedicated posties.
[3:15] It only features hand posties.
[3:17] Make sure you have no bone selected and from there you can easily apply any of those posties
[3:23] by simply left clicking on it.
[3:25] For the work cycle I'm going to use a relaxed closed hand.
[3:29] To apply it to the opposite hand I can hold control and left click on the post.
[3:35] We can now close the asset browser and close the asset library.
[3:39] Replace the timeline by the action editor.
[3:42] Switch mode from dope sheet to action editor.
[3:45] Create a new action, give it a relevant name and create a new slot that will automatically
[3:50] be assigned to our armature.
[3:52] A basic world cycle is generally animated over a second so I can go on frame 24 and
[3:58] press control and to set the end frame assuming that we're using 24 frames per second as
[4:05] a frame rate.
[4:06] In the action editor under view we can enable the playback controls and finally to keep
[4:12] our action as clean as possible we can go to edit, preferences, animation and enable
[4:19] the option only insert available.
[4:22] This will prevent blender from creating new keys like unlocked channels for example.
[4:28] From there we can select any bone on our character, press K and choose whole character.
[4:34] It creates a key on the available transform channels along with all the custom properties.
[4:40] Finally to expose our rig UI we need to open the text editor.
[4:44] There you will find the linked a rig UI text file, just open it and run the script.
[4:50] We can now start animating.


### First pose [4:51]
**Transcript (timestamped):**
[4:52] The character default setup is ideal for world cycles, you don't need to switch any
[4:57] mechanism.
[4:58] Since we'll keep the exercise as simple as possible we'll only work on the torso, legs
[5:04] and arms.
[5:05] You can solo those controllers collection by clicking the little star icon next to the
[5:10] collection name.
[5:11] And don't do as I did, don't forget to enable the auto record for the keys.
[5:17] Let's build the first pose.
[5:19] Now what you need to understand is that we don't need our poses to be perfect right away.
[5:25] We refine our poses as we go along.
[5:27] The first pose is the contact pose.
[5:30] It's the moment where the front foot touches the ground, generally with the heel.
[5:34] To keep it simple we can push one leg back and the other forward, raise the heel of the
[5:40] back foot and raise the toes of the front foot.
[5:44] We can lower a bit the center of gravity to be able to spread the legs a little more.
[5:49] To keep the exercise simple, don't use the center of gravity or torso controller to rotate
[5:56] the character torso.
[5:58] The hips and chest move the opposite way.
[6:02] We call it contraposter.
[6:03] Let's start with the hips and twist them so that they point to our character's right
[6:08] side and give more range to our legs.
[6:11] We can now rotate the chest the opposite way.
[6:14] You can consider the contact pose as the extreme for the legs and the arms.
[6:20] It's the time where the hands and feet are further away from the body.
[6:24] When you pose the arms, make sure that you also pose the shoulders and adjust the pose
[6:30] of each joint, the arm for arm and wrist.
[6:34] See how the character feels like he's leaning backward because of his relaxed pose.
[6:41] To fix that, we can use the center of gravity or torso.
[6:45] We don't want to rotate it side to side but we can rotate the character forward using
[6:50] it.
[6:51] This is our base pose.
[6:52] I will give it some tweaks just to reduce a bit the amplitude of the arm.
[6:57] As it feels like my character is walking really fast, I want something a little more relaxed.
[7:03] And since I'm a professional animator, I forgot to enable the auto keying.
[7:07] And as I move on to the next key, I will lose my pose.
[7:11] So I'm gonna fix that and move on.
[7:14] One thing I advise you to do too is to slightly push the foot inward based on their rest pose.
[7:21] When we walk, our feet tend to go one in front of the other.
[7:25] For feminine work, you will exaggerate that.
[7:28] If you're animating a big guy, a giant, a warrior, you will spread the feet more.
[7:35] So for such a regular guy, I just want to slightly push them inside.
[7:40] Also, you can slightly twist the arms so that the biceps feel more natural.
[7:46] Your elbows are not perfectly pointing backward.
[7:50] They are slightly pointing to the outside.
[7:53] And now it feels a little more natural.
[7:55] With our first pose created, we can select all our keys, press Shift D to duplicate them
[8:01] and move them to frame 13.
[8:03] I moved them to frame 12 because unfortunately I need to wear glasses.
[8:08] Select all the controllers, press Ctrl C to copy the pose and Ctrl Shift V to paste the mirror to pose.
[8:15] If we play the animation, we can see we have some interpolation between those keys.
[8:19] So we can select them all and press T and choose constant.
[8:23] Finally, we can select our first keys, duplicate them and move them to frame 25 again.
[8:30] I need to wear my glasses.


### Passing pose [8:31]
**Transcript (timestamped):**
[8:31] The first pose we created was the contact pose where the feet are the furthest away one from the other.
[8:37] The next pose is the passing pose where the feet are the closest one to the other.
[8:42] And by the way, if you're enjoying this content so far, please consider leaving a like, a nice comment and subscribe.
[8:48] The passing pose occurs halfway through the step.
[8:51] So it should occur six frames later than the first step on frame 7.
[8:56] I started on frame 6, I will fix that later on, you get it.
[9:00] First, we want to flatten the front foot and move it so that it's beneath our character.
[9:05] That's also the time where our weight will be mostly on that passing foot.
[9:11] So from the front view, I need to push the center of gravity of the torso controller to the right on that left foot.
[9:20] I will select the hips and press Alt R to cancel the rotation.
[9:24] I want to reset the rotation as it's a pretty neutral pose for the hips, twist wise.
[9:30] We can bring the back foot forward so that it's almost aligned with the foot contacting the ground.
[9:37] When we walk, we try to waste as less energy as possible.
[9:42] So keep the foot as close to the ground as possible.
[9:46] Push the character up a little bit.
[9:49] And now we can adjust the other part of the body.
[9:52] We should cancel the rotation of the torso too because it's a neutral pose.
[9:58] And it's also the time where the arms are crossing the body.
[10:02] What you want to do is to make them drag a little bit.
[10:05] Think of it as adding a bit of delay on the arms.
[10:08] So the arm that was on the back is slightly on the back.
[10:12] And the arm coming from the front is slightly bend it toward the front.
[10:18] We want the supporting leg to be as straight as possible.
[10:21] Don't hesitate to move the center of gravity toward that leg.
[10:25] That will induce pressure to the hips.
[10:27] So we want to raise the hips on the supporting leg.
[10:31] I'm pretty satisfied with the pose.
[10:32] So I will select all the controllers, press Ctrl C to copy their pose,
[10:37] go 12 frames later and press Ctrl Shift V to paste the mirrored pose.
[10:43] Seems like we finally have a walk going on.
[10:47] And that's the time I realized I didn't position my keys properly.
[10:52] So I will offset them by one key.
[10:54] So we have a key on frame 1, 7, 13, 19 and 25.


### Up/Push pose [11:00]
**Transcript (timestamped):**
[11:00] Before we create the next poses, we can give colors to our existing keys.
[11:04] Just select your keyframes and press the R shortcut.
[11:07] The keyframe type has no influence on your blender file.
[11:11] It doesn't matter what you choose.
[11:13] That rule though, don't apply to the generated type.
[11:17] This one is used by some add-ons, but it's not the topic of that lesson.
[11:21] So I will just give my contact pose and my passing pose different colors
[11:26] so that it's a little easier to identify them.
[11:29] Now, in between those poses, we have to create two different poses.
[11:34] The up and down pose.
[11:36] After the first passing pose, on frame 10, we have the up pose.
[11:42] There is a fantastic tool to interpolate a pose between two poses.
[11:47] It's a breakdowner.
[11:48] I select all my controllers and I then press Shift E.
[11:53] When I move the mouse cursor to the right or the left,
[11:56] the current pose will blend toward the next or previous pose.
[12:00] It's a fantastic tool, so let me know in the comment
[12:03] if you would like a dedicated tutorial.
[12:06] Here, I will only be using it on the left foot, the contacting foot,
[12:10] to get an accurate position.
[12:12] I select the foot, press Shift E,
[12:14] and I don't move the mouse cursor since I want this foot to be right in the middle
[12:19] of the neighboring poses.
[12:21] Because during a walk, the foot on the ground has a linear speed.
[12:26] From there, we can work on the pose.
[12:28] So basically, it's the moment where the character is the highest.
[12:32] I raised the heel a little bit and now I will push my character up.
[12:37] As we push on the leg, the center of gravity will move toward the other side.
[12:41] So we can slightly push the character to his right.
[12:45] Then we can move the front foot a bit forward.
[12:48] We keep it close to the ground because we don't want to waste energy
[12:52] raising the foot too high.
[12:54] Note that I never use the foot controller to rotate it.
[12:58] I always use the heel controller.
[13:01] You could use both, but when you start mixing different controllers
[13:05] to perform the same pose, it becomes harder to edit.
[13:09] So generally, when I'm animating a walk or a run cycle,
[13:14] I just use the heel controller to rotate the foot forward and backward.
[13:20] Now, when it comes to the hips, chest, and arms,
[13:24] I will kind of blend between the previous and next pose.
[13:29] The hips start to twist toward the front leg,
[13:32] while the chest twists the opposite side, but it's very subtle yet.
[13:38] Don't forget to check out the reference if you have some difficulties.
[13:42] The arm swinging forward is slightly straighter,
[13:45] while the arm swinging backward is slightly bent.
[13:50] From there, a lot goes into fine-tucking the pose.
[13:53] So it's hard to explain what to do, what not to do.
[13:57] It's just a feeling and also comparing it to the reference I may have.
[14:03] I was obviously not using the reference I provided
[14:07] because it didn't exist before I've done it,
[14:09] but you can easily find real-life walk cycle references on YouTube
[14:14] by simply typing in walk cycle.
[14:17] As usual, once I'm happy with the pose,
[14:20] I will copy and paste it mirrored 12 frames later.
[14:25] It already feels like we're getting close to a full walk cycle.
[14:29] We're only left with one key pose to be created, the down pose.


### Down pose [14:34]
**Transcript (timestamped):**
[14:35] This is the final step of our walk cycle.
[14:39] It's the down pose.
[14:40] It's the moment the character is the lowest just after the contacting pose.
[14:45] It's the moment we absorb the weight, the fall forward of the step.
[14:51] As we did before, I will use the breakdowner with Shift E
[14:55] to move the front foot, the contacting foot,
[14:57] right in the middle of the previous and next pose.
[15:01] I will make sure it's flat-footed, so I will clear the rotation
[15:05] on the toes and on the heel, and then I will lower the center of gravity.
[15:11] I will push the back foot as far as I can
[15:14] because it's the last pose before these foots leaves the ground.
[15:18] So it's not supporting that much weight anymore,
[15:21] so we can bend it a little more by rotating the heel.
[15:25] Basically, the straighter your leg, the more you're pushing with it.
[15:30] And the down pose is the little exception where the front foot is supporting the whole weight
[15:36] just after we land.
[15:38] That's why there is this down pose.
[15:41] And this is where you use the more energy in your walk.
[15:44] If you've ever done squats or fonts at the gym,
[15:48] having your legs straight is not the hardest part.
[15:51] It's way harder to support your weight whenever your legs are bent.
[15:56] Regarding the chest, this pose is pretty similar to the previous one.
[16:00] I just like to slightly push the rotation a little further
[16:05] and do the same with the arm.
[16:07] Keep the pose, but just push it slightly more forward for the forward arm
[16:12] and slightly more backward for the backward arm.
[16:15] Basically, the motion of the arms is slowing down
[16:19] before swinging the opposite direction.
[16:22] And this is what we're creating by having pretty similar poses.
[16:27] I will push that a little more here and there.
[16:30] And once I'm happy with the result, as usual,
[16:33] I will copy the whole pose and paste it nearer 12 frames later.
[16:38] I'm also giving the up and down poses a color just for the sake of presentation.
[16:45] And here we are with our base walk cycle.
[16:48] Now, obviously, there's a lot more we could do.
[16:51] But as you can see, we can get a pretty satisfying blocking of the animation pretty easily.
[16:58] And that's a great exercise.


### Final touch [16:59]
**Transcript (timestamped):**
[16:59] Now, if you want to learn how to create a very detailed walk cycle
[17:04] with all the steps, the secondary motion, the full polish with the graph editor,
[17:10] check out my course Alive.
[17:12] And if you want to learn how to rig this kind of character,
[17:15] check out the Art of Effective Rigging.
[17:17] All right, enough self-promotion, but you know, everyone got bills to pay.
[17:22] The final touch I'd like to give is to work a bit on the feet.
[17:26] When the feet are on the ground, they move in a straight line.
[17:29] But when they are in the air, they should rotate a bit and swing to the side.
[17:34] On the passing pose, I will push the foot slightly to the side.
[17:39] And I will slightly twist it inward.
[17:41] Depending on the person, it can twist outward, inward, it can rotate also.
[17:47] Then, before the contacting pose, I will rotate the foot around the z-axis
[17:52] so that it points out a little bit.
[17:54] And I will then exaggerate this rotation on the contact pose.
[18:00] So basically, as the heel contacts the ground, the foot is slightly rotated outward.
[18:07] And as the foot gets flattened, it also gets straighter.
[18:12] Then I can copy-paste the different poses to the mirrored poses.
[18:17] This is a little detail, but those slight rotations will make it feel more organic, less robotic.
[18:24] So if you're a beginner starting with a walk cycle, at first just make it feel right.
[18:31] And once you're done with that, check a real-life reference,
[18:35] check how the feet and hands rotate, and add those little details to your poses.
[18:42] And your walk will feel way more natural.
[18:45] This is the end of this tutorial.
[18:47] I hope you enjoyed it, and I'll see you very very soon.



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

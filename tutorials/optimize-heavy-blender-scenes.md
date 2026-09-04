---
title: Optimize Heavy Blender Scenes
source: YouTube
url: https://www.youtube.com/watch?v=SLVbMEF5LVU
author: roe.num77
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/optimize-heavy-blender-scenes/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Optimize Heavy Blender Scenes

**Source:** [YouTube](https://www.youtube.com/watch?v=SLVbMEF5LVU)
**Author:** roe.num77
**Duration:** 14m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py optimize-heavy-blender-scenes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So this is a 10GB scene that I made a while ago using Word Creator and Blender.
[0:06] The amount of objects, scatters, texture size, kitpatch3D, PAP, 3D scans, you get where I'm going.
[0:15] As a result, I can't even move in the viewport while using the solid view.
[0:20] But then comes these magical buttons, which makes the scene so much optimized.
[0:26] That allows me to navigate so easy, including the fact that this area is 2048 meters long.
[0:36] It is so huge, but I can now work with it easily.
[0:40] So in this tutorial, once for an eternity, you are going to learn how to perfectly and of course
[0:46] easily optimize our scene. And I'm not talking about Blender's default optimization setting,
[0:52] but instead you are going to use an addon called the MemSaver, which has been helping me for a long
[0:59] time with the large-scale environments. Ever since I grabbed it and yeah, you heard it right,
[1:06] grabbed it. It is a free addon. So first, we start with a basic scene to learn the interface and workflow
[1:14] of the MemSaver and then we get to the real game. And there I will teach you some really cool tips and
[1:21] tricks on how to get a perfect result with this addon. This is a one-time tutorial, but it is a
[1:28] lifetime workflow. The link will be in the description to download the addon. So without any
[1:33] further ado, let's get this going. So make sure to download the addon using the link in the description.
[1:40] Now to install it, just drag and drop the zip file into Blender. Then hit OK. And now if we go to
[1:47] edit preferences under the addons tab, here we can search for MemSaver. Make sure to check these
[1:53] bugs to activate it. Now if we press N, we can see the addon in the site menu. In the site menu,
[1:59] it is called Polygonic. So over here, there are two characters and both of them are hyper realistic.
[2:06] And then something is realistic. It means it is pretty heavy for Blender to handle it. And this
[2:12] is when we need to optimize our scene. So let's learn how to use the MemSaver addon. When we
[2:19] expand it, there are a few options. The ones that I am interested in and I have been taking advantage of
[2:26] are these two, resize images and decimate meshes. So we start with the resize images.
[2:34] Resize images means lower the quality of the image textures. For example, if you have an object that
[2:41] has 8K resolution textures maps, you can decrease the quality to a lower version, 4K, 2K, HD,
[2:50] 520. And yeah, you can decide how much you like the quality to be decreased. So this is a ground
[2:57] plane with 8K textures. To decrease the quality of image textures, the hit resize images. A new
[3:06] window will show up with two options, target and desired size. Target means which objects
[3:13] should have an image resize. And yeah, you can choose some of the specific objects to be resized.
[3:20] We will get to it in the next example. For now, we keep the target on scene objects.
[3:27] Which means the entire objects that exist inside this scene. Then we get to the more important one,
[3:34] desired size. So over here, you can choose what will be the quality of your resized images. And
[3:42] this is a very cool feature. In the next example, you will realize how it really works. So for this
[3:49] ground plane, I choose 512. And then the magical button, hit OK. Now Belender starts calculating
[3:58] and boom. By just one click, the image maps have been resized and you can see the quality have
[4:06] decreased. By the way, you can see the catch folder from here. Mimsaver will save the images over here.
[4:13] And the cool part is, you don't have to make new folders for a new scene. Mimsaver will remember
[4:20] which textures were for which scenes. Meaning, we don't even need to open the catch folder.
[4:27] Now, you may say, well, the quality has decreased. We could use a lower quality texture in the first
[4:34] place. What's the whole point of using this add-on? Well, because over here, we have a very cool feature.
[4:43] Redart images to originals. Again, we have the target option. Let's keep it on scene objects.
[4:50] And then hit OK. This is just so cool. The texture maps have gained their original 8K quality. And
[4:59] yeah, the process is totally procedural. It is not destructive and that's so cool. That's a very
[5:05] great add-on. Now, let's get to another example. So in this example, I have two realistic characters.
[5:13] One of them is close to the camera and the camera depth of field is set on it. But the other one
[5:20] is behind the main character and it is blurry because of the depth of field. So why not decreasing
[5:26] the quality if it is not that much visible? So I select all the objects related to this soldier
[5:34] at the back. Then I hit resize images. And this time, I make sure to set the target on selected
[5:42] objects because I want to only decrease the quality of this character, not this one. Then for a
[5:49] desired size, let's go for 64 and then hit OK and wait for it to be calculated. So the quality
[5:58] have decreased and it looks pretty good from the camera view. And if you take a look at it here,
[6:03] you can see it had a very significant downside on the quality of the textures because it is
[6:10] blurry due to the depth of field. We can barely notice that. And that's the trick. You have the
[6:16] ability to decrease the quality of the objects that are away from the camera so that you can add
[6:22] more quality to the objects that are in focus. And if you think the quality has decreased too much,
[6:30] you can hit resize and this time set it on higher value like 128 or maybe 256. And you can see that
[6:43] this is totally procedural and it is fantastic. Just fantastic. Now let's get to this cool one,
[6:51] decimate measures. Well, if we take a look at this plane in edit mode, this is just so dense. It has
[6:59] too much geometry and we can definitely decrease the amount of it to a reasonable level. So we
[7:06] select the plane and hit decimate measures. We keep the target on selected objects and then we have
[7:14] the decimation ratio which goes from 0 to 1. 1 means no changes to the geometry and as it goes
[7:23] towards 0, more geometry will be removed. Let's set it on 0.1 and hit OK. But before that over
[7:32] here we have the statistics and if you don't have it enabled, you can enable it from here.
[7:41] So right now this plane has 5,222,912 triangles and that's a considerable value. Now let's
[7:54] decimate it by a decimation ratio of 0.1 to see how much it can be optimized. So done. It now has
[8:05] 522,000 triangles. Almost 5 million triangles have been reduced and you can't even tell the
[8:15] difference over here. You barely can see the difference. This is amazing and again the cool
[8:22] part is you can tweak it at any time that you like. Let's say I want to set it on 0.3 to give some
[8:31] geometry back to the plane and yeah you can do it easily because the process is totally procedural
[8:37] and no need to mention that you can revert meshes to originals so that you will have the original
[8:46] geometry of your mesh. That's just insane. So this was how the add-on works. Now we get to the
[8:54] real game. Let's say we have a scene that is so huge and heavy. How should we properly optimize it the
[9:03] way that in the render there is no quality downside and yeah no quality downside. So here I will teach
[9:12] you a perfect optimization workflow that you can use in every single one of your projects. So this is
[9:19] a 10 gigabyte scene that I made using word creator and blender. This is a huge scene in which there
[9:26] are so many high quality assets, a bunch of vegetation scatters using geo scatter. I can barely move
[9:34] inside the viewport while using the solid view and it is totally impossible to work with the scene
[9:42] and if I try to switch into rendered view believe me blender will just most probably crash or it says
[9:50] system is out of GPU. So the first thing we do is to resize images. To do that we go to
[9:57] name saver add-on and hit resize images. For the target we choose scene objects which means we are
[10:06] going to resize the images of every object inside this scene. Then for the desired size let's go for
[10:14] 64 and hit okay. Because this scene is so huge and it has so many objects we should wait a bit for
[10:21] it to be calculated and while the process is being done let me tell you something important.
[10:27] So here there is a simple tree scatter made with geo scatter. The tree models are high quality and
[10:35] we want to optimize them. The trees that I use to scatter are in this collection. So I have used
[10:42] these trees to scatter them over here. So I select the trees and then resize their images.
[10:48] For the target I choose selected objects and desired size let's go for 32 for example hit
[10:56] okay. This is a very low value but I just want you to see how it can actually affect the scatters
[11:04] as well. So as you can see the changes have been applied to the scatters as well and it will be
[11:10] applied to the entire trees inside the scatter and it doesn't matter how you scatter trees geo
[11:17] scatter geometry nodes or particle system. It works for all of them of course all of them come from
[11:24] geometry nodes. Now let's take a look at our scene. So the process is done which means now we should
[11:30] be able to switch into rendered view and now I can easily work with this scene and add more textures
[11:38] objects or scatters. This is just so cool. A few seconds ago I couldn't even move or switch into
[11:46] rendered view but now I'm just easily walking around the scene and that's a very cool add-on with
[11:53] very cool features. But this is just not the end. We have optimized the scene to a significant amount
[12:01] and we can take it to a higher level. So let's do that. So we get back to our good friend MemeSaver
[12:09] and this time we go for decimate meshes and again we keep the target on scene objects which means
[12:17] all the objects inside this scene and a decimation ratio of 0.1 will do a great job. Let's hit okay
[12:25] and now we should wait for it to be calculated. So done and you can definitely see the changes over
[12:32] here. It has changed the scene, the objects, their geometry and image textures a lot and if I switch
[12:40] into rendered view well I can definitely say we still have a lot of quality over here but our scene
[12:48] has been optimized pretty well. So over here in this building shall I say I have the hero character.
[12:56] I have set my camera on it like so and I want to make a shot in this area at this angle. So what I do
[13:04] is to see what objects are visible or they are close to the camera. So we have the character,
[13:11] the top part of this building and a few objects in the background. So I select these objects
[13:19] and revert their images to originals and this time I make sure to set the target
[13:29] on selected objects and then hit okay. Then we click on revert meshes to originals and again
[13:36] we make sure to set the target on selected objects and hit okay. So the process is done and let's
[13:43] take a look in the rendered view because I do believe something interesting is going to happen.
[13:49] And done! This is just so cool. This is absolutely insane. What could be more insane than the fact
[13:58] that your blender can now handle a 10 gigabyte scene? This is just fantastic. So now the objects
[14:06] that are inside the camera view have their original quality but all the other objects
[14:12] have been optimized to a significant amount and the viewport is now so responsive and working
[14:20] with the scene is just so easy. So this was my workflow to optimize heavy scene and I hope you
[14:27] can take advantage of it in order to have an easier time working on your scenes. If you have
[14:33] enjoyed the tutorial don't forget to like the video and subscribe to the channel because more
[14:39] and better are on the way. So see you next time.



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

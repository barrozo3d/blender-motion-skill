---
title: I made the VFX tool Blender was missing... (Full Workflow)
source: YouTube
url: https://www.youtube.com/watch?v=TWYYOKlwgds
author: InLightVFX
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/i-made-the-vfx-tool-blender-was-missing-full-workflow/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# I made the VFX tool Blender was missing... (Full Workflow)

**Source:** [YouTube](https://www.youtube.com/watch?v=TWYYOKlwgds)
**Author:** InLightVFX
**Duration:** 26m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py i-made-the-vfx-tool-blender-was-missing-full-workflow <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In the world around us, straight lines appear straight.
[0:03] Except for when you film with a camera lens that makes straight lines appear curved or distorted.
[0:08] This is called lens distortion.
[0:10] Now as a VFX artist, if I want to put myself in this CGI environment, lens distortion poses a unique challenge.
[0:17] That's because while a real camera lens produces images which have distortion, a virtual camera lens renders images which have no distortion.
[0:24] If we try to put these two together, things won't align properly.
[0:27] So the big question is, how do we merge this imperfect distorted footage with this perfectly undistorted CGI world?
[0:35] Well first, we start with the footage and we remove the lens distortion.
[0:39] So now both the footage and the CGI environment have no distortion, which means we can properly merge the two together.
[0:46] And finally, we reapply the lens distortion so that this final shot has the same distortion as the original footage.
[0:52] So the workflow is undistort, do the VFX work, redistort.
[0:57] Simple to understand but a bit more difficult in practice.
[1:00] So today we'll dive into this workflow and I'll show you a custom blender tool I made to help you handle lens distortion the right way.
[1:12] Now it's been about two years since my last tutorial.
[1:15] And in that tutorial, I said, I'm very excited to announce that I've been working really hard on a VFX course.
[1:22] Now I'm excited to announce that my Blender VFX course is finished.
[1:27] It took me two years to make.
[1:28] It's the biggest creative project of my life and it's the one I'm most proud of because now over 1000 students are taking the course and I get to be there helping them learn and create their own amazing VFX with Blender.
[1:39] Now on Monday, September 7th, the course will be 20% off but only for the first 100 people.
[1:44] Also, since I keep adding more content to the course, the price is going up after the sale.
[1:49] So Monday is really the best time to buy the course.
[1:52] To learn more about the course and get details about the sale, click the link in the description.
[1:56] Alright, now back to the tutorial.
[1:58] The first thing we need to figure out is how to remove the lens distortion from this footage.
[2:03] The most common way to do this is to take the same camera and lens that you use to film the footage and point it at something like this calibration grid.
[2:10] This makes it easy to see how the lens distorts the image.
[2:12] To remove the lens distortion, I need to take a similar grid and figure out some sort of special math equation that distorts these points so they look like the real distortion.
[2:21] Once we figure this out, we can just reverse the math to go back to the normal grid.
[2:25] I can then just apply that same math to my footage and it should remove the lens distortion.
[2:30] So let's talk more about the special math that allows us to warp these images like this and it will help to first understand a few properties of real lens distortion.
[2:38] For starters, normal lenses have a point called the optical center.
[2:41] There is zero lens distortion right at the optical center and then lens distortion radiates outwards symmetrically around the optical center.
[2:49] The amount of lens distortion for a certain point can be calculated based on the distance of that point from the optical center.
[2:54] We'll give this distance the variable r for radius.
[2:57] So to simulate lens distortion, we can take the coordinates of this point and multiply them by r, the distance of the point from the optical center.
[3:04] And this will give us new coordinates.
[3:06] If we do this for all the points, our grid transforms into something that looks like this.
[3:10] This is the most simple lens distortion model and you can see how if we change the optical center, the distortion radiates around that point.
[3:17] And this is great, but there are a few ways we can improve this model.
[3:20] For starters, remember we said the optical center should have zero distortion.
[3:24] To recreate this property, we need to add one to the radius so that a coordinate at the optical center, which has a radius of zero, is just multiplied by one.
[3:32] And so therefore is unchanged.
[3:34] With this adjustment, our grid looks like this.
[3:36] Finally, we'll multiply the radius by a variable we'll call k1.
[3:39] By changing the value of k1, we can change the scale of the distortion.
[3:43] And now we understand the three basic ingredients of any lens model.
[3:47] We start with the optical center.
[3:48] We calculate the radius of a point to the optical center.
[3:51] And we use that radius and other variables in a special scaling function.
[3:55] The scaling function is really the secret sauce that makes a lens model special.
[3:59] If I change this equation slightly, adding input variables k2 and focal length, this gives us the brown con ready lens model.
[4:06] Now, I don't want you to be too concerned with the underlying math of these lens models.
[4:10] So let's just abstract this away for now.
[4:12] This model was published all the way back in 1966.
[4:15] And we still use it today because by changing the variables, we can pretty accurately recreate the distortion of most standard lenses.
[4:22] One thing this model struggles to recreate is the distortion of a wide fisheye lens, which has a really small focal length.
[4:28] You'll see if I lower the focal length down, the points kind of explode and this model falls apart.
[4:33] So 50 years after the brown con ready model was released, the canola brand or fisheye model was created.
[4:39] It takes the same input variables, but has a different scaling function, which handles wide focal lengths much better.
[4:45] The point is different models fit different types of lenses.
[4:48] Now remember, my goal is to distort this grid.
[4:50] So these points look the same as the real grid reference to do this.
[4:53] I could just play around with different values till I get distortion that looks close.
[4:57] But doing this by eye is not going to give us the level of accuracy we need.
[5:00] Instead, we can use a program that detects these corners and then calculates the best values to remove the lens distortion.
[5:06] And guess what? I made a tool that does exactly this.
[5:10] It's called Undistort. It works in Blender and you can find it linked in the description.
[5:15] Just so you know, the plugin only works in Blender 5.2 or newer.
[5:19] So once you have it installed, open the movie clip editor.
[5:21] To access the plugin, we need to have a movie clip open.
[5:24] So for now, I'll open up my main footage.
[5:26] Then on the right, open the track panel, go to the camera drop town, open lens, and here we see the distortion calibration tool.
[5:33] Now to start, go into the setup section, open checkerboard.
[5:36] These default settings are probably good.
[5:39] Click export and choose where to save this.
[5:41] This creates this image of a checkerboard pattern, sometimes what we call a lens grid.
[5:45] And the way we'll use this is by opening up this image and making it full screen on a monitor.
[5:49] Then grab the camera and lens you want to calibrate and put it on a tripod pointed at the lens grid.
[5:54] You want the camera to have a perfectly flat view of the center of the lens grid, making sure that it's level in all directions.
[6:00] Finally, you want to make sure your lens grid fills the full view and it's in focus.
[6:04] Then record a short video of the grid.
[6:06] If I want to remove the lens distortion from this footage, it's important that the lens grid is captured with the exact same camera setup,
[6:13] including lens, focal length, and recording format.
[6:16] Alright, so back in Blender, let's bring in the lens grid we captured.
[6:19] If you recorded a short video, move to a frame that looks good and then keep all these default settings and hit detect.
[6:25] This might take a few seconds and then hopefully you see these markers placed on the corners of your grid.
[6:29] You can zoom in and check these, move them or delete any if they don't look right, but these all look good.
[6:34] So next I'll hit solve.
[6:35] When I do this in the results section, you can see all the lens models that were solved for.
[6:39] Next to each of them, you see a listed error value.
[6:42] A lower value generally indicates a better solution.
[6:44] In this case, the Nuke model looks pretty good.
[6:46] So I'll choose this one.
[6:47] And then in the detail section, I can see the values that it calculated.
[6:51] If I now hit apply to clip, this copies all these values from here, all the way up here, because these are the values that Blender actually uses.
[6:59] And you'll notice we switched to viewing the undistorted image, which you can toggle in the clip display dropdown with this render undistorted checkbox.
[7:06] To apply this undistortion to my actual footage, which we still have open here, I'll go back to the calibration grid and then back down here in the results section for the target clip.
[7:15] I'll choose the footage and click apply.
[7:18] And now if we look at the footage, we can see that those Nuke lens distortion values have all been copied over and these are effectively removing the lens distortion.
[7:26] Now I want to export this undistorted footage so that I can re-import it.
[7:30] And there's a few good reasons for that, which I'll explain as we go.
[7:33] But first, to export this undistorted footage, we're going to use a technique that is standard in Pro VFX workflows, ST maps.
[7:40] This is what an ST map looks like.
[7:42] If we break this apart, you'll see it's made up of a red channel, which goes from 0 to 1 horizontally, and a green channel that goes from 0 to 1 vertically.
[7:49] Put these together and we get this.
[7:51] So if we sample the color of a pixel, the red and green values just give us coordinates.
[7:55] Define how an input image is mapped to an output image.
[7:58] If we change the scale or the rotation of the ST map, you can see how this affects the output.
[8:03] The cool thing is that we can apply an effect to this ST map like this twist effect and the output will be deformed in the same way.
[8:09] Now you might be wondering, why don't we just apply the effect directly to the image?
[8:13] Well, by applying the effect to the ST map, we can then export the map and then bring it into a different program or project.
[8:19] And even if this program doesn't have the twist effect, we can still take any input image and apply the same deformation, assuming this program supports ST mapping.
[8:27] In our case, instead of applying this twist effect to the ST map, we're going to apply the lens distortion.
[8:32] And now this ST map has the complex lens distortion baked right into it.
[8:37] This means going forward, we can save and reuse this map anytime we need to remove lens distortion from footage filmed with this same lens and camera.
[8:45] So back here in Blender, let's export this undistorted footage using ST maps.
[8:49] Here in my plugin, there is this export ST map section.
[8:52] In the first drop down, you select the lens data you want to export.
[8:55] If you select current clip data, that will use the lens data that's up here.
[8:59] Then in the next drop down, we choose the program we want to export for.
[9:03] Blender just expects ST maps in a slightly different format from the other programs.
[9:07] And then we have these options, native and overscan and undistort and distort.
[9:11] Well, I want to remove the lens distortion, so that is undistorting the image.
[9:15] But what does native and overscan mean?
[9:17] Well, often when we undistort an image, parts of the image go outside the original image area.
[9:22] To make sure this stuff isn't cut off, we need to add padding or what we call overscan.
[9:26] So we have the native image area and the overscan image area.
[9:30] In most cases, we want to keep this overscan area and I'll explain why later.
[9:34] So back in the plugin settings, we're going to choose overscan.
[9:37] We can choose where to save the map. Then we can choose just to export the ST map alone.
[9:41] But let's click create compositor setup. This might take a few seconds, but then it should say that it created a new compositor node group with this ST map.
[9:49] So let's open up the compositor and I'm going to clean things up a bit.
[9:52] And then I'll open up another window and make this one the image editor.
[9:56] And up here, I want to look at the viewer node, then hold control shift and click on this node and you should see something on the right.
[10:02] So by having a viewer node selected up here, we'll see whatever is connected to the viewer node in the compositor.
[10:07] Now this image is getting cut off, as you can see in the edges here.
[10:10] To fix this in the compositor options menu, change your device from GPU to CPU.
[10:15] I'm not sure why GPU isn't cooperating, but now we see the full undistorted image, including those overscan areas.
[10:21] So how exactly is all this setup?
[10:23] Well, we have our movie clip here and we have our ST map here.
[10:26] Now this looks a bit different than the ST maps I described earlier.
[10:29] And that's because in Blender, ST maps not only have the standard red channel and the standard green channel,
[10:34] but it also needs a blue channel with a solid value of one.
[10:37] And finally, we have this node and this is just a map UV node, which has been renamed undistorted.
[10:42] As you can see, it takes the image in one input and warps it by the ST map and the other input.
[10:47] By the way, anytime you use an ST map, make sure that the color space is set to non color.
[10:53] Okay, now to export this in the viewer, I'll go into the overlays menu and turn on the text info and render region.
[10:59] This shows us the region that will actually be exported.
[11:02] And you can see it's quite a bit smaller than what we need.
[11:05] Up here, you can see that's because my render size is set to 1920 by 1080, while this image is a lot bigger.
[11:10] To fix this, I'll open up another window.
[11:12] We'll change it to the properties editor and in the output properties, let's set the resolution to this image size.
[11:18] So 13204 by 9903.
[11:21] And now you can see the render region is the correct size.
[11:24] Now this is a huge image to export.
[11:26] So I will lower this percent slider to 50 to render at half resolution, which will shrink the render region.
[11:31] Now in the compositor, let's add a scale node with the scale type set to render size.
[11:35] And that will scale our output to this render resolution.
[11:38] Now you need to make sure that whatever you want to export is connected to this group output node, because that's what's actually saved out.
[11:44] Finally, choose which file format you want to save out and where you want to save the file and hit render animation.
[11:50] With that rendered out, let's come back to the movie clip editor.
[11:53] I'll make some space here and let's open the file we just exported.
[11:56] Now here we could do camera tracking, but this shot is static.
[11:59] So I'll just go right into the 3D viewport, select the camera and let's bring back the property editor so we can go into the camera properties.
[12:07] I'll enable background images, choose add image, movie clip and let's open the undistorted clip we just imported.
[12:14] Then go to view, viewport, camera to look through this camera.
[12:18] And you should see your footage in the background and the dimensions of the camera should be correct since we set the right aspect ratio in our project resolution.
[12:26] Alright, so there we go.
[12:27] We figured out how to remove the lens distortion from this footage, so now both the real camera and the virtual camera have no distortion.
[12:34] Next, we want to figure out how zoomed in or zoomed out the virtual camera should be.
[12:39] The technical term for this is field of view.
[12:41] We want the field of view of the virtual camera to match the field of view of the real camera.
[12:47] Field of view is determined by sensor size and focal length.
[12:50] Now what exactly are those things?
[12:52] Well every lens projects a circular image.
[12:54] The focal length of the lens determines how zoomed in or zoomed out that image is.
[12:58] Now only part of this image is captured by the camera sensor.
[13:01] Therefore the sensor size also impacts the field of view.
[13:04] So field of view is actually a function of the sensor size divided by the focal length.
[13:08] This means that if we double the sensor size we get this field of view.
[13:12] We'll put this image over here.
[13:13] But now watch this.
[13:14] If we reset the sensor size and instead we cut the focal length in half, we actually get the same field of view.
[13:20] As you can see this is the same image.
[13:22] So hopefully this helps you appreciate the relationship between sensor size and focal length.
[13:26] So how do we figure out the sensor size and focal length of our real camera?
[13:29] Well when you use a single image to calibrate lens distortion, the solver actually calculates focal length as part of the solution to remove the lens distortion.
[13:37] So can we just use this focal length?
[13:39] Well not quite.
[13:40] The problem is that the solver can find multiple solutions with different focal lengths that all produce this exact same undistorted image.
[13:47] Now only one of these solutions can represent the true focal length of the lens that we filmed with.
[13:52] But odds are the solver probably found one of these solutions which removes the lens distortion just fine but doesn't provide a realistic focal length calculation.
[14:00] And this is just a natural limitation of calibrating with a single image that we need to be aware of.
[14:05] If none of that made sense, just know that single image calibration is great for removing lens distortion, but you shouldn't trust the focal length that it calculates.
[14:13] To show you this a bit more concretely, I'm back here in the movie clip editor where we did the lens calibration.
[14:18] Here in the results section we chose the nuke model and if you open the details drop down, you can see the nuke model is actually the one that doesn't estimate the focal length.
[14:26] So we couldn't use the estimate even if we wanted to.
[14:29] But if we switch to these other models, you'll see the focal length estimate here in the table and the warning that single frame focal and optical center are unreliable.
[14:37] Again, while the solver is able to find the best focal length for removing the lens distortion, it's not the best in terms of representing the true focal length of the lens.
[14:46] So here are a few ways to figure out the center width and focal length of your camera.
[14:50] First, you can just use the specs of your lens and camera.
[14:53] And I know my lens has a focal length of 7.5mm and a quick search shows that my camera has a center width of 17.3mm.
[15:01] So I'll go back into Blender and I'll enter in 7.5 for my focal length.
[15:05] Then for the sensor width, I'll change this from auto to horizontal to make sure we're changing the width and I'll enter in 17.3.
[15:12] Now before we go on our merry way, there's one very important thing we need to be mindful of.
[15:17] Remember when we undistorted our image, we wound up with an overscan area and the native image area.
[15:22] These actually have different fields of view.
[15:24] The camera specs we just found for focal length and sensor width represent the native image area.
[15:29] So how do we calculate the overscan focal length and sensor width?
[15:32] Well, we know the native resolution is 5760x4320 and the overscan resolution is this large number.
[15:38] By dividing the width values, we calculate that the overscan is 2.29x bigger than the native image area.
[15:45] We'll call this number the overscan multiplier.
[15:47] For the overscan focal length, it's most accurate to keep this the same focal length.
[15:51] And then to calculate the overscan sensor width, we take the native width and we multiply it by this overscan multiplier,
[15:56] which gives us our new overscan sensor width.
[15:59] So you can think of the overscan area as just a larger camera sensor.
[16:02] To find the overscan multiplier, we can come back to the Movie Clip Editor with the lens grid open.
[16:07] And here in the results section, we see for the Nuke model we're using, the calculated overscan multiplier is listed right here.
[16:13] So we'll go back to the 3D viewport.
[16:15] And again, since we're using the overscan, here in our camera settings, we'll multiply the center width by that multiplier.
[16:21] Alright, so that's how you can use the lens and camera specs to figure out the field of view of our camera.
[16:26] The second way we can figure out the field of view is by doing camera tracking.
[16:29] Now, since this shot is static, there's no camera movement to track.
[16:33] But here's a different shot where the camera is moving and I've added a bunch of tracking markers.
[16:37] Here in the solve tab in the solve dropdown, we can enable refine focal length to tell Blender to guess the focal length as it solves the camera motion.
[16:45] Now, currently the sensor width and focal length are set to their defaults.
[16:48] But watch this focal length.
[16:49] When I hit the solve camera motion button, it doesn't change.
[16:53] Now, you probably won't have this issue.
[16:55] But since this is such an extreme lens and these default values are so far away from the real values, Blender is having a hard time.
[17:02] So let's help Blender out a bit and enter in the sensor width and focal length values we just calculated using the camera specs.
[17:08] And here we're using the overscan sensor width since we're tracking the footage with overscan included.
[17:13] Now, when we hit solve camera motion again, Blender is able to refine this focal length and the result is not far off from our camera specs, which is a good sign.
[17:21] And beyond the focal length, we can even have Blender estimate the optical center.
[17:25] And it can even solve the lens distortion if you're tracking a shot that still has distortion.
[17:29] The accuracy of Blender's estimates depend on having a good amount of accurate tracking markers with enough camera parallax.
[17:36] And since we have that for the shot, I'm going to trust the focal length estimate that it gives us.
[17:40] And actually, since I filmed the shot with the same camera lens as our main VFX shot, I'll take this focal length estimate and I'll use it for our main VFX shot.
[17:48] Alright, the final and I think the best way to figure out focal length and sensor width is to use a feature in my plugin called multi-image calibration.
[17:56] You see, the problem with single image calibration is that the solver can't tell the difference between a grid captured up close with a wide angle lens and a grid captured far away with the lens zoomed in.
[18:06] One way we can prevent this ambiguity is by giving the solver multiple images to calibrate from.
[18:11] To get set up for multi-image calibration, go back to the plugin, go to the setup section and open the Charruco board dropdown.
[18:18] Here you can use the default settings and save out a PNG.
[18:21] Just like before, we'll open up this image on our monitor, then we're going to take our camera and record a video of the board.
[18:27] This time, our goal is to capture multiple angles of the board from up close and farther away.
[18:32] Also, the full board does not need to be visible in every frame.
[18:35] In fact, it's good to capture frames where the board goes off the edges, as you can see me doing here.
[18:40] This is because lens distortion will be greatest at the edges, so we want to capture that data.
[18:45] And finally, you want to keep the board sharp and in focus, so a higher shutter speed and high aperture value can help this.
[18:51] Now, instead of a video, you can also take multiple photos.
[18:54] Whatever you do, again, we want to make sure that these calibration images and our original footage are captured with the exact same camera setup and settings.
[19:02] Back in Blender, I'm going to drag in the first image in the sequence I shot and all the images should be loaded.
[19:07] And now in the plugin, we have the option to solve using the full clip, which is what we want.
[19:11] With the frame step set to 1, this will use every frame for the solving process.
[19:15] And this works well since I shot photos and each of them are quite different from each other.
[19:19] But if you recorded a video like this, using every frame for the solver is going to take a long time and the solver will get confused when the frames are so similar.
[19:27] So for a video, you should set the frame step to something higher, like 50 or 100 frames.
[19:32] Then, all that's left to do is hit detect and solve, and we wait.
[19:35] The way that this works is that the special Chorruco board we're using gives each corner point a unique pattern.
[19:41] This allows the solver to track the same points across multiple frames.
[19:44] It calibrates our lens with pretty much the same math used by the camera tracker to figure out the focal length, optical center, and distortion.
[19:51] Only instead of needing to manually place all these tracking markers, the plugin can track the Chorruco points automatically.
[19:58] Once it finishes, you should see this button, View Coverage Plot.
[20:01] If I click this, I can then come into the image editor and open this new coverage plot image.
[20:06] This image shows the position of all the points that were used in the solving process.
[20:10] Naturally, you'll have more points in the center of the frame, but ideally you want to see points all the way to the edges.
[20:15] So this looks pretty good.
[20:17] Back here in the results, we can see the details, and again, it looks like the Nuke and fisheye models have the lowest error.
[20:23] I could choose Nuke, but remember this model doesn't estimate the focal length, so I'm going to select fisheye.
[20:28] Now remember, our camera center width should be around 17.3 millimeters, and currently it's set to 35.
[20:34] The center width that's listed here is actually just using whatever value we have set up here for the center width.
[20:39] So you can see if I change this center width, the center width value here in the table is synced up.
[20:44] And not only this, but the focal length also changes in a way that makes the resulting field of view stay constant.
[20:50] So I'm going to set the center width to 17.3, taken from our camera specs.
[20:54] Now this multi-image calibration solved everything much better than the single image calibration did.
[20:59] So I'm going to export some new ST maps.
[21:02] I'll choose the fisheye model, then I want the overscan, undistort, and also distort maps.
[21:07] We're going to use the distort soon, and we'll create a compositor setup with these.
[21:11] Now into the compositor, let me get a little bit organized.
[21:15] Here we have two ST maps chained together.
[21:18] First the footage is being undistorted, so that we keep the overscan, and the second map reapplies the distortion.
[21:24] So essentially these two cancel out, and this final result should look like the original footage.
[21:29] And you can see that these do indeed match, and this is a good check that you can do.
[21:33] Now I'm going to fast forward and go through the same export process we've talked about earlier,
[21:37] making sure to change the project resolution, since our new ST map is a different size.
[21:42] Now just before we export this, I want to change my movie clip to the actual footage, and then we would render this out.
[21:47] Then back here in the 3D viewport, I'm actually going to delete our old camera.
[21:51] I'll come back to the multi-frame calibration, and here at the bottom you can see a handy button called create camera.
[21:57] With the overscan and fisheye model selected, this will create a camera using these fisheye overscan values.
[22:03] And this is nice because not only do we not have to copy over the sensor width and focal length values,
[22:08] but these optical center values, which we can now trust, actually affect some camera settings called shift X and Y,
[22:14] which the create camera button will take care of.
[22:16] So we'll hit create camera, and this will set the correct project resolution, though we already did that.
[22:21] Now we can come back into the 3D viewport, and we can see the new camera.
[22:24] Let's rotate this a bit, and go into view, camera, active camera.
[22:28] Then I will go over here into the camera settings, and we can see the correct focal length,
[22:32] sensor width, and shift values have been set.
[22:35] All we need to do now is bring in the new undistorted footage.
[22:38] Alright, so finally we have it all set up, so our real camera and the virtual camera have the same field of view.
[22:45] The only problem now is that our CGI environment looks like this.
[22:49] So at this point, we need to do the VFX.
[22:52] So on BlenderKit, I found this really cool environment made by this artist, David Tirindeli.
[22:58] And then with the scene loaded in Blender, we're going to take the camera that we set up, look through it,
[23:02] and we need to figure out the right position for this camera in 3D space, so that I'm at the right scale,
[23:07] and I appear like I'm sitting on this bench.
[23:09] I took a bunch of measurements of the real scene to make this process a lot easier.
[23:13] Next up is the lighting.
[23:14] I have this light, which recreates the light coming from my big softbox here,
[23:18] and you can see over here I have this reflector that is bouncing warm light into the back of my head.
[23:23] And I put that there because I really wanted to have some nice warm sunlight in this environment.
[23:27] And finally, I created this creepy figure aligned with where I'm sitting,
[23:31] and this cast shadows to make it look like I'm actually in the environment.
[23:34] And since these foot objects need to be perfectly lined up,
[23:37] I made sure that I didn't move my feet while I was filming to prevent a lot of extra work.
[23:41] Okay, now once you're ready to render the scene,
[23:43] just remember we set our project resolution quite high,
[23:46] and even at 50%, this is still a pretty big render.
[23:49] So feel free to make this even smaller if you want.
[23:51] Now I'm going to come into the compositor, and here I have a few things laid out.
[23:55] I have my original footage, which has distortion,
[23:57] then I cut myself out of the footage, still distorted,
[24:00] then I have a render of my CG environment with the overscan field of view,
[24:04] and then we have two ST maps, one to apply the distortion and one to remove the distortion.
[24:08] At this point, I want to apply the distortion to my CG environment.
[24:11] This is the last step of the process, reapplying the distortion.
[24:15] So I'll create a map UV node, connect the image, connect the distort ST map,
[24:20] and now this environment has been distorted.
[24:22] Now the way these ST maps work, the resolution of the input actually doesn't matter.
[24:26] The ST map will always scale the input to the size of the ST map.
[24:30] To prove this, I'll add a scale node and scale the environment way down to 5%,
[24:34] and you can see in the output, while we're losing detail, the overall size remains correct.
[24:39] Let me just reset this real quick.
[24:41] The most important thing is that we give this ST map an input,
[24:44] which has the same aspect ratio as the undistorted overscan ST map.
[24:48] Now remember, we set the project resolution to the size of this map.
[24:51] So as long as we render at some percentage of this resolution,
[24:55] then the aspect ratio of our render will be correct.
[24:58] Alright, so now both the environment and my cutout have the original lens distortion.
[25:02] So I just need to merge these two together.
[25:04] I'll create an alpha over node, connect the environment to the background,
[25:07] and I'll put myself in the foreground.
[25:09] Then let's view this output, and there we go.
[25:12] Everything is lining up.
[25:13] So the key thing to notice here is that for the final composite,
[25:16] we never actually undistort the original footage.
[25:18] We keep it distorted, and we only apply the distortion to the VFX.
[25:22] The main reason that we undistorted the footage earlier was so that here in the 3D scene,
[25:26] we can see the undistorted footage in the background to help line everything up.
[25:30] And undistorting the footage is also really important if you're doing camera tracking.
[25:34] Now one final note, we rendered this environment with the overscan included.
[25:38] But I'm going to bring up some nodes I have hiding down here,
[25:41] because I want to show you that this is what the render would look like without the overscan.
[25:45] You can see it's a lot smaller, and this is nice because this will render a lot faster.
[25:49] But the only problem is, when we distort this, we get these transparent edges.
[25:54] And so that's the main reason we work with overscan,
[25:56] to make sure that when we distort the VFX, we're not missing the edges.
[26:00] And with a bit more compositing work and some final color grading,
[26:03] we wind up with a shot that looks like this.
[26:06] Alright, well I hope all of that made some sort of sense,
[26:09] and that the distortion plugin actually works.
[26:12] Remember to check out my Blender VFX course linked below,
[26:15] that sale is happening Monday, September 7th.
[26:18] Other than that, thanks for watching, and I'll catch you in another video.
[26:26] Bye!



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

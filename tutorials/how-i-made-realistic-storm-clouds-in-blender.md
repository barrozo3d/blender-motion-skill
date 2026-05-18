---
title: How I Made Realistic Storm Clouds in Blender!
source: YouTube
url: https://www.youtube.com/watch?v=Kep7URnyXgU
author: c g s l a v
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["geometry-nodes", "volume", "rendering", "cycles", "lighting", "hdri", "organic", "intermediate", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/
frame_count: 0
---

# How I Made Realistic Storm Clouds in Blender!

**Source:** [YouTube](https://www.youtube.com/watch?v=Kep7URnyXgU)
**Author:** c g s l a v
**Duration:** 21m32s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** An amazing landscape just isn't complete without an atmospheric sky.  It's a heart of fainting scene, especially when combined with stunning light.  Do you want to create a job drop in sky and blanda like this one?  In this tutorial I'll show you my ways to create stunning skies from quick to an advanced method for dynamic and stormy effect  with dynamic light rays and realistic clouds to transform your scenes into epic artwork.  And here is my blanda scene for demonstrating how we can create skies in blanda.  As you can see it's simple basic light, just environment color, that's all.  And it looks a bit dull and lifeless.  But we can easily change that by it in a vibrant sky and dynamic light.  And you know this is way to a sky in blanda.


### Easy way to add sky in Blender [0:51]
**Transcript:** I've got even two super straightforward methods, just take a simple plane, rotate it and place it behind your scene.  Then in the shad editor apply sky image as a base color and use the same image or animation.  But the image and strings and voila!  A gorgeous atmospheric sky, just a couple of clicks.  It remains only to find on the plane position to hide anything we don't want to see in the frame.  Living only this tiny sky in the camera view.  Good, the second is a way to add a sky is total history forward.  We can simply use a new hri in the wall shader.  Likely there are tons of free hri available on Blanda Kit or polyharen that we can use in our scene,  which also let us create an awesome sky in blanda.  As you can see this is another really effective method to craft in atmospheric sky.  Check this incredible clouds.  And both of these method works great for different types of scenes, but they do come with some big drawbacks.


### Create Light Rays in Blender [2:09]
**Transcript:** And if you want to add sun rays and god rays or atmospheric light to your scene and at the same time,  how to create atmospheric light rays in blanda.  And to do this, we need a simple cue with volume material.  I've already got one in my asset browser.  Just drop it into the scene, scale it and move it where you want to those light rays to appear.  Next, we need to take shell light.  I've got already to use lights in my asset tool.  This is a simple blanda spotlight.  Place this light inside the volume cube and rotate it.  Now you can see the stunning light rays in action.  And I want to highlight the field behind this house.  So I rotate this light to direct this beam right to that spot.  Next, let's decrease the volume's density.  It's a bit too intense right now.  So why these two methods of fading sky in blanda aren't always too much convenient?  The problem is that our sky doesn't really interact with this scene, especially with the light.  For example, if I move this sky cause of the light, the light still will not eliminate the clouds because it's just a flat plane.  And now we come to the exciting part.  How to create the realistic awesome sky with clouds that actually int...


### How to create Clouds in Blender [3:52]
**Transcript:** So let's create some clouds in blanda for this scene.  To get started, I'll add a bit of the sphere and increase the size.  Then apply scale and let's go to geometry notes.  Next, select our object and create new notes setup.  The goal here is to create realistic clouds from this sphere.  And then by duplicating it, build a larger impressive cloud shape.  But let's take it step by step.  Just we need to convert this mesh to a volume using the mesh to volume not.  You can already see the volume takes shape in the report.  But clouds aren't just a bunch of spheres alone.  They have a distorted and organic look with fine details, especially in southern areas.  In other words, beyond the main cloud shape, we also get these subtle extra details, extra particles.  To start creating that realistic cloud effect, we will use the distribute point in volume not.  This allows us to convert the volume into point cloud.  And from there, we can get built in.  Next, we need to convert this point cloud back to volume using the point volume not.  Now it's already starting to look much closer to a real cloud shape.  After that, let's convert it to mesh again so we can clearly see this cloud-like mesh...


### Large Scale Clouds in Blender [12:09]
**Transcript:** It's super easy. Since we build these clouds using geometry knots I can simply go to edit more on this base sphere or base object and use shift did to duplicate it.  As you can see everything is set up in geometry knots applies automatically to the new geometry.  Pretty cool right?  This way we can create all sorts of shapes for our clouds.  First I disabled the geometry knots and just duplicate them the most object the within the larger one.  I duplicate the sphere as I sink it might look good shaping it into what feels like a big cloud.  After that I enable geometry knots again turn it to volume knot and boom that's it.  Looks fantastic doesn't it?  Finally we need to add a material to these clouds.  In geometry knots I only set material knot which let us assign a material to those clouds but first we need to create a material in the shade editor.  And since this volume will use volume shader here and connect it to volume output.  Set the color to pure white. Now we can apply this material using the set material knot.  Look at that it's coming together beautifully.  If you notice some rough quality like we see here at the edges of the clouds we can fix that.  In the last mesh vol...


### Create Cloudy Sky in Blender [15:05]
**Transcript:** Alright let's bring these clouds into the main scene.  I'll just copy this cloud object switch to the main scene and paste it here.  Nice!  Now we can move these clouds from the scene, scale them if needed.  And most importantly to make them for specific needs.  Just like we did in the clouds setup you can duplicate more of the lead spheres within the clouds geometry to get it look you want.  Then enable the volume knots and check out the adjusted clouds in the scene.  So I took the single cloud we created earlier and used it across the whole scene.  Duplicating it your time and making some tweaks.  As that's now I got these clouds.  Let's enable pre-render and now we can see how our light interact with the clouds.  Letting us not only create light rays but also beautifully highlight the sky and clouds so with this light.


### Light Linking Tricks [16:13]
**Transcript:** But here's the cool trick I used with the light.  I'm not going to use the same light we set up for the light rays to highlight those clouds.  Instead I go to Saturn's, head to Sadentop and open light linking.  I drag the entire clouds collection here and then check this check box.  Now the light will link to all these cloud objects but since we uncheck this box it will exclude the clouds lighting up every scene else in the scene except the sky.  This way I can use separate light sources, one just for light rays and another for clouds.  So next I'd spot light and place it behind the clouds to create sunlight effect coming through the clouds sky.  Now you can see this light illuminating the clouds.  This setup is way more flexible. Letting us control everything with two separate light sources for different purposes.  One dedicated for the clouds and another one just for light rays and highlight in the field in the scene.  So if I remove the light linking for example you can see it still highlights parts of the clouds.  But what I really want is the light coming through the clouds like the sun coming through the air onto the earth.  I could move this texture light and rotate it to ca...


### Volume effects for realistic Sky [18:10]
**Transcript:** Finally I want to tweak the horizon. Right now it doesn't look great and I want our clouds and blend seamlessly with horizon and the forest in the background.  I'm creating a mind-sale Kevin Storm clouds formation rolling towards us.  So does this? I duplicate the volume cube, scale it up and move it out to the scene positioning behind the clouds.  Then scale it once more to cover the entire frame. Something like this here.  Next I duplicate the volume shader and start looking with it.  Increase the density and now it's starting to look really impressive.  To refine this and remove the top part of the volume so the effect will focus it only near the horizon I need a mask.  For example I will use a gradient texture where it weighs mapping and color and a classic combo I'd say.  Rotate the gradient by 90 degrees. Yeah negative 90 degrees and move it up.  Switch the color ramp to be splined to soften the mask.  Now use this color ramp as the density value in the volume shader.  And there we go. This effect now covers only the part of the horizon I want.  The lower section of this cloud and horizon.  Because the gradient texture exists a mask that I don't know if everything is a bowl a...


### Volume Blender Optimization [19:50]
**Transcript:** So this is how you can create clouds and atmospheric sky right in blender.  Essentially there are three methods I use and before we wrap up a quick knot on optimization.  Since everything here is built with volumes and there are a lot of volumes in the scene now it's clear on this directly impacts performance.  Especially when for the final image you will want the smaller value of voxel size to get much sharper details.  And if you don't want to wait forever for the render finish you can do it with the global volume settings since the render settings here.  By default these settings are way too high for a final image but we can adjust them slightly.  I set max step to 500 well and increase step rate render from 1 to 3.  I also adjust the viewport settings to avoid overloaded the GPU while walking.  This way you can save some time or rather avoid wasting it because the quality doesn't suffer at all.  Just make sure to check test render to avoid any artifacts on the render.  You might need to find on the settings for your own scene.  So thank you for watching this video. Don't forget to subscribe to my channel, Instagram, X and Patreon to access my classes and sets.  And I'll catch y...



---

## Structured Notes

### Core Technique
Creates realistic volumetric storm clouds using a multi-pass Geometry Nodes pipeline — Mesh to Volume → Distribute Points in Volume → Points to Volume → Volume to Mesh — cycling between representations to add organic fine detail, combined with Light Linking to separately control cloud illumination and god ray effects.

### Summary
The tutorial presents three sky methods (image plane, HDRI, and full volumetric clouds) and focuses on the advanced volumetric approach. Each cloud shape starts as a duplicated Sphere that goes through a Geometry Nodes pipeline: Mesh to Volume → Distribute Points in Volume (adds sub-detail noise) → Points to Volume → back to Mesh → assign white Volume Scatter material. Clouds are built by duplicating and reshaping the base sphere — the GN pipeline auto-applies. God rays use a Volume Scatter cube with a Spotlight inside. A key trick uses Light Linking to assign one Spotlight exclusively to the clouds (for rim/backlight) and a separate Spotlight for the ground god rays. A second large Volume Scatter cube with a Gradient Texture mask creates atmospheric horizon haze. Optimization: Max Steps: 500, Step Rate Render: 3 in render settings.

### Key Steps
1. Add a **Sphere** → Apply Scale → add **Geometry Nodes** modifier → click New
2. In GN: **Mesh to Volume** node (Voxel Size: 0.1) → **Distribute Points in Volume** (Density: 5–10) → **Points to Volume** (Radius: 0.15) → **Volume to Mesh** → **Set Material** (white Volume shader)
3. Duplicate the sphere and reshape in Edit Mode to build cumulus cloud clusters; the GN pipeline auto-applies
4. Assign a **Volume Scatter** material: Color: white; Density: 0.05–0.2; Anisotropy: 0.5
5. For god rays: add a large **Cube** → assign Volume Scatter material (Density: 0.01) → place a **Spotlight** inside it; adjust Spotlight angle for beam direction
6. Use **Light Linking** (Object Properties → Visibility → Light Linking): create one Spotlight linked only to cloud collection for cloud rim light; keep second Spotlight for ground fill and god rays
7. For horizon haze: duplicate Volume Scatter cube → scale to fill horizon → add **Gradient Texture** (rotated -90°) → **Color Ramp** (B-Spline) as Density mask to fade haze at top
8. Optimize in Render Properties → Volume: Max Steps: 500; Step Rate (Render): 3

### Nodes / Settings
- Mesh to Volume — Voxel Size: 0.1–0.05 (smaller = more detail, slower)
- Distribute Points in Volume — Density: 5–20 (controls fine cloud texture)
- Points to Volume — Radius: 0.1–0.2; combined with the mesh conversion adds organic blob detail
- Volume to Mesh — Threshold: 0.1 for clean mesh extraction
- Volume Scatter material — Density: 0.05–0.2; Anisotropy: 0.4–0.7; Color: pure white
- Spotlight (god rays) — inside Volume Scatter cube; Energy: 1000–5000 W; angle toward scene
- Light Linking — separate Spotlights for clouds vs. ground; use Include/Exclude collections
- Gradient Texture — Rotate mapping -90° for vertical gradient as horizon density mask
- Render Volume settings — Max Steps: 500; Step Rate Render: 3 (performance optimization)

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#geometry-nodes #volume #rendering #cycles #lighting #hdri #organic #intermediate #advanced

---

## Related Tutorials
- [3 Easy Lighting Setups | Blender Tutorial](./3-easy-lighting-setups-blender-tutorial.md)
- [How to create a Cinematic Landscape inside Blender | Full tutorial with Project file](./how-to-create-a-cinematic-landscape-inside-blender-full-tuto.md)
- [Tutorial: How to make a volumetric projector in Blender 4.5](./tutorial-how-to-make-a-volumetric-projector-in-blender-45.md)
- [3D Smoke (Blender Geometry Nodes)](./3d-smoke-blender-geometry-nodes.md)

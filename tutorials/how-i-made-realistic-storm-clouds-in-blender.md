---
title: How I Made Realistic Storm Clouds in Blender!
source: YouTube
url: https://www.youtube.com/watch?v=Kep7URnyXgU
author: c g s l a v
ingested: 2026-06-25
blender_version: "Blender 4.3.1 -- observed in all 8 frames"
tags: [volume, clouds, geometry-nodes, rendering, lighting, atmosphere, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
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
**Transcript:** And if you want to add sun rays and god rays or atmospheric light to your scene and at the same time,  how to create atmospheric light rays in blanda.  And to do this, we need a simple cue with volume material.  I've already got one in my asset browser.  Just drop it into the scene, scale it and move it where you want to those light rays to appear.  Next, we need to take shell light.  I've got already to use lights in my asset tool.  This is a simple blanda spotlight.  Place this light inside the volume cube and rotate it.  Now you can see the stunning light rays in action.  And I want to highlight the field behind this house.  So I rotate this light to direct this beam right to that spot.  Next, let's decrease the volume's density.  It's a bit too intense right now.  So why these two methods of fading sky in blanda aren't always too much convenient?  The problem is that our sky doesn't really interact with this scene, especially with the light.  For example, if I move this sky cause of the light, the light still will not eliminate the clouds because it's just a flat plane.  And now we come to the exciting part.  How to create the realistic awesome sky with clouds that actually interact with the light,  producing stunning light beams that highlight the clouds beautifully.


### How to create Clouds in Blender [3:52]
**Transcript:** So let's create some clouds in blanda for this scene.  To get started, I'll add a bit of the sphere and increase the size.  Then apply scale and let's go to geometry notes.  Next, select our object and create new notes setup.  The goal here is to create realistic clouds from this sphere.  And then by duplicating it, build a larger impressive cloud shape.  But let's take it step by step.  Just we need to convert this mesh to a volume using the mesh to volume not.  You can already see the volume takes shape in the report.  But clouds aren't just a bunch of spheres alone.  They have a distorted and organic look with fine details, especially in southern areas.  In other words, beyond the main cloud shape, we also get these subtle extra details, extra particles.  To start creating that realistic cloud effect, we will use the distribute point in volume not.  This allows us to convert the volume into point cloud.  And from there, we can get built in.  Next, we need to convert this point cloud back to volume using the point volume not.  Now it's already starting to look much closer to a real cloud shape.  After that, let's convert it to mesh again so we can clearly see this cloud-like mesh structure.  Yeah, looking good.  Now we can boost the density of the points to refine it further.  Nice. That's almost exactly what we need.  And we need to convert everything back to volume one more time.  To see this effect more clearly, let's add some light to the environment like sky texture in Blenda.  Enable preview render, and I also run it transparent in the render settings to remove the background from now.  Now it's really starting to look like a cloud.  So let's take another look at how this works.  We start with the first knot to convert it to volume.  Then add a point cloud, convert them to volume, turn it to the mesh, and then back to the volume again.  So this is basic setup. You might be wondering why we go through all these steps.  I'm not into volume, then match, and back again instead of stopping off as a first volume since it already looks like a cloud-like.  By using this action and knots we can make our clouds look even more realistic.  For now, I'll disable the final knot to view the mesh in the viewport.  And next, I'll change the amount to size in each knot.  This is crucial for proper scaling the clouds.  In this case, when a scale's object is an entire effect that just does a new scale without distorting or stretching the details.  It works much more accurately.  Now let's add some realism to the cloud and around the mice it's shape to make it look more natural.  So with more of this fine organic details like we see here.  To do this, I add a set position knot and place it right after the distribute point and volume knot.  With this we can use the offset to achieve the points in different directions along the x, y, and the axis.  But instead of just using simple values, let's use a noise texture for example.  And check normalize in this knot and adjust the scale in the noise texture to control this offset.  To find on this effect even more, we can add the vector math knot, set it to scale and adjust it so the points spread out as much as needed.  Depending on type of clouds you won't, of course.  I'll keep the spread fairly moderate so as I don't need a huge scatter of this one.  Next, I'll add another set position knot, just duplicate in the previous one and place it in the right of the heat.  With this knot we can add even more variation to this points for a richer cloud effect.  Here I'm going to use a varanoi texture and connect it to the offset.  To make this walk I need the specific combination of knots.  First, I add a vector math knot and set it to scale.  Then add a simple math knot and switch to multiply and duplicate this math knot here.  To tie it all together I need the position information from the mesh.  So I'll add a position knot and connect it to the vector math knot and the varanoi texture in the second set up.  Awesome, now we're building something truly dynamic.  In this first multiply knot I set it to negative 1 but in the second one I set it to 1.  Let's see how this walk and do I as a combination as a key.  The first knot pulls all points closer together creating high density in the center of the object.  Essentially I compress the particles to maximize density.  If you look at real clouds you'll notice there's density is higher near the center, while the edges are more transparent and barely.  Sometimes even letting lights find roses.  To achieve this I use these two knots.  The first one compress the particles as much as possible to build this dense core.  Then in the next knot I do the opposite, losing up the edge to reduce density here.  This gives us the perfect effect of transparency and lightness for the cloud.  Now if I disable the point position knot notice a difference.  This setup looks like more natural and we can easily control how five points spread out from the center of the object.  And it also depends on type of clouds you are going for.  For my scene I seen can you dance or clouds like the kind of some storm before the storm.  But that's not all.  I will add another set position knot placing in just before the final mesh to volume knot.  With this knot I want to add some tiny details like those with the fees or like clouds edges we can see here.  Something like that.  So I bring another nice texture and connect it to the self set.  Already you can see this effect shaping up on the mesh.  This noise takes you slightly breaks up as the surface of the mesh but that's exactly what we are going for.  To control this effect further I'll duplicate this skill knot.  Now check out how it's coming to go.  When I enable the mesh to volume knot check out the effect or the volume.  Now we've got a lot of details on the surface.  As always it depends on type of clouds you want to create but the beauty of this setup is that every part of this cloud is fully customizable.  For this artwork I use certain set if the clouds fairly compact not to scatter it out what you know.  Now that's where I've got this cloud piece how do we turn it to a large scale cloud for starting atmospheric clouding sky.


### Large Scale Clouds in Blender [12:09]
**Transcript:** It's super easy. Since we build these clouds using geometry knots I can simply go to edit more on this base sphere or base object and use shift did to duplicate it.  As you can see everything is set up in geometry knots applies automatically to the new geometry.  Pretty cool right?  This way we can create all sorts of shapes for our clouds.  First I disabled the geometry knots and just duplicate them the most object the within the larger one.  I duplicate the sphere as I sink it might look good shaping it into what feels like a big cloud.  After that I enable geometry knots again turn it to volume knot and boom that's it.  Looks fantastic doesn't it?  Finally we need to add a material to these clouds.  In geometry knots I only set material knot which let us assign a material to those clouds but first we need to create a material in the shade editor.  And since this volume will use volume shader here and connect it to volume output.  Set the color to pure white. Now we can apply this material using the set material knot.  Look at that it's coming together beautifully.  If you notice some rough quality like we see here at the edges of the clouds we can fix that.  In the last mesh volume knot we can increase or even decrease the work cell size.  For example set it to 0.1 to get much more sharper details on the edges.  And this more the values the more detailed it becomes.  So here is my complete geometry knots setup for creating clouds in blender.  Save this if you want to use it later.  Or you can grab this blender file including the clouds and all these knots on my pattern.  Plus for this scene I created a new pack of trees for blender and it's completely free on my pattern.  You may follow the link in the description and all the loads is blender tree pack absolutely for free.  But if you like the content and want to support my channel even further consider to pay the subscription on my pattern.  You'll unlock exclusive tutorials, master classes and all my assets.  Plus this blender scene is already live on my pattern where members always get older access before it goes public.  Check out the link and join the crew to keep creating awesome stuff.


### Create Cloudy Sky in Blender [15:05]
**Transcript:** Alright let's bring these clouds into the main scene.  I'll just copy this cloud object switch to the main scene and paste it here.  Nice!  Now we can move these clouds from the scene, scale them if needed.  And most importantly to make them for specific needs.  Just like we did in the clouds setup you can duplicate more of the lead spheres within the clouds geometry to get it look you want.  Then enable the volume knots and check out the adjusted clouds in the scene.  So I took the single cloud we created earlier and used it across the whole scene.  Duplicating it your time and making some tweaks.  As that's now I got these clouds.  Let's enable pre-render and now we can see how our light interact with the clouds.  Letting us not only create light rays but also beautifully highlight the sky and clouds so with this light.


### Light Linking Tricks [16:13]
**Transcript:** But here's the cool trick I used with the light.  I'm not going to use the same light we set up for the light rays to highlight those clouds.  Instead I go to Saturn's, head to Sadentop and open light linking.  I drag the entire clouds collection here and then check this check box.  Now the light will link to all these cloud objects but since we uncheck this box it will exclude the clouds lighting up every scene else in the scene except the sky.  This way I can use separate light sources, one just for light rays and another for clouds.  So next I'd spot light and place it behind the clouds to create sunlight effect coming through the clouds sky.  Now you can see this light illuminating the clouds.  This setup is way more flexible. Letting us control everything with two separate light sources for different purposes.  One dedicated for the clouds and another one just for light rays and highlight in the field in the scene.  So if I remove the light linking for example you can see it still highlights parts of the clouds.  But what I really want is the light coming through the clouds like the sun coming through the air onto the earth.  I could move this texture light and rotate it to cast some lights through the clouds but then I lose light on the ground.  All we could spend a ton of times trying to adjust light beams to boss heat the ground and light up the clouds the way we need.  For me it's way more flexible to use two light sources in the scene or different devices.  In the camera view it still looks like a single unified light source.


### Volume effects for realistic Sky [18:10]
**Transcript:** Finally I want to tweak the horizon. Right now it doesn't look great and I want our clouds and blend seamlessly with horizon and the forest in the background.  I'm creating a mind-sale Kevin Storm clouds formation rolling towards us.  So does this? I duplicate the volume cube, scale it up and move it out to the scene positioning behind the clouds.  Then scale it once more to cover the entire frame. Something like this here.  Next I duplicate the volume shader and start looking with it.  Increase the density and now it's starting to look really impressive.  To refine this and remove the top part of the volume so the effect will focus it only near the horizon I need a mask.  For example I will use a gradient texture where it weighs mapping and color and a classic combo I'd say.  Rotate the gradient by 90 degrees. Yeah negative 90 degrees and move it up.  Switch the color ramp to be splined to soften the mask.  Now use this color ramp as the density value in the volume shader.  And there we go. This effect now covers only the part of the horizon I want.  The lower section of this cloud and horizon.  Because the gradient texture exists a mask that I don't know if everything is a bowl as we can see.


### Volume Blender Optimization [19:50]
**Transcript:** So this is how you can create clouds and atmospheric sky right in blender.  Essentially there are three methods I use and before we wrap up a quick knot on optimization.  Since everything here is built with volumes and there are a lot of volumes in the scene now it's clear on this directly impacts performance.  Especially when for the final image you will want the smaller value of voxel size to get much sharper details.  And if you don't want to wait forever for the render finish you can do it with the global volume settings since the render settings here.  By default these settings are way too high for a final image but we can adjust them slightly.  I set max step to 500 well and increase step rate render from 1 to 3.  I also adjust the viewport settings to avoid overloaded the GPU while walking.  This way you can save some time or rather avoid wasting it because the quality doesn't suffer at all.  Just make sure to check test render to avoid any artifacts on the render.  You might need to find on the settings for your own scene.  So thank you for watching this video. Don't forget to subscribe to my channel, Instagram, X and Patreon to access my classes and sets.  And I'll catch you in the next one.



---

## Captured Frames

- [1:20] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_000.jpg
- [2:45] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_001.jpg
- [6:00] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_002.jpg
- [9:30] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_003.jpg
- [13:00] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_004.jpg
- [15:40] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_005.jpg
- [16:50] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_006.jpg
- [19:00] tutorials/frames/how-i-made-realistic-storm-clouds-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
Procedural storm clouds via a GeoNodes volume pipeline: Icosphere → Mesh to Volume → Distribute Points in Volume → Set Position (Noise + Voronoi for organic scatter and center-density compression) → Points to Volume → Volume to Mesh → final Set Position (Noise for wispy edges) → Mesh to Volume. Volume material = Volume Scatter (white). Light Linking (Blender 4.x) separates cloud lighting from scene lighting. Horizon haze: duplicate volume cube + Gradient Texture density mask.

### Summary
c g s l a v demonstrates three sky methods (2D image plane, HDRI, procedural volumetric) and focuses on the advanced procedural cloud pipeline. The GeoNodes cloud setup: start with Icosphere → Mesh to Volume (initial blob shape) → Distribute Points in Volume (create point cloud in the blob) → Set Position with Noise Texture offset (scatter points organically) + Voronoi compression trick (negative multiply pulls points to center for dense core, positive multiply loosens edges for translucent rim) → Points to Volume → Volume to Mesh → another Set Position (Noise Texture for fine surface wispy detail) → final Mesh to Volume. Volume material: Volume Scatter (white, optional absorption). Build larger clouds by duplicating spheres in Edit Mode before enabling GeoNodes. Light Linking: assign cloud objects to a dedicated light (Render Settings → Light Linking) so one spotlight illuminates only clouds (from behind, like sun-through-clouds) and another spotlight creates god rays in a separate volume cube. Horizon haze: second large volume cube + Gradient Texture (rotated 90°) as density mask → Volume Scatter focuses only at horizon level.

### Key Steps
1. **Quick methods (simple):** (a) Plane with sky image → Emission material; (b) HDRI in World shader. Both lack light interaction.
2. **God rays / light rays:** Cube with Volume Scatter material (density ~low) → place Spotlight inside cube → rotate to illuminate desired area in scene.
3. **GeoNodes cloud base:** Icosphere → Geometry Nodes → New. `Mesh to Volume` → `Distribute Points in Volume`. Values read off the graph [frame_003]: **Mesh to Volume** `Density` 1.000, `Voxel Size` **0.5 m**, `Interior Band Width` **0.2 m**; **Distribute Points in Volume** in **Random** mode, `Density` 5.000, `Seed` 0. The base object is an **Icosphere** at 7,992 verts / 7,950 faces [frame_003].
4. **Organic point scatter:** `Set Position` after Distribute Points: `Offset` = `Noise Texture` → Vector Math in **Scale** mode → Offset [frame_003]. Observed settings: Noise Texture **3D**, type **fBM**, `Normalize` **off**, `Scale` 3.000, `Detail` 3.000, `Roughness` 0.000, `Lacunarity` 2.000, `Distortion` 0.000; the Vector Math `Scale` field is **5.000**.
5. **Density gradient (center dense, edges wispy):** Voronoi / Position-based compression: Vector Math (multiply by −1) pushes points toward center → dense core. Second Set Position (multiply by +1) → loosens edges → translucent rim. Key for realistic cloud look. The **Voronoi Texture** in that branch is **3D**, **F1**, **Euclidean**, `Normalize` off, `Scale` **0.300**, `Detail` 0.000, `Roughness` 0.500, `Lacunarity` 2.000, `Randomness` 1.000 [frame_003].
6. **Back to volume:** Points to Volume → Volume to Mesh (for viewport preview/detail control).
7. **Wispy surface detail:** Set Position (before final Mesh to Volume) with another Noise Texture + Scale Vector Math → breaks up surface for organic edge detail.
8. **Final volume:** Mesh to Volume (final node) → Set Material node with Volume Scatter shader (white color).
9. **Scale properly:** Use "Amount to Size" in each Mesh to Volume node to prevent proportional distortion when scaling the object.
10. **Build large cloud:** Edit Mode → Shift+D to duplicate spheres → reshape → enable GeoNodes → automatic cloud formation.
11. **Bring into scene:** Copy cloud object to main scene; duplicate multiple times; position clouds at horizon.
12. **Light Linking:** Render Settings → Light Linking → drag cloud collection → uncheck box → assigned light only illuminates clouds. Create second Spotlight behind clouds (sun-through-clouds effect).
13. **Horizon haze:** Duplicate volume cube, scale large, extend to horizon → Volume Scatter material + Gradient Texture (rotated −90°) → Color Ramp (B-Spline) as Density → focuses haze only at horizon.
14. **Optimization:** Render Settings → Volume → Max Steps = 500; Step Rate Render = 3 (saves time without visual loss); Viewport step rate increase to avoid GPU overload.

### Nodes / Settings
- `Mesh to Volume` — converts mesh to volumetric field; "Amount to Size" prevents scale distortion. Observed: `Density` 1.000, `Voxel Size` 0.5 m, `Interior Band Width` 0.2 m [frame_003]
- `Distribute Points in Volume` — **Random** mode, `Density` 5.000, `Seed` 0 [frame_003]
- `Set Position` + `Noise Texture` (3D, fBM, Scale 3.0, Detail 3.0, Roughness 0.0, Lacunarity 2.0, Distortion 0.0) → Vector Math *Scale* 5.000 → `Offset`; center-push via Vector × −1 (compress), × +1 (expand edges) [frame_003]
- `Voronoi Texture` — 3D / F1 / Euclidean, Scale 0.300, Detail 0.000, Roughness 0.500, Lacunarity 2.000, Randomness 1.000 [frame_003]
- `Points to Volume` → `Volume to Mesh` — intermediate mesh for viewport preview and detail editing
- `Set Position` + `Noise Texture` (before final Mesh to Volume) — fine wispy surface variation
- Volume material: `Volume Scatter` (white, density ~0.3–1.0); adjust Anisotropy
- Light Linking (Render Settings): separates cloud light from scene light
- Horizon haze: `Gradient Texture` (rotated −90°) + `Color Ramp` (B-Spline) → Volume Scatter Density
- Render optimization: Max Steps = 500; Step Rate = 3; small voxel size for final render only

### Difficulty
Intermediate — requires GeoNodes volume pipeline understanding and Light Linking setup.

### Blender Version
Blender 4.x (Light Linking feature; GeoNodes volume nodes available in 3.x+)

### Tags
#volume #clouds #geometry-nodes #rendering #lighting #atmosphere #intermediate

---

## Frame verification (2026-09-01)

| | |
|---|---|
| **Corrected** | `blender_version` was `Blender 4.x` by inference. The status bar reads **4.3.1**, identically across **all eight** frames [frame_000 … frame_007]. |
| **Added** | every numeric setting in the cloud graph, none of which the transcript carried: Mesh to Volume (Density 1.0, Voxel Size 0.5 m, Interior Band Width 0.2 m), Distribute Points in Volume (Random, Density 5.0, Seed 0), Noise Texture (3D/fBM, 3.0/3.0/0.0/2.0/0.0), Vector Math Scale 5.000, Voronoi (3D/F1/Euclidean, 0.3/0.0/0.5/2.0/1.0) [frame_003]. |

📐 **Method note.** The wide node-editor shot is unreadable at 1280×720 as
captured — the node names resolve, the numeric fields do not. Cropping the node
cluster and rescaling 3× made every field legible, and cropping the status-bar
corner at 8× across all eight frames is what settled the version digit that a
single frame left ambiguous between 4.3.1 and 4.5.1. **A frame that looks
unreadable at full size is often readable in pieces** — worth trying before
recording a set as ungrounded.

---

## Related Tutorials
- `3d-smoke-blender-geometry-nodes.md` — advanced GeoNodes volume/fluid sim companion
- `how-to-create-a-cinematic-landscape-inside-blender-full-tutorial-with-project-fi.md` — cinematic landscape with sky atmosphere
- `tutorial-how-to-make-a-volumetric-projector-in-blender-45.md` — volumetric light effects companion
- `fundamentals-of-lighting-in-blender.md` — lighting theory for the light linking and placement decisions

---
title: Photoreal Metahumans In Blender
source: YouTube
url: https://www.youtube.com/watch?v=kaDtwG3JimM
author: Extra 3d
ingested: 2026-07-28
blender_version: "Not specified (UI shows modern tab layout with Geometry Nodes tab + Cycles GPU compute, consistent with Blender 4.x)"
tags: [materials, shaders, rigging, animation, cycles, organic, advanced]
extraction_status: complete
frames_dir: tutorials/frames/photoreal-metahumans-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Photoreal Metahumans In Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=kaDtwG3JimM)
**Author:** Extra 3d
**Duration:** 12m26s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Creating 3D humans from scratch has always been incredibly hard, but over time, we've
[0:04] got an easy methods like MetaHumans that lets you generate a character in minutes.
[0:09] But making those easy characters look truly photorealistic, that is where things get complicated.
[0:14] And let's be honest, just getting all of this imported into Blender without breaking
[0:17] everything is a massive pain.
[0:19] And this is where this video comes in, because we're going to cover everything, from setting
[0:23] up the software and plugins, to creating photorealistic human results, and importing
[0:29] everything into Blender, including the hair and grooms.
[0:32] So stick around until the end, because the final step is what brings the entire character
[0:36] to life.
[0:37] Let's start with the references, and before you skip this chapter, know that it's the


### References [0:38]
**Transcript (timestamped):**
[0:42] most crucial part of the entire process.
[0:44] It only takes a few minutes, and all you have to do is organize your references into categories,
[0:50] like skin color, face shape, groom, height and body.
[0:52] I recommend using PureF, which is a free tool that makes this really easy.
[1:00] The next step is to get a head base mesh, because human faces are incredibly complex.
[1:05] Even though MetaHuman gives you a good amount of control over facial features, it's still
[1:09] not enough to perfectly match a real person.
[1:12] So we basically need a head shape of a real human, which will act as a base shape for
[1:15] the MetaHuman.
[1:16] So, to get our character head model, there are two ways to do this.
[1:21] The first method is to physically scan someone with your phone.
[1:24] The only limitation is that you actually have to go outside and interact with a real human.
[1:28] And since we don't touch grass, I don't think that's happening.
[1:31] The absolute best option is to use today's sponsor, MeshieAI.
[1:36] They recently rolled out their Meshie6 update, and it creates incredibly accurate results.
[1:41] Just take your reference image of a person, and upload it to Meshie's image to 3DTool.
[1:46] Make sure it has a clean white background.
[1:48] If it has a bad background, just click this button, which will use Meshie's built-in
[1:51] background remover, which will make a clean background in seconds.
[1:55] Make sure you are using face shots like these, which shows both sides of the face, along
[1:59] with a neutral pose, to get the best results.
[2:02] Meshie gives you a ton of options to tweak the output.
[2:04] But if you want the best results for a head mesh, just copy my settings and go with the
[2:08] standard topology model type, and select Meshie6 model.
[2:13] There are also other options like auto-split and multi-view, which are best for 3D printing.
[2:18] But we are only focusing on the head model, so we are going to skip that.
[2:22] Once you are ready, just click the generate button, and the model will generate super
[2:26] fast.
[2:27] Once the mesh is generated, you can compare it with the original image, and it looks
[2:31] super accurate, and it doesn't stop at just the geometry.
[2:34] Meshie also generates highly detailed textures that map directly onto your model, so that
[2:38] you don't have to paint them manually.
[2:40] We are just going to skip the textures for now, and to download this mesh, just click
[2:44] the download button and make sure the GLB format is selected.
[2:49] And once it's downloaded, drag the file straight into Blender, and it will bring up an import
[2:53] pop-up.
[2:54] Just click the import button, and it will import the head mesh.
[2:58] Now we have a fantastic base mesh ready to go, and now all we have to do is prepare it
[3:02] for MetaHuman.
[3:03] Over 10 million creators are already using Meshie to speed up their 3D production.
[3:08] But now, new users can get more than 50% off their subscription.
[3:12] Hit the link in the description to try Meshie today.
[3:15] Now let's get back to the workflow and prepare this mesh for MetaHuman.


### Head Base Generation [3:16]
**Transcript (timestamped):**
[3:19] So since we gave out a clear reference image, the output is already perfect, but if you
[3:24] see any extra stuff, you can just remove it in the edit mode.
[3:28] Make sure your model is not parented to anything, just press ALT P and clear parent without
[3:32] transformations.
[3:33] Now the main thing you have to do is go to Mesh.
[3:37] Make sure you are in the edit mode and everything is selected.
[3:41] Go to Mesh, Merge, and select Merge by Distance.
[3:44] Now that we are done with the mesh, just export it as FBX, and make sure to check this option,
[3:50] which will only export the selected object in the viewport.
[3:55] Now let's set up Unreal Engine.


### UE5 Setup [3:56]
**Transcript (timestamped):**
[3:57] So first off, you will need Epic Games Launcher.
[4:01] Download it from the official website, the link is in description.
[4:04] Once downloaded, install it.
[4:06] While it's installing, create a free account on Epic Games.
[4:10] It's just a simple process.
[4:12] Once Epic Launcher is installed, sign in and go to the Unreal tab.
[4:17] You can go with the latest version, but I have 5.6 already installed, so I am going to go
[4:21] with that version.
[4:22] Just make sure MetaHuman Core Data is selected in the options.
[4:26] You can check this even after the engine is installed.
[4:30] Once Unreal is installed, open it and create a new blank project.
[4:34] Name it whatever you want, and you can just create how many humans you want in this one
[4:37] file.
[4:38] So just name it something simple.
[4:40] Also note the location where you are saving.
[4:43] This will come in handy.
[4:46] Now I know the new UI and everything looks a little confusing, but we won't be doing
[4:50] anything complex in this area at all.
[4:52] Our work is mainly in the MetaHuman Editor, which works like a game character designer,
[4:56] so no worries at all.
[4:59] First go down here and open the Content Browser.
[5:01] This is your space where you can make folders and create components.
[5:05] To keep things simple and organized, create 4 folders, name 1 Imports, Identities, Characters
[5:11] and Exports.
[5:12] First drag the FBX into the Imports folder.
[5:17] Also go into the Plugins and search for MetaHuman.
[5:20] Enable every plugin you see.
[5:23] And once you do that, it will ask you to restart.
[5:25] Just click the Restart button and it will do that for you.
[5:29] This is something you only have to do once, and we can now start with the main process
[5:33] now.
[5:34] Before we do that, just change this mode to Wireframe to improve some performance.


### Facial Features Track [5:39]
**Transcript (timestamped):**
[5:41] Now go into the Identity folder and right click and search for MetaHuman.
[5:45] This will give you a bunch of options.
[5:47] Select the MetaHuman Identity.
[5:49] Name it similarly to what you named the import.
[5:52] Now double click it and it will open a new tab.
[5:55] So first off, select the component and choose the head model that you imported.
[5:59] After that go over here and change the field of view to 20.
[6:06] Press E and it will activate the rotation gizmo.
[6:09] Rotate the model so that it's facing the camera.
[6:11] You can use the arrow keys to move a little back so the whole head is in the frame.
[6:15] Now you just have to go through these options, so the first one will lock the frame.
[6:19] And after that you can start tracking the facial details.
[6:22] Once you're happy with that, generate the MetaHuman head mesh and compare it.
[6:26] To finish this process, just click this button to generate the rig and you can close the
[6:30] Identity tab.
[6:32] Make sure to save your project to keep everything secure.


### Metahuman creation [6:37]
**Transcript (timestamped):**
[6:39] Now go into the Character tab and right click and again search for MetaHuman and create
[6:43] a MetaHuman character.
[6:45] Name it and double click it.
[6:47] This will open the MetaHuman editor.
[6:49] Now you get this default mesh which looks horrible for some reason.
[6:53] And we're not going to use that, so the first best thing to do for the best output is to
[6:56] select a preset that is close to your reference.
[6:59] And for this video, I'm going to choose this one.
[7:02] This is because it has some similarities in the groom and body proportion.
[7:05] This gives us a big advantage and saves a lot of time.
[7:09] Once you select the preset, it will basically just come up.
[7:12] You can also disable the groom for now and you can start with the skin and the head shape.
[7:17] Now let's select the conform button and select the mesh that we tracked earlier from the
[7:20] Identity.
[7:22] Uncheck both of these and just proceed.
[7:25] This will transform the head shape.
[7:26] And now let's start the skin.
[7:28] So just follow your references and just copy the color.
[7:31] Once you are done with that, you can play with this slider which gives you about 150
[7:35] plus face textures.
[7:37] And once you're happy with the results, you can move on to the groom section.
[7:40] This part is so easy, just add whatever style you want that is close to your references
[7:45] and you are pretty much done.
[7:47] In the end, go into the body section and click the model button.
[7:50] This will give you a lot of options.
[7:52] Just play with these and try to get the shape like the reference and that's it.
[7:56] Once you are done with this, we are ready to export it.


### Export the character [8:01]
**Transcript (timestamped):**
[8:04] Now that we are done with the character creation, you can just click this button to create the
[8:08] character rig.
[8:09] And you can also download the textures.
[8:11] I'm going to go with 4K for this one.
[8:13] I'm just doing this because I'm also recording.
[8:15] And it's very hard to do both of these at the same time.
[8:19] Once the character is rigged and the textures are downloaded, go into the assemble tab.
[8:23] So first off, export this at the normal settings, which is set to cinematic.
[8:28] Just click assemble.
[8:29] And once it's assembled, you have to export it again with DCC format.
[8:33] You can save it in a different location.
[8:35] Just remember the file paths.
[8:37] Once you do this, we are basically done exporting the character.
[8:40] Let's just export the groom system.
[8:43] So first off, go into the content browser and go where you have exported the cinematic
[8:47] option.
[8:48] Once you go there, just go into this directory and you will find the grooms.
[8:52] Search for LOD0 and you will find all of the grooms that you have used.
[8:56] To export it, you just have to right click the groom and search for export.
[9:00] You will get the export option.
[9:02] Just click that and it will ask you for a location.
[9:05] Just select any location, keep it organized, select the name and export it.
[9:10] Do the same for the rest of the objects.
[9:12] Now for the textures, go into this directory and export this texture only for each group.
[9:17] You can do this in the same manner.
[9:19] Just store it as PNGs.
[9:21] Once you do this, we are basically done with exporting from Unreal Engine.
[9:25] So now that we are done exporting it from Unreal Engine, let's first set up Blender


### Blender Addon Setup [9:28]
**Transcript (timestamped):**
[9:29] for importing Unreal Engine MetaHumans.
[9:32] This is a one-time process, so I'm just keeping this as a separate chapter.
[9:36] Go to Polyhammer's website.
[9:37] You can find the link in the description and register your portal account.
[9:41] This is actually free.
[9:43] It has some paid features, but the core version is free.
[9:46] I am also using the free version as well.
[9:48] Open the products tab.
[9:52] This will ask you to create a token.
[9:54] I have linked a guide on how to install this, but basically you have to copy the token and
[9:59] you have to go into preferences, go into the extensions tab and click this repositories
[10:03] tab in the top.
[10:05] Click the plus icon and add a remote repository.
[10:08] Paste the token here.
[10:11] For the URL, just close this tab and it will give you this link that you can paste here
[10:16] and that's it.
[10:17] This will install the extension and once that's enabled, you are basically done.
[10:21] Now that everything is set up, just go into where you exported the DCC format of the MetaHuman.


### Import the character [10:22]
**Transcript (timestamped):**
[10:28] You'll find a DNA file there.
[10:29] Just drag it into Blender and it will open this panel.
[10:32] Just import it and you will have the character, but the grooms will be missing.
[10:37] To add the grooms, go to where you exported the FBX files.
[10:41] Drag those and import all of those that you exported.
[10:46] So first off, let's texture the grooms.
[10:48] Select any groom, go into the shader editor, create a new material for that groom and first
[10:52] drag the image texture that we exported.
[10:55] This image texture has three channels, red, green and blue.
[10:59] So add a separate color node and extract it like this.
[11:02] Just follow me and copy this shader setup.
[11:14] Also go into the light path tab and increase the transparent value to 64.
[11:20] Once you are done with this, you can change the color of the shader and you can just copy
[11:24] this shader for all of the grooms, just change the image texture for each.
[11:28] Once you are done setting up the groom, you also have to bind it to the character.
[11:32] Select the groom, go into the modifiers tab.
[11:35] Add a surface to form modifier, select the face mesh and click the bind button, which
[11:40] will basically bind the groom to the face.
[11:42] Do this for all of the grooms and this is it.
[11:44] This is basically a very simple method.
[11:47] The most difficult part was just setting it up and because that was just a one time thing,
[11:51] now you can easily create more characters and just import them.
[11:56] You can also add these facial features from here or import any animations.
[12:00] For you guys, I have linked some Polyhammer tutorials which cover animation and MoCap
[12:05] for these characters.
[12:06] So yeah, you can check that out for more information.
[12:09] Thanks for watching.
[12:10] See you in the next one.



---

## Captured Frames

- [1:45] tutorials/frames/photoreal-metahumans-in-blender/frame_000.jpg
- [2:30] tutorials/frames/photoreal-metahumans-in-blender/frame_001.jpg
- [5:55] tutorials/frames/photoreal-metahumans-in-blender/frame_002.jpg
- [6:55] tutorials/frames/photoreal-metahumans-in-blender/frame_003.jpg
- [7:20] tutorials/frames/photoreal-metahumans-in-blender/frame_004.jpg
- [8:25] tutorials/frames/photoreal-metahumans-in-blender/frame_005.jpg
- [10:35] tutorials/frames/photoreal-metahumans-in-blender/frame_006.jpg
- [11:05] tutorials/frames/photoreal-metahumans-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
A cross-application photoreal-human pipeline: generate a likeness-matched head base mesh from a single photo (Meshy AI), drive Unreal Engine 5's MetaHuman Identity/Character tools with that mesh to build a rigged, textured, groomed character, then export the DNA rig + grooms and reassemble the full character (with working hair/beard shaders) inside Blender via the free Polyhammer add-on.

### Summary
The video walks through creating a photorealistic MetaHuman entirely from one reference photo. A single front-facing image is turned into a textured 3D head mesh in Meshy AI, cleaned up and re-exported from Blender as FBX, then used inside Unreal Engine's MetaHuman Identity tool to facial-track and conform a MetaHuman preset to match the real person's head shape, skin, and groom. The finished character (rig, 4K textures, grooms) is exported in DCC format and DNA/groom files, then reassembled in Blender using the Polyhammer add-on: the DNA file brings in the rigged head/body, groom FBX files are imported separately, and a shared node-based hair shader (Image Texture -> Separate Color -> Principled BSDF, high transparent bounces) is built and bound to the face with a Surface Deform modifier.

### Key Steps
1. **Reference gathering:** Collect and categorize references (skin color, face shape, groom, height, body) in PureRef — treated as the most important step.
2. **Head base mesh (Meshy AI):** Upload a clean, neutral-pose, front-facing reference photo to Meshy's Image-to-3D tool; use Standard topology + Meshy 6 model + A-Pose; generate, compare against the reference, and download as GLB (frame_000, frame_001 — result: 232,748 tris / 116,357 verts clay mesh).
3. **Prep in Blender:** Import the GLB, `Alt+P` > Clear Parent (Keep Transform off), Edit Mode > select all > `Mesh > Merge > By Distance`, then export as FBX with "Selected Objects Only" checked.
4. **UE5 project setup:** Install Epic Games Launcher + Unreal Engine (5.6 used), enable the MetaHuman Core Data option during install, create a blank project, enable all MetaHuman plugins in Plugins browser (restart required), and organize the Content Browser into Imports / Identities / Characters / Exports folders.
5. **MetaHuman Identity (facial tracking):** Create a MetaHuman Identity asset, assign the imported head FBX as its component, set camera Field of View to 20, rotate the model to face camera (`E` for rotation gizmo), lock the frame, run facial tracking, generate the MetaHuman head mesh, then generate the rig (frame_002 shows the Identity editor's footage/tracking view).
6. **MetaHuman Character build:** Create a MetaHuman Character asset, pick a preset close to the reference for groom/body proportions (frame_003 shows the default/unconformed body in the Blend sub-tab), then in the Head tab use `Conform > From Identity` to transform the head shape to the tracked mesh (frame_004), match skin tone/texture (150+ face texture variants available), add a groom preset matching the reference, and sculpt the body via the Model sliders.
7. **Rig + export from UE:** Generate the full rig, download textures at 4K, go to the Assembly tab and export once at Cinematic settings, then re-export in DCC format (frame_005 shows the rigged, textured result with beard groom).
8. **Groom export:** In the Cinematic export folder, locate LOD0 groom assets, right-click each groom > Export, and export the corresponding groom textures as PNG.
9. **Blender add-on setup (one-time):** Create a free Polyhammer account, generate an API token, and add it as a remote repository under Preferences > Add-ons/Extensions > Repositories to install the Polyhammer MetaHuman importer.
10. **Reassembly in Blender:** Drag the exported DNA file into Blender and import it (brings in the rigged head/body but no hair, frame_006). Import the exported groom FBX files separately. For each groom, build a shader in the Shader Editor: Image Texture -> Separate Color node (RGB channels split) -> Principled BSDF, and raise Render Properties > Light Paths > Transparent > Max Bounces to 64 for correct hair-card transparency (frame_007). Bind each groom to the face with a Surface Deform modifier (select target face mesh, click Bind).

### Nodes / Settings
- **Meshy AI:** Image-to-3D, Model Type = Standard, AI Model = Meshy 6, Pose = A-Pose, Image Enhancement on.
- **Blender mesh cleanup:** `Mesh > Merge > By Distance`; FBX export with "Selected Objects" only.
- **UE5 MetaHuman Identity:** Field of View = 20; rotation gizmo (`E`) to align footage; frame lock before tracking.
- **UE5 MetaHuman Character:** Conform panel > "From Identity" (Import DNA Options, both checkboxes unchecked per the video); Skin section slider (150+ face textures); Body > Model sliders; Assembly export = Cinematic, then DCC format.
- **Blender groom shader (Shader Editor):** Image Texture node -> Separate Color node (splits R/G/B groom texture channels) -> Base Color input of Principled BSDF.
- **Render Properties > Light Paths > Transparent > Max Bounces = 64** (needed for hair-card groom transparency to render correctly).
- **Groom binding:** Surface Deform modifier on each groom object, Target = face mesh, then click Bind.

### Difficulty
Advanced — not a single-app Blender technique, but a full pipeline across Meshy AI, Unreal Engine 5 (MetaHuman Identity + Character + plugins), the third-party Polyhammer add-on, and Blender shading/modifiers. Individual steps are approachable but the setup (UE5 + plugins + Polyhammer token) is a real barrier and is explicitly called out as "the most difficult part" in the video.

### Blender Version
Not stated explicitly in the transcript. The captured Blender viewport (frame_006/frame_007) shows the modern tab layout (Layout/Modeling/Sculpting/UV Editing/Texture Paint/Shading/Animation/Rendering/Compositing/Geometry Nodes/Scripting) with Cycles + GPU Compute — consistent with Blender 4.x.

### Tags
#materials #shaders #rigging #animation #cycles #organic #advanced

---

## Related Tutorials
- **MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior | Inside Unreal** (`tutorials/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea.md`) — shares the exact MetaHuman DNA / Unreal Engine -> Blender rigging pipeline (tags: metahuman, dna, rigging, unreal-engine); that video covers customizing the DNA-driven facial rig behavior after import, a natural next step once this video's character is in Blender.
- No other library entries currently share 2+ of this tutorial's approved tags (materials/shaders/rigging/animation/cycles/organic/advanced) in combination with the MetaHuman/UE5 subject matter — this is the first full photo-to-MetaHuman pipeline entry in the library.

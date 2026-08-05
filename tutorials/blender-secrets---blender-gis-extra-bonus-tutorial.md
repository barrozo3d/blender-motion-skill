---
title: Blender Secrets - Blender GIS (Extra Bonus Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=IcL7N335oCk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (BlenderGIS + Gaffer add-on workflow, 2.8x-4.x)"
tags: [procedural, materials, lighting, hdri, rendering, cycles, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Blender GIS (Extra Bonus Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=IcL7N335oCk)
**Author:** Blender Secrets
**Duration:** 6m54s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, it's Jan and I wanted to go a little bit further in depth on Blender GIS, which
[0:08] is something that I made a short one minute video about a few days, weeks ago.
[0:13] And there seemed to be some confusion about whether I'd made the opening render of the
[0:24] Matterhorn Mountain with Blender GIS.
[0:27] And yes, I definitely did.
[0:30] I just probably went a little bit too fast in the video, so I'll show you now step by
[0:34] step how to make such a nice render.


### CGBoost Course [0:37]
**Transcript (timestamped):**
[0:37] And if you're interested in this kind of stuff and you want to know more in depth with a
[0:42] real video course, how to make environments in Blender, I couldn't recommend anything
[0:48] that's better than the course Martin Kleckner made over on CGBoost.
[0:52] He really spent months figuring out every single variable button you can press in Blender
[0:59] just to make the most awesome nature render.
[1:01] So I would definitely check it out.
[1:03] You can find the link in the description.


### Blender Tutorial [1:05]
**Transcript (timestamped):**
[1:07] Alrighty, so here we are in Blender and I've already put a screenshot from Google Maps
[1:12] of the Matterhorn exact location because otherwise I would never find it.
[1:16] And here we're going to the GIS menu to load the base map, which basically just loads the
[1:21] whole earth and then you can zoom in to where you want.
[1:26] So obviously the Matterhorn is in the blurry place of Europe.
[1:31] In fact, it's in Switzerland.
[1:34] I can already see it.
[1:35] It's right there.
[1:40] It looks like we are targeting you Switzerland for destruction or something from space.
[1:46] There it is.
[1:51] Now you can lock by pressing L you can lock the region that you've selected like this
[1:56] region.
[1:57] I don't want to zoom in anymore, but I do want to increase the resolution.
[2:00] So I press L to lock and then I scroll up on the mouse wheel and it will still increase
[2:05] the resolution.
[2:07] But it takes a long time.
[2:08] I've sped it up here.
[2:09] It takes forever to download.
[2:10] It can take like 20 minutes or something.
[2:14] And then you get this shiny plane and you can download the height map as well, which
[2:20] also takes a minute or five or 10.
[2:23] And you get this shiny blob of relief.
[2:27] I really recommend you embed the texture in the file and save it because otherwise if
[2:32] it crashes you lose the resolution of the terrain.
[2:36] You lose the height map, I mean.
[2:39] Here to get the most out of it, I subdefide it in edit mode.
[2:44] You really have to do that.
[2:45] Otherwise you don't have enough detail.
[2:52] Reduce the specularity and increase the roughness of that map.
[2:55] Otherwise it will look strangely shiny and I can tell you from experience that Switzerland
[3:02] is not shiny like that.
[3:05] So here I'm adding a HDRI with Gaffer add-on, which is probably the best add-on I've ever
[3:11] bought.
[3:13] And the blender is already unhappy because it's so many subdivisions.
[3:18] So I've turned on simple file.
[3:22] And I'm adding a camera, but the camera doesn't see anything because it's all too big.
[3:26] So I have to add, I have to increase the clipping and otherwise it's a massive, massive mesh
[3:36] basically.
[3:39] So I've locked the camera to view so I can move around and find a nice shot here.
[3:44] Later I will increase the height of these mountains a bit in the modifier, the displacement
[3:52] modifier because it's a bit too boring now.
[3:56] So now I'm just trying to search which one is the Matterhorn again and finding a nice
[4:03] angle with the camera.
[4:10] And changing the length of the lens a bit to make it a bit more dramatic.
[4:14] 30mm is a good camera lens length for this kind of stuff.
[4:24] So I just added an empty, although you can see it because the overlays were turned off.
[4:30] The empty will be the target for the depth of field of the camera, which is always nice,
[4:36] but in this case the mesh is just so gigantic that you can't really see the depth of field.
[4:43] So I was trying to scale it down and see if I could get a bit more blurry in this.
[4:50] And experimenting a bit more with the HDRIs.
[4:53] They're mostly from HDRI Haven, but you can just automatically download them all with


### Bonus [4:55]
**Transcript (timestamped):**
[4:58] the Gaffer add-on.
[4:59] It's really awesome.
[5:01] And this is my book.
[5:02] I was just...
[5:03] Sometimes I read my own book.
[5:05] I was just checking which picture that I used for the background.
[5:10] It's this one from textures.com.
[5:17] I downloaded it as an image on-plane with the images as planes add-on.
[5:24] I wanted to emit, of course, and just kind of line it up with the camera.
[5:29] If I were really smart, which unfortunately I'm not, I would have parented it to the camera.
[5:35] But I didn't, so later I have to move it again when I move the camera.
[5:42] Here I'm rotating this HDRI a bit and setting up some kind of camera move.
[5:50] You can actually scale keyframes in the timeline, which can be very handy.
[5:57] But Blender get crashing when I try to render it.
[5:59] So here is a quick tip.
[6:02] You can increase the scale of your camera.
[6:05] That way you can get kind of the camera fulcrum or the area which is inside the camera view.
[6:10] And then just select everything else and just delete it.
[6:22] That way you massively reduce the amount of memory you have to use and then you can actually
[6:27] render it.
[6:28] So here you go.
[6:30] This is the render shot.
[6:31] I added a little bit of rotation to the camera movement.
[6:38] So yeah, good luck with the Blender GIS.
[6:40] It was a lot of fun.
[6:41] You need some patience, but it's worth it.



---

## Captured Frames

- [1:20] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_000.jpg
- [1:45] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_001.jpg
- [2:25] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_002.jpg
- [2:54] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_003.jpg
- [3:20] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_004.jpg
- [4:15] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_005.jpg
- [5:20] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_006.jpg
- [6:30] tutorials/frames/blender-secrets---blender-gis-extra-bonus-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Real-world terrain generation using the BlenderGIS add-on: import a real satellite basemap and height-map displacement for an actual mountain location (the Matterhorn), then dress it into a cinematic HDRI-lit render with camera framing, depth of field, and a memory-optimization trick for rendering a massive real-world-scale mesh.

### Summary
A screen-recorded walkthrough (looser, narrated "here's how I actually did it" style) recreating the author's Matterhorn render. Frame 000 shows the GIS add-on's basemap-loading dialog next to a live-updating satellite preview panel. Frame 001 shows zooming into the correct real-world location (Swiss Alps/Matterhorn area) within that satellite basemap viewer. Frame 002 shows the payoff of the locked, high-resolution basemap + downloaded height map: a 3D textured terrain plane matching the satellite image exactly, viewed side-by-side with the source imagery. Frame 003 shows the material fix in progress — a Shader Editor node graph (Base Color/Specular/Roughness sockets visible) being adjusted per the transcript's "reduce specularity, increase roughness" tip so the terrain doesn't read as shiny plastic. Frame 004 shows the object's right-click context menu open over the terrain (Shade Smooth/Subdivide-adjacent options), consistent with the "subdivide in Edit Mode for enough detail" step. Frame 005 shows Camera Perspective view with the camera's view-frustum bounds drawn directly over the mountain terrain, framing a dramatic angle before rendering. Frame 006 shows an Image-as-Planes background texture (dawn/dusk sky photo) lined up behind the terrain from the camera's point of view, with the World/Background node visible in the properties panel. Frame 007 shows the finished cinematic render: golden-hour lit jagged peaks with volumetric-looking atmosphere and shallow depth of field in the foreground.

### Key Steps
1. **Import real-world terrain via BlenderGIS:** open the GIS menu → load the basemap (loads the whole Earth as a live satellite viewer); zoom/pan to the target real-world location; press L to lock the selected region once framed correctly, then scroll the mouse wheel to increase resolution without changing the region (this download can take up to ~20 minutes at high resolution).
2. Download the height map for that same locked region (a few to ten minutes) — this produces a textured, displaced terrain plane matching the real landscape.
3. **Preserve the download:** embed the downloaded texture in the .blend file and save immediately — if Blender crashes, an un-embedded high-res height map/texture download is lost.
4. **Add detail:** Subdivide the terrain plane in Edit Mode — the raw GIS mesh doesn't have enough resolution/detail on its own for a close-up cinematic render.
5. **Fix the material:** reduce Specular and increase Roughness on the terrain's Principled BSDF — the default GIS-imported material reads unrealistically shiny/plastic-like otherwise.
6. **HDRI lighting:** add an HDRI environment via the Gaffer add-on (fast HDRI browsing/downloading, sourced mostly from HDRI Haven / Poly Haven) for realistic outdoor lighting.
7. **Handle the huge mesh:** enable Simple/Wireframe-style display for the terrain object in the viewport so Blender stays responsive with that many subdivisions; increase the Camera's Clip End distance since a real-world-scale mesh this large otherwise falls outside the default clipping range; Lock Camera to View to freely fly around and find a composition.
8. **Cinematic camera setup:** pick a ~30mm focal length for a dramatic wide-angle look; add an Empty as the camera's Depth of Field focus target (note: at this real-world scale the DOF effect may barely read — try scaling the Empty/adjusting focus distance to get visible blur); increase mountain height via the Displace modifier's strength if the default relief looks too flat/boring.
9. **Background sky:** import a sky/dusk photo via Images as Planes, line it up behind the terrain from the camera's POV (the author notes he should have parented this plane to the camera to avoid re-aligning it after every camera move, but didn't).
10. **Animate:** rotate the HDRI and set up a simple camera move; keyframes can be scaled directly in the Timeline for quick timing adjustments.
11. **Render-crash fix for massive meshes:** if Blender crashes on render due to the huge real-world-scale terrain, scale up the Camera object itself so its view frustum ("camera fulcrum") encompasses more of the scene at a coarser transform scale, select everything outside that frustum and delete it — this drastically cuts memory usage and makes the render actually completable.

### Nodes / Settings
- **Add-on:** BlenderGIS (basemap loading/locking/resolution, height-map download), Gaffer (HDRI browsing/auto-download), Images as Planes (background sky photo).
- **Shading:** Principled BSDF (lowered Specular, raised Roughness for realistic terrain material).
- **Modifiers:** Displace (mountain height/relief strength).
- **Camera:** Clip End (increased for real-world-scale meshes), 30mm focal length, Depth of Field target Empty, Lock Camera to View.
- **Viewport:** Simple/Wireframe display mode for large meshes to keep the viewport responsive.
- **Workflow trick:** scale up camera + delete geometry outside its frustum to reduce render memory footprint on massive real-world-scale scenes.

### Difficulty
Advanced

### Blender Version
Not specified — BlenderGIS + Gaffer add-on workflow, consistent with modern Blender 2.8x-4.x.

### Tags
procedural, materials, lighting, hdri, rendering, cycles, advanced

---

## Related Tutorials
- [Blender Secrets - 4 tips for Cinematic Lighting](blender-secrets---4-tips-for-cinematic-lighting.md) — shares lighting, hdri, materials, cycles; same channel, same Gaffer add-on referenced in both.
- [Blender Secrets - 4 tips for Photoreal Lighting](blender-secrets---4-tips-for-photoreal-lighting.md) — shares lighting, hdri, cycles, materials, rendering; same channel, directly complementary (HDRI/photoreal outdoor lighting fundamentals applied here to a real terrain).

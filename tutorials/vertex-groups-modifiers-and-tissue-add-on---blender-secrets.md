---
title: Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=75inBBl39es
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.3.2 (explicitly named — Tissue add-on confirmed still working the same way)"
tags: [organic, procedural, abstract, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=75inBBl39es)
**Author:** Blender Secrets
**Duration:** 7m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So I was going through my book randomly just hunting for outdated topics and updating them.
[0:06] And I found this tissue topic about the tissue add-on, which is pretty interesting and I hadn't used this add-on for years.
[0:14] So I figured I would make a updated version of it.
[0:17] And although the add-on still works pretty much the same in Blender 4.3.2, I thought it would be interesting to do a new video about it.
[0:26] And to make it a bit more interesting this time, instead of a sphere, I used these human-based meshes from the Blender Studio.
[0:33] And you can download this from the Blender demo scenes page.
[0:37] To download it, just click on this.
[0:38] And while we're downloading, we come to this page, which urges us to donate to Blender.
[0:43] It's pretty shocking that less than 0.1% of users donate to Blender.
[0:49] So definitely something to consider, even if you just pay one time.
[0:52] Once you extract the download, then you get this blend file, which contains all the assets.
[0:57] And as you can see, there are already marked as assets.
[1:01] So you don't actually need to do anything in this file.
[1:04] You don't even need to open it really.
[1:05] And all you need to do is save it in a location where you can just keep it there.
[1:12] So don't keep it on your desktop.
[1:13] Don't keep it in your downloads folder.
[1:15] Keep it in like a 3D assets folder on a hard drive somewhere.
[1:19] And then in preferences, you can set the file path.
[1:22] So under file paths, you just add wherever you keep it, and it will just add it to your asset browser from then on.
[1:30] So once you have an asset browser open, then you can just find it here.
[1:34] So you can find it in the drop down human-based meshes bundle.
[1:37] And then you can just drag and drop these assets.
[1:40] And one more thing about that, I think by default, this is set to append.
[1:45] But if not, then just choose append here and to use these assets super easy, you just drag and drop them.
[1:52] But I would recommend because now this is something that you cannot edit before you click anywhere, open this at collection panel and uncheck instance.
[2:00] Because otherwise it's just an instance and you won't be able to do anything with it.
[2:04] So let me just select this and then Alt and G to set its location.
[2:08] And then I can just close this as a browser like this.
[2:11] And then to install the tissue add-on, you go to get extensions and you just type tissue and then you just click on install.
[2:20] And after that, it will also be in the add-ons.
[2:22] And then you can find it here in the option panel, the tissue tab.
[2:27] I'm just going to add two levels of subdivision with control two.
[2:30] And then I'm just going to apply it with control A and visual geometry to mesh.
[2:35] So now we have a lot more geometry to work with, which will be interesting with the tissue add-on.
[2:40] And I'm just going to check that the scale is applied.
[2:42] And it looks like the scale is a bit different than one.
[2:45] So I'm just going to apply the scale as well.
[2:47] So I'll control A and choose scale and just click on apply.
[2:52] And let's turn on shade smooth and let's use a matte cap.
[2:56] It's a bit more interesting to look at.
[2:58] And then let's go to weight paint mode because we need to have a vertex group on this one.
[3:03] So now when I start to draw with the weight paint tool, you see that it turns red.
[3:09] And red means that the vertices here, so if I go to edit mode, you can see these vertices,
[3:15] these now have a value of one or a weight of one.
[3:19] And if I select them, then I select not just the ones that have a value of one,
[3:23] but just everything that has a value above zero in this vertex group.
[3:28] So the best way to visualize those values is with this weight paint visualization,
[3:33] which has red as one, blue as zero and green and yellow and cyan and so on as everything in between.
[3:40] To weight paint, just left click with the mouse and paint or to erase,
[3:45] you just hold control and you paint with the mouse as well.
[3:48] So that just turns it into zero value.
[3:51] And it would be nice if we can mirror this symmetrically automatically.
[3:56] So in the brush panel, go to symmetry and just click on the X here.
[4:02] And then as you can see, it will mirror that to the other side on the X axis or whatever axis that you need.
[4:09] And for some reason, I have had the experience that I had to uncheck the mirror vertex group option before it worked.
[4:16] And indeed, if I turn it off, it still mirrors the vertex group.
[4:19] So I'm not sure what that option is for.
[4:21] But anyway, it works.
[4:23] And so yeah, let's draw a strange vertex group.
[4:26] Okay, so I've unleashed my creativity on this vertex group.
[4:30] And by the way, if you want, you can also soften the border.
[4:33] So if you hold shift, just like with painting and with sculpting,
[4:38] then you kind of soften the edges.
[4:40] You kind of smooth it out.
[4:42] All right.
[4:42] So that's our vertex group painted.
[4:45] So now what we can do with this, let me just go back to object mode.
[4:49] We can add a decimate modifier to this.
[4:52] And to see better what we're doing, I will enable in the viewport overlay is the wireframe option.
[4:57] So even in object mode now, we can see the wireframe.
[5:00] And yeah, I'm just going to lower this ratio.
[5:02] And of course, now is just doing a sort of general reduction of the geometry.
[5:08] However, if I use that vertex group that we painted, so here in the vertex group,
[5:13] it's just named group by default.
[5:15] And so now it's using the vertex group that we painted as the input for where to decimate.
[5:20] And this is somewhere interesting modern art.
[5:22] Maybe somebody would like to really print this, but I think I will increase the ratio a little bit,
[5:27] maybe to something like 0.4.
[5:30] That looks pretty interesting already.
[5:32] And you can also increase and decrease the ratio of the influence.
[5:37] And so yeah, it gives us something like this.
[5:38] You can also invert the vertex group by clicking on this button here.
[5:42] So that's also something that you can experiment with.
[5:45] Maybe that's more interesting in this case.
[5:46] Let me get something like this.
[5:48] If you're happy with your result of the decimate modifier, you can apply it.
[5:52] Just click on apply here.
[5:53] And so now this is what the geometry actually looks like.
[5:56] And so now let's finally use the tissue add on to in the tissue panel here in the option panel.
[6:01] I just click on convert to jewel mesh and make sure you have the object selected.
[6:06] So click on convert to jewel mesh and it takes a couple of seconds to do some calculations.
[6:12] And then what you get is this.
[6:15] So very interesting kind of honeycomb structure.
[6:18] And yeah, to make this even more interesting, we can now add a wireframe modifier.
[6:22] And I think we need to reduce the thickness quite significantly here.
[6:26] So just reduce the thickness value.
[6:29] And in fact, you can also uncheck the option replace original.
[6:32] And that just puts the wireframe as another model on top of the original.
[6:37] So then you get something like this.
[6:38] And let me just turn off the wireframe and maybe use a more interesting madcap.
[6:44] So then you get something like this, which is some kind of weird futuristic mask, I guess.
[6:49] And yeah, you can play a bit more with the thickness.
[6:52] We still have that vertex group.
[6:54] So in fact, we could also use that here to control the thickness of these lines.
[6:59] So then you get something like this, which is also pretty cool.
[7:02] And we can also invert that vertex group again to get something like this.
[7:06] We still have this factor values.
[7:08] If you think that these lines, for example, are too thin, then you can reduce what the
[7:12] vertex group is doing by increasing this vector value like this.
[7:15] So that's just one option of the tissue add on.
[7:18] And yeah, you can see how powerful it can be to use vertex groups inside of modifiers as well.
[7:24] And definitely also check out the talks that the author of this add on did.
[7:28] They're very interesting.
[7:29] His name is Alessandro Zomperrelli.
[7:31] And he talked about the tissue add on and he does amazing things with it.
[7:35] So definitely check that out as well.
[7:37] So if you're interested to read more about this topic, you can read about it in my ebook.
[7:42] And you can also find the blend file and another version of the same topic as well.
[7:46] And you can ask questions about it if you want.
[7:49] And I will try my best to help.
[7:51] So thanks a lot for watching.
[7:52] See you later.



---

## Captured Frames

- [1:40] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_000.jpg
- [3:03] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_001.jpg
- [4:26] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_002.jpg
- [5:08] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_003.jpg
- [6:12] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_004.jpg
- [6:37] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_005.jpg
- [6:59] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_006.jpg
- [7:06] tutorials/frames/vertex-groups-modifiers-and-tissue-add-on---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Using a hand-painted Vertex Group as a live input to drive both a Decimate modifier's density and the free Tissue add-on's honeycomb-style mesh generation — demonstrated on a free Blender Studio human base mesh, showing how vertex groups can act as general-purpose "masks" for modifiers beyond just deformation.

### Summary
Frame 000 shows the source asset: the Asset Browser's "Human Base Meshes Bundle" (from Blender Studio's free demo-scenes page) open, showing body/head/hand/foot variants in both Realistic and Stylized styles as draggable assets. Frame 001 shows the base head mesh entirely painted solid blue in Weight Paint mode — the starting (all-zero) vertex group before any painting, brush Radius circle visible over the forehead. Frame 002 shows the vertex group mid-paint: a colorful red/yellow/green/blue heatmap pattern across the face and forehead (red = weight 1, blue = weight 0), the Brush Symmetry panel open in the sidebar with the X mirror axis enabled — confirming symmetric painting. Frame 003 shows the Decimate modifier applied without any vertex group influence: a uniformly dense triangulated mesh across the whole head/neck, Decimate settings (Ratio, Symmetry, Triangulate, Vertex Group field) visible in the sidebar. Frame 004 shows the Tissue add-on's "Convert to Dual Mesh" operator highlighted in the Tissue Tools panel (Template, Dual Mesh, Polyhedra Decomposition, Frame/Weathered Wireframe, Convert to Curve, Custom Contour options) on the base geometry. Frame 005 shows the resulting honeycomb/cellular structure after "Convert to Dual Mesh" — an organic pebbled cell pattern covering the entire face and neck. Frame 006 shows a Wireframe modifier applied on top of the dual-mesh result (Thickness, Offset, Boundary, Replace Original, Even Thickness, Crease Edges, Material Offset, Vertex Group field all visible in the sidebar) — a pink/blue/purple color-graded viewport shading, producing a fine wireframe lattice mask-like structure over the face. Frame 007 shows the same Wireframe-modifier result from a slightly different angle with the vertex group field populated ("Group") and a Factor value set — the vertex group now controlling the wireframe's line thickness variation across the face, thicker in some regions and thinner in others.

### Key Steps
1. **Source a free rigged-quality base mesh:** download the "Human Base Meshes" bundle from Blender Studio's free demo-scenes page (donation-supported); the extracted .blend already has objects pre-marked as Assets, so it doesn't need to be opened directly — just save it to a permanent location (not Desktop/Downloads) and add that folder as an Asset Library under Preferences > File Paths so it appears in the Asset Browser.
2. **Bring an asset into the scene correctly:** drag-and-drop the desired asset from the Asset Browser (default Import Method should be Append, not Link); before interacting with it further, open the N-panel's Collection settings and **uncheck Instance** — otherwise the dragged-in object remains a non-editable instance; Alt+G to reset its location to the world origin afterward.
3. **Install the Tissue add-on:** Preferences > Get Extensions, search "tissue," Install — it then also appears under Add-ons and adds a "Tissue" tab in the N-panel.
4. **Prep the mesh for detail work:** add a Subdivision modifier (Ctrl+2 for two levels) and apply it via Ctrl+A > Visual Geometry to Mesh to bake in real geometry for the Tissue add-on to work with; apply Scale (Ctrl+A > Scale) if it isn't already 1; Shade Smooth and switch to a Matcap for clearer viewing.
5. **Paint a Vertex Group in Weight Paint mode:** left-click-drag to paint weight (red = 1), Ctrl-drag to erase (back to 0) — the weight-paint color ramp runs red (1) → yellow/green/cyan (intermediate) → blue (0), and this visualization is the easiest way to judge a vertex group's values at a glance. In Edit Mode, selecting the vertex group selects every vertex with a weight *above* zero, not just weight-1 vertices. Enable **X Symmetry** in the brush's Symmetry panel to mirror strokes automatically across the X axis (the author notes needing to disable "Mirror Vertex Group" for symmetry to actually work correctly, despite the option's name suggesting the opposite — worth testing on your own version). Hold Shift while painting to soften/smooth the edges of the painted region, similar to sculpting.
6. **Use the vertex group to drive a Decimate modifier:** add a Decimate modifier; enable the Viewport Wireframe overlay (visible even in Object Mode) to see the effect clearly; lowering the Ratio with no Vertex Group assigned does a uniform density reduction everywhere. Assigning the painted Vertex Group in the modifier's Vertex Group field instead concentrates decimation according to the painted weights, and the group's Invert toggle flips which areas are preserved vs. reduced — producing a striking, controllable "digital sculpture" look; a Factor/Influence value further tunes how strongly the group affects the result. Apply once satisfied.
7. **Convert the geometry with the Tissue add-on:** with the object selected, in the Tissue panel click **Convert to Dual Mesh** — this takes a few seconds to compute and produces an organic, honeycomb/cellular tiled structure across the entire surface, following the underlying mesh's topology.
8. **Add a Wireframe modifier for a lattice/mask look:** stack a Wireframe modifier on the dual-mesh result and significantly reduce its Thickness value; unchecking **Replace Original** keeps the wireframe as an additional layer on top of the base geometry rather than replacing it, producing a combined mask-like appearance under an appropriately eerie Matcap. The same painted Vertex Group can be assigned to the Wireframe modifier's own Vertex Group field to make line thickness vary across the surface — thicker in high-weight areas, thinner in low-weight ones (or the reverse, via Invert) — and the modifier's own Factor/vector-influence value can be raised to reduce how strongly the vertex group affects thickness if the lines read as too thin.

### Nodes / Settings
- **Asset Browser / Preferences:** File Paths > Asset Libraries (add a folder to surface .blend assets), Import Method (Append vs. Link), Collection "Instance" checkbox (must be unchecked to edit a dragged-in asset).
- **Tissue add-on (Extensions):** Tissue Tools panel — Template, Dual Mesh, Convert to Dual Mesh (the operator used here), Polyhedra Decomposition, Frame/Weathered Wireframe, Convert to Curve, Custom Contour.
- **Vertex Groups / Weight Paint:** paint (LMB) / erase (Ctrl+LMB), weight color ramp (red=1 → blue=0), Brush Symmetry (X axis), Shift-hold to soften, Select vertex group selects all weight > 0.
- **Modifiers:** Decimate (Ratio, Symmetry, Triangulate, Vertex Group field + Invert), Wireframe (Thickness, Offset, Boundary, Replace Original, Even Thickness, Crease Edges, Material Offset, Vertex Group field), Subdivision Surface (Ctrl+2, prep step).
- **Finalizing:** Ctrl+A > Visual Geometry to Mesh (bake modifiers), Ctrl+A > Scale (apply scale).

### Difficulty
Intermediate

### Blender Version
Blender 4.3.2 — explicitly named; the author confirms the Tissue add-on still functions the same way in this version.

### Tags
organic, procedural, abstract, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Tissue add-on or vertex-group-driven modifier masking in this depth.

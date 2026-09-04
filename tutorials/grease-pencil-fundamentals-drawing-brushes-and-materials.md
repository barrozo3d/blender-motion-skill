---
title: Grease Pencil Fundamentals: Drawing Brushes and Materials
source: Blender Studio
url: https://studio.blender.org/training/grease-pencil-fundamentals/5c40c1d379f30a0147c0c19a/
author: Matias Mendiola (Blender Studio)
ingested: 2026-09-03
blender_version: "2.80 (status bar reads v2.80.39) — see the version caveat: Grease Pencil was rewritten as GPv3 in 4.3"
tags: [grease-pencil, materials, brushes, texturing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/
frame_count: 8
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Grease Pencil Fundamentals: Drawing Brushes and Materials

**Source:** [Blender Studio](https://studio.blender.org/training/grease-pencil-fundamentals/5c40c1d379f30a0147c0c19a/)
**Author:** Matias Mendiola (Blender Studio)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In Grease Pencil, the combination of a brush and a material will define the look and feel
[0:10] of your strokes.
[0:12] Each tool has their own brush types.
[0:15] Pre-hand drawing tool and primitive use draw brushes.
[0:21] Fill tool, fill brushes.
[0:23] And eraser tool, eraser brushes.
[0:27] The brush settings can be modified in the Active Tool panel or in the top bar.
[0:37] The main settings for drawing brushes are Radius, Strength and Material.
[0:43] Radius controls the brush size.
[0:45] You can change the size value on the top bar or with the F key.
[0:55] Radius controls the opacity of the strokes and the value can be adjusted with Shift F
[0:59] key.
[1:05] If you want to keep your values always the same along your lines, you can turn off the
[1:09] use of the tablet pressure.
[1:12] Last, you can choose the material to use with the Brush Delector.
[1:18] But if you want to add, delete or modify materials, you must use the Material section
[1:23] in Properties Editor.
[1:24] There are two main properties in the Special Material for Grease Pencil.
[1:29] Stroke to set the line color and Fill to set the color of the interior space enclosed
[1:36] by the strokes.
[1:38] You can use the checkboxes to choose which one will be used in a particular material.
[1:44] By default Stroke and Fill use a solid color that you can change with the color wheel.
[1:50] As with these main settings, you can play to obtain different kinds of lines and colors
[1:55] to use on your drawings.
[2:12] Materials are linked to the strokes, so if you change the setting, it will be affect
[2:16] all the strokes that use it.
[2:19] To add, delete or rename a material, use the Materials list.
[3:19] Grease Pencil has some draw brushes presets, like Pencil, Pen, Noise, Block, Marker and
[3:33] Ink.
[3:35] But if you want a more precise control on your brushes, you can go to the Brush option
[3:39] panel.
[3:40] The first two parameters affect your line while you are drawing.
[3:44] With Input Sample and Active Smooth, you can control the balance between precision and
[3:48] smoothness of your lines.
[3:51] It's up to you to find the right balance based on your sensation while you are drawing and
[3:55] the hardware you are using.
[4:05] Angle and Factor control the thickness of your line.
[4:08] Angle set the direction of the maximum thickness, and Factor is how strong the thickness difference
[4:13] will be.
[4:22] Post Processing settings activate some process that affect the lines after they were made.
[4:27] Basically, to make them smoother and less jagged.
[4:37] Stabilizer settings control the parameter to steady the pen giving you more precision
[4:41] while drawing.
[4:56] Finally, Randomness parameters help to make more expressive lines.
[5:14] But if this option is not enough, you can go further and use the Curve panel for a more
[5:19] precise control on sensitivity, strength and shitter.
[5:44] The next step is to create a new texture brush.
[5:53] Go to the Active Tool panel and create a new brush with the Add Brush button.
[5:59] Next, go to the Materials panel to create a new material for the brush.
[6:05] Add a new slow to the list and create a new stroke material.
[6:09] Bring the stroke style to Texture and open the image you want to use.
[6:25] If you are using a black and white or alpha image as texture, use this pattern to allow
[6:29] you to change the color of your line.
[6:43] As with fill, it has also multiple styles other than solid color.
[6:49] Gradient, Checkerboard and Texture.
[7:19] The Grish Pencil Brush and Material System is flexible enough for multiple artistic styles.



---

## Captured Frames

- [0:45] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_000.jpg
- [1:30] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_001.jpg
- [3:25] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_002.jpg
- [3:50] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_003.jpg
- [4:10] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_004.jpg
- [5:20] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_005.jpg
- [6:15] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_006.jpg
- [6:55] tutorials/frames/grease-pencil-fundamentals-drawing-brushes-and-materials/frame_007.jpg

---

## Structured Notes

### Core Technique
How Grease Pencil's **brush** and **material** systems divide the work: the brush controls *how a stroke is laid down* (size, opacity, smoothing, stabilisation, randomness), the material controls *how it looks once drawn* (Stroke colour/style and Fill colour/style), and the two are independent — the same brush over a different material gives a completely different line. Materials are linked to strokes, so editing one material restyles every stroke already drawn with it. The lesson ends by building a **texture brush**: a new brush paired with a new material whose Stroke Style is set to Texture.

### Summary
Brush versus material: stroke colour, fill style, the stabilizer, jitter and the texture brush. Each Grease Pencil tool has its own brush family — the freehand draw tool and the primitives use **draw** brushes, the fill tool uses **fill** brushes, the eraser uses **eraser** brushes. Brush settings live in the Active Tool panel or the top bar, which in [frame_001] reads `Draw Pencil | Radius 221px | Strength 0.936 | Material: Red`, followed by the **Brush / Options / Curves / Appearance** menus.

The three main draw-brush settings are **Radius** (size, adjustable with **F**), **Strength** (opacity, adjustable with **Shift+F**), and **Material**. Tablet pressure can be switched off to hold those values constant along a line. The brush's Material selector only *chooses* a material — adding, deleting or editing one is done in the Material section of the Properties editor.

A Grease Pencil material has two independent halves, both visible in [frame_001]'s Surface panel: **Stroke** (the line itself — `Mode Type: Line`, `Style: Solid`, `Color: red`) and **Fill** (the colour of the area enclosed by the strokes). Each has its own checkbox, so a material can be stroke-only, fill-only, or both. The materials list in that frame holds `Black`, `Red`, `Grey`, with the active `Red` slot showing **12 users** — the direct evidence for "materials are linked to the strokes": edit that slot and all twelve strokes change.

Six draw-brush presets ship with the template — **Pencil, Pen, Noise, Block, Marker, Ink**. [frame_007] confirms the set from the other side: the Outliner in the lesson's demo file holds one collection per preset (`Pencil`, `Pen`, `Noise`, `Block`, `Marker`, `Ink`) beside a `Brushes_options` collection.

For finer control, the **Options** panel ([frame_003], captured with it open) exposes the whole brush model at once:

- **Input Samples** (`5`) and **Active Smooth** (`0.000`) — the precision-versus-smoothness balance applied *while drawing*. The right values depend on the drawing hardware.
- **Angle** (`0°`) and **Factor** (`0.000`) — line thickness variation: Angle sets the direction of maximum thickness, Factor how pronounced the difference is.
- **Post-processing Settings** (enabled) — applied *after* a stroke is made, to smooth and de-jag it: `Smooth` + `Iterations`, `Smooth Thickness` + `Iterations`, `Subdivision Steps` (`3`), `Randomness`.
- **Stabilizer Settings** (`Radius 40`, `Factor 0.900`) — steadies the pen for more precise strokes.
- **Random Settings** — `Pressure`, `Strength`, `UV`, `Jitter`, for deliberately more expressive, less mechanical lines.

Beyond those, the header's **Curves** menu gives curve-based control over sensitivity, strength and jitter.

The final section builds a texture brush: add a brush with **Add Brush** in the Active Tool panel, add a new material slot, set its **Stroke Style** to **Texture** and load an image. A black-and-white or alpha image is the useful case, because it leaves the line's colour under the material's control rather than baking it into the texture. Fill has the same range of styles: besides Solid, it offers **Gradient, Checkerboard and Texture** — [frame_007] shows a Gradient fill in use on the cactus, with `Gradient Type: Linear`, a primary and Secondary Color, `Mix Factor 0.300`, Flip Colors, and Location / Scale / Angle controls for placing the gradient.

### Key Steps
1. Pick the tool first — freehand draw and primitives take **draw** brushes, the fill tool **fill** brushes, the eraser **eraser** brushes.
2. Set the three main draw-brush values in the top bar or Active Tool panel: **Radius** (size, **F**), **Strength** (opacity, **Shift+F**), **Material**.
3. Turn **off tablet pressure** when you want radius/strength to stay constant along a stroke.
4. Add, delete or rename materials in the **Material** section of the Properties editor — the brush's Material selector only picks from that list.
5. Configure the material's two halves independently: enable **Stroke** for the line and/or **Fill** for the enclosed area, each with its own Style and Colour.
6. Remember materials are shared: changing a material's settings restyles every stroke already using it (the active slot shows its user count, `12` in [frame_001]).
7. Start from a preset — **Pencil, Pen, Noise, Block, Marker, Ink** — then refine in the **Options** panel.
8. Balance **Input Samples** against **Active Smooth** for precision versus smoothness while drawing; tune to your hardware and hand.
9. Shape line weight with **Angle** (direction of maximum thickness) and **Factor** (how strong the variation is).
10. Use **Post-processing Settings** (Smooth, Smooth Thickness, Subdivision Steps, Randomness) to clean strokes after they are drawn, and **Stabilizer Settings** (Radius, Factor) to steady the pen while drawing.
11. Add life with **Random Settings** — Pressure, Strength, UV, Jitter — or the **Curves** menu for curve-based sensitivity / strength / jitter.
12. To build a **texture brush**: **Add Brush** in the Active Tool panel → add a new material slot → set **Stroke Style: Texture** → load the image. Use a black-and-white or alpha image so the line colour stays controlled by the material.
13. For fills, choose among **Solid, Gradient, Checkerboard, Texture**; a Gradient fill adds Gradient Type, Secondary Color, Mix Factor, Flip Colors and Location/Scale/Angle placement.

### Nodes / Settings
- **Brush top bar / Active Tool panel** — `Radius` (**F**), `Strength` (**Shift+F**), `Material`, plus the **Brush / Options / Curves / Appearance** menus.
- **Draw-brush presets** — Pencil, Pen, Noise, Block, Marker, Ink.
- **Options ▸ stroke shaping** — `Input Samples`, `Active Smooth`, `Angle`, `Factor`.
- **Options ▸ Post-processing Settings** — `Smooth` + `Iterations`, `Smooth Thickness` + `Iterations`, `Subdivision Steps`, `Randomness`.
- **Options ▸ Stabilizer Settings** — `Radius`, `Factor`.
- **Options ▸ Random Settings** — `Pressure`, `Strength`, `UV`, `Jitter`.
- **Curves menu** — curve-based sensitivity, strength and jitter.
- **Material ▸ Surface ▸ Stroke** — checkbox, `Mode Type` (Line), `Style` (Solid / Texture), `Color`.
- **Material ▸ Surface ▸ Fill** — checkbox, `Style` (Solid / Gradient / Checkerboard / Texture); Gradient adds `Gradient Type`, `Secondary Color`, `Mix Factor`, `Flip Colors`, `Location X/Y`, `Scale X/Y`, `Angle`.
- **Materials list** — per-object slots with a user count, the concrete reason a material edit propagates to every stroke using it.

### Difficulty
Beginner

### Blender Version
**2.80** — the status bar reads `v2.80.39` in [frame_001], [frame_003] and [frame_007].

⚠️ **Read this entry for the model, not for the menu paths.** Grease Pencil was rewritten as **Grease Pencil v3** in Blender 4.3. The division of labour taught here — brush controls how a stroke is laid down, material controls how it looks, materials are shared by every stroke that uses them — is the durable part and still holds. Panel locations, and some setting names, have moved since. Cross-check any specific control against a modern entry before relying on it.

⚠️ **Transcript artifacts, all resolved against the frames.** Whisper rendered several terms wrongly on this Spanish-accented narration and the on-screen UI settles each one: "shitter" is **Jitter** (visible under Random Settings in [frame_003]), "add a new slow to the list" is a new **slot**, "Brush Delector" is the brush **selector**, "Pre-hand drawing tool" is **freehand**, and "Grish Pencil" is Grease Pencil. One is a genuine slip by the narrator rather than a mishear: the audio says *"Radius controls the opacity of the strokes ... adjusted with Shift F"* immediately after defining Radius as size — the setting that controls opacity is **Strength**, which is what **Shift+F** adjusts, and [frame_001]'s header shows the two as separate fields.

### Tags
grease-pencil, materials, brushes, texturing, beginner

---

## Related Tutorials
- `grease-pencil-fundamentals-2d-animation.md` — the companion lesson from the same course; it animates with these brushes and materials, and shares the version caveat above.
- `daily-blender-tip-97---exploring-grease-pencil---different-brushes.md` — a short tour of the same draw-brush presets in isolation.
- `daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil.md` — the rough-to-clean inking pass these brushes and materials are used for.
- `grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea.md` — **read alongside the version caveat**: where the modern Grease Pencil drawing tools ended up after the GPv3 rewrite.

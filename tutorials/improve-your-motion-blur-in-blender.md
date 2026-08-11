---
title: Improve your Motion Blur in Blender
source: YouTube
url: https://www.youtube.com/watch?v=VeW-3BWUtlM
author: Dantti
ingested: 2026-08-11
blender_version: "Not specified"
tags: [compositing, motion-blur, view-layers, holdout, render-layers, grease-pencil, workflow, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/improve-your-motion-blur-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Improve your Motion Blur in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=VeW-3BWUtlM)
**Author:** Dantti
**Duration:** 2m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Nyt on disappear Sinak민uise
[0:01] perfume fibers,
[0:06] nuovan tyY scalposin ros Dubin
[0:14] 1.
[0:17] умi
[0:24] Onda täysin puesik Yum confusion Sampio 4
[0:27] opens�いた
[0:29] infSCWe inины
[0:30] tthis example have
[0:32] placeshings and bodyobject toLED
[0:33] separate collection
[0:35] Transparency is turned on
[0:37] for better results
[0:38] know Nable this holdout option
[0:40] at the toggle menu to get this icon
[0:42] to switch on and off
[0:44] Holdout means the collection won't
[0:46] be rendered at all
[0:47] so you can use that collection
[0:48] as a mask which is really powerful
[0:51] let's create a new view layer
[0:53] name the original view
[0:54] for ine детikäivyt pakkuvSOASSИOkay India- singing design to
[0:56] WINGS, toggle this setting to see them both at the
[0:58] outliner. Adjust the budget view layer, disable WINGS
[1:01] collection entirely and at the WINGS view layer mark
[1:05] the body collection as a holdout. If your collection has other
[1:08] collections inside mark them as well. Reset the motion plot back
[1:13] to the default settings by pressing
[1:15] assume backspace here, switch to compositing workspace,
[1:18] check use nodes, duplicate this самly
[1:21] render layers node with SHIFT D to move it below.
[1:24] Esitt你看Ultsprinci on armoista tai hienote brus finansioida.
[1:30] Ulo kelamo A ja Erk putijampia.
[1:33] Nyt lämpintälaita ker 가자 pog washing.
[1:36] Lappungenerointe shop Global
[1:39] Melkorobint hace torkittakounced.
[1:44] Pertää jusota Es часть 2k psycho's Sight】
[1:48] ...neuda nä spin sectori sürp Seconditionen.
[1:52] T 알려 soybean voi utsal과maan esнет ..
[1:55] skoida veeninen ya kiinni huomilla siitä, että
[1:58] ��� manufacturings voi hyökyä yleensä yhte olmuşuutta is então
[2:05] viljaigon sciiftiä manipuutiin ajatell updates virun
[2:08] ja säällsää merrymša tarjoamaan
[2:10] att gear harorna mu Täär vilja용i
[2:13] zuginen you kaucheramaa
[2:15] by two
[2:17] mitigation
[2:20] Se Hybrid OS-emissionilla entiasluuttaa ohj virutaankin on siitä waiting odpow史inaa, joissa on sympathioita und plast Isabella buffer entry PLT poly Dragon Maria picks up a file.
[2:31] M Brusne作aiset pääsköii
[2:34] Nוף osat Laureningen per cooking



---

## Captured Frames

- [0:36] tutorials/frames/improve-your-motion-blur-in-blender/frame_000.jpg
- [0:45] tutorials/frames/improve-your-motion-blur-in-blender/frame_001.jpg
- [0:58] tutorials/frames/improve-your-motion-blur-in-blender/frame_002.jpg
- [1:10] tutorials/frames/improve-your-motion-blur-in-blender/frame_003.jpg
- [1:22] tutorials/frames/improve-your-motion-blur-in-blender/frame_004.jpg
- [1:50] tutorials/frames/improve-your-motion-blur-in-blender/frame_005.jpg
- [2:20] tutorials/frames/improve-your-motion-blur-in-blender/frame_006.jpg
- [2:38] tutorials/frames/improve-your-motion-blur-in-blender/frame_007.jpg

---

## Structured Notes

> **Source note — degraded transcript.** Whisper's audio transcription for this video is badly corrupted from roughly 1:24 onward (garbled multilingual hallucination, not real speech-to-text). This extraction leans primarily on the 8 captured frames' visible node graphs and panels — which don't depend on transcript accuracy — rather than the narration. Confidence is high for the compositor node setup (directly read off-screen in frames 004–007) and for the render/view-layer setup (frames 000–003, cross-checked against the coherent 0:29–1:24 portion of the transcript).

### Core Technique
Faking per-part directional motion blur in Blender's **Compositor** (via the Directional Blur node) applied to Holdout-masked, separately-rendered View Layers — instead of relying on Cycles' native render-time motion blur — so each moving part can get independently-tuned blur length/spin/zoom, and so the technique also works on object types (e.g. Grease Pencil) that don't get good native motion blur.

### Summary
Dantti demonstrates a workaround for motion blur that doesn't look right (or doesn't work at all, as with Grease Pencil) using Blender's default render-time motion blur. Using an "Ornithopter" rig (a Model/Body plus a Wings collection containing Leg1/Leg2/Base parts) as the example, he isolates each moving part into its own View Layer using collection **Holdout** toggles (so a layer renders only its own part, transparent everywhere else — Render Properties → Film → Transparent is required for this), resets native motion blur back to default since it isn't what does the final work, then in the **Compositing** workspace feeds each isolated Render Layers node through its own **Directional Blur** node (independent Iterations/Center/Distance/Angle/Spin/Zoom per part) and recombines all the blurred layers with **Add** nodes into the final Composite output (Use Alpha enabled to preserve transparency). The description notes this also works with Grease Pencil objects and warns that adding a background back in after rendering to transparency needs its own separate pass, or parts (like the wings) may not show up correctly.

### Key Steps
1. Organize the moving object into separate collections per part that needs independent blur control (seen in-frame: an `ORNITHOPTER` hierarchy with a `Wings` collection and a `Model`/`Body` collection; a later view layer further isolates `Leg1`, `Leg2`, and `Base` sub-parts).
2. In **Render Properties → Film**, enable **Transparent** (Filter Size 1.50px, Overscan 3% in the example) so isolated per-part renders come out with real alpha instead of a background.
3. Use the Outliner's collection **Holdout** restriction toggle to exclude a collection from a given View Layer's render entirely — a holdout collection still occludes/interacts but contributes nothing to the render, letting other collections render in isolation.
4. Create one **View Layer** per part that needs its own blur: e.g. a `Body` layer with the `Wings` collection marked/disabled as holdout, and a `Wings` layer with the `Model`/`Body` marked as holdout (and if a collection has nested sub-collections, holdout those too).
5. Reset any native per-object **Motion Blur** settings back to default (`Alt+Backspace` on the setting) — it is explicitly not what produces the final blurred look in this workflow.
6. Switch to the **Compositing** workspace and enable **Use Nodes**.
7. Add one **Render Layers** node per View Layer created in step 4 (each pointing at its own view layer — `Body`, `Wings`, and further per-part layers as needed).
8. Feed each Render Layers node's Image output into its own **Directional Blur** node. Parameters seen in-frame: **Iterations** (e.g. 8), **Center X/Y** (0.5/0.5 = image center), **Distance** (small negative value, e.g. −0.08), **Angle** (blur direction, e.g. 5°), **Spin** (rotational blur component, e.g. 3.1°), **Zoom** (radial/zoom blur component, 0 = none). Because this is a 2D post-process, it applies uniformly to whatever is in that render layer regardless of source object type — this is what makes it work for Grease Pencil, unlike native 3D motion-vector-based blur.
9. Recombine the blurred per-part layers with **Add** (Mix) nodes chained together (Fac 1.000, Clamp enabled), feeding the final result into **Composite** with **Use Alpha** checked so transparency survives the whole stack.
10. (Per the video description, not clearly visible in the corrupted back half) Add a background as its own separate layer/pass rather than compositing straight onto transparency, since parts can fail to show up correctly if this is done carelessly.

### Nodes / Settings
- **Render Properties → Film:** Transparent ✓, Filter Size 1.50px, Overscan 3%
- **Outliner:** per-collection Holdout restriction toggle, used per-View-Layer
- **View Layers:** one per isolated moving part (`Body`, `Wings`, and further per-part layers like `Leg1`/`Leg2`/`Base` seen in-frame)
- **Compositor:** Render Layers (one per view layer) → Directional Blur (Iterations, Center X/Y, Distance, Angle, Spin, Zoom) → Add/Mix (Fac 1.000, Clamp) chained across all layers → Composite (Use Alpha ✓)
- **Native Motion Blur** (Render Properties): explicitly reset to default (`Alt+Backspace`) — not used for the final look

### Difficulty
Intermediate — requires comfort with View Layers, collection Holdout, and Compositor node-graph fundamentals; the core insight (fake the blur in comp per isolated layer instead of relying on render-time blur) is simple once seen, but reconstructing it here required reading the node graphs directly since narration failed for most of the video.

### Blender Version
Not specified.

### Tags
compositing, motion-blur, view-layers, holdout, render-layers, grease-pencil, workflow, intermediate

---

## Related Tutorials
- [My Stylized Blender NPR Pipeline - NOXIOUS Shot Breakdown](my-stylized-blender-npr-pipeline---noxious-shot-breakdown.md) — shares `grease-pencil`, `compositing`, `render-passes`; same Holdout-masked-View-Layer-into-Compositor pattern (there: AOV/Line-Art passes; here: per-part Directional Blur), both aimed at working around Grease Pencil's limited native render support.

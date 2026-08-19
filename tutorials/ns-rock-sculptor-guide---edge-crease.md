---
title: NS Rock Sculptor Guide - Edge Crease
source: YouTube
url: https://www.youtube.com/watch?v=YEtwMhsKh1A
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, organic, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---edge-crease/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Edge Crease

**Source:** [YouTube](https://www.youtube.com/watch?v=YEtwMhsKh1A)
**Author:** Nick Sayce
**Duration:** 3m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] edge crease, I think I'm going to use this one. There's a few ways to sharpen edges.
[0:14] There's several ways. One of them is a manual way. The other one is with this. I tend to
[0:19] do a mixture of both because if you look at the, it's been quad remeshed and that's not,
[0:25] that's not, I don't know what's up there. Something's going wrong there. Let me just check.
[0:30] What's, oh, hello. It's just the, I don't know why it's done that. It's not the end of the world
[0:39] because we'll just, I'm just going to remesh it real quick and I'll solve that. Sculpt, Sculpt Rock.
[0:45] There you go. So what I'm looking is for any edges that I can possibly strengthen using the edge
[0:53] crease edges that do this. I can't find a way to remesh it to follow the contours. This one I'd
[1:00] have to do. I'd probably do manually. And what I mean by that is, so if I wanted this edge to be
[1:05] a bit sharper, I just shift and contract, so click and then control click, press GG to move them on
[1:12] the normals. And that just adds a bit more of a sharp edge there. These are more difficult,
[1:19] but they're doable. It just means you have to start moving more vertices together to get that
[1:27] sharpness because as I say, the remesh doesn't really account too well for corners. So yeah,
[1:35] you can just sharpen those corners just using, doing it manually like this. That's another way.
[1:43] Or when the option is there, which is not always, but when it is, I like to use it. I want to
[1:49] turn this into quite a sharp edge. And again, I could do it two ways. I could grab all these
[1:57] to there, press GG and then bring it close up. And there we've got a nice sharp edge. Or
[2:06] the easier way when you have the option is to select the sharpish bit and then using this
[2:13] edge crease, which is underneath the gulp. We don't need that open. You'll see once I put,
[2:20] once I add this, so one is I never use one, even 0.5 is quite high. So I give it a weight of about
[2:26] 0.3, press apply crease. And then again, it's added a bit of sharpness there. When we've got
[2:36] edge wear on, it'll be easier to see. But as I say, there's several ways to
[2:40] increase the, I've done this on the presets. So it's not something you're going to have to do
[2:48] for them, but it just adds a bit. It's not something that can be programmed easily at all.
[2:56] So that's why that's an option, which is the edge tree. Edge trees, edge crease. That is edge crease.
[3:03] Edge crease. Yeah, we're good. We can move on to colour.



---

## Captured Frames

- [0:10] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_000.jpg
- [0:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_001.jpg
- [1:15] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_002.jpg
- [1:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_003.jpg
- [2:15] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_004.jpg
- [2:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_005.jpg

---

> **Third-party add-on note:** This tutorial covers the **Edge Crease** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). The panel's "Enter Edit Mode" / "Clear All Creases" buttons are add-on-provided shortcuts wrapping Blender's own native Edge Crease mesh data — but the panel also exposes its own weight field + "Apply Crease" button (confirmed in the corrected transcript below), not just a bare Shift+E passthrough.

**Transcription note (root cause + fix):** The original ingest's Whisper transcript (395 chars, `small` model) was a genuine bug, not silent/music-only audio — the `small` model degenerated into a repeating loop on this video's quiet, pause-heavy narration ("I can't find a way to sharpen/remesh the edges to follow the contours" repeated near-verbatim every ~30s), a known Whisper failure mode. Re-downloaded the audio fresh and re-transcribed with the `medium` model: same audio, correct decode, full 2387-char coherent transcript (above) recovered on the first attempt — confirms this was a model-capacity issue, not a download/bot-check/audio problem. Structured Notes below now combine the real narration with the 6 captured frames.

## Structured Notes

### Core Technique
Marking specific mesh edges with Blender's native Edge Crease so the Subdivision Surface modifier keeps those edges sharp/faceted instead of rounding the whole rock into a uniform smooth blob — done either fully manually (select verts, nudge along normals) or via the add-on's own weighted "Apply Crease" control.

### Summary
Nick Sayce walks through sharpening edges on a procedurally-remeshed rock (base mesh built earlier in the NS Rock Sculptor pipeline, here named "Sculpt Rock") using the add-on's Edge Crease panel. He opens by noting there are "a few ways to sharpen edges... I tend to do a mixture of both." First he hits a remesh glitch (quad-remesh produced a bad result on part of the mesh) and re-runs the Voxel/Quad remesh to fix it before continuing — a reminder that this step assumes a clean remeshed base. He then demonstrates two techniques side by side: (1) the **fully manual** approach — click an edge, Ctrl+click the next to extend the selection along an edge loop, then G G (double-tap Grab, which constrains movement to the vertex normal in Blender) to nudge the selected verts and manually punch a sharper crease into the surface; he says this is necessary because "the remesh doesn't really account too well for corners," so tight corners often need this hand-adjustment regardless of the crease tool. (2) The **Edge Crease panel** approach — select the edge(s) to sharpen, open the add-on's crease control ("underneath the [gulp]" — exact UI label not clearly caught in the audio, but it's the panel's own crease sub-section), set a weight (he specifically avoids 1.0 or even 0.5 as "quite high," settling on **~0.3**), then press **Apply Crease**. He calls this the "easier way when you have the option" — implying it doesn't apply to every mesh state — and notes edge crease also interacts with the add-on's separate **Edge Wear** feature ("when we've got edge wear on, it'll be easier to see"), and that some baseline creasing is already baked into the add-on's presets. He closes by confirming the workflow ("edge crease, edge crease, yeah, we're good") and moving on to the Colour tab next.

### Key Steps
1. Ensure the base mesh has already been remeshed cleanly (Sculpt Settings tab) — a bad quad-remesh will produce broken geometry that needs re-running before creasing makes sense.
2. Decide per-edge whether the Edge Crease panel's weighted tool will reach it, or whether it needs the fully manual approach — tight/complex corners often don't remesh cleanly and need manual handling either way.
3. **Manual method:** click one end vertex/edge, Ctrl+click to extend selection along the loop, then press **G G** (Grab twice — constrains movement along the vertex normal) and nudge inward/outward to physically sharpen the surface at that edge.
4. **Panel method:** select the target edge(s), open the add-on's Edge Crease sub-panel, set a **weight** (he uses ~0.3 — even 0.5 is called "quite high," 1.0 avoided), then click **Apply Crease**.
5. Toggle the add-on's **Edge Wear** feature on to more easily see how the crease reads once shaded/worn, rather than judging purely off the flat/matcap silhouette.
6. Use **Clear All Creases** to reset the object's crease weights back to zero if starting over.
7. Repeat per problem edge — this is an iterative, look-then-adjust pass, not a one-shot global operation — then move on to the Colour tab.

### Nodes / Settings
- Sidebar section "Edge Crease" (panel order across the series: Sculpt Settings → Weight Paint → Edge Crease → Colour → Moss → Filters → Colour Ramps → Displacement → Bump → Geometry → Scatter)
- "Enter Edit Mode" button — jumps into Blender's native Edit Mode / edge-select
- Crease **weight field** (recommended ~0.3, avoid 1.0/0.5 per the narration) + **"Apply Crease"** button — add-on convenience wrapper over Blender's native Edge Crease data
- "Clear All Creases" button — resets Blender's native Edge Crease data on the object
- Manual technique: Ctrl+click edge-loop extend, then **G G** (Grab-Grab, normal-constrained move)
- Related add-on feature referenced in-narration: **Edge Wear** (separate tab/toggle, makes creased edges read more clearly when previewing)
- Underlying mechanism: standard Blender Edge Crease data, consumed by the Subdivision Surface modifier already present in the modifier stack

### Difficulty
Intermediate (two techniques to know — a weighted panel tool and a fully manual vertex-nudge fallback for edges the remesh/crease combo doesn't handle well)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally in the corrected transcript either) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
procedural, geometry-nodes, organic, product-viz, intermediate

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Edge Crease tab.
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide-sculpt-settings.md) — same add-on/series, Sculpt Settings tab (adjacent in panel order — this episode's base mesh/Subdivision Surface level and the quad-remesh step referenced in the narration come from there).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs (directly relevant — that episode's decimation step explicitly warns Edge Wear/crease-adjacent detail must be applied before decimating).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (its Subdivision Surface viewport-level guidance directly affects how visible edge creases read, per that episode's own notes).
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab (where this episode's narration explicitly hands off next).
- [Daily Blender Tip 59 - Crease Edges](daily-blender-tip-59---crease-edges.md) — the underlying native Blender technique (Shift+E, or Shift+E then 1/-1 for max/reset) that this add-on's own weight-field + Apply Crease control wraps.

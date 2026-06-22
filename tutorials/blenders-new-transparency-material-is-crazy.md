---
title: Blender's NEW Transparency Material is CRAZY!
source: YouTube
url: https://www.youtube.com/watch?v=U2I8YDrO5Jc
author: SouthernShotty
ingested: 2026-06-22
blender_version: "5.2"
tags: [materials, shaders, rendering, lighting, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blenders-new-transparency-material-is-crazy/
frame_count: 0
---

# Blender's NEW Transparency Material is CRAZY!

**Source:** [YouTube](https://www.youtube.com/watch?v=U2I8YDrO5Jc)
**Author:** SouthernShotty
**Duration:** 10m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Blender 5.2 adds an awesome new feature to the Principled BSDF node called Thin Walls, which makes certain types of transparent materials much easier to pull off. It improves things like paper transparency, creating thin film-like materials like bubbles, and makes it much easier for light passing through foliage to create more realistic environmental renders, and it even fixes the infamous dark [music] glass effect problem people have in Blender. Where when you try and light through something like a glass window, you will lose a ton of light energy and the glass itself will almost appear &gt;&gt; [music] &gt;&gt; dark. But the greatest part of all of this new feature is that not only does it improve everything visually and make the process simpler, it also renders quicker. So before we get started, I want to say thank you to the sponsor of this video, which is Storyblocks, and let's dive in and get started. Now at the end of this video, I'm going to show you how to use it to make this cool effect right here, but first we're going to go through some of the boring settings, and then I'm going to show it in some practical examples. If you're feeling impatie...



---

## Structured Notes

### Core Technique
Using Blender 5.2's new "Thin Walls" option on the Principled BSDF to render thin transparent/translucent materials (paper, bubbles/thin film, foliage backlight) more realistically and faster, while fixing the classic "dark glass" light-loss problem.

### Summary
SouthernShotty introduces Thin Walls, a new Principled BSDF feature in Blender 5.2 aimed at thin transparent materials. It improves paper transparency, thin-film materials like bubbles, and light passing through foliage for more realistic environment renders. It also fixes the well-known "dark glass" problem, where lighting through glass (e.g. a window) loses a large amount of light energy and the glass appears unnaturally dark. Beyond the visual improvement, Thin Walls also renders faster than the workarounds it replaces. The video covers the underlying settings first, then practical examples, building toward a specific effect demonstrated at the end. (Transcript truncated by ingestion at ~1200 characters — Whisper failed on this run so the captions fallback was used, which doesn't preserve chapter segmentation; the actual settings walkthrough, practical examples, and final effect build were not captured here and would need a follow-up pass with working Whisper transcription for full node-level detail.)

### Key Steps
1. [Context] Understand Thin Walls as a new Principled BSDF option in Blender 5.2 for thin transparent/translucent surfaces
2. [Use cases] Recognize target materials: paper, bubble/thin-film surfaces, backlit foliage, and glass (fixing the dark-glass light-loss issue)
3. [Settings] Review the Thin Walls toggle/parameters on the Principled BSDF (exact UI location and parameters not captured in available transcript)
4. [Practical examples] Apply Thin Walls across the example materials shown later in the video
5. [Final effect] Build the showcased effect using Thin Walls (not captured — see truncation note above)

### Nodes / Settings
- `Principled BSDF` > Thin Walls (new in Blender 5.2) — improves thin transparent material rendering (paper, bubbles/thin film, foliage backlight) and fixes the dark-glass light-loss artifact, while rendering faster than prior workarounds

### Difficulty
Intermediate

### Blender Version
5.2

### Tags
materials, shaders, rendering, lighting, blender-5x, intermediate

---

## Related Tutorials
- [Blender 5 Beginner Tutorial - Part 2 - Materials and rendering](blender-5-beginner-tutorial-part-2-materials-and-rendering.md) — foundational Principled BSDF / material basics this new feature builds on

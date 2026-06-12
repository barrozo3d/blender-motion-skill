---
title: My Circle Problem in Blender (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=89ZPdMI_nE8
author: Ducky 3D
ingested: 2026-06-12
blender_version: "Blender 4.x+"
tags: [wave-texture, curves, seam-fix, animation, motion-graphics, procedural, shader-animation, ducky-3d, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/my-circle-problem-in-blender-tutorial/
frame_count: 0
---

# My Circle Problem in Blender (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=89ZPdMI_nE8)
**Author:** Ducky 3D
**Duration:** 18m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going? So I used to have a problem with animating a wave texture on a curve. It's supposed to look like this. And if it works right, you can make some really interesting animations. My problem is I have this issue. The wave texture is kind of breaking on the curve. And for a while until I fixed it, just refused to make animations because that was a huge problem. It broke the animation. It made it ugly. I didn't like it. I couldn't get the wave texture to be seamless. So today we're going to make this animation. And first, I'm going to show you how to fix that problem. And with it, we're going to make a beautiful animation that will allow you to make a lot more other really cool animations. I just released the tutorial for this animation on Patreon. It's very similar to it. It's really cool. It's really interesting. If you want to check that out, along with a couple other animations like that on Patreon as well, I've really been into this style. And you have a ton of other tutorials and project files available on Patreon right now. If you want to check that out, linked in the description. And you can also get a discount if you subscribe annually. So with that being said, le...



---

## Structured Notes

### Core Technique
**Fixing wave texture seam on circular curves** — when a Wave texture is applied to a curve object that loops, it creates a visible seam/break where the texture wraps. The fix uses curve-aware UV mapping so the Wave texture tiles seamlessly around the full circumference, enabling smooth looping wave animations on circle/ring curves.

### Summary
18-minute tutorial by Ducky 3D about solving a persistent personal frustration: wave textures on closed curves always broke at the seam. The standard texture coordinate approach creates a discontinuity where the curve meets itself. The fix involves using the curve's native spline parameter (or a custom driver-based approach) to generate UVs that go from 0 to 1 uniformly around the full loop, so the Wave texture tiles seamlessly. Once fixed, demonstrates how to build a flowing ring animation that's a foundation for many other motion graphics.

### Key Steps

**The Problem:**
- Wave Texture on a circle curve → visible break/seam where curve starts/ends
- Texture Coordinate → Generated/Object: treats curve as a box bounding box, not as a 1D loop
- Makes wave look correct everywhere EXCEPT the seam point → kills the animation

**The Fix — Seamless Wave on Curves:**
1. Select curve → Properties → Object Data Properties (green curve icon)
2. Enable **Curve → Fill Mode: Full** (if using 3D curves) OR keep 2D
3. In Shader Editor:
   - Add **Texture Coordinate** → use **UV** (requires curve to have UV generated)
   - OR: use a **Driver** on a mapping node offset to compensate for the seam
4. Alternative: Convert curve to mesh → use UV Unwrap → unwrap as single strip → get 0–1 U coordinate along length
5. The unwrapped U value goes 0 → 1 smoothly around the full circle → feed into Wave Texture
6. Wave tiles once (or N times) around the full loop seamlessly

**Making the Animation:**
1. Animate the Wave texture **Phase** value (driver or keyframe)
2. Phase 0→1 over the loop duration = wave moves along the curve
3. Since UV is seamless, wave flows continuously with no pop

**Design Pattern (from the tutorial):**
- Circle curve with flowing wave pattern → add taper object or bevel profile
- Animate wave phase + curve rotation simultaneously for dynamic motion
- Use Geometry Nodes or shapekey-driven profile for variation

### Nodes / Settings

**Seamless Curve Wave Setup:**
```
// Method: Mesh approach (most reliable)
Curve Object → Convert to Mesh (Alt+C / Object → Convert)
Edit Mode → UV Unwrap → "Unwrap" → single strip UV
Shader: 
  Texture Coordinate (UV) → Wave Texture (Vector)
  // UV goes 0→1 around the loop → seamless tiling

// Animate:
Wave Texture → Phase → Keyframe 0 at frame 0, 1.0 at last frame
// Creates smooth continuous flow
```

**Alternative — Spline Parameter (Geometry Nodes):**
```
Geometry Nodes on Curve:
  Spline Parameter node → Factor output (0→1 along spline)
  → Set as UV or feed directly to Wave Texture via attribute
// Factor is inherently seamless on closed splines
```

### Difficulty
Intermediate — requires understanding of UV mapping or Geometry Nodes spline parameters

### Blender Version
Blender 4.x+ (technique applicable to all modern versions)

### Tags
wave-texture, curves, seam-fix, animation, motion-graphics, procedural, shader-animation, ducky-3d, intermediate

---

## Related Tutorials
- `tutorials/replacing-adobe-after-effects-with-blender-tutorial.md` — Ducky 3D wave+Voronoi 2D animation
- `tutorials/a-powerful-lighting-node-in-blender-50.md` — Ducky 3D compositing glare effects

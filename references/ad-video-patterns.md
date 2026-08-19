---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Ad & Brand Video Patterns

Proven structural patterns for luxury/brand 3D ad videos. Each includes narrative arc, camera, materials, and timing.

---

## Pattern 1: The Hero Product Reveal

**Used for:** Watches, jewelry, perfume, luxury goods.
**Duration:** 8–15s

### Narrative Arc
1. Black void → subtle atmosphere (particles, volume)
2. Product materializes (from nothing, or from particles/light)
3. Camera orbits, showing key design details
4. Hold on hero angle — best angle with perfect lighting
5. Logo/brand text appears (in post, not in render)

### Blender Setup
```
- Product: high-poly model, polished gold/chrome material
- Background: black world, 0 strength
- Lighting: 3-point studio rig (see lighting-composition.md)
- Reveal: particles converge → product, OR product rises from below frame
- Camera: orbit 90°–180° during reveal, then hold
- Motion blur: camera orbit needs motion blur (shutter 0.5)
```

### Material Priority
- Product: metallic, high specular — this IS the ad
- Background: nothing — focus stays on product
- Catchlights: deliberately placed to show product's best angles

---

## Pattern 2: Material Transformation

**Used for:** Material brands, paint, coating, luxury finishing.
**Duration:** 5–10s

### Narrative Arc
1. Object in raw/base state (matte, unfinished)
2. Transformation sweeps across surface (wave, liquid, particle front)
3. Final state: polished, premium material
4. Close-up on surface quality

### Blender Setup
```
- Two materials: before and after
- Mix Shader: Factor animated 0→1
- Transition edge: Noise Texture → Map Range → Mix Factor (creates organic front edge)
- Camera: extreme macro close-up during transformation
- Lighting: strong specular to make material quality visible
```

---

## Pattern 3: Exploded View / Technical Reveal

**Used for:** Tech products, watches (movement), mechanical objects.
**Duration:** 10–20s

### Narrative Arc
1. Assembled product visible
2. Parts separate and float outward (exploded view)
3. Camera moves between components, showing detail
4. Parts reassemble with satisfaction

### Blender Setup
```
- Model: pre-separated parts (each as individual object)
- Animation: animate each part position outward from center
- Timing: staggered delays per part (0.1s between each)
- Easing: ease-out explosion, ease-in reassembly
- Labels: in After Effects (not in Blender render)
```

---

## Pattern 4: Particle Origin / Genesis

**Used for:** Brand identity films, abstract luxury, fragrance.
**Duration:** 8–20s

### Narrative Arc
1. Empty dark space
2. Particles appear from nowhere, swirling
3. Particles converge and assemble into logo/product
4. Final form holds, particles still orbit as atmosphere

### Blender Setup
```
- GeoNodes Simulation Zone
- Phase 1: Random positions, high velocity
- Phase 2: Lerp toward target (logo mesh positions)
- Phase 3: Hold — remaining particles orbit loosely
- Material: metallic/emissive tiny instances
- Render: point cloud for performance (Cycles)
```

---

## Pattern 5: Zoetrope / Single-Frame Loop

**Used for:** Fashion, watches, technical products.
**Duration:** 3–8s loop

### Narrative Arc
- Object/scene is a carousel — each position in 3D space is a different frame of animation
- Carousel rotates → animation plays

### Blender Setup
```
- Place N copies of model around circular path
- Each copy: animated one frame ahead of previous
- Carousel (parent Empty): slow rotation
- Camera: static, aimed at the passing models
- As carousel rotates: animation plays like a zoetrope
- Reference: Albin's IWC Schaffhausen video (luIhh4384Q8)
```

---

## Pattern 6: Material as Landscape (Macro)

**Used for:** Luxury fabrics, surfaces, materials, food.
**Duration:** 5–12s

### Narrative Arc
1. Extreme close-up — surface texture fills entire frame
2. Camera slowly pulls back (or sweeps across surface)
3. Logo/brand context arrives at end

### Blender Setup
```
- Camera: 200mm focal length equivalent, extreme DOF
- Object: simple shape, rich procedural texture
- Displacement: high Subdivision Surface + displacement modifier
- Lighting: grazing angle light (parallel to surface) to reveal texture
- Camera move: very slow, almost imperceptible drift
- Scale: make surface elements huge relative to camera
```

---

## Pattern 7: Liquid / Fluid Moment

**Used for:** Beverages, perfume, skincare, food.
**Duration:** 3–8s

### Narrative Arc
1. Liquid pours, splashes, or falls
2. Freeze at peak moment (optional)
3. Product label/logo composited in post

### Blender Setup
```
- Mantaflow liquid simulation, resolution 128–256
- Bake simulation, then bake mesh
- Material: glass shader with volume absorption (color of liquid)
- Lighting: backlit (light through liquid shows color)
- Freeze frame trick: render one frame at peak, hold 1–2s in NLA
```

---

## Structural Templates by Platform

### Instagram Reel / TikTok (9:16, 6–10s)
```
0.0–0.5s: instant hook — most dramatic frame first
0.5–4.0s: core motion/reveal
4.0–6.0s: product hold + brand moment
6.0–8.0s: CTA (text overlay in post)
Resolution: 1080×1920 (9:16)
```

### Instagram Feed (1:1 or 4:5, 3–7s)
```
0.0–1.0s: beauty shot establishing mood
1.0–5.0s: motion/detail
5.0–7.0s: product hero frame
Resolution: 1080×1080 or 1080×1350
```

### YouTube Pre-roll (16:9, 6–30s, must hook in 5s)
```
0–5s: hook (survives skip) — product reveal or dramatic visual
5–15s: storytelling motion
15–30s: product detail + brand
Resolution: 1920×1080 or 3840×2160
```

### Cinema/Large Screen (2.39:1, 10–60s)
```
Widescreen drama, slow pacing acceptable
Highest render quality needed (4K, 1024+ samples)
Color grade critical — calibrated monitor required
```

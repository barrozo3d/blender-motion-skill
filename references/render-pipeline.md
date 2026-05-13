# Render Pipeline

From Blender Cycles to final deliverable, including After Effects compositing.

---

## Cycles Settings for Motion Design

### Quality Presets

| Use | Samples | Denoiser | Time/frame (RTX 4090) |
|-----|---------|----------|-----------------------|
| Quick preview | 64 | OIDN | ~10s |
| Draft | 128 | OIDN | ~30s |
| Test render | 256 | OIDN | ~1min |
| Standard | 512 | OIDN | ~3min |
| High quality | 1024 | OIDN | ~6min |
| Premium (Albin's setting) | 2048 | OIDN | ~6–12min |
| Caustics / volume | 2048+ | None | ~20–30min |

### Recommended Settings (4.5 LTS)
```
Render Engine: Cycles
Device: GPU Compute (CUDA for NVIDIA)
Samples: 512 (preview) → 1024–2048 (final)
Denoiser: OpenImageDenoise (OIDN) — GPU accelerated in 4.5
Denoiser Input: RGB + Albedo + Normal (best quality)

Light Paths:
  Max Bounces: Total 12, Diffuse 4, Glossy 4, Transmission 12
  (High Transmission needed for glass/liquid)
  Caustics: off (save time) unless caustics are the subject

Volume:
  Step Rate: 0.1 (quality) or 1.0 (speed)
  Max Steps: 256
```

### Motion Blur Settings
```
Render Properties → Motion Blur: Enable
Shutter: 0.5 (cinematic standard = 180° shutter equivalent)
Position: Center on Frame
Steps: 1 (fast) to 4 (smooth, complex motion)
Note: motion blur dramatically increases render time
Tip: render without blur, add in compositor for speed
```

### Adaptive Sampling (speeds up flat areas)
```
Enable in: Render Properties → Sampling → Adaptive Sampling
Min Samples: 0 (auto)
Threshold: 0.01 (quality) → 0.05 (speed)
Result: noisy areas get full samples, flat areas stop early
```

---

## Output Settings

### For After Effects workflow
```
Output: OpenEXR Multilayer (32-bit float)
Color Space: Linear
Compression: ZIP (lossless, good balance)
Frame range: render as image sequence (not video file)
Why: if a frame fails, re-render just that frame
```

### For direct delivery
```
Output: PNG (lossless) or JPEG (lossy, smaller)
Color Space: sRGB
Then: assemble in Blender VSE or AE
```

### Render Passes for AE compositing
```
Enable in: View Layer Properties → Passes

Essential:
- Combined (beauty)
- Depth (Z-pass for DOF in AE)

For grading control:
- Diffuse Color + Direct + Indirect
- Specular Direct + Indirect  
- Emit (for separate bloom control)
- Shadow (for relight)

For compositing:
- Normal (for relighting)
- Object Index (for per-object effects)
- Cryptomatte (for clean masking)
```

---

## After Effects Pipeline

### Import EXR Sequence
```
1. Import → .exr sequence → Interpret Footage: 32-bit
2. Set frame rate to match Blender output (typically 24 or 25 fps)
3. EXtractoR or ProEXR plugin: split multi-layer EXR into separate layers
```

### Standard Grade Stack (Albin Merle approach)
```
1. Raw Cycles output (linear)
2. Color Balance: Lift/Gamma/Gain for overall grade
3. Curves: fine-tune contrast and color channel balance
4. Lumetri Color: creative look application
5. Optical Flares or Lens Flare: add lens artifacts
6. Film grain overlay: separate grain pass or grain effect
7. Vignette: dark edges via Ellipse mask + Curves
8. Chromatic Aberration: Channel Blur slight R/G/B offset
9. Composite logo/text/cards: separate tracked layer
```

### Bloom / Glow
```
Option A — Blender Compositor:
  Glare node: Type = Fog Glow, Threshold = 0.8, Size = 8
  Benefit: physically accurate, baked into render

Option B — After Effects:
  Effect → Stylize → Glow
  Threshold: 60–80%, Radius: 20–40
  Benefit: adjustable after render, can be art-directed
  
Albin's approach: Blender compositor for initial glow, refine in AE
```

### Depth of Field in Post (using Z-pass)
```
AE: Camera Lens Blur or Frischluft Lenscare
Z-pass → Depth Map layer → apply to beauty pass
Benefit: re-focus after render without re-rendering
Limitation: edge artifacts on foreground/background separation
```

---

## Render Farm (when local is too slow)

### LeTruc Studio (referenced by Albin Merle)
- French render farm, used for Albin's "Veloce" / frozen motion blur piece
- Handles Cycles rendering

### General render farm requirements
```
1. Pack all external assets: File → External Data → Pack All Into .blend
2. Export .blend file (self-contained)
3. Set frame range and output path in .blend
4. Upload to farm, specify Blender version (match your local version exactly)
5. Download rendered frames
6. Assemble in AE or Blender VSE
```

### Warning: simulations on render farm
```
Bake simulations LOCALLY before sending to farm
Farms cannot run interactive simulations
Pack baked cache files with the .blend:
  File → External Data → Pack All (includes caches)
  OR: use relative paths and zip the entire project folder
```

---

## Final Delivery Specs

| Platform | Codec | Resolution | Frame Rate | Color |
|---|---|---|---|---|
| Instagram/TikTok | H.264 | 1080×1920 | 25/30fps | sRGB |
| YouTube | H.264 or H.265 | 3840×2160 | 25/30fps | sRGB |
| Digital cinema | DCP (via separate tool) | 4096×2160 | 24fps | XYZ |
| Client master | ProRes 4444 | 4K | 25/30fps | sRGB |
| Archive | PNG sequence or EXR | Original | Original | Linear |

### Export from AE
```
Composition → Add to Render Queue
Output Module: H.264 (via Media Encoder) or ProRes
Color: Premultiplied Alpha for transparency
Frame rate: match project
```

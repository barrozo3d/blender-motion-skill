# Lighting, Ambiance & Composition

---

## Lighting Rigs for Motion & Ad Video

### 1. Luxury Dark Studio (most common for brand/ad work)
**Look:** Deep black background, single hard light source, strong specular, rim light separating subject from background.

```
Setup:
- World: pure black (Strength 0)
- Key light: Area light, 1000W–5000W, positioned 45° above and to the side
- Rim light: Area light behind subject, warm color (3200K), 200–500W
- Optional fill: very soft area light opposite key, 50–100W (barely there)
- No HDRI — all manual lights
```
Used by: Albin Merle (Mauviel, Cartier, IWC), luxury watch ads, jewelry.

---

### 2. HDRI + Hero Light
**Look:** Natural ambient from all directions, one dominant directional light for drama.

```
Setup:
- World: HDRI texture (Poly Haven recommended)
  → Rotate HDRI to control ambient direction
  → Strength: 0.3–0.8 (low, fill only)
- Hero light: Sun or Area, high intensity, matches HDRI direction
- Benefit: natural reflections + controlled drama
```
Best for: product renders that need to feel "in a world," outdoor scenes.

---

### 3. Volume Atmosphere
**Look:** Light rays (god rays), depth haze, light visibly scattering through space.

```
Setup:
- Add a large cube around the scene
- Assign Principled Volume shader: Density 0.005–0.05, Anisotropy 0.3–0.6
- Or: World > Volume > Principled Volume (fills entire world)
- Light rays: high-intensity Spot or Sun light + volume scatter
- Cycles only — EEVEE volumetrics work but lower quality
- Samples: 512+ (volume is noisy at low samples)
```
Warning: dramatically increases render time. Use adaptive sampling.

---

### 4. Neon / Emissive Environment
**Look:** Scene lit purely from glowing geometry, no visible light sources.

```
Setup:
- World strength: 0 (black)
- Emission shaders on scene elements (strength 5–50)
- Enable Bloom in: Render Properties > Color Management > Look
  OR compositor Glare node (Fog Glow, threshold 0.8)
- Cycles: enable caustics if emission should cast caustic light
- Color: choose dominant hue for mood (cyan, magenta, amber)
```

---

### 5. Macro / Tabletop
**Look:** Extreme close-up, soft even lighting, minimal shadows.

```
Setup:
- 2–3 area lights, large relative to subject, positioned close
- Softbox approximation: area light with high size value (2m+)
- One light from above (key), one from front-below (fill)
- Diffuse curtain effect: white plane geometry as light blocker/bounce
- Focal length: 100–200mm equivalent
```

---

## Color Temperature Quick Reference (Blender 4.5+)

Use the Temperature parameter (Kelvin) on lights directly:

| Kelvin | Mood | Use |
|--------|------|-----|
| 1800–2400K | Candlelight, fire | Intimate, warm drama |
| 2700–3200K | Warm tungsten | Luxury, comfort, gold |
| 4000K | Neutral white | Studio, clean |
| 5500K | Daylight | Natural, open |
| 6500–7000K | Overcast sky | Cold, clinical, tech |
| 8000–10000K | Blue sky shade | Very cold, futuristic |

**Gold/luxury palette:** Key at 3200K, rim at 2700K → warm golden-hour feel.
**Tech/cold palette:** Key at 6500K, rim at 8000K → cold precision feel.

---

## Shadow Quality Control

| Goal | Setting |
|------|---------|
| Soft shadow edges | Increase light size (area lights) |
| Hard shadow edges | Small light source or Sun light |
| No shadow (fill) | Uncheck "Cast Shadow" on light |
| Colored shadows | Glass/transparent material on shadow caster |
| Contact shadows | Enable in EEVEE, or just use Cycles |

---

## Composition Principles for 3D Motion

### Rule of Thirds in 3D
- Enable camera overlay: View > Overlays > Composition Guides > Thirds
- Place subject eye-line or key feature at a third intersection
- For product reveals: start off-thirds, animate to center for the hold

### Golden Ratio / Spiral
- Enable: Overlays > Composition Guides > Golden Ratio
- Works best for single-hero product shots
- Spiral path suggests camera movement direction

### Central Symmetry (for brand logos and hero products)
- Subject dead center, perfect bilateral symmetry
- Extremely powerful for logos and architectural reveals
- Camera: exactly front or top orthographic for maximum symmetry

### Negative Space (luxury standard)
- Subject occupies 20–30% of frame, rest is black/dark
- Creates breathing room, premium feel
- Common in Albin Merle's work: tiny logo in vast dark space

### Depth Layering
- Foreground element (blurred) + midground subject + background
- Creates cinematic depth without complex scenes
- In Blender: camera DOF + place simple geometry in foreground

---

## Camera Lenses & Their Character

| Focal length (35mm equiv.) | Character | Best for |
|---|---|---|
| 14–20mm | Extreme perspective, dramatic | Architectural, environment |
| 24–35mm | Wide, contextual | Product in environment |
| 50mm | Natural, neutral | Versatile |
| 85–100mm | Flattering compression | Hero product shots |
| 135–200mm | Heavy compression, shallow DOF | Isolated product, macro detail |
| Orthographic | No perspective at all | Technical diagrams, certain motion design |

**Blender camera setup:**
- Sensor Width: 36mm (full-frame equivalent)
- Focal Length: set in mm
- DOF: enable + set focus distance or use Empty as focus target

---

## Cinematic Camera Moves for Motion Design

### Orbit (most common for product)
```
- Place Empty at subject center
- Parent camera to Empty
- Animate Empty's Z rotation
- Ease in/out with bezier handles on f-curve
```

### Push-in / Pull-out
```
- Animate camera location along its local Z axis
- Or: animate focal length (zoom) — different feel than physical move
- Physical move = parallax shift; focal length = compression change
```

### Crane / Arc
```
- Camera paths along Bezier curve
- Path > Object Constraint > Follow Path
- Animate "Offset" for speed control
- Point camera with Track To constraint to subject
```

### Subtle Drift (handheld feel)
```
- Add Noise modifier to camera location f-curves
- Scale: 0.002–0.01 (very subtle)
- Strength: 0.1–0.3
- Rough: 0.7 (irregular, not too regular)
```

---

## Render Settings for Cinematic Look

### Aspect Ratios
| Format | Resolution | Use |
|---|---|---|
| 16:9 | 1920×1080 / 3840×2160 | Standard video, YouTube |
| 9:16 | 1080×1920 | Instagram/TikTok vertical |
| 1:1 | 1080×1080 | Instagram square |
| 2.39:1 | 2560×1072 | Cinematic widescreen |
| 4:5 | 1080×1350 | Instagram portrait |

### Film Grain (Blender Compositor)
```
- Filter > Add Glare: no
- Instead: Render Passes > Diffuse > separate pass
- Add grain as a compositor texture overlay
- Or: Film > Grain in Render Properties (built-in, simple)
```

### Color Science
- Color Management > View Transform: **Filmic** (default, good for most)
- For high-contrast luxury: **AgX** (Blender 3.5+, better highlight rolloff)
- For flat grade: **None** (export raw, grade in AE)
- Exposure: adjust in Color Management (not in lights)

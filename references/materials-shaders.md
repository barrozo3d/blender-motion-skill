# Materials & Shaders

Cycle-ready material recipes for motion design. All use Principled BSDF unless noted.

---

## Metal Recipes

### Polished Gold
```
Base Color: RGB(1.0, 0.76, 0.34) — warm gold
Metallic: 1.0
Roughness: 0.05–0.10
IOR: 0.47 (gold IOR)
Specular Tint: 1.0
Result: mirror-like gold, catches every light
```

### Brushed Gold
```
Base Color: RGB(1.0, 0.76, 0.34)
Metallic: 1.0
Roughness: 0.3–0.4 (anisotropic)
Anisotropic: 0.8
Anisotropic Rotation: 0.0 (adjust for brush direction)
Tangent: driven by UV or geometry tangent
```

### Chrome / Mirror
```
Base Color: RGB(0.9, 0.9, 0.9)
Metallic: 1.0
Roughness: 0.0
Result: perfect mirror reflection
Note: needs interesting environment to look good (HDRI)
```

### Dark Gunmetal
```
Base Color: RGB(0.05, 0.05, 0.06)
Metallic: 1.0
Roughness: 0.3
Result: dark industrial metal
```

### Liquid Mercury
```
Base Color: RGB(0.8, 0.8, 0.85)
Metallic: 1.0
Roughness: 0.0
Coat: 1.0, Coat Roughness: 0.0 (Blender 4.0+)
Result: mirror-like with slight bluish cast
```

---

## Glass & Refractive

### Clear Glass (Thin)
```
Transmission: 1.0
Roughness: 0.0
IOR: 1.45
Thickness: 0 (thin glass approximation)
Enable: Render > Light Paths > Caustics (for accurate caustics)
```

### Thick Glass / Crystal
```
Transmission: 1.0
IOR: 1.52
Roughness: 0.0
Add: Volume Absorption (inside mesh) — color adds glass tint
Samples: 1024+ for clean caustics
```

### Frosted Glass
```
Transmission: 1.0
Roughness: 0.2–0.5 (more = more frosted)
IOR: 1.45
```

### Glass with Color
```
Transmission: 1.0
Base Color: tinted (e.g. amber, green)
IOR: 1.45
Roughness: 0.0–0.1
OR: use Volume Absorption for deeper color effect
```

---

## Liquid Materials

### Water
```
Transmission: 1.0
IOR: 1.333
Roughness: 0.0
Volume Absorption: slight blue tint at density 0.01
```

### Colored Liquid (Ink/Juice)
```
Transmission: 0.8–1.0
Base Color: liquid color
Volume Absorption: heavy (density 0.5–2.0, color matching liquid)
```

### Honey / Thick Liquid
```
Transmission: 0.9
IOR: 1.49
Base Color: amber (1.0, 0.6, 0.1)
Volume Absorption: density 0.2, amber color
Roughness: 0.05
```

---

## Fabric & Organic

### Principled Hair (Blender 3.5+) — for curves/strands
```
Melanin: 0.0–1.0 (0=white/blond, 1=black)
Melanin Redness: 0–1 (warm/cool)
Roughness: 0.1–0.3
Radial Roughness: 0.3
Coat: 0.1 (slight shine)
Use for: hair, fiber, knitted texture, fine cables
```

### Velvet / Fabric
```
Sheen: 1.0
Sheen Roughness: 0.3
Base Color: fabric color
Roughness: 0.8
Metallic: 0
```

### Skin (for motion design characters)
```
Subsurface: 0.3–0.8
Subsurface Radius: (1.0, 0.2, 0.1) — red scatters more
Base Color: skin tone
Roughness: 0.5
Specular: 0.3
```

---

## Volume & Atmosphere

### Smoke / Gas
```
Shader: Principled Volume
Density: driven by "density" attribute (from smoke sim)
Color: driven by "flame" for fire, or set manually
Scatter Color: light gray for neutral smoke, warm for dusty
Anisotropy: 0.0 (neutral) to 0.5 (forward scatter)
```

### Gold Dust Particle Material
```
Base Color: RGB(1.0, 0.78, 0.28)
Metallic: 1.0
Roughness: 0.1
Apply to: tiny UV sphere instances
Tip: add slight Base Color variation per instance using Random per Island + Color Ramp
```

### Emissive / Neon
```
Shader: Emission
Color: neon color (cyan, magenta, etc.)
Strength: 5–50 (high enough to cause bloom)
Mix with Diffuse using Mix Shader for surface detail
Enable Bloom in: Properties > Render > Color Management
```

---

## Procedural Textures (No UV needed)

### Procedural Noise (Organic variation)
```
Texture Coordinates → Object
Noise Texture: Scale 3–10, Detail 6, Roughness 0.6
Color Ramp: map to material parameter
Use for: roughness variation, subtle color shift, displacement
```

### Procedural Wood Grain
```
Wave Texture (Bands, Rings) → Color Ramp → Base Color
Scale: 5, Distortion: 1.5, Detail: 4
Add Noise to distort waves for natural grain
```

### Procedural Metal Scratches
```
Voronoi Texture (F1, Distance to Edge) → Color Ramp (thin bright lines)
Mix with main metallic material: Factor 0.0–0.1 (subtle)
Scale: 50–200 for fine scratches
```

---

## Compositor Integration (Material Passes)

For maximum grading control in After Effects:
```
Render Properties → Passes:
- Combined (beauty pass)
- Diffuse Color + Diffuse Light
- Specular Light (for separate highlight grading)
- Emit (separate bloom control in AE)
- Shadow Catcher (for compositing on backgrounds)
- Depth (Z pass for DOF in AE)

Output: OpenEXR Multilayer
In AE: EXtractoR or ProEXR plugin to split passes
```

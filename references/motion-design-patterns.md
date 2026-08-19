---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Motion Design Patterns

Core animation patterns for 3D motion design. Each includes timing, easing, and Blender implementation.

---

## Reveal Patterns

### Logo Draw-On
```
Technique: Trim Curve animated 0→1
Timing: 1–3 seconds, ease-in at start, hold at end
Blender: Curve → GeoNodes → Trim Curve → animate End value
Easing: Bezier handle on f-curve, slow start, fast mid, slight ease end
Variation: add Curve to Mesh for thickness, taper at tip
```

### Particle Assemble (particles fly in to form shape)
```
Technique: Simulation Zone — points start scattered, converge to target
Timing: 1–2s convergence, 0.5s hold
Blender: GeoNodes sim: lerp position toward target (Mix node)
Easing: use smoothstep for natural deceleration
Variation: spiral path to target instead of straight line
```

### Dust/Sand Reveal
```
Technique: particles scatter away → logo underneath revealed
Timing: 0.5s fast scatter (force field burst), hold on clean logo
Blender: Force Field → Vortex, strength spike then zero
Or: Simulation Zone → random velocity outward from center, gravity pulls down
```

### Material Transition (liquid metal / glass morph)
```
Technique: Mix Shader between two materials, animated Factor
Timing: 1–2s, ease in/out
Blender: Two shaders → Mix Shader → Factor driven by f-curve
Variation: use noise texture animated W to create organic front edge
```

### Wireframe to Solid Reveal
```
Technique: mix between wireframe and solid geometry
Timing: 1.5s
Blender: 
  Option A: GeoNodes Wireframe node → Mix with Solid, lerp over time
  Option B: Shrinkwrap modifier animated from wireframe position to solid
```

---

## Loop Patterns

### Seamless Rotation Loop
```
Technique: animate rotation, use NLA editor to set cycle
Blender:
  - Animate one full 360° rotation over N frames
  - F-curve modifier → Cycles → Repeat with Offset
  - OR: Extrapolation → Linear for continuous spin
Tip: start and end on same frame for perfect loop
```

### Noise/Organic Drift Loop
```
Technique: Noise modifier on position, with phase offset for seamless loop
Blender:
  - F-curve Modifier → Noise → Scale = loop_length, Strength = drift amount
  - Phase: ensure end value = start value (tune with offset)
  - W input of Noise Texture: animate from 0 to 1, then loop
```

### Particle Loop
```
Technique: particles with matching start/end state
Blender:
  - Particle system: Lifetime = total_frames, emit continuously
  - OR: GeoNodes sim — reset particle state at frame 0 and loop_frame
  - Trick: render 2× the loop duration, use middle portion
```

---

## Transformation Patterns

### Morph Between Two Shapes
```
Technique: Shape Keys
Blender:
  - Model shape A (Basis shape key)
  - Model shape B (second shape key)
  - Animate Value from 0→1 with ease in/out
  - Works with GeoNodes: interpolate between two position sets
```

### Twist / Spiral Warp
```
Technique: Simple Deform modifier → Twist
Blender:
  - Add Simple Deform: Twist, animate Angle from 0 → 720°
  - Axis: Z for vertical twist
  - Limits: control which part deforms
```

### Scale Reveal (pop)
```
Technique: animate scale from 0 → overshoot → settle
Timing: fast (0.2s), with overshoot (+10%) then settle
Blender: 3 keyframes — 0.0, 1.1, 1.0 — bezier handles
Classic motion design: "squash and stretch" easing
```

### Elastic/Bounce
```
Technique: custom easing via f-curve shape
Blender: use Graph Editor, manually shape bezier for bounce
Or: use Elastic modifier on f-curve (built-in)
Physics alternative: Soft Body → Goal = 1.0 for rigid elastic behavior
```

---

## Camera Motion Patterns

### Cinematic Push-In (hero moment)
```
Timing: 2–4 seconds, very slow, ease-in only
Blender: keyframe camera Z (local), very slow start → stop exactly on subject
Focal length: keep constant (physical move, not zoom)
Add: slight noise drift for handheld feel
```

### Orbital Reveal
```
Timing: 3–8 seconds, 90°–360° rotation
Blender: Empty at origin → camera parented → animate Empty Y rotation
Ease: start slow, constant mid, slow end
Combine: slight vertical arc (animate camera Z or parent Z)
```

### Whip Pan Transition
```
Timing: 2–6 frames (very fast)
Blender: extreme rotation keyframe between two shots
Compositor: Directional Blur on the fast frames
Or: motion blur at high shutter angle (180°+)
```

### Dutch Tilt Intro
```
Technique: camera rotated ~10–15° on Z axis
Normalize at: camera rotates back to 0 during scene settle
Blender: animate camera Z rotation from 12° → 0°
```

---

## Timing Reference for Ad/Brand Video

| Segment | Duration | Note |
|---|---|---|
| Hook / first impression | 0–1s | Must land before skip |
| Main reveal | 1–3s | Core visual impact |
| Detail / texture hold | 3–5s | Let material quality read |
| Logo/brand reveal | 5–7s | Payoff moment |
| Call to action | 7–10s | Text overlay in post |
| Total short ad | 6–10s | Instagram/TikTok standard |
| Total long ad | 15–30s | YouTube pre-roll |

### Albin Merle timing patterns (from analysis)
- Most pieces: 10–88 seconds, often matching audio beat precisely
- Short experiments: 10–30s, single technique showcase
- Branded work: 25–60s, narrative arc with reveal payoff
- Loops: 10–15s, designed for social media repeat viewing

---

## Audio Sync Techniques

### Beat-Matched Animation
```
1. Import audio into Blender Video Sequence Editor
2. Play timeline with audio: identify beat times
3. Place keyframes on exact beat frames
4. Use Snap to Frame: ensure keyframes land on beat
5. Blender: Timeline > Sync > AV Sync (keeps audio/video locked)
```

### Reactive Animation (audio-driven)
```
1. Bake sound to f-curve: Graph Editor → Key → Bake Sound to F-Curves
2. Select audio file, frequency range for the parameter to react to
3. Result: f-curve that follows audio amplitude
4. Apply to: scale, position, emission strength, material factor
```

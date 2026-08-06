---
title: Daily Blender Tip 90 - How To Have Characters Interact With Physics Simulations
source: YouTube
url: https://www.youtube.com/watch?v=RXTJshRSyjk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Rigid Body physics (Active/Passive/Animated) and bone-parenting are version-agnostic core Blender features"
tags: [rigging, character, simulation, rigid-body, advanced]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 90 - How To Have Characters Interact With Physics Simulations

**Source:** [YouTube](https://www.youtube.com/watch?v=RXTJshRSyjk)
**Author:** Blender Secrets
**Duration:** 1m54s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'SIMPLE CHARACTER PHYSICS INTERACTION'
- **CRITICAL:** Empty transcript in chapter 'Do the same for the parts of the body that will interact the most with the physics simulation of the wall.'
- **CRITICAL:** Total transcript only 1 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (1 chars) in 'They also need to be set as "animated" Rigid body objects. Otherwise they won't move.'

---


Frames captured — see "Captured Frames" section below.


### SIMPLE CHARACTER PHYSICS INTERACTION [0:00]

### Do the same for the parts of the body that will interact the most with the physics simulation of the wall. [0:34]

### They also need to be set as "animated" Rigid body objects. Otherwise they won't move. [1:30]
**Transcript (timestamped):**
[1:30] .



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_001.jpg
- [0:55] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_002.jpg
- [1:20] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_003.jpg
- [1:40] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_004.jpg
- [1:52] tutorials/frames/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 7 (final) of the rigging series: since a rigged/animated character's armature/bones cannot directly drive a Rigid Body physics simulation, this workaround adds simple primitive proxies (icospheres) parented to key bones (e.g. the head, or limbs that need to interact with a simulation), sets those proxies as **Active Rigid Body** objects with the **Animated** flag enabled — letting a keyframed/animated character physically knock through a Rigid Body wall simulation.

### Summary
Frame 000 shows the character walking through and shattering a brick wall (pink/red fractured chunks flying), captioned "Normally, a rigged character, armature or bones won't interact in a physics simulation." — establishing the core problem this tip solves. Frame 001 shows an icosphere primitive positioned exactly at the character's head, parented in Pose Mode to the head bone, captioned "Add a primitive like an icosphere at the location of the head bones, parent it (in pose mode) to the bone." Frame 002 shows the character's skeleton with green icospheres now also placed at multiple limb/joint locations (shoulders, chest, legs), the destructible wall visible in the background, captioned "The wall consists of cubes set to Active physics objects and the ground is a Passive physics object." Frame 003 shows just the icospheres (character mesh hidden) — a cluster of proxy spheres matching the character's pose, captioned "Hide the character mesh and select the icospheres, make them Active physics objects." Frame 004 shows the Physics Properties Rigid Body panel with **Animated** checked (Dynamic, Type: Active, and other settings visible), captioned "They also need to be set as 'animated' Rigid body objects. Otherwise they won't move." — without the Animated flag, a Rigid Body object ignores its own keyframes/parent-driven motion and would otherwise just fall passively. Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Recognize the core limitation: a character's **armature/bones** cannot themselves be assigned Rigid Body physics, so they cannot directly collide with or influence a Rigid Body simulation (e.g. a shattering brick wall).
2. Add simple primitive objects (**icospheres** work well) at the locations of key bones that need to physically interact with the simulation — e.g. the head, hands, or torso.
3. In **Pose Mode**, parent each icosphere to its corresponding bone (Ctrl+P > Bone) so it follows that bone's animated movement exactly.
4. Set up the destructible simulation normally: the wall's individual pieces as **Active** Rigid Body objects, the ground as a **Passive** Rigid Body object.
5. Hide the character mesh (to simplify selection) and select all the icosphere proxies; set them as **Active** Rigid Body objects too.
6. Critically, enable the **Animated** checkbox on each icosphere's Rigid Body settings — this tells the physics engine to respect the object's own keyframed/parented motion (following the bone) rather than letting gravity/passive physics override it. Without this flag, the proxies would simply fall instead of tracking the character's movement.
7. Result: the invisible icosphere proxies, driven by the character's bone animation, physically collide with and knock apart the Rigid Body wall as the character walks through it.

### Nodes / Settings
- **Proxy objects:** Icosphere (or similar simple primitive) parented to bones (Ctrl+P > Bone, in Pose Mode).
- **Physics > Rigid Body:** Active (proxies and wall pieces), Passive (ground); **Animated** flag enabled on the bone-driven proxies specifically.

### Difficulty
Advanced

### Blender Version
Not specified — Rigid Body physics (Active/Passive/Animated) and bone-parenting are version-agnostic core Blender features.

### Tags
rigging, character, simulation, rigid-body, advanced

---

## Related Tutorials
- [Daily Blender Tip 89 - Riggin With Seperate Objects Or Not?](daily-blender-tip-89---riggin-with-seperate-objects-or-not.md) — shares rigging, character; this is the final Part 7 of the same 7-part character rigging series (Tips 84–90), covering physics-simulation interaction via bone-parented Animated Rigid Body proxies.
- [Daily Blender Tip 75 - More Fracture Stuff!](daily-blender-tip-75---more-fracture-stuff.md) — shares rigid-body, simulation; provides the Cell Fracture + Rigid Body wall-shattering setup this tutorial's character interacts with.

# Knowledge Gap To-Do List

Generated 2026-08-20 from a library-wide gap analysis (313 ingested tutorials
checked against `SKILL.md` scope + all `references/*.md`). Every gap below was
**measured** — each line records how many tutorial files actually mention the
topic — not guessed. Ingest with `python ingest.py "[URL]"` from this directory,
then run the mandatory extraction pass (see `SKILL.md` Mode 3).

> **How the counts were taken.** Case-insensitive regex over all 313 tutorial
> files (not `INDEX.md`, which counts tags rather than content), then every thin
> result hand-checked by listing the matching files. That second step changed
> two numbers: a search for "python" matched **10** files, but whole-word `\bbpy\b`
> matches **2**; "motion track|camera track" matched **6**, but five are passing
> mentions inside other tutorials and only **1** is a dedicated tracking
> tutorial. *Suspect the instrument before the data.*

**This library is broad and deep.** Geometry nodes 99, shaders/materials 221,
lighting/HDRI 107, Cycles 106, cameras 138, add-ons 161, rigging 67, particles
54. The gaps below are the narrow bands where an **ad/brand production** workflow
— this skill's stated focus — runs out of coverage.

## Pending

### 1. Python / `bpy` scripting — **2 tutorials**

Whole-word `\bbpy\b` matches **2 of 313**
(`blender-secrets---long-version-marvelous-designer-like-cloth-grabbing.md`,
`frozen-motion-blur-bridge-geo-nodes-breakdown.md`), and in both it is incidental
rather than the subject. For a library this size aimed at repeatable client work,
scripting and automation are effectively uncovered.

- [ ] **bpy fundamentals for motion design** — the scripting workspace, operators
      vs data API, driving object/material properties from script
- [ ] **Batch automation** — scripting variant renders (colourways, aspect
      ratios, logo swaps) across a shot, which is the recurring ad-work task

### 2. Camera / motion tracking — **1 dedicated tutorial**

Only `camera-tracking-in-blender-for-beginners-motion-tracking-tutorial.md`
covers it directly; the other five hits are passing mentions. Putting a product
or 3D element into live footage is core ad/brand work, and this is the thinnest
part of it.

- [ ] **Production camera solve** — solve error, refining intrinsics, lens
      distortion, setting scene scale and floor
- [ ] **Object tracking** (not just camera) — tracking a moving product/hand so
      3D can be parented to it

### 3. Non-linear animation (NLA) — **6 mentions, no dedicated tutorial**

`\bnla\b` appears inside broader animation courses (walk cycle, follow-path,
graph editor, mocap) but nothing teaches the NLA editor itself. NLA is how
motion-design work gets re-timed and re-used across cuts.

- [ ] **NLA editor workflow** — actions as strips, blending/influence, looping a
      cycle, re-timing without destroying keys

### 4. Delivery: batch / command-line rendering — **2 tutorials**

`render farm|command.?line render` matches **2 of 313**. An ad deliverable is
usually many renders (aspect ratios, cutdowns, versions); nothing covers driving
that from outside the UI.

- [ ] **Command-line rendering** — `blender -b -f/-a`, overriding output paths
      and formats per version, and rendering a range on another machine

### 5. Interchange: USD / Alembic / FBX — **12 tutorials**

Light for pipeline work (`\busd\b|alembic|\bfbx\b` = 12). Relevant when a brand
job has to hand geometry/caches to another tool or vendor.

- [ ] **Alembic / USD caching out of Blender** — what survives the round trip
      (shading, instancing, geo nodes) and what does not

### 6. OSL — **1 tutorial** (low priority)

`\bosl\b|open shading` matches 1. Niche and Cycles-CPU-only; listed for
completeness. Ingest only if a genuinely motion-design-relevant source appears —
**do not manufacture coverage.**

## Notes on what is NOT a gap

Measured and healthy, recorded so nobody "fills" a gap that does not exist:

| Topic | Files (of 313) |
|---|---|
| Shaders / materials | 221 |
| Add-ons | 161 |
| Cameras / shots | 138 |
| Lighting / HDRI | 107 |
| Cycles | 106 |
| Geometry nodes | 99 |
| Hair / curves | 92 |
| Text / typography | 91 |
| Rigging / armatures | 67 |
| Compositor | 65 |
| EEVEE | 55 |
| Particles | 54 |
| Drivers / constraints | 54 |
| Cloth / soft body | 44 |
| Logo / brand work | 41 |
| Smoke / fire | 37 |
| NPR / toon / stylized | 37 |
| Colour management (AgX/Filmic/ACES) | 27 |
| Grease Pencil | 26 |
| Fluid / Mantaflow | 26 |
| Rigid body | 19 |
| Simulation nodes/zones | 17 |

## Completed

(none yet — this list was created 2026-08-20 and nothing on it has been ingested)

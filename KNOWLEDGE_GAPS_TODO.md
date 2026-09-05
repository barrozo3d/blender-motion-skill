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

### 1. ✅ Python / `bpy` scripting — **CLOSED 2026-09-04** — **5 tutorials** (was 2)

The 2 previous hits were incidental mentions inside other tutorials. Two pages
from the official API docs make scripting a subject rather than a side effect.

- [x] **bpy fundamentals for motion design** — the scripting workspace, operators
      vs data API, driving object/material properties from script
      ✅ `python-api-quickstart.md` — `bpy.data` vs `bpy.ops` vs `bpy.context`;
      **data-blocks cannot be created by calling the class** (`bpy.types.Mesh()`
      raises by design — create through the collection); **`bpy.context` is
      read-only** and its members change with the area it is read from; custom
      properties on any ID (basic types, 1024-level nesting limit, animatable and
      driver-usable); operator `poll()` gating; the Operator Cheat Sheet; and
      Developer Extras + Python Tooltips so every button reveals its attribute.
      ✅ `python-api-overview.md` — the embedded interpreter, **executing a script
      vs importing it as a module** (and the advice not to directly execute
      scripts that register classes), the six `bpy.types` base classes available
      for integration, `bpy.utils.register_class`, `scripts/startup/`, and
      add-ons as extensions with `blender_manifest.toml`.
- [x] **Batch automation** — scripting variant renders (colourways, aspect
      ratios, logo swaps) across a shot
      ✅ Covered jointly by `command-line-arguments.md` (the `-o` path templating
      with `#` padding and `{blend_name}`, `-F` format override, `-E` engine, `-s`
      / `-e` / `-j`, and Cycles options after `--`) and `python-api-overview.md`
      (`--python`, and running a registered tool headless). ⚠️ **What is
      documented is the mechanism, not a worked variant-render script** — the two
      pages give every piece; nobody's example assembles them for an ad
      deliverable. Left as a tick because the gap asked for coverage of the
      capability, and manufacturing a tutorial would be inventing a source.

### 2. ✅ Camera / motion tracking — **CLOSED 2026-09-04** — **13 tutorials** (was 6, only 1 dedicated)

- [x] **Production camera solve** — solve error, refining intrinsics, lens
      distortion, setting scene scale and floor
      ✅ `tracking-camera-panel.md` — Sensor Width, Pixel Aspect (and how to
      derive it), Focal Length, Optical Center; the four distortion models
      (**Polynomial**, **Division** for fisheye, **Nuke** matching the Nuke
      compositor, **Brown-Conrady** with radial *and* tangential); positive =
      barrel, negative = pincushion, mixed = moustache; and the warning that
      **camera presets exclude distortion coefficients and the principal point**.
      ✅ `solving-camera-motion.md` — **Refine** (Focal Length, Optical Center,
      Radial, Tangential — needing approximate initial values), **Cleanup** by
      minimum Frames and maximum reprojection **Error** with Select / Delete
      Track / Delete Segments, and the **Orientation** tools: Floor, Wall, Set
      Origin, Set X/Y Axis, Set Scale, Apply Scale with Distance in scene units.
      Plus the Tripod solver caveat — **more tracks do not help; 5–10 per frame**.
      ✅ `editing-motion-tracks.md` — the 2D pass, the different failure behaviour
      of sequence vs frame-by-frame tracking, the directionally counterintuitive
      Clear Before/After, and **Refine** for occlusion recovery.
      ✅ `motion-tracking-introduction.md` — and the honest part: **there is no
      built-in lens calibration tool**; the documented routes are Annotation
      poly-line matching inside Blender, or OpenCV grid calibration, which uses
      the same distortion model.
- [x] **Object tracking** (not just camera) — tracking a moving product/hand so
      3D can be parented to it
      ✅ `object-solver-constraint.md` — register the object in the Objects Panel,
      track **at least eight markers**, Solve Camera/Object Motion, add the
      constraint, **Set Inverse**; the Camera field and when it needs its own
      Camera Solver Constraint; and the strict re-tweak order (Apply Visual
      Transform → disable → adjust → Set Inverse → enable).

### 3. ✅ Non-linear animation (NLA) — **CLOSED 2026-09-04** — **8** (was 6 mentions, no dedicated page)

- [x] **NLA editor workflow** — actions as strips, blending/influence, looping a
      cycle, re-timing without destroying keys
      ✅ `nla-editor-introduction.md` — actions as reusable segments, tracks
      layering higher-over-lower with blending, the **Action Track** and why other
      editors show only the active action, **Tweak Mode** (`Tab`), Show Control
      F-Curves for Animated Influence, and the preview-range operators.
      ✅ `nla-tracks.md` — Mute / Lock / Solo, Disable NLA stack, and **Push Down
      Action** as the loop that builds layered animation; **Pin** for viewing
      keyframes at original vs strip-scaled time points, which is precisely
      "re-timing without destroying keys".

### 4. ✅ Delivery: batch / command-line rendering — **CLOSED 2026-09-04** — **4** (was 2)

- [x] **Command-line rendering** — `blender -b -f/-a`, overriding output paths
      and formats per version, and rendering a range on another machine
      ✅ `rendering-from-the-command-line.md` — the worked invocations plus the
      two rules that silently produce wrong results: **arguments execute in the
      order given** (so `-f`/`-a` must be last) and **arguments are case
      sensitive** (`-F` ≠ `-f`). No display needed, so it runs over SSH.
      ✅ `command-line-arguments.md` — the full reference: `-o` with `//`,
      `#` padding, `{blend_name}` templating and the automatic `####` when no `#`
      is present; `-F` format override; `-E`/`-t`/`-s`/`-e`/`-j`/`-S`; and Cycles
      options after `--`.

### 5. ✅ Interchange: USD / Alembic / FBX — **CLOSED 2026-09-04** — **14** (was 12)

- [x] **Alembic / USD caching out of Blender** — what survives the round trip
      (shading, instancing, geo nodes) and what does not
      ✅ `alembic-import-and-export.md` — the contract stated outright: Alembic
      stores the **computed result** (vertex positions, transforms) and
      deliberately **not** the rig or dependency graph. Automatic **Mesh Sequence
      Cache** modifiers and **Transform Cache Constraint** on import; **Validate
      Meshes** recommended because corrupt data can crash display or editing and
      is not always visible; **Is Sequence**, **Set Frame Range**, **Always Add
      Cache Reader**; Scale 1.0 on export for Blender units.
      ✅ `universal-scene-description-usd.md` — the USD option groups both ways,
      Coordinate System Orientation on import, and the **Exporter Limitations**
      and **USD Primvar data types** sections that say what does not survive.
      ⚠️ **That entry is a map of the option groups, not a per-option reference**,
      and says so in the file — the page is deep and the entry summarises it.

> ⚙️ **Ingest notes for docs.blender.org (reusable).** Both doc sets append
> chrome to `<title>` — " - Blender 5.2 LTS Manual" and " - Blender Python API"
> — so **`--title` is required**. Pin the **versioned** path
> (`/manual/en/5.2/`, `/api/5.2/`) rather than `latest`, so the entry keeps
> describing the version it was read from. Section landing pages are near-empty
> (`ug/node_graph.html`-style stubs, 400–1,200 chars) — measure with
> `fetch_article()` first. The tracking sub-pages are **not** reachable from
> `movie_clip/tracking/index.html`; they are listed on `movie_clip/index.html`.
>
> ✅ **Blender 5.2.1 LTS is installed here** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25) — found by checking rather than assuming, on the day two
> "not installed" claims proved false elsewhere. `blender --help` therefore gives
> the exact CLI reference for the real build, and the manual's own version line
> matches it.

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

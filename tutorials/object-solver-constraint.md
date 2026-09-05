---
title: Object Solver Constraint
source: Article
url: https://docs.blender.org/manual/en/5.2/animation/constraints/motion_tracking/object_solver.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [tracking, object-tracking, animation, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/object-solver-constraint/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Object Solver Constraint

**Source:** [Article](https://docs.blender.org/manual/en/5.2/animation/constraints/motion_tracking/object_solver.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Object Solver Constraint ¶ The Object Solver constraint makes a Blender object imitate the motion of a real-world object. Usage ¶ Start by loading a video file into the Movie Clip Editor , registering the physical object in the Objects Panel , and using motion tracking to track at least eight markers on that physical object. Then use Solve Camera/Object Motion to reconstruct the motion of the physical object, and finally add this constraint to a Blender object. Options ¶ Object Solver constraint. ¶ Active Clip Whether the physical object is in the scene’s Active Clip . If unchecked, a selector appears for choosing another clip. Object The physical object whose motion to imitate. See the Objects Panel in the Movie Clip Editor’s Sidebar for setting this up. Camera The Blender camera matching the physical camera that recorded the object. If left empty, the scene’s active camera is used. If the physical camera was in motion, the Blender camera should have a Camera Solver Constraint . This constraint is useful even if the physical camera was stationary, because it makes the tracking markers appear at their reconstructed world positions in the 3D Viewport (if the Motion Tracking overlay is enabled). Set Inverse Tell the constraint that the current Location of the Blender object (that is, its position with the constraint disabled ) is the correct position for the current frame. Once this information is saved, the object will also be in the correct position for the other frames. When initially adding the constraint: Bring the object into position for the current frame. Add the constraint. Click Set Inverse . When tweaking the object’s position at a later point: Run Apply Visual Transform . (This may move the object to a different position.) Disable the constraint. (This will bring the object back to its previous position.) Tweak the object’s position as desired. Click Set Inverse . Enable the constraint. Clear Inverse Resets the relative transformation that was stored by Set Inverse . Constraint to F-Curve Replaces the constraint by a set of equivalent keyframes. Influence How strongly the constraint affects its owner. On this page Object Solver Constraint Usage Options



---

## Structured Notes

### Core Technique
Make a Blender object imitate a tracked real-world object: track **at least eight markers** on it, solve its motion, then bind a Blender object with the **Object Solver** constraint and press **Set Inverse**.

### Summary
This closes the "object tracking, not just camera" bullet. The workflow is specific and the numbers matter: register the physical object in the **Objects Panel** of the Movie Clip Editor's sidebar, track **at least eight markers** on it, run **Solve Camera/Object Motion**, then add the constraint. The **Camera** field should point at the Blender camera matching the physical one — and if that camera moved, it needs its own **Camera Solver Constraint**. The page makes a point that is easy to miss: the constraint is **useful even when the physical camera was stationary**, because it places the tracking markers at their reconstructed world positions in the 3D Viewport when the Motion Tracking overlay is on. **Set Inverse** is the operation everything hinges on — it tells the constraint that the object's current location (its position with the constraint *disabled*) is correct for the current frame, after which the other frames follow. Re-tweaking later has a strict order the page spells out: **Apply Visual Transform**, disable the constraint, adjust, **Set Inverse**, re-enable.

### Key Steps
1. Load the footage into the **Movie Clip Editor**.
2. Register the physical object in the **Objects Panel** (Movie Clip Editor sidebar).
3. Track **at least eight markers** on that physical object.
4. Run **Solve Camera/Object Motion** to reconstruct its motion.
5. Add the **Object Solver** constraint to the Blender object that should imitate it.
6. Set **Active Clip** (or pick another clip with the selector that appears) and choose the **Object**.
7. Set **Camera** to the Blender camera matching the physical one — leave empty for the scene's active camera. ⚠️ If the physical camera moved, that Blender camera needs a **Camera Solver Constraint** of its own.
8. Bring the object into position for the current frame, then click **Set Inverse**.
9. To adjust later, follow the order exactly: **Apply Visual Transform** → disable the constraint (the object returns to its previous position) → tweak → **Set Inverse** → re-enable.
10. Use **Clear Inverse** to reset the stored relative transform, **Constraint to F-Curve** to bake the constraint into keyframes, and **Influence** to scale its effect.

### Nodes / Settings
- **Object Solver constraint** — **Active Clip**, **Object**, **Camera**, **Set Inverse**, **Clear Inverse**, **Constraint to F-Curve**, **Influence**.
- Prerequisites: **Objects Panel** registration, **≥ 8 tracked markers**, **Solve Camera/Object Motion**.
- Companion: **Camera Solver Constraint** for a moving physical camera.
- Bonus behaviour: with a stationary camera it still places markers at reconstructed world positions when the **Motion Tracking overlay** is enabled.

### Difficulty
Intermediate

### Blender Version
Blender 5.2.

### Tags
`tracking`, `object-tracking`, `animation`, `blender-5x`, `intermediate`

---

## Related Tutorials
- [Solving Camera Motion](solving-camera-motion.md) — the solve this constraint consumes.
- [Motion Tracking Introduction](motion-tracking-introduction.md) — object versus camera solving in context.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.

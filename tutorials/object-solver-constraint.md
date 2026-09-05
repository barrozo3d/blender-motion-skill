---
title: Object Solver Constraint
source: Article
url: https://docs.blender.org/manual/en/5.2/animation/constraints/motion_tracking/object_solver.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
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
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

---
title: Rendering From The Command Line
source: Article
url: https://docs.blender.org/manual/en/5.2/advanced/command_line/render.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [command-line, rendering, pipeline, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/rendering-from-the-command-line/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Rendering From The Command Line

**Source:** [Article](https://docs.blender.org/manual/en/5.2/advanced/command_line/render.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Rendering From The Command Line ¶ In some situations we want to increase the render speed, access Blender remotely to render something or build scripts that use the command line. One advantage of using the command line is that we do not need a graphical display (no need for X server on Linux for example) and consequently we can render via a remote shell (typically SSH). See Command Line Arguments for a full list of arguments (for example to specify which scene to render, the end frame number, etc.), or simply run: blender --help See Command Line Launching for specific instructions on launching Blender from the command line. Note Arguments are executed in the order they are given! The following command will not work, since the output and extension are set after Blender is told to render: blender -b file.blend -a -x 1 -o //render The following command will behave as expected: blender -b file.blend -x 1 -o //render -a Always position -f or -a as the last arguments. Single Image ¶ blender -b file.blend -f 10 -b Render in the background (without UI). file.blend Path to the blend-file to render. -f 10 Render only the 10th frame. blender -b file.blend -o /project/renders/frame_##### -F OPEN_EXR -f -2 -o /project/renders/frame_##### Path of where to save the rendered image, using five padded zeros for the frame number. -F OPEN_EXR Override the image format specified in the blend-file and save to an OpenEXR image. -f -2 Render only the second last frame. Warning Arguments are case sensitive! -F and -f are not the same. Animation ¶ blender -b file.blend -a -a Render the whole animation using all the settings saved in the blend-file. blender -b file.blend -E CYCLES -s 10 -e 500 -t 2 -a -E CYCLES Use the “Cycles Render” engine. For a list of available render engines, run blender -E help . -s 10 -e 500 Set the start frame to 10 and the end frame to 500 . -t 2 Use only two threads. Cycles ¶ In addition to the options above, which apply to all render engines, Cycles has additional options to further control its behavior. See Cycles Render Options On this page Rendering From The Command Line Single Image Animation Cycles



---

## Structured Notes

### Core Technique
Render without a GUI — `blender -b file.blend ... -a` — with the two rules that decide whether it works: **arguments execute in the order given**, and **they are case sensitive**.

### Summary
Short, and it earns its place entirely on two gotchas that silently produce the wrong result. **Order matters**: `blender -b file.blend -a -x 1 -o //render` does *not* work, because output and extension are set *after* Blender has been told to render — `-f` and `-a` must come **last**. **Case matters**: `-F` (render format) and `-f` (render frame) are different arguments, and confusing them is a quiet failure rather than an error. Beyond that it gives the canonical invocations: a single frame with `-f 10`; a frame written to a padded path in a chosen format with `-o /project/renders/frame_##### -F OPEN_EXR -f -2` (where `-2` means the second-*last* frame); a whole animation with `-a` using the blend-file's own settings; and a bounded render on a chosen engine and thread count with `-E CYCLES -s 10 -e 500 -t 2 -a`. The framing is the pipeline argument for doing it this way at all: no graphical display is needed (no X server on Linux), so the render can run over SSH.

### Key Steps
1. Render in the background with **`-b`** — no display required, so it runs over a remote shell.
2. ⚠️ **Put `-f` or `-a` last.** Arguments execute in order, so anything set after them is set too late.
3. ⚠️ **Watch case** — `-F` is the format, `-f` is the frame.
4. Single frame: `blender -b file.blend -f 10`.
5. Single frame, explicit path and format: `blender -b file.blend -o /project/renders/frame_##### -F OPEN_EXR -f -2` — five `#` give five-digit padding, `-2` is the second-last frame.
6. Whole animation on the file's own settings: `blender -b file.blend -a`.
7. Bounded animation with engine and threads: `blender -b file.blend -E CYCLES -s 10 -e 500 -t 2 -a`; `blender -E help` lists engines.
8. Reach for the full argument list with `blender --help` or the Command Line Arguments page; Cycles-specific options live in Cycles Render Options.

### Nodes / Settings
- `-b` background; `-a` animation; `-f <frame>` single frame (negative = relative to the end); `-s` / `-e` start and end; `-t` threads; `-E` engine (`-E help`); `-o` output path with `#` padding; `-F` format override (e.g. `OPEN_EXR`); `-x 1` add extension.
- Rules: **arguments execute in order** (`-f`/`-a` last), **arguments are case sensitive** (`-F` ≠ `-f`).
- Motivation: no graphical display needed — renders over SSH.

### Difficulty
Intermediate

### Blender Version
Blender 5.2.

### Tags
`command-line`, `rendering`, `pipeline`, `blender-5x`, `intermediate`

---

## Related Tutorials
- [Command Line Arguments](command-line-arguments.md) — every argument these examples draw on.
- [Python API Overview](python-api-overview.md) — `--python` for variant logic the command line cannot express.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.

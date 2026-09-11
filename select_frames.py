"""
select_frames.py — Content-aware frame capture (Step 2 of the pipeline).

ingest.py (Step 1) no longer picks frame timestamps itself — it deliberately
makes no API calls, so it can't judge *which* moments in a tutorial are worth
a still. Instead it saves a per-sentence timestamped transcript and defers
frame capture here.

Workflow:
  1. Run `python ingest.py <url>` — collects transcript, no video/frames yet.
  2. Read the timestamped transcript in tutorials/<slug>.md ("## Raw Data").
     Pick moments that actually show a technique/result worth a still — not
     blind percentages of the runtime. Do this even for chapters with official
     titles: verify the real moment against the chapter's own timestamps
     instead of trusting `chapter_start + 5s`.
  3. Run this script with those timestamps:
       python select_frames.py <slug> 10 60 4:20 8:05 ...
     (accepts plain seconds or mm:ss, mixed freely)
  4. Write the Structured Notes section using the transcript + captured frames.

This reuses ingest.py's download_video_low()/extract_frames() unchanged, so
there's no duplicated yt-dlp/ffmpeg logic to drift out of sync.
"""

import os
import struct
import subprocess
import re
import sys
import shutil
import argparse
import tempfile
from pathlib import Path

import ingest  # same directory — reuse download_video_low / extract_frames



def _jpeg_height(path):
    """Height from the JPEG SOF marker. No PIL dependency (same approach as
    reground_frames.py, which needs it for the identical reason)."""
    try:
        data = Path(path).read_bytes()[:200000]
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                return struct.unpack(">HH", data[i + 5:i + 9])[0]
            if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    except Exception:
        pass
    return None


def _rescue_download(url, tmp, min_height):
    """Re-fetch via the DEFAULT player client when the normal chain came back
    short.

    download_video_low() tries `web_embedded` and then falls back to the skill's
    own client, which for most skills is `android` -- and android exposes ONE
    muxed stream at 640x360. So a transient web_embedded failure silently yields
    360p frames, and the existing safeguard never notices because it counts
    frames and not their height. Measured 2026-09-10: the 84-minute chops class
    logged "Falling back to this skill's own player client" and produced 26
    frames at 360p while reporting "All requested frames captured".

    Two predicates carry this, both learned in reground_frames.py:
      * `protocol^=https` avoids the default client's fragmented HLS ladder --
        on 0XnjEVcaq6A it picks a 985-fragment stream that comes down at 38KB/s.
      * `height>=N` with `-S +height` takes the SMALLEST rung that clears the
        target rather than the largest, because only 16:9 sources ladder at
        720/1080 and a cap lands below the target forever on the others.
    """
    fmt = (f"bestvideo[height>={min_height}][protocol^=https][ext=mp4]/"
           f"bestvideo[height>={min_height}][protocol^=https]/"
           f"best[height>={min_height}][protocol^=https]")
    out = str(tmp / "rescue.%(ext)s")
    subprocess.run([sys.executable, "-m", "yt_dlp", "-f", fmt, "-S", "+height",
                    "--no-playlist", "-o", out, url],
                   capture_output=True, timeout=3600, check=True)
    got = sorted(Path(tmp).glob("rescue.*"))
    return str(got[0]) if got else None

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"


def split_label(raw):
    """Split `3:45=buoyancy-dir` into ('3:45', 'buoyancy dir').

    WHY LABELS EXIST. Capture used to record a timestamp and a path and nothing
    else -- the *reason* a moment was chosen lived only in the operator's head,
    and Step 3 (often a different session) had no record of it. So the notes
    fell back on the one self-describing thing in the file, the transcript, and
    the frames sat beside them grounding nothing. Measured across the corpus in
    2026-09, that is the most common shape of the defect: frames that were
    genuinely well chosen, next to notes written from narration.

    The label is also the only durable record of what a frame showed. Frames are
    gitignored and device-local; the .md survives the disk.
    """
    if "=" in raw:
        ts, _, label = raw.partition("=")
        return ts.strip(), label.strip().replace("-", " ").replace("_", " ")
    return raw.strip(), None


def parse_timestamp(raw):
    """Accept plain seconds ('485', '485.0') or 'mm:ss' / 'h:mm:ss'."""
    raw, _ = split_label(raw)
    if ":" not in raw:
        return float(raw)
    parts = [float(p) for p in raw.split(":")]
    seconds = 0.0
    for p in parts:
        seconds = seconds * 60 + p
    return seconds


def read_frontmatter_field(content, key):
    m = re.search(rf'^{key}:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def set_frontmatter_field(content, key, value):
    if re.search(rf'^{key}:.*$', content, re.MULTILINE):
        return re.sub(rf'^{key}:.*$', f'{key}: {value}', content, count=1, flags=re.MULTILINE)
    # Field doesn't exist yet — insert before the closing '---' of frontmatter
    end = content.index("\n---", content.index("---") + 3)
    return content[:end] + f"\n{key}: {value}" + content[end:]


def main():
    parser = argparse.ArgumentParser(
        description="Extract content-anchored frames for a collected tutorial (Step 2)"
    )
    parser.add_argument("slug", help="Tutorial slug (tutorials/<slug>.md must exist)")
    parser.add_argument("timestamps", nargs="*",
                         help="Timestamps to capture, seconds or mm:ss (e.g. 10 60 4:20 8:05). "
                              "Append =LABEL to record WHY the moment was chosen -- "
                              "`3:45=buoyancy-dir 5:15=gas-resize-tracking`. The label is written "
                              "into the Captured Frames list, so Step 3 opens a file that already "
                              "says what each frame is for.")
    parser.add_argument("--at-max", action="store_true",
                         help="fetch each timestamp as a short SECTION at the source's best "
                              "height instead of the capped whole-file download (plan §3.6) -- "
                              "for frame ARBITRATION, when a frame is deciding a transcript word")
    parser.add_argument("--auto", type=int, metavar="N",
                         help="allocate N timestamps by SCREEN ACTIVITY (plan §3.8) -- a density "
                              "allocator, not an importance oracle; combine with your own picks")
    parser.add_argument("--from-flags", action="store_true",
                         help="also capture the ingest's uncertainty_frames (plan §3.7 item 4) -- "
                              "the spans where Whisper and YouTube's captions disagreed")
    parser.add_argument("--force", action="store_true",
                         help="Re-capture even if frame_status is already 'complete'")
    args = parser.parse_args()

    out_md = TUTORIALS_DIR / f"{args.slug}.md"
    if not out_md.exists():
        print(f"ERROR: {out_md} not found. Run ingest.py first.")
        sys.exit(1)

    content = out_md.read_text(encoding="utf-8")
    frame_status = read_frontmatter_field(content, "frame_status")
    if frame_status == "complete" and not args.force:
        print(f"      frame_status is already 'complete' — pass --force to re-capture.")
        sys.exit(1)
    if frame_status == "skipped" and not args.force:
        print(f"      frame_status is 'skipped' (ingested with --skip-video) — pass --force to override.")
        sys.exit(1)

    url = read_frontmatter_field(content, "url")
    if not url:
        print("ERROR: no 'url' field found in frontmatter.")
        sys.exit(1)

    timestamps = [parse_timestamp(t) for t in args.timestamps]
    labels = [split_label(t)[1] for t in args.timestamps]
    if args.from_flags:
        # §3.7 item 4: aim the frame budget at what the detectors distrust.
        # ⚠️ These come from Step 1's caption cross-check and mean "the two ASRs
        # disagreed here", NOT "this is an important moment". Combine them with
        # content-anchored picks; they are not a substitute for reading the
        # transcript.
        raw = read_frontmatter_field(content, "uncertainty_frames") or ""
        flagged = [float(x) for x in re.findall(r"[-+]?\d*\.?\d+", raw)]
        if not flagged:
            print("      --from-flags: no uncertainty_frames recorded for this tutorial.")
        else:
            added = [t for t in flagged if all(abs(t - e) > 1.0 for e in timestamps)]
            print(f"      --from-flags: +{len(added)} uncertainty timestamp(s) "
                  f"({len(flagged) - len(added)} already covered)")
            timestamps += added
        timestamps.sort()
    if not timestamps and not args.auto:
        print("ERROR: no timestamps given and none found. Pass timestamps, --auto N, or --from-flags "
              "on a tutorial that recorded uncertainty_frames.")
        sys.exit(1)
    out_dir = ingest.FRAMES_DIR / args.slug

    # On a re-capture (--force), clear any frames from a previous run first —
    # otherwise a smaller timestamp count than before leaves stale orphaned
    # frame_NNN.jpg files that don't correspond to any current timestamp.
    if out_dir.exists():
        stale = list(out_dir.glob("frame_*.jpg"))
        if stale:
            print(f"      Clearing {len(stale)} frame(s) from a previous capture...")
            for f in stale:
                f.unlink()

    tmp = Path(tempfile.mkdtemp())
    try:
        print(f"[1/3] Downloading video (lowest quality) for {args.slug}...")
        if args.at_max:
            # §3.6 escalation, and the answer to open question 5: spend the cost
            # only where 720 vs 1080 can change an OUTCOME. A section grab is
            # seconds, so this needs no whole-file download at all.
            # ⚠️ --auto cannot run here: activity allocation needs the whole
            # runtime, and this deliberately never fetches it.
            if args.auto:
                print("ERROR: --at-max and --auto are incompatible -- activity allocation "
                      "needs the whole video, which --at-max deliberately never downloads.")
                sys.exit(1)
            out_dir.mkdir(parents=True, exist_ok=True)
            frame_paths, heights = [], []
            for i, ts in enumerate(timestamps):
                dst = out_dir / f"frame_{i:03d}.jpg"
                got, h = ingest.capture_frame_at_source_max(url, ts, dst, tmp)
                if got:
                    frame_paths.append(dst); heights.append(h)
                    print(f"      {ts:.1f}s -> {h}p")
                else:
                    print(f"      {ts:.1f}s -> FAILED ({h})")
            if heights:
                print(f"[2/3] {len(frame_paths)}/{len(timestamps)} frame(s) at source max "
                      f"(heights: {sorted(set(str(x) for x in heights))})")
            video = None
        else:
            video = ingest.download_video_low(url, tmp)

        if args.auto:
            # §3.8: allocate by screen activity, per-stretch rather than one
            # interval for the whole video.
            # ⚠️ A DENSITY allocator, not an importance oracle. It says "sample
            # more here", never "this is what matters" -- a viewport orbit is a
            # huge pixel delta carrying almost nothing, a typed parameter value a
            # tiny one carrying a great deal. The transcript still decides.
            # duration is left to the allocator: it uses the last scdet
            # sample's time, which is the runtime it actually measured. Passing
            # a separately-probed duration would only introduce a second source
            # of truth for the same number.
            # §3.8 second half: the transcript is a free second signal that
            # needs no video. It covers what scdet cannot -- a typed parameter
            # value is a tiny pixel delta and a loud verbal one.
            auto_ts, why = ingest.plan_density_timestamps(
                video, args.auto,
                transcript=ingest.parse_transcript_timeline(content))
            added = [t for t in auto_ts if all(abs(t - e) > 1.0 for e in timestamps)]
            print(f"      --auto: {why}")
            print(f"      --auto: +{len(added)} timestamp(s) "
                  f"({len(auto_ts) - len(added)} already covered)")
            timestamps = sorted(timestamps + added)

        if not args.at_max:
            print(f"[2/3] Extracting {len(timestamps)} content-anchored frame(s)...")
            frame_paths = ingest.extract_frames(video, timestamps, out_dir)
        print(f"      {len(frame_paths)}/{len(timestamps)} frame(s) saved to "
              f"{out_dir.relative_to(SKILL_DIR)}")

        # HEIGHT guard. The count check below asks "did we get every frame?" and
        # says nothing about whether they are legible -- which is the entire
        # point of the resolution policy. Verify it here rather than discovering
        # 360p frames weeks later in a grounding citation.
        if frame_paths and not args.at_max:
            target = int(os.environ.get("INGEST_FRAME_HEIGHT",
                                        ingest.DEFAULT_FRAME_HEIGHT))
            got = [h for h in (_jpeg_height(p) for p in frame_paths) if h]
            shortest = min(got) if got else None
            if shortest is not None and shortest < target:
                print(f"[SAFEGUARD] {shortest}p < this skill's {target}p -- the "
                      f"player client capped the download. Rescuing via the "
                      f"default client...")
                try:
                    rescued = _rescue_download(url, tmp, target)
                except Exception as exc:
                    rescued = None
                    print(f"      rescue download failed ({type(exc).__name__})")
                if rescued:
                    frame_paths = ingest.extract_frames(rescued, timestamps, out_dir)
                    got = [h for h in (_jpeg_height(p) for p in frame_paths) if h]
                    shortest = min(got) if got else shortest
                    print(f"      re-extracted {len(frame_paths)} frame(s) at {shortest}p")
                if shortest is not None and shortest < target:
                    note = (f"Frames captured at {shortest}p, below the {target}p "
                            f"this skill's policy asks for. The rescue via the "
                            f"default client did not beat it, so the source "
                            f"itself may not offer a taller stream.")
                    print(f"[SAFEGUARD] WARNING: {note}")
                    content = ingest.append_safeguard_note(content, note, level="WARNING")

        if len(frame_paths) == 0:
            note = "0 frames captured — check ffmpeg is in PATH and the video downloaded correctly."
            print(f"[SAFEGUARD] CRITICAL: {note}")
            content = ingest.append_safeguard_note(content, note, level="CRITICAL")
        elif len(frame_paths) < len(timestamps):
            note = f"Partial frame capture: only {len(frame_paths)}/{len(timestamps)} requested frames were captured."
            print(f"[SAFEGUARD] WARNING: only {len(frame_paths)}/{len(timestamps)} "
                  f"requested frames were captured.")
            content = ingest.append_safeguard_note(content, note, level="WARNING")
        else:
            print("[SAFEGUARD] All requested frames captured.")

        # Update frontmatter
        print("[3/3] Updating tutorial file...")
        content = set_frontmatter_field(content, "frame_count", str(len(frame_paths)))
        content = set_frontmatter_field(content, "frame_status", "complete")
        content = set_frontmatter_field(
            content, "frame_selection",
            # This records WHICH CODE PATH RAN -- timestamps were supplied
            # explicitly rather than derived from runtime percentages. It is NOT
            # a judgement that anyone looked at the frames, and it cannot be:
            # this script never sees the pixels. Two entries were found on
            # 2026-09-11 carrying this stamp over evenly-spaced round-number
            # moments (a 42-minute course framed at 1:30/7:00/12:00/18:00/...),
            # because percentages typed in by hand arrive here looking exactly
            # like moments chosen by eye. The old wording claimed "not blind
            # percentages", which this script has no way to know.
            # The trustworthy signal is `grounding: key-steps-anchored`, which
            # is earned by passing `validate.py --grounding <slug>`.
            "explicit-timestamps (supplied to select_frames.py; NOT evidence "
            "that the frames were read -- see `grounding:`)"
        )

        # Replace the "not captured yet" instructional note, if still present
        content = re.sub(
            r"Frames are not captured yet\.[\s\S]*?frontmatter before you write the Structured Notes below\.",
            "Frames captured — see \"Captured Frames\" section below.",
            content,
        )

        captured_section = "\n## Captured Frames\n\n"
        for _i, (ts, fp) in enumerate(zip(timestamps, frame_paths)):
            mm, ss = int(ts) // 60, int(ts) % 60
            # The label records WHY this moment was chosen. Without it Step 3 has
            # nothing to work from but the transcript, which is how frames and notes
            # drifted apart across the corpus. It also outlives the pixels, which are
            # gitignored and device-local.
            _label = labels[_i] if _i < len(labels) else None
            _suffix = f" \u2014 {_label}" if _label else ""
            captured_section += (f"- [{mm}:{ss:02d}] "
                                 f"{fp.relative_to(SKILL_DIR).as_posix()}{_suffix}\n")
        captured_section += "\n---\n"

        if "\n## Captured Frames\n" in content:
            # The old section runs to its `---` rule -- or, when it is the LAST
            # section in the file, to the next top-level heading or EOF. Matching
            # only the `---` form was a silent no-op on those entries: re.sub
            # replaced nothing, so the frames on disk were rewritten while their
            # citations kept the OLD timestamps. That is worse than a crash --
            # the entry still looks grounded while every reference points at a
            # moment that is no longer there. Found 2026-09-10 on
            # 53-recreating-our-solver-with-pops-v1-1080p, whose section ends the
            # file. Fail loudly rather than write a file that lies.
            content, _n = re.subn(
                r"\n## Captured Frames\n(?:.*?\n---\n|.*?(?=\n## )|.*\Z)",
                captured_section, content, count=1, flags=re.DOTALL)
            if _n != 1:
                sys.exit("ERROR: could not rewrite the existing '## Captured "
                         "Frames' section; refusing to leave stale citations.")
        else:
            content = content.replace("\n## Structured Notes",
                                       f"{captured_section}\n## Structured Notes", 1)

        out_md.write_text(content, encoding="utf-8")
        print(f"      Done. {out_md.relative_to(SKILL_DIR)} updated (not committed — "
              f"commit together with the Structured Notes once written).")
        # `frame_status: complete` means PIXELS EXIST. It has never meant the
        # entry is grounded, and reading it that way is what produced 1,300+
        # entries whose notes were written from narration alone. Say so here, in
        # the same breath as "Done", because this is the moment the operator
        # decides whether they are finished.
        print(f"      NOT FINISHED. Step 3 is still owed on this entry: read every "
              f"frame, correct the notes against it, and anchor EVERY Key Step "
              f"with [frame_NNN].")
        print(f"      Gate:  python validate.py --grounding {args.slug}")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

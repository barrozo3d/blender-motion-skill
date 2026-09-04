"""
ingest.py — Data collection for blender-motion skill (Step 1 of 2)

NO API CALLS. Collects everything and saves to disk for Claude Code extraction.

Pipeline (Step 1 — this script):
  1. yt-dlp metadata + chapter parsing
  2. Whisper transcription (falls back to yt-dlp captions), per-sentence
     timestamps preserved even inside chapters
  3. Transcript segmented by chapters (or one "Full Content" section)
  4. Save raw .md to tutorials/<slug>.md (frame_status: pending-selection)
  5. Update INDEX.md with pending stub
  6. git commit + push (raw .md + INDEX only)

No video is downloaded and no frames are extracted here — frame timestamps
need judgment (which moment actually shows the technique), not a blind
percentage split, so that's deferred to select_frames.py (Step 2), run by
Claude Code after reading the timestamped transcript. See select_frames.py's
docstring for that step. Frames land in tutorials/frames/<slug>/ (local only,
not committed to git) once selected.

Usage:
  python ingest.py <youtube-url>
  python ingest.py <youtube-url> --whisper-model small
  python ingest.py <youtube-url> --skip-video   (no frames ever, text-only extraction)
  python ingest.py <article-url>
"""

import sys, os, re, json, subprocess, tempfile, shutil, argparse
from datetime import datetime
from pathlib import Path

try:
    import scan_promo
except ImportError:                       # pragma: no cover - scanner is optional
    scan_promo = None


# Ensure stdout handles Unicode on Windows (cp1252 default breaks non-ASCII titles)
# and flushes per line — block-buffered prints otherwise arrive after subprocess
# (git/yt-dlp) output when both are captured, scrambling the step order in logs.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

# ── Configuration ─────────────────────────────────────────────────────────────

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
FRAMES_DIR    = TUTORIALS_DIR / "frames"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"
def _default_whisper_model():
    """small on GPU (better accuracy, still fast), base on CPU (speed matters more)."""
    try:
        import torch
        if torch.cuda.is_available():
            return "small"
    except Exception:
        pass
    return "base"

DEFAULT_WHISPER = _default_whisper_model()

# ── Utilities ─────────────────────────────────────────────────────────────────

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")[:80]

def _ytdlp_cmd():
    """Return yt-dlp invocation, using cookies.txt if present for YouTube bot bypass.

    Without cookies.txt, the 'android' player client is forced — as of 2026-08
    YouTube's default web_safari client started throwing HTTP 429 + "Sign in
    to confirm you're not a bot" on many (not all) videos. The android client
    sidesteps that check without needing authentication. It only exposes a
    single combined mp4 (no audio-only stream), which is fine here since
    download_audio() re-encodes whatever format it gets to mp3 anyway.

    If a video still fails under the android client too, fall back to cookies:
    1. Install browser extension: 'Get cookies.txt LOCALLY' (Chrome/Edge/Firefox)
    2. Go to youtube.com while logged in
    3. Click the extension -> Export -> save as cookies.txt in this skill directory
    4. Re-run ingest.py — it will pick up cookies.txt automatically
    """
    base = ["yt-dlp"] if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]
    cookies_file = SKILL_DIR / "cookies.txt"
    if cookies_file.exists():
        return base + ["--cookies", str(cookies_file), "--remote-components", "ejs:github"]
    return base + ["--extractor-args", "youtube:player_client=android"]

def check_prerequisites():
    missing = []
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                       capture_output=True)
    if r.returncode != 0:
        missing.append("yt-dlp (pip install yt-dlp)")
    if missing:
        print("Missing prerequisites:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)

    has_ffmpeg  = bool(shutil.which("ffmpeg"))
    has_whisper = False
    try:
        import whisper
        has_whisper = True
    except ImportError:
        pass

    return has_ffmpeg, has_whisper

# ── Step 1: Metadata ───────────────────────────────────────────────────────────

def get_info(url):
    r = subprocess.run(
        _ytdlp_cmd() + ["--dump-json", "--no-playlist", url],
        capture_output=True, text=True, timeout=60, check=True
    )
    return json.loads(r.stdout)

# ── Step 2: Transcript ─────────────────────────────────────────────────────────

WHISPER_VOCAB_HINT = ("Blender, geometry nodes, Cycles, EEVEE, shader editor, Node Wrangler, Principled BSDF, subdivision surface, UV unwrap, HDRI, compositor, grease pencil, VDB, displacement, bevel, boolean, Mix Shader, Color Ramp")

def _load_whisper_model(model_name):
    """First use of a model downloads its weights, and tqdm floods captured
    output with hundreds of progress-bar lines on stderr. Print one notice
    instead; replay the captured stderr only if loading actually fails."""
    import io, contextlib, whisper
    cache_dir = Path(os.getenv("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "whisper"
    if not (cache_dir / f"{model_name}.pt").exists():
        print(f"      Whisper model '{model_name}' not cached yet - downloading weights (one-time)...")
    captured = io.StringIO()
    try:
        with contextlib.redirect_stderr(captured):
            return whisper.load_model(model_name)
    except Exception:
        sys.stderr.write(captured.getvalue())
        raise

# ── Per-video decoder priming (ULTIMATE_PIPELINE_PLAN.md §3.7 item 2) ──────────
#
# get_info() already calls --dump-json, so the video's own title, chapter titles
# and description are in hand before a single second of audio is decoded — and a
# tutorial description usually NAMES the exact nodes being demonstrated. Until
# 2026-09-03 none of it reached the decoder: initial_prompt was the static,
# skill-wide WHISPER_VOCAB_HINT and nothing else.
#
# This attacks the accent-substitution class AT THE SOURCE rather than detecting
# it afterwards: Whisper is far likelier to emit "Cull Volume" when that phrase
# is already in its prompt. (§3.2's wk8-05 case — "call the velocity" is really
# "cull" — is exactly this, and locally it took a frame to settle.)
#
# ⚠️ LANGUAGE GUARD, and it is not decoration. The single most expensive bug in
# this pipeline's history was a wrong-language initial_prompt: feeding an ENGLISH
# hint to a RUSSIAN decode triggered Whisper's multilingual-drift failure mode
# across five of nuke-em-all's Week 1 lessons (Spanish, Hangul and Chinese
# bleeding into the transcript). Metadata is attacker-adjacent in the same way —
# a Russian, Japanese or Arabic title appended to an English prompt is the same
# mistake arriving through a different door. Non-Latin-script candidates are
# therefore DROPPED, not transliterated.
#
# ⚠️ Whisper's prompt window is ~224 tokens. This is a SELECTION problem, not a
# dump: past the window the decoder silently truncates, and what falls off the
# end is whatever was appended last.

PROMPT_TOKEN_BUDGET = 224      # half of Whisper's n_text_ctx=448
PROMPT_CHARS_PER_TOKEN = 3.0   # deliberately pessimistic — rare technical terms
                               # tokenize worse than prose, and overshooting the
                               # window fails silently.
_NON_LATIN_RE = re.compile(
    r"[\u0400-\u04FF\u0500-\u052F"      # Cyrillic
    r"\u0590-\u05FF\u0600-\u06FF"       # Hebrew, Arabic
    r"\u0900-\u097F\u0E00-\u0E7F"       # Devanagari, Thai
    r"\u3040-\u30FF\u3400-\u4DBF"       # Kana, CJK ext-A
    r"\u4E00-\u9FFF\uAC00-\uD7AF]"      # CJK, Hangul
)

def _looks_technical(tok):
    """A term worth spending prompt budget on: CamelCase, ALLCAPS, or carrying a
    digit. Ordinary prose words are already well within Whisper's language model
    and buy nothing; node names and version strings are precisely what it fumbles."""
    if len(tok) < 2 or len(tok) > 30:
        return False
    if any(c.isdigit() for c in tok):
        return True
    if tok.isupper():
        return True
    return tok[0].isupper() and any(c.isupper() for c in tok[1:])

def build_video_prompt(base_hint, info, budget_tokens=PROMPT_TOKEN_BUDGET):
    """
    Extend this skill's static vocab hint with terms from THIS video's metadata,
    highest-value first: chapter titles (they name the actual steps), then the
    video title, then technical-looking tokens from the description.

    Returns base_hint unchanged when info is empty, when priming is disabled via
    INGEST_PROMPT_PRIMING=0, or when nothing survives the filters — so every
    caller can pass info unconditionally.
    """
    if not info or os.getenv("INGEST_PROMPT_PRIMING", "1").lower() in ("0", "false", "no"):
        return base_hint
    cands = []
    for ch in (info.get("chapters") or []):
        t = (ch.get("title") or "").strip()
        if t:
            cands.append(t)
    title = (info.get("title") or "").strip()
    if title:
        cands.append(title)
    for tok in re.findall(r"[A-Za-z][\w.+#/-]{1,29}", info.get("description") or ""):
        if _looks_technical(tok):
            cands.append(tok)

    budget_chars = int(budget_tokens * PROMPT_CHARS_PER_TOKEN)
    seen = {w.lower() for w in re.findall(r"[A-Za-z][\w+#-]*", base_hint)}
    picked, used = [], len(base_hint)
    for cand in cands:
        cand = re.sub(r"\s+", " ", cand).strip(" -–—:|.,")
        if not cand or len(cand) > 80:
            continue
        if _NON_LATIN_RE.search(cand):
            continue          # see the LANGUAGE GUARD note above
        key = cand.lower()
        if key in seen:
            continue
        if used + len(cand) + 2 > budget_chars:
            break             # budget is spent; drop the rest rather than
                              # letting Whisper truncate at an arbitrary point
        seen.add(key)
        picked.append(cand)
        used += len(cand) + 2
    return base_hint + ". " + ", ".join(picked) if picked else base_hint

def whisper_transcribe(audio_path, model_name, info=None, language=None):
    model = _load_whisper_model(model_name)
    # initial_prompt biases decoding toward this skill's vocabulary — without it
    # Whisper mis-hears domain terms (e.g. "COPs" -> "cups", "Houdini" -> "Odini").
    # `info` is optional so every existing caller keeps working; when supplied,
    # the video's own title/chapters/description extend the hint (§3.7 item 2).
    prompt = build_video_prompt(WHISPER_VOCAB_HINT, info)
    # ⚠️ `language=None` keeps Whisper's per-chunk AUTO-DETECT, which is the
    # long-standing behaviour and is right for a library that genuinely holds
    # Russian, Hindi, Spanish and Chinese tutorials alongside English ones.
    # 🔴 But auto-detect can LATCH ONTO THE WRONG LANGUAGE AND STAY THERE.
    # Documented case: a 4h42m ENGLISH Rebelway lighting course transcribed as
    # 6,496 of ~6,531 lines of fluent, fabricated RUSSIAN -- not gibberish, so
    # no repetition safeguard caught it. Two retries (small, then medium) both
    # failed; the fix is to stop asking Whisper to guess.
    # Pass `--language en` for a source you KNOW the language of. It is opt-in
    # precisely because forcing it globally would wreck the non-English
    # entries this library legitimately contains.
    kwargs = {"initial_prompt": prompt}
    if language:
        kwargs["language"] = language
    return model.transcribe(str(audio_path), **kwargs)

def download_audio(url, tmp):
    out = str(tmp / "audio.%(ext)s")
    cmd = _ytdlp_cmd() + ["-x", "--audio-format", "mp3", "--audio-quality", "0",
         "--no-playlist", "-o", out, url]
    # YouTube throttling makes one-off download failures common; a single retry
    # usually recovers and preserves the timestamped Whisper transcript instead
    # of degrading to the timestamp-less captions fallback.
    for attempt in (1, 2):
        try:
            subprocess.run(cmd, capture_output=True, timeout=300, check=True)
            break
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            print("      Audio download failed - retrying once...")
    for f in tmp.iterdir():
        if f.suffix in (".mp3", ".m4a", ".ogg", ".webm"):
            return f
    raise FileNotFoundError("Audio file not found after download")

# ── Caption cross-check (ULTIMATE_PIPELINE_PLAN.md §3.7 item 1) ────────────────
#
# YouTube hands us a SECOND, INDEPENDENT ASR transcript for free, from a
# different vendor. Until 2026-09-03 it was thrown away twice over: captions
# were fetched only when Whisper FAILED, and the parser then discarded the cue
# timings, flattening everything into one string.
#
# ⚠️ The asymmetry that makes this worth keeping: Whisper FABRICATES over
# silence (§3.3 shape 1 — 3.2s at −75.7 dB became segments of 0.02-0.08s);
# Google's ASR generally emits NOTHING there. So a Whisper segment with no
# caption counterpart anywhere in its window is a fabrication CANDIDATE, and
# that is §3.3's shapes 1, 2, 4 and 5 caught MECHANICALLY — the class that cost
# a manual slice re-decode every single time on the local course.
#
# ⚠️ AND THE LIMIT, which is not optional: auto-captions carry their own errors.
# Disagreement means "LOOK HERE". It never means "Whisper is wrong." Nothing
# below edits, deletes, reorders or overrides a Whisper segment — it reports,
# and a human or a later extraction pass decides.

_VTT_TIME_RE = re.compile(
    r"(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})"
)

def _vtt_secs(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0

def ytdlp_caption_cues(url, tmp):
    """
    Fetch YouTube's auto-captions and return [(start, end, text), ...] with the
    cue TIMINGS INTACT. The timings are the entire point: a second transcript
    with no clock cannot be aligned against Whisper's segments, which is why the
    old flat-string parser was useless as a witness even though it already had
    the data in hand.

    Returns [] when no caption track exists — common on small channels. Every
    caller must read [] as "NO WITNESS AVAILABLE", never as "no problems found".

    ⚠️ ENGLISH IS HARDCODED (`--sub-lang en`), and that is an assumption, not a
    fact about the world. All five skills' online paths are English-facing today,
    so it holds — but a non-English tutorial returns [] here and the run reports
    "no caption track", which is indistinguishable from a video that genuinely
    has none. It degrades safely and says so, which is why this is documented
    rather than urgent.

    ⚠️ Note the asymmetry with §3.7 item 2 next door: `build_video_prompt()`
    makes its language assumption EXPLICIT and enforced (non-Latin metadata is
    dropped). This function makes the same class of assumption silently. When
    the online path gains a PROFILE dict (Phase 2 onward), the caption language
    belongs in it beside the prompt's — one language decision, one place.
    """
    try:
        subprocess.run(
            _ytdlp_cmd() + ["--write-auto-subs", "--sub-lang", "en",
             "--sub-format", "vtt", "--skip-download", "--no-playlist",
             "-o", str(tmp / "%(id)s"), url],
            capture_output=True, timeout=120
        )
    except Exception:
        return []
    for f in sorted(tmp.glob("*.vtt")):
        cues, start, end, buf = [], None, None, []
        for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = _VTT_TIME_RE.search(line)
            if m:
                if start is not None:
                    txt = re.sub(r"\s+", " ", " ".join(buf)).strip()
                    if txt and (not cues or cues[-1][2] != txt):
                        cues.append((start, end, txt))
                g = m.groups()
                start, end, buf = _vtt_secs(*g[:4]), _vtt_secs(*g[4:]), []
                continue
            if line.startswith("WEBVTT") or line.strip().isdigit() or not line.strip():
                continue
            # YouTube's rolling auto-captions embed per-word timing tags
            # (<00:00:01.234><c>word</c>) — strip the markup, keep the words.
            clean = re.sub(r"<[^>]+>", "", line).strip()
            if clean:
                buf.append(clean)
        if start is not None:
            txt = re.sub(r"\s+", " ", " ".join(buf)).strip()
            if txt and (not cues or cues[-1][2] != txt):
                cues.append((start, end, txt))
        try:
            f.unlink()
        except OSError:
            pass
        if cues:
            return cues
    return []

def ytdlp_captions(url, tmp):
    """Flat caption text with no timings — the Whisper-failed fallback path's
    original contract, unchanged. Now derived from ytdlp_caption_cues() so there
    is ONE VTT parser in this file rather than two free to drift apart."""
    return " ".join(t for _, _, t in ytdlp_caption_cues(url, tmp))

# Tuned to keep this a pointer, not a second flag storm. The corpus lesson from
# §3.4 applies verbatim: the flag list is not the defect list.
CROSSCHECK_MIN_CUES = 10     # below this the caption track is too sparse to be
                             # evidence of anything; treat as "no witness".
CROSSCHECK_PAD_SEC = 2.0     # the two ASRs drift; only a total miss counts.
CROSSCHECK_MIN_CHARS = 15    # short interjections are noise on both sides.
CROSSCHECK_MAX_REPORT = 10   # cap what reaches the safeguard box.

def caption_crosscheck(segments, cues):
    """
    Return the Whisper segments that NO caption cue overlaps, as
    [{start, end, text}, ...] — fabrication CANDIDATES, in the §3.3 sense.

    Three deliberate suppressions, each one a false-positive class:
      * fewer than CROSSCHECK_MIN_CUES cues -> return [] outright. A sparse or
        absent caption track is missing evidence, not exculpatory evidence.
      * only judge inside the span the caption track actually covers. Captions
        routinely start late and stop early; a Whisper segment beyond either end
        is uncovered, not contradicted.
      * require CROSSCHECK_PAD_SEC of clearance on both sides, because the two
        decoders disagree about boundaries constantly without disagreeing about
        content.

    ⚠️ A hit is a REASON TO LISTEN, never a verdict. See the module note above.
    """
    if len(cues) < CROSSCHECK_MIN_CUES:
        return []
    cue_lo = min(c[0] for c in cues)
    cue_hi = max(c[1] for c in cues)
    out = []
    for seg in segments:
        s, e = seg.get("start"), seg.get("end")
        text = (seg.get("text") or "").strip()
        if s is None or e is None or len(text) < CROSSCHECK_MIN_CHARS:
            continue
        if s < cue_lo or e > cue_hi:
            continue
        lo, hi = s - CROSSCHECK_PAD_SEC, e + CROSSCHECK_PAD_SEC
        if any(cs < hi and ce > lo for cs, ce, _ in cues):
            continue
        out.append({"start": s, "end": e, "text": text})
    return out

def caption_crosscheck_note(flags, n_cues):
    """One safeguard-report line, or None when there is nothing to say. Kept
    beside the detector so the WORDING cannot drift from the rule — the note has
    to carry the limit, or a future reader treats a candidate as a finding."""
    if not flags:
        return None
    shown = flags[:CROSSCHECK_MAX_REPORT]
    spans = "; ".join(f"{f['start']:.1f}-{f['end']:.1f}s \"{f['text'][:60]}\"" for f in shown)
    more = f" (+{len(flags) - len(shown)} more)" if len(flags) > len(shown) else ""
    return (
        f"Caption cross-check: {len(flags)} Whisper span(s) have NO counterpart in "
        f"YouTube's {n_cues}-cue auto-caption track. Whisper fabricates over silence "
        f"where Google's ASR usually emits nothing, so these are the spans worth "
        f"listening to first. NOT a verdict — auto-captions have their own errors, "
        f"and disagreement means 'look here', never 'Whisper is wrong'. Spans: "
        f"{spans}{more}"
    )


# ── In-run slice re-decode (ULTIMATE_PIPELINE_PLAN.md §3.7 item 3) ────────────
#
# §3.2 calls the isolated-slice re-decode "the single biggest protocol change of
# the project": when a span looks wrong, cutting it out and decoding it ALONE
# with the course prompt produces a genuinely independent second reading. Locally
# that was a manual step, done dozens of times across Weeks 7-8.
#
# The audio is ALREADY in the temp directory during a run, so this costs one
# extra short decode and stores nothing.
#
# ⚠️ DO NOT ARCHIVE AUDIO TO MAKE THIS EASIER. The plan declines that explicitly:
# archiving serves retroactive re-checking, which decision #1 has already ruled
# out, and it would accumulate junk for every span where nothing was said.
#
# ⚠️ ALWAYS OVERLAP KNOWN-GOOD TEXT ON BOTH SIDES -- "the agreement is what
# validates the splice" (§3.2). A slice whose overlaps do NOT agree with the full
# decode is not a better witness, it is a different one, and this reports that
# rather than trusting it.
#
# ⚠️ AND A SLICE CAN DEGENERATE TOO (§3.4). One produced seventeen consecutive
# "So it's." where the full run was correct. Read a slice only inside the span it
# was cut for, and never treat it as automatically the better reading.

SLICE_OVERLAP_SEC = 4.0      # known-good context on each side
SLICE_MIN_CLUSTER = 3        # fewer flags than this is not a cluster
SLICE_CLUSTER_GAP = 20.0     # flags farther apart than this are separate events
SLICE_MAX_PER_RUN = 2        # each slice is another Whisper load; bound the cost


def cluster_flag_spans(flags, min_count=SLICE_MIN_CLUSTER, max_gap=SLICE_CLUSTER_GAP):
    """Group flagged spans into clusters worth a second decode.

    A lone flag is not worth a re-decode -- §3.4's "the flag list is not the
    defect list" applies here too. A RUN of them in one stretch is a different
    signal, the same way a repeat burst is different from a repeated line."""
    ts = sorted(f["start"] for f in flags or [] if f.get("start") is not None)
    ends = {f["start"]: f.get("end", f["start"]) for f in flags or [] if f.get("start") is not None}
    if not ts:
        return []
    clusters, cur = [], [ts[0]]
    for t in ts[1:]:
        if t - cur[-1] <= max_gap:
            cur.append(t)
        else:
            clusters.append(cur); cur = [t]
    clusters.append(cur)
    return [(c[0], ends.get(c[-1], c[-1]), len(c)) for c in clusters if len(c) >= min_count]


def redecode_slice(audio_path, start, end, model_name, tmp, overlap=SLICE_OVERLAP_SEC):
    """Cut [start-overlap, end+overlap] and decode it alone. Returns text or ''.

    16 kHz mono, matching what Whisper resamples to anyway -- §3.2's recipe."""
    lo = max(0.0, start - overlap)
    dur = (end + overlap) - lo
    out = Path(tmp) / f"slice_{int(lo)}_{int(dur)}.wav"
    try:
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(lo),
             "-t", str(dur), "-i", str(audio_path), "-ac", "1", "-ar", "16000", str(out)],
            capture_output=True, timeout=120, check=True)
    except Exception:
        return ""
    try:
        model = _load_whisper_model(model_name)
        r = model.transcribe(str(out), initial_prompt=WHISPER_VOCAB_HINT)
        return (r.get("text") or "").strip()
    except Exception:
        return ""
    finally:
        try:
            out.unlink()
        except OSError:
            pass


def _norm_words(s):
    return re.findall(r"[a-z']+", (s or "").lower())


def slice_agreement(full_text, slice_text):
    """0-1 similarity between the full decode's span text and the slice's.

    ⚠️ This is the OVERLAP CHECK in spirit: high agreement means the slice
    corroborates and there is nothing to look at; LOW agreement is the finding,
    and it means "listen to this span", not "the slice is right"."""
    import difflib
    a, b = " ".join(_norm_words(full_text)), " ".join(_norm_words(slice_text))
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def slice_redecode_note(results):
    """One safeguard line, or None. Keeps the limit attached to the finding."""
    if not results:
        return None
    parts = []
    for r in results:
        parts.append(f"{r['start']:.1f}-{r['end']:.1f}s ({r['n_flags']} flags, "
                     f"agreement {r['agreement']:.2f}): slice heard \"{r['slice'][:90]}\"")
    return ("Slice re-decode: " + "; ".join(parts) +
            ". A span was cut out and decoded ALONE with overlap on both sides, giving an "
            "independent second reading. LOW agreement means listen to this span -- it does "
            "NOT mean the slice is correct: a slice can degenerate too (one produced "
            "seventeen consecutive 'So it's.' where the full run was fine). Nothing was "
            "changed; the audio was not kept.")

def segment_by_chapters(transcript, chapters):
    """
    Bucket the Whisper transcript into sections (by official chapters, or one
    "Full Content" section if none exist). Each section keeps both a joined
    `text` blob (for the completeness/hallucination safeguards) and a
    per-sentence `segments` list of (start_seconds, text) tuples — the fine
    timestamps are what let Step 2 pick content-anchored frame moments instead
    of trusting chapter boundaries blindly.
    """
    segs = transcript.get("segments", [])
    if not chapters:
        all_segs = [(s.get("start", 0), s["text"].strip()) for s in segs]
        return [{"title": "Full Content", "start": 0,
                 "text": transcript.get("text", "").strip(),
                 "segments": all_segs}]
    result = []
    for i, ch in enumerate(chapters):
        t0 = ch.get("start_time", 0)
        t1 = chapters[i+1].get("start_time", float("inf")) if i+1 < len(chapters) else float("inf")
        in_range = [s for s in segs if t0 <= s.get("start", 0) < t1]
        text = " ".join(s["text"].strip() for s in in_range).strip()
        seg_list = [(s.get("start", 0), s["text"].strip()) for s in in_range]
        result.append({"title": ch.get("title", f"Chapter {i+1}"), "start": t0,
                        "text": text, "segments": seg_list})
    return result

# ── Step 3: Frame extraction ───────────────────────────────────────────────────

# Frame-capture height for THIS skill (the skill-adapter layer of
# ULTIMATE_PIPELINE_PLAN.md 3.6). Deliberately a module constant rather than a
# literal inside download_video_low(): that function is drift-gated by
# validate.py::check_script_drift(), so its source must stay byte-identical
# across all five skills while the VALUE differs per skill.
# content here is more often viewport/result-led than parameter-pane-led, so 720p
# is the cost/legibility balance. Raise it per run for a UI-heavy screencast.
# Override for one run with the INGEST_FRAME_HEIGHT environment variable.
DEFAULT_FRAME_HEIGHT = "720"



def _frame_client_attempts():
    """yt-dlp base commands to try for a VIDEO download, best client first.

    Extracted from download_video_low() so the source-max escalation below uses
    exactly the same client logic instead of a second copy that could drift.
    See download_video_low()'s docstring for why web_embedded is required: the
    `android` client four skills force exposes ONE muxed 640x360 stream, so any
    height selector silently falls through to 360p. Audio stays on android --
    that is E3b's decision and this does not reopen it."""
    base = _ytdlp_cmd()
    if "--cookies" in base:
        return [base]
    stripped, i = [], 0
    while i < len(base):
        if (base[i] == "--extractor-args" and i + 1 < len(base)
                and base[i + 1].startswith("youtube:player_client")):
            i += 2
            continue
        stripped.append(base[i])
        i += 1
    preferred = stripped + ["--extractor-args", "youtube:player_client=web_embedded"]
    return [preferred] if preferred == base else [preferred, base]


# ── Source-max frame escalation (ULTIMATE_PIPELINE_PLAN.md §3.6) ──────────────
#
# ⚠️ This is the ANSWER TO OPEN QUESTION 5, and it is deliberately NOT a bulk
# reground. Measured 2026-09-03: 98.0% of houdini-wand's 3,205 frames, 98.6% of
# nuke-em-all's 590 and 100% of paint-me's 899 sit in the 720-1079 band, and
# NONE are >=1080 -- so "reground the corpus at 1080" would mean re-downloading
# ~590 tutorials, not a subset. Against that: the earlier campaign already took
# readability from 3.5% to 95%, nothing is illegible, and since Phase 0 new
# ingests already default to 1080 for the dense-UI skills, so the gap closes on
# its own going forward. Frames are also gitignored and device-local, so a bulk
# reground here would not help the other machine at all.
#
# The cost is therefore spent only where 720 vs 1080 can change an OUTCOME:
# §3.2's frame arbitration, where a frame is being used to decide a transcript
# word. wk8-05's "call the velocity" is really "cull", and only the `Cull Volume`
# parameter visible in frame settled it. That is the case worth a fresh grab.
#
# ⚠️ VERIFIED 2026-09-03, because §3.6 flagged it untested: `--download-sections`
# with `--force-keyframes-at-cuts` works against these sources -- a 10s section
# fetched in 2.4s. But the FIRST verification came back 640x360, because the
# default client caps there; without _frame_client_attempts() this escalation
# would have returned frames WORSE than the 720p baseline it exists to improve.

FRAME_SECTION_WINDOW = 6.0     # seconds around the timestamp to fetch


def capture_frame_at_source_max(url, timestamp, out_path, tmp,
                                window=FRAME_SECTION_WINDOW):
    """Re-fetch a few seconds around `timestamp` at the source's best height and
    extract one frame. Returns (path, height) or (None, reason).

    Downloads a SECTION, not the file: a targeted grab is seconds, which is what
    removes the cost argument behind the 720p batch cap for this one case."""
    lo = max(0.0, timestamp - window / 2.0)
    hi = lo + window
    fmt = "bestvideo[ext=mp4]/bestvideo/best"
    clip = Path(tmp) / f"atmax_{int(timestamp)}.%(ext)s"
    got = None
    for base in _frame_client_attempts():
        cmd = base + ["-f", fmt, "--download-sections", f"*{lo}-{hi}",
                      "--force-keyframes-at-cuts", "--no-playlist",
                      "-o", str(clip), url]
        try:
            subprocess.run(cmd, capture_output=True, timeout=300, check=True)
        except Exception:
            continue
        cands = sorted(Path(tmp).glob(f"atmax_{int(timestamp)}.*"))
        if cands:
            got = cands[0]
            break
    if not got:
        return None, "section download failed on every player client"

    h = _probe_height(got)
    # Offset inside the clip, not the original timeline.
    off = max(0.0, timestamp - lo)
    try:
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
             "-ss", str(off), "-i", str(got), "-vframes", "1", "-q:v", "2",
             str(out_path)],
            capture_output=True, timeout=120, check=True)
    except Exception as e:
        return None, f"frame extract failed ({e})"
    finally:
        try:
            got.unlink()
        except OSError:
            pass
    return out_path, h


def _probe_height(video_path):
    """Video height via ffprobe, or None."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=height", "-of", "csv=p=0", str(video_path)],
            capture_output=True, text=True, timeout=60).stdout.strip()
        return int(out.splitlines()[0])
    except Exception:
        return None

def download_video_low(url, tmp):
    """
    Download the video for frame extraction, at a resolution frames can be READ at.

    This used to request `worst[ext=mp4]/worst` -- literally the lowest stream
    available -- which produced 256x144 frames. Measured 2026-08-19 across the
    ingested libraries: unreal-sidekick's frames are 256x144 (avg 11KB) and
    nuke-em-all's are 256x144/426x240, resolutions at which node names and
    parameter values in a screencast are simply not legible. Frame grounding
    cannot work when the frame cannot be read, so the whole point of Step 2 was
    being lost.

    Capped at 720p rather than uncapped: frames are only sampled at a handful of
    timestamps, but yt-dlp still downloads the whole file, and these run in
    batches of hundreds. Set INGEST_FRAME_HEIGHT to raise it (1080 helps for
    dense UI like Nuke's node graph or Houdini's parameter pane).

    PLAYER CLIENT (added 2026-08-24, plan batch D1). The height cap above is
    only reachable if the player client actually exposes the adaptive ladder.
    The `android` client that four of the five skills force in _ytdlp_cmd()
    exposes ONE muxed stream -- itag 18, 640x360 -- so `bestvideo[height<=720]`
    has nothing to match and selection falls all the way through to that 360p
    stream. Measured on O6T5eVYJHsA: android offers 640x360 and nothing else;
    web_embedded offers the full ladder up to 1920x1080. This silently undid
    D0b for four of the five skills: D1's first run re-captured 119 tutorials
    and got 640x360 (360x360 for vertical shorts) -- better than 256x144, but
    not the 720p D0b was written to deliver, and not enough for a Houdini
    parameter pane.

    So the FRAME download asks for web_embedded first and falls back to
    whatever _ytdlp_cmd() chose if that fails. Audio (Step 1) is deliberately
    left alone: it re-encodes to mp3 and does not care about resolution, and
    android is the client that survives YouTube's bot check -- which is what
    E3b decided and this does not reopen. The cookies path already exposes the
    full ladder, so it is passed through untouched.
    """
    h = os.environ.get("INGEST_FRAME_HEIGHT", DEFAULT_FRAME_HEIGHT)
    fmt = (f"bestvideo[height<={h}][ext=mp4]/bestvideo[height<={h}]/"
           f"best[height<={h}][ext=mp4]/best[height<={h}]/best")
    out = str(tmp / "video.%(ext)s")
    client_attempts = _frame_client_attempts()
    # Same one-off YouTube throttling failures as the audio download in Step 1;
    # a single retry usually recovers (select_frames.py depends on this helper).
    last_err = None
    for ci, client_base in enumerate(client_attempts):
        cmd = client_base + ["-f", fmt, "--no-playlist", "-o", out, url]
        for attempt in (1, 2):
            try:
                subprocess.run(cmd, capture_output=True, timeout=600, check=True)
                last_err = None
                break
            except subprocess.CalledProcessError as exc:
                last_err = exc
                if attempt == 1:
                    print("      Video download failed - retrying once...")
        if last_err is None:
            break
        if ci < len(client_attempts) - 1:
            print("      Falling back to this skill's own player client...")
    if last_err is not None:
        raise last_err
    for f in tmp.iterdir():
        if f.suffix in (".mp4", ".webm", ".mkv"):
            return f
    raise FileNotFoundError("Video not found after download")


# ── Frame-density allocation (ULTIMATE_PIPELINE_PLAN.md §3.8) ─────────────────
#
# Local course ingest ran at 62 frames/lesson (7.6/min); online ingest's median
# is 7 across 501 files -- at least 8x. Part of that gap is a per-video attention
# BUDGET and does not close. But WHERE the frames you can afford go is a RULE,
# and rules port: density scales with screen activity, not with runtime. Week 6's
# VEX-heavy lessons settled at ~4s intervals, roughly 7x denser than the stated
# 20-30s baseline, decided entirely by what was on screen.
#
# ⚠️ THIS IS A DENSITY ALLOCATOR, NOT AN IMPORTANCE ORACLE, and the distinction
# is the whole reason it is safe to automate. It decides where to sample MORE.
# It does not decide what matters -- the transcript still does. Scene scoring is
# NOISY on a screencast: a viewport orbit is an enormous pixel delta carrying
# almost no information, while a value typed into a parameter field is a tiny
# delta carrying a great deal. Never present its output as "the important
# moments".
#
# ⚠️ Pairs with, and does not replace, §3.7 item 4's flag-directed spend. The two
# cover different failure modes: richness catches what was never captured,
# uncertainty catches what was captured wrong.

DENSITY_SAMPLE_FPS = 4        # scdet at source fps is ~30x more work for no
                              # extra signal at these window sizes.
DENSITY_WINDOW_SEC = 5.0
DENSITY_MIN_GAP_SEC = 3.0     # frames closer than this are near-duplicates


def scene_activity(video_path, sample_fps=DENSITY_SAMPLE_FPS):
    """[(time, score), ...] from ffmpeg's scdet, decimated to sample_fps.

    Returns [] when ffmpeg is unavailable or the probe fails -- callers must read
    that as "no activity signal", never as "no activity"."""
    try:
        r = subprocess.run(
            ["ffmpeg", "-hide_banner", "-nostats", "-i", str(video_path),
             "-vf", f"fps={sample_fps},scdet=threshold=0", "-f", "null", "-"],
            capture_output=True, text=True, timeout=900,
        )
    except Exception:
        return []
    out = []
    for m in re.finditer(r"lavfi\.scd\.score:\s*([0-9.]+),\s*lavfi\.scd\.time:\s*([0-9.]+)",
                         r.stderr or ""):
        out.append((float(m.group(2)), float(m.group(1))))
    return out



# ── The transcript's own density signal (§3.8, second half) ───────────────────
#
# ⚠️ This needs NO VIDEO AT ALL, which is what makes it worth having beside
# scdet rather than instead of it. §3.8: "imperative and deictic speech --
# 'click this', 'set that to', 'now I'm going to add' -- clusters exactly where
# the hands are working, while a talking-head recap runs high words-per-minute
# with no deixis."
#
# ⚠️ The two signals fail differently, and that is the entire argument for using
# both. scdet sees a viewport orbit as an enormous change carrying almost no
# information; this sees it as nothing at all, because nobody said "click this".
# Conversely a value typed into a parameter field is a tiny pixel delta and a
# loud verbal one. Neither is an importance oracle; together they miss less.
#
# ⚠️ ENGLISH-ONLY, and silently so if not stated: the word lists below are
# English. On a non-English transcript this returns a flat zero signal, which
# the caller must read as "no transcript signal", never as "no activity". The
# same class of assumption as ytdlp_caption_cues' --sub-lang en.

DEIXIS_WORDS = frozenset("""
this that these those here there
""".split())

ACTION_VERBS = frozenset("""
click set add drag select open press type hit create delete move change
increase decrease connect plug turn enable disable choose pick put copy paste
rename bring drop hold scroll zoom jump grab snap merge split extrude bevel
scale rotate translate assign attach detach duplicate group ungroup
""".split())

TRANSCRIPT_LINE_RE = re.compile(r"^\[(\d+):(\d{2})\]\s+(.*)$")


def parse_transcript_timeline(content):
    """[(seconds, text), ...] from a tutorial .md's timestamped transcript."""
    out = []
    for line in content.splitlines():
        m = TRANSCRIPT_LINE_RE.match(line.strip())
        if m:
            out.append((int(m.group(1)) * 60 + int(m.group(2)), m.group(3)))
    return out


def transcript_activity(timeline, window=DENSITY_WINDOW_SEC):
    """{window_index: score} -- density of imperative/deictic speech.

    Score is per-window COUNT of action verbs and deictic words, not a rate:
    a stretch of dense instruction produces many in a row, and normalising by
    word count would flatten exactly the difference being looked for."""
    buckets = {}
    for t, text in timeline:
        words = re.findall(r"[a-z']+", text.lower())
        hits = sum(1 for w in words if w in ACTION_VERBS or w in DEIXIS_WORDS)
        if hits:
            buckets[int(t // window)] = buckets.get(int(t // window), 0) + hits
    return buckets

def plan_density_timestamps(video_path, n_frames, duration_sec=None,
                            window=DENSITY_WINDOW_SEC, min_gap=DENSITY_MIN_GAP_SEC,
                            transcript=None):
    """Allocate n_frames across the runtime PROPORTIONAL TO SCREEN CHANGE.

    Allocation is per-STRETCH, not per-video: one interval for a whole tutorial
    is exactly the thing being replaced. Within a chosen window the peak-change
    moment is taken, since that is when something on screen actually happened.

    ⚠️ THE FLOOR (§3.8's Week 3 rule): never return nothing. "Even short recap /
    homework / intro lessons tend to have real screen content -- always sample at
    least 1-2 frames before assuming a short lesson needs zero visual
    verification." It paid for itself twice: wk6-18's closing photograph was the
    only content not in the transcript at all, and wk7-17's "throne, bridge,
    cave" was settled by frames. Online, 9 corpus files already carry
    frame_count: 0 -- a 30-second video is exactly the class that gets nothing.

    Falls back to EVEN spacing when there is no activity signal, and says so via
    the returned reason string."""
    n_frames = max(1, int(n_frames))
    samples = scene_activity(video_path)
    if not samples:
        if not duration_sec or duration_sec <= 0:
            return [0.0], "no activity signal and no duration -- single frame at 0s"
        step = duration_sec / (n_frames + 1)
        return ([round(step * (i + 1), 2) for i in range(n_frames)],
                "no activity signal (ffmpeg/scdet unavailable) -- fell back to EVEN spacing")

    end = duration_sec or samples[-1][0]
    buckets = {}
    for t, score in samples:
        buckets.setdefault(int(t // window), []).append((t, score))
    if not buckets:
        return [0.0], "no buckets"

    weights = {k: sum(s for _, s in v) for k, v in buckets.items()}

    # Blend in the transcript signal when one is available. Both are normalised
    # to 0-1 first: their raw units are unrelated (pixel change vs word counts)
    # and summing them unnormalised would let whichever happens to be numerically
    # larger silently win.
    # ⚠️ Equal weight is a DEFAULT, not a measurement. Nothing here establishes
    # that screen change and spoken deixis deserve the same say; it is the
    # neutral choice until someone measures a better one.
    tr_note = ""
    if transcript:
        tr = transcript_activity(transcript, window)
        if tr:
            wmax = max(weights.values()) or 1.0
            tmax = max(tr.values()) or 1
            # ⚠️ Clamp to the runtime scdet actually measured. A transcript can
            # outrun its video -- a truncated or partial download, or simply the
            # wrong transcript -- and an unclamped blend then proposes timestamps
            # past the end of the file, which extract_frames silently fails on.
            # Caught by a test that paired a transcript with the wrong video and
            # got 242.5s out of a 190s clip.
            last_window = max(buckets) if buckets else 0
            for k in set(weights) | set(tr):
                if k > last_window:
                    continue
                weights[k] = (weights.get(k, 0.0) / wmax) + (tr.get(k, 0) / tmax)
                buckets.setdefault(k, [(k * window + window / 2, 0.0)])
            tr_note = f" + transcript deixis over {len(tr)} window(s)"
        else:
            tr_note = " (transcript present but no English action/deictic words found)"

    total = sum(weights.values())
    order = sorted(buckets, key=lambda k: (-weights[k], k))

    picked = []
    if total <= 0:
        # A completely static video still gets frames -- the floor applies.
        step = end / (n_frames + 1)
        return ([round(step * (i + 1), 2) for i in range(n_frames)],
                "zero measured change (static screen) -- fell back to EVEN spacing")

    for k in order:
        if len(picked) >= n_frames:
            break
        peak_t = max(buckets[k], key=lambda ts: ts[1])[0]
        if all(abs(peak_t - p) >= min_gap for p in picked):
            picked.append(round(peak_t, 2))
    # Top up from evenly spaced positions if activity was too concentrated.
    if len(picked) < n_frames:
        step = end / (n_frames + 1)
        for i in range(n_frames):
            cand = round(step * (i + 1), 2)
            if len(picked) >= n_frames:
                break
            if all(abs(cand - p) >= min_gap for p in picked):
                picked.append(cand)
    picked.sort()
    return picked, (f"activity-weighted over {len(buckets)} window(s) of {window:g}s "
                    f"from {len(samples)} sample(s){tr_note}")

def extract_frames(video_path, timestamps, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for i, ts in enumerate(timestamps):
        dst = out_dir / f"frame_{i:03d}.jpg"
        subprocess.run(
            ["ffmpeg", "-ss", str(max(ts, 0)), "-i", str(video_path),
             "-frames:v", "1", "-q:v", "2", str(dst), "-y"],
            capture_output=True
        )
        if dst.exists():
            frames.append(dst)
    return frames

# ── Ingest safeguards ─────────────────────────────────────────────────────────

_STOP_WORDS = {
    'the','a','an','and','or','in','of','to','is','it','i','we','you','this',
    'that','for','are','on','at','be','by','with','have','was','as','from',
    'so','if','but','not','do','my','me','he','she','they','up','out','just',
    'can','all','now','will','our','when','their','what','about','here','one',
    'been','some','get','which','there','has','had','his','her','its','them',
    'then','than','also','into','more','would','could','should','very','like',
}

def _detect_hallucination(text):
    """Content word repeated >= 8x in last 50 words → probable ASR loop."""
    import collections
    lines = [l for l in text.splitlines()
             if not re.search(r'frame_\d+\.(jpg|png)|tutorials[/\\]frames', l, re.I)]
    words = re.findall(r'\b[a-z]+\b', ' '.join(lines).lower())
    if not words:
        return False, '', 0
    tail = [w for w in words[-50:] if w not in _STOP_WORDS]
    if not tail:
        return False, '', 0
    top_word, top_count = collections.Counter(tail).most_common(1)[0]
    return top_count >= 8, top_word, top_count

def run_safeguards(ch_transcripts, duration_sec=None):
    """
    Run all Step-1 ingest quality checks (transcript completeness + ASR hallucination).
    Returns (warnings, critical) — critical items mark extraction_status: needs-review.

    Frame-count validation is NOT done here: ingest.py no longer downloads video or
    extracts frames (deferred to select_frames.py, Step 2), so there's nothing to check
    yet at this point. See select_frames.py's own safeguard checks + append_safeguard_note()
    for the frame-capture-time equivalent.
    """
    warnings, critical = [], []
    total_chars = sum(len(ch.get('text', '')) for ch in ch_transcripts)

    # 1. Chapter transcript coverage
    for ch in ch_transcripts:
        text = ch.get('text', '').strip()
        name = ch.get('title', '?')
        if not text:
            critical.append(f"Empty transcript in chapter '{name}'")
        elif len(text) < 50:
            warnings.append(f"Very short transcript ({len(text)} chars) in '{name}'")

    # 2. Total transcript completeness
    # ⚠️ DURATION-AWARE FLOOR. A flat 500-char minimum is a false positive on
    # any genuinely SHORT video: a 28s homework lesson physically cannot
    # contain 500 characters of speech, and flagging it "captions unavailable
    # or audio silent" says something false about a complete, healthy
    # transcript. Caught 2026-09-03 on designing-destruction-wk6-18-homework:
    # 28.6s, 448 chars, five coherent sentences, zero flags, review already
    # done -- and stuck at needs-review purely because of this threshold.
    # 5 chars/sec is deliberately far below real speech (~12-15) so the check
    # still catches silent or failed audio at any length; it only stops the
    # absolute floor from being applied to clips too short to reach it.
    floor = 500
    if duration_sec:
        floor = min(500, int(duration_sec * 5))
    if total_chars < floor:
        critical.append(
            f"Total transcript only {total_chars} chars (min {floor}"
            + (f" for {int(duration_sec)}s" if duration_sec else "")
            + "). Captions unavailable or audio silent — extraction will be poor."
        )
    elif total_chars < 1200:
        warnings.append(
            f"Thin transcript: {total_chars} chars. "
            "Notes may be shallow — consider --whisper-model small."
        )

    # 3. ASR hallucination detection (per chapter)
    for ch in ch_transcripts:
        text = ch.get('text', '')
        if len(text) > 200:
            hallu, word, count = _detect_hallucination(text)
            if hallu:
                critical.append(
                    f"ASR hallucination in '{ch.get('title', '?')}': "
                    f"'{word}' x{count} in last 50 content words. "
                    "Review and truncate the affected section before extracting."
                )

    return warnings, critical

def promo_hint_at_ingest(ch_transcripts, duration_secs):
    """Ingest-time promo hint. Returns a WARNING string, or None.

    Deliberately a WARNING and never a CRITICAL, and it is worth knowing why.

    The strong promo signal is the extraction pass's own prose -- an entry
    saying "course trailer only", "no step-by-step content". At ingest time
    that prose DOES NOT EXIST YET: the Structured Notes are written in Step 1,
    after this runs. All that is available here is the raw transcript and the
    duration, and those are structural signals only.

    Structural signals corroborate; they do not accuse. "Short video, ends with
    a call to action" is also a fair description of a good one-minute feature
    tutorial, which is how most plugin and add-on documentation is published.
    Marking those `needs-review` would be wrong, and would train whoever reads
    the flag to ignore it.

    So this does the one useful thing it honestly can: it tells the extraction
    pass to answer the question explicitly. If the notes then say "trailer, no
    technique", validate.py check #11 catches it with a real signal -- and if
    the notes say otherwise, nothing was lost. The gate is at validate time;
    this only makes sure the gate has something true to read.
    """
    if scan_promo is None:
        return None
    if not (0 < duration_secs < 180):
        return None
    text = " ".join(ch.get("text", "") for ch in ch_transcripts).strip()
    if not text:
        return None
    tail = text[int(len(text) * 0.85):]
    hits = [rx for rx in scan_promo.CTA if re.search(rx, tail, re.IGNORECASE)]
    if not hits:
        return None
    return (
        f"Possible promotional entry: {int(duration_secs)}s video whose "
        f"transcript ends with {len(hits)} call-to-action phrase(s). This may "
        "be a course trailer rather than a tutorial -- or simply a short "
        "one-feature tutorial, which looks identical from here. WHEN "
        "EXTRACTING, ANSWER EXPLICITLY IN THE NOTES: does this demonstrate a "
        "technique, or only advertise one? Say so in plain words ('trailer "
        "only -- no step-by-step content' / 'short feature tutorial, N steps "
        "shown'). validate.py check #11 reads that sentence."
    )


def _print_safeguard_report(warnings, critical):
    if not warnings and not critical:
        print("[SAFEGUARD] All checks passed")
        return
    print("[SAFEGUARD] Quality issues found:")
    for w in warnings:
        print(f"      WARNING  : {w}")
    for c in critical:
        print(f"      CRITICAL : {c}")
    if critical:
        print("      => extraction_status set to 'needs-review'")

def build_safeguard_section(warnings, critical):
    """
    Render the WARNING/CRITICAL findings as a markdown section. Returns "" if both
    lists are empty (clean ingests get no extra section — matches the console
    behavior of only speaking up when something's actually wrong).

    Persisting this into the .md file (not just printing to console) is what makes
    a `needs-review` flag auditable later — otherwise the *reason* a tutorial got
    flagged only ever existed in whatever terminal happened to be open at ingest time.
    """
    if not warnings and not critical:
        return ""
    lines = [
        "\n## Ingest Safeguard Report\n",
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n",
    ]
    for c in critical:
        lines.append(f"- **CRITICAL:** {c}")
    for w in warnings:
        lines.append(f"- WARNING: {w}")
    lines.append("\n---\n")
    return "\n".join(lines)

def append_safeguard_note(content, note, level="WARNING"):
    """
    Insert one more finding into an existing '## Ingest Safeguard Report' section,
    or create that section if this is the first finding for the file (e.g. Step 1's
    transcript checks were clean but Step 2's frame-capture check in select_frames.py
    found a problem). Shared by both ingest.py and select_frames.py so all quality-check
    reasoning ends up in one place inside the file, regardless of which step found it.
    """
    line = f"- **{level}:** {note}" if level == "CRITICAL" else f"- {level}: {note}"
        # Tolerate a hand-annotated header ('(reviewed, resolved)', '-- Reviewed');
        # the strict form silently failed to find an existing box. (E5, 2026-08-24)
    m = re.search(r"\n## Ingest Safeguard Report[^\n]*\n.*?\n---\n", content, re.DOTALL)
    if m:
        insertion_point = content.rindex("\n---\n", m.start(), m.end())
        return content[:insertion_point] + line + "\n" + content[insertion_point:]
    header = "## Raw Data (for Claude Code extraction)\n"
    idx = content.index(header) + len(header)
    section = (
        "\n## Ingest Safeguard Report\n\n"
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n\n"
        f"{line}\n\n---\n"
    )
    return content[:idx] + section + content[idx:]

# ── Build raw .md ──────────────────────────────────────────────────────────────


# §3.7 item 4 -- spend the frame budget where the transcript is UNCERTAIN.
#
# ⚠️ The plan's wording for this item is STALE, written against an older
# pipeline: "capture extra frames at flagged timestamps, IN THE SAME RUN while
# the video is still in the temp directory". ingest.py no longer downloads video
# at all -- frame capture moved to Step 2 (select_frames.py) so a human or model
# picks content-anchored moments instead of the script guessing. There is no
# video in temp to spend frames from.
#
# So the item is implemented as a HANDOFF rather than a capture: Step 1 records
# the timestamps its detectors distrust, and Step 2 spends frames there via
# `select_frames.py <slug> --from-flags`. Same intent -- aim the budget at
# uncertainty -- adapted to where the video actually lives now.
#
# ⚠️ These are the CROSS-CHECK's spans. They say "the two ASRs disagree here",
# never "this is what matters in the video". Richness-directed selection (§3.8)
# is a different signal and does not come from this field.

def uncertainty_timestamps(cap_flags, limit=8):
    """Distinct, rounded start times from caption cross-check flags."""
    seen, out = set(), []
    for f in cap_flags or []:
        t = f.get("start")
        if t is None:
            continue
        key = round(float(t), 1)
        if key in seen:
            continue
        seen.add(key)
        out.append(key)
        if len(out) >= limit:
            break
    return sorted(out)


def fmt_uncertainty(ts):
    """Render the frontmatter list. Always emits a list, never omits the key --
    an absent field and an empty one would be indistinguishable to Step 2, and
    "no disagreement found" must not read the same as "never checked"."""
    return "[" + ", ".join(f"{v:g}" for v in (ts or [])) + "]"

def source_host(url):
    """The human name of the host a VIDEO came from, for its `source:` field.

    ⚠️ The label used to be the literal "YouTube" whenever the video path ran,
    which was true for exactly as long as that path only ever ran on YouTube.
    `--video-url` made it false. The field is NOT decoration: it is the only
    provenance marker an entry carries, `retrieval_test.py::provenance()`
    classifies by it, and `validate.py::is_youtube_source()` reads it -- a
    Blender Studio lesson labelled "YouTube" is a lie told to every later
    measurement.

    ⚠️ Only the VIDEO branch calls this. An article keeps its "Article" label,
    which describes the KIND of source rather than its host, and that
    distinction is what the templates have always encoded.
    """
    u = (url or "").lower()
    if "youtube.com" in u or "youtu.be" in u:
        return "YouTube"
    if "studio.blender.org" in u:
        return "Blender Studio"
    m = re.match(r"https?://(?:www\.)?([^/]+)", u)
    return m.group(1) if m else "Unknown"


def build_raw_md(info, ch_transcripts, slug, frame_status="pending-selection",
                  sg_warnings=None, sg_critical=None, is_yt=True, uncertainty_ts=None):
    title    = info.get("title", "Unknown")
    url      = info.get("webpage_url", "")
    author   = info.get("uploader", "Unknown")
    today    = datetime.now().strftime("%Y-%m-%d")
    duration = info.get("duration", 0)
    dur_str  = f"{int(duration)//60}m{int(duration)%60}s" if duration else "unknown"
    source_label = source_host(url) if is_yt else "Article"

    # Chapter breakdown with per-sentence timestamped transcript.
    # No frames yet at this point — frame capture is Step 2 (content-aware,
    # see select_frames.py), not blind-timestamped here in Step 1.
    chapters_section = ""
    for ch in ch_transcripts:
        t_fmt = f"{int(ch.get('start',0))//60}:{int(ch.get('start',0))%60:02d}"
        chapters_section += f"\n### {ch['title']} [{t_fmt}]\n"
        segs = ch.get('segments') or []
        if segs:
            chapters_section += "**Transcript (timestamped):**\n"
            for t, txt in segs:
                if not txt:
                    continue
                mm, ss = int(t) // 60, int(t) % 60
                chapters_section += f"[{mm}:{ss:02d}] {txt}\n"
            chapters_section += "\n"
        elif ch.get("text"):
            chapters_section += f"**Transcript:** {ch['text']}\n\n"

    if frame_status == "skipped":
        frame_note = "Frame capture was skipped for this ingest (--skip-video). Text-only extraction."
    else:
        frame_note = (
            f"Frames are not captured yet. Read the timestamped transcript below, pick moments\n"
            f"that actually show a technique/result worth a still (not blind percentages —\n"
            f"even within a named chapter, verify the real moment against its timestamps), then run:\n"
            f"  python select_frames.py {slug} <ts1> <ts2> ...\n"
            f"(seconds or mm:ss). This appends a \"Captured Frames\" section and updates the\n"
            f"frontmatter before you write the Structured Notes below."
        )

    safeguard_section = build_safeguard_section(sg_warnings or [], sg_critical or [])

    return f"""---
title: {title}
source: {source_label}
url: {url}
author: {author}
ingested: {today}
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/{slug}/
frame_count: 0
frame_status: {frame_status}
uncertainty_frames: {fmt_uncertainty(uncertainty_ts)}
---

# {title}

**Source:** [{source_label}]({url})
**Author:** {author}
**Duration:** {dur_str} | {len(ch_transcripts)} section(s)

---

## Raw Data (for Claude Code extraction)
{safeguard_section}

{frame_note}

{chapters_section}

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
"""

def update_index_pending(info, slug, filename, is_yt=True):
    title  = info.get("title", "Unknown")
    url    = info.get("webpage_url", "")
    author = info.get("uploader", "Unknown")
    source_label = source_host(url) if is_yt else "Article"

    entry = f"""

### {title}
- **Source:** {source_label}
- **URL:** {url}
- **Author:** {author}
- **Blender Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    if f"tutorials/{filename}" in content or (url and url in content):
        print(f"      INDEX.md already has an entry for {filename} — skipping (re-ingest will refresh the .md file but not duplicate the index)")
        return
    placeholder = "*(Empty — add your first tutorial by saying"
    if placeholder in content:
        content = re.sub(r"\*\(Empty[^)]+\)\*", entry.strip(), content)
    elif "\n---\n\n## Tag Reference" in content:
        content = content.replace("\n---\n\n## Tag Reference",
                                  f"{entry}\n---\n\n## Tag Reference")
    else:
        idx = content.rfind("\n---")
        if idx != -1:
            content = content[:idx] + entry + content[idx:]
        else:
            content += entry
    INDEX_FILE.write_text(content, encoding="utf-8")

def update_readme_tutorial_count():
    """
    Keep README.md's "N tutorials ingested" line in sync with the real count on
    disk, so it can never silently go stale the way a hand-written number would.
    No-op if README.md has no line matching the expected pattern (e.g. it was
    reworded) — fails quiet rather than corrupting the file.
    """
    readme = SKILL_DIR / "README.md"
    if not readme.exists():
        return
    count = len([f for f in TUTORIALS_DIR.glob("*.md") if f.name != "INDEX.md"])
    content = readme.read_text(encoding="utf-8")
    new_content = re.sub(
        r"\*\*\d+\s*tutorials ingested\*\*",
        f"**{count} tutorials ingested**",
        content,
        count=1,
    )
    if new_content != content:
        readme.write_text(new_content, encoding="utf-8")

def fetch_article(url):
    """Fetch a web article or documentation page as plain text.

    Vendor documentation (D4b) is why this is more than a tag-strip. Foundry's
    Katana docs are MadCap Flare pages: ~220KB of HTML where the real article
    lives in a div#mc-main-content, wrapped in five <nav> blocks, a footer and a
    cookie widget. Stripping tags off the whole page and keeping the first 8000
    characters spent part of the budget on "Skip To Main Content / Account
    Settings / Search Tips" and then truncated the GafferThree page mid-sentence
    at roughly a quarter of its content (29,449 clean chars measured).

    So: drop chrome elements, prefer a main-content container when the page
    declares one, and only then strip tags. The cap is raised because a doc page
    is legitimately longer than a blog post and much shorter than a transcript.
    (E-workstream / D4b, 2026-08-24)
    """
    import urllib.request
    from urllib.parse import urlparse

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw_html = resp.read().decode("utf-8", errors="ignore")

    # Extract <title> BEFORE stripping tags - stripping first left this dead code
    # (it searched html that no longer had any tags, so title always fell back
    # to the raw URL, which then poisoned the slug/filename too).
    from html import unescape          # module name would shadow the html local
    tm = re.search(r"<title[^>]*>(.*?)</title>", raw_html, re.I | re.S)
    title = tm.group(1) if tm else url
    # Decode entities BEFORE collapsing whitespace. The old ad-hoc list handled
    # only &#x27; &#39; &rsquo; &amp;, so a &#160; (non-breaking space) survived
    # into the title, the H1, frames_dir AND the slug -- a 2026-08-24 ingest
    # produced "setting-up-usdpreviewsurface160materials.md".
    title = unescape(title)
    title = re.sub(r"\s+", " ", title).strip()

    # 1. remove non-content elements outright
    html = re.sub(r"<(script|style|nav|footer)[^>]*>.*?</\1>", " ",
                  raw_html, flags=re.DOTALL | re.I)

    # 2. prefer the page's own main-content container when it declares one.
    #    Nested divs make a balanced match impractical, so cut from the opening
    #    tag to the first nav/footer that follows it.
    for marker in (r'<\w+[^>]*id="mc-main-content"[^>]*>',      # MadCap Flare
                   r'<main[^>]*>',                              # HTML5
                   r'<\w+[^>]*role="main"[^>]*>',
                   r'<article[^>]*>'):
        m = re.search(marker, html, re.I)
        if m:
            html = html[m.end():]
            cut = re.search(r"<(footer|nav)\b", html, re.I)
            if cut:
                html = html[:cut.start()]
            break

    # 3. tags -> text
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&nbsp;|&#160;", " ", html)
    html = re.sub(r"&[a-z#0-9]+;", " ", html)
    text = re.sub(r"\s+", " ", html).strip()

    # 4. trim trailing feedback/cookie widgets that survive inside the container
    for tail in (r"Give Feedback.*$", r"You must accept cookies.*$",
                 r"How can we improve.*$"):
        text = re.sub(tail, "", text, flags=re.I | re.DOTALL).strip()

    return {"title": title, "uploader": urlparse(url).netloc,
            "description": text[:25000], "duration": 0,
            "webpage_url": url, "chapters": []}

# ── Main ───────────────────────────────────────────────────────────────────────

def find_duplicate_by_video_id(video_id, exclude_name):
    """Return the tutorial file that already references this YouTube video ID, if any.

    Slug/URL checks miss re-ingests where the uploader changed the title (new slug,
    new URL text) — the 11-char video ID is the stable identity, so search for it.
    """
    if not video_id:
        return None
    needle = f"v={video_id}"
    for f in TUTORIALS_DIR.glob("*.md"):
        if f.name in ("INDEX.md", exclude_name):
            continue
        try:
            if needle in f.read_text(encoding="utf-8", errors="ignore"):
                return f
        except OSError:
            continue
    return None


def main():
    parser = argparse.ArgumentParser(description="Blender tutorial data collection (Step 1 of 2)")
    parser.add_argument("url")
    parser.add_argument("--whisper-model", default=DEFAULT_WHISPER,
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite an existing tutorial file even if extraction_status: complete")
    parser.add_argument("--language", default=None, metavar="CODE",
                        help="Force Whisper's language (e.g. en). Default is "
                             "auto-detect; use this when you KNOW the source "
                             "language and auto-detect has drifted.")
    parser.add_argument("--video-url", action="store_true",
                        help="Treat a NON-YouTube url as a video page yt-dlp can download "
                             "(e.g. a self-hosted Blender Studio lesson) instead of an article")
    parser.add_argument("--title", default=None,
                        help="Override the fetched title (generic extractors append site chrome)")
    parser.add_argument("--author", default=None,
                        help="Override the fetched author (generic extractors rarely report one)")
    args = parser.parse_args()

    has_ffmpeg, has_whisper = check_prerequisites()
    # ⚠️ This flag answers "run the VIDEO pipeline", not "this is YouTube". They
    # were the same question for as long as every video source was YouTube, and
    # the name is kept because everything downstream reads it as the video path.
    # Opt-in only: without --video-url a non-YouTube url still goes to
    # fetch_article exactly as before, so no existing behaviour moves.
    # ⚠️ The one genuinely YouTube-specific consumer is the duplicate guard,
    # which greps for the extractor's id -- harmless on another host, where the
    # id is that host's own and still worth catching a re-ingest by. The caption
    # cross-check finds no track off-YouTube and SAYS so, per §3.7's rule that a
    # missing witness is reported rather than assumed clean.
    is_yt = ("youtube.com" in args.url or "youtu.be" in args.url
             or args.video_url)
    tmp = Path(tempfile.mkdtemp())

    try:
        # 1. Metadata
        print("[1/4] Fetching metadata...")
        if is_yt:
            info = get_info(args.url)
        else:
            info = fetch_article(args.url)

        # ⚠️ Applied to `info` itself, not just to local `title`, so the
        # overrides reach build_raw_md / update_index_pending / the slug --
        # every consumer reads them back out of `info`. Generic extractors
        # append site chrome to the title ("... - Blender Studio (1)") and
        # usually report no uploader at all, and a slug built from chrome is
        # frozen identity the moment the file is committed.
        if args.title:
            info["title"] = args.title
        if args.author:
            info["uploader"] = args.author
        title    = info.get("title", "Unknown")
        chapters = info.get("chapters") or []
        duration = info.get("duration", 0)
        print(f"      {title}")
        print(f"      {len(chapters)} chapter(s), {int(duration//60)}m{int(duration)%60}s")

        slug   = slugify(title)
        out_md = TUTORIALS_DIR / f"{slug}.md"

        if is_yt and not args.force:
            dup = find_duplicate_by_video_id(info.get("id", ""), out_md.name)
            if dup:
                print(f"      This video is already in the library under a different title:")
                print(f"        {dup.name}")
                print(f"      Skipping (same YouTube video ID). Pass --force to ingest anyway.")
                return

        if out_md.exists() and not args.force:
            existing = out_md.read_text(encoding="utf-8")
            if "extraction_status: complete" in existing:
                print(f"      {out_md.name} is already fully extracted — refusing to overwrite.")
                print(f"      Pass --force to re-collect anyway (this will wipe the existing Structured Notes).")
                return

        # 2. Transcript (per-sentence timestamps preserved — see segment_by_chapters)
        ch_transcripts = []
        used_captions_fallback = False
        _cap_note = None
        _cap_flags = []
        _slice_results = []
        if is_yt:
            if has_whisper:
                print(f"[2/4] Downloading audio + transcribing with Whisper ({args.whisper_model})...")
                try:
                    audio = download_audio(args.url, tmp)
                    transcript = whisper_transcribe(audio, args.whisper_model, info,
                                                    language=args.language)
                    ch_transcripts = segment_by_chapters(transcript, chapters)
                    print(f"      {len(transcript.get('segments',[]))} segments -> {len(ch_transcripts)} sections")
                    # §3.7 item 1: a second, independent ASR pass we already had
                    # access to and were discarding. Report-only -- see
                    # caption_crosscheck() for why it never overrules Whisper.
                    if os.getenv("INGEST_CAPTION_CROSSCHECK", "1").lower() not in ("0", "false", "no"):
                        try:
                            _cues = ytdlp_caption_cues(args.url, tmp)
                            _cap_flags = caption_crosscheck(transcript.get("segments", []), _cues)
                            _cap_note = caption_crosscheck_note(_cap_flags, len(_cues))
                            if _cues:
                                print(f"      caption cross-check: {len(_cues)} cues, "
                                      f"{len(_cap_flags)} unsupported span(s)")
                            else:
                                print("      caption cross-check: no caption track "
                                      "(no second witness available -- not a clean result)")
                        except Exception as _e:
                            print(f"      caption cross-check skipped ({_e})")
                    # §3.7 item 3: when flags CLUSTER, cut that span out and
                    # decode it alone while the audio is still here. Reports;
                    # never replaces. Stores nothing.
                    if os.getenv("INGEST_SLICE_REDECODE", "1").lower() not in ("0", "false", "no"):
                        try:
                            _clusters = cluster_flag_spans(_cap_flags)[:SLICE_MAX_PER_RUN]
                            for _s, _e2, _n in _clusters:
                                _full = " ".join(
                                    (sg.get("text") or "") for sg in transcript.get("segments", [])
                                    if sg.get("start") is not None and _s <= sg["start"] <= _e2)
                                _sl = redecode_slice(audio, _s, _e2, args.whisper_model, tmp)
                                if not _sl:
                                    continue
                                _ag = slice_agreement(_full, _sl)
                                _slice_results.append({"start": _s, "end": _e2, "n_flags": _n,
                                                       "agreement": _ag, "slice": _sl})
                                print(f"      slice re-decode {_s:.0f}-{_e2:.0f}s "
                                      f"({_n} flags): agreement {_ag:.2f}")
                            if not _clusters:
                                print("      slice re-decode: no flag clusters "
                                      f"(need {SLICE_MIN_CLUSTER}+ within {SLICE_CLUSTER_GAP:g}s)")
                        except Exception as _e:
                            print(f"      slice re-decode skipped ({_e})")
                except Exception as e:
                    print(f"      Whisper failed ({e}), using yt-dlp captions")
                    used_captions_fallback = True
                    text = ytdlp_captions(args.url, tmp)
                    ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
            else:
                print("[2/4] Whisper not installed - using yt-dlp captions (pip install openai-whisper for better results)")
                used_captions_fallback = True
                text = ytdlp_captions(args.url, tmp)
                ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
        else:
            print("[2/4] Article - using page text")
            ch_transcripts = [{"title": "Full Content", "start": 0,
                               "text": info.get("description", ""), "segments": []}]

        # Frame capture is deferred to Step 2 (select_frames.py), driven by Claude
        # reading the timestamped transcript below — content-aware beats blind
        # percentage timestamps, and picking *which* moments matter needs judgment
        # this script deliberately doesn't have (no API calls made here).
        can_have_frames = is_yt and not args.skip_video and has_ffmpeg
        frame_status = "pending-selection" if can_have_frames else "skipped"
        if not can_have_frames:
            reason = "article" if not is_yt else ("--skip-video" if args.skip_video else "ffmpeg not found")
            print(f"[3/4] Frame capture skipped ({reason})")
        else:
            print("[3/4] Frame capture deferred to Step 2 (content-aware selection via select_frames.py)")

        # Safeguard checks — transcript completeness/hallucination only; frame-count
        # validation now happens in select_frames.py once real timestamps are chosen.
        sg_warnings, sg_critical = run_safeguards(ch_transcripts,
                                                  info.get("duration", 0))
        if _cap_note:
            sg_warnings.append(_cap_note)
        _slice_note = slice_redecode_note(_slice_results)
        if _slice_note:
            sg_warnings.append(_slice_note)
        _promo = promo_hint_at_ingest(ch_transcripts, info.get("duration", 0))
        if _promo:
            sg_warnings.append(_promo)
        if used_captions_fallback:
            sg_warnings.append('Transcript came from the yt-dlp captions fallback - NO per-sentence timestamps. Content-anchored frame selection (select_frames.py) will have to estimate moments; consider re-running ingest.py to retry Whisper before extracting.')
        _print_safeguard_report(sg_warnings, sg_critical)

        # 4. Write raw .md + commit
        print("[4/4] Writing raw tutorial file...")
        md = build_raw_md(info, ch_transcripts, slug, frame_status, sg_warnings, sg_critical,
                          is_yt=is_yt,
                          uncertainty_ts=uncertainty_timestamps(_cap_flags))
        if sg_critical:
            md = md.replace("extraction_status: pending", "extraction_status: needs-review", 1)
        out_md.write_text(md, encoding="utf-8")
        update_index_pending(info, slug, out_md.name, is_yt=is_yt)
        update_readme_tutorial_count()

        print("      Committing raw data to GitHub...")
        os.chdir(SKILL_DIR)
        git_add = [str(out_md.relative_to(SKILL_DIR)), str(INDEX_FILE.relative_to(SKILL_DIR))]
        if (SKILL_DIR / "README.md").exists():
            git_add.append("README.md")
        subprocess.run(["git", "add"] + git_add, check=True)
        subprocess.run(["git", "commit", "-m", f"collect: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)

        # Summary for Claude Code
        print(f"\n{'='*60}")
        print(f"  Collection complete. Claude Code: run extraction now.")
        print(f"  Tutorial file: tutorials/{out_md.name}")
        if can_have_frames:
            print(f"  Next: read the timestamped transcript, then run")
            print(f"        python select_frames.py {slug} <ts1> <ts2> ...")
            print(f"        before writing Structured Notes.")
        else:
            print(f"  Frames:        none (text-only extraction)")
        print(f"{'='*60}\n")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()

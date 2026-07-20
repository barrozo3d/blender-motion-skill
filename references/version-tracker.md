# Version Tracker — Blender Releases

**Purpose:** Track which Blender versions are covered and when the release channel was last checked.
Used by the auto-version-check rule in SKILL.md.

---

## Last Check
- **last_checked:** 2026-07-18
- **checked_by:** Skill maintenance session

## Known Versions (covered)
| Version | Coverage | Date |
|---------|----------|------|
| 5.2 LTS (current) | tutorials/everything-new-in-blender-52-lts.md + tutorials/everything-new-in-blender-52-geometry-nodes.md; summarized in references/blender-versions.md | 2026-07-18 |
| 5.1 and earlier | references/blender-versions.md feature tables | 2026-05 |

## How to Check for New Versions
1. Fetch `https://developer.blender.org/docs/release_notes/` (index of all release notes)
2. If a version newer than the table above appears:
   a. Fetch its sub-pages (at `https://developer.blender.org/docs/release_notes/<X.Y>/`)
   b. Add its features to `references/blender-versions.md` (version table + feature tables + migration notes)
   c. Add a row to Known Versions here; update last_checked
   d. Commit and push: `git commit -m "update: Blender <X.Y> release notes ingested"`
3. If no new version: just update last_checked.

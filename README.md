# Music Video Director

A Codex-compatible skill for directing high-impact, editable music videos inside [OpenFilm](https://github.com/openfilm/openfilm). It combines the song, canonical lyrics and supplied images/footage with storyboarding, motion typography, VFX treatment, and a local review loop.

**Status:** v0.1.0 — orchestration plus dependency-free media inventory and timing validators. No claim of autonomous word alignment or VFX generation yet.

## Installation

From your OpenFilm project, install the skill for Codex:

```bash
npx skills add luigicollesi/music-video-director
```

If OpenFilm Desktop lists external skills as disabled, enable `music-video-director` under Settings → Agents → Codex and start a new session.

## Local requirements

Python 3 and FFmpeg's `ffprobe` for optional asset inventory. OpenFilm provides composition, editing and rendering. No Scenario, Remotion or paid account is required.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/inspect_media.py /path/to/assets --output /path/to/project/analysis/media.json
python3 scripts/validate_timing.py references/timing-example.json
```

## Planned milestones

1. v0.1 — creative-direction protocol, quality gates, media metadata inventory and tests.
2. v0.2 — optional local beat/onset analysis and verified lyric alignment; the timing schema and structural validator are already implemented.
3. v0.3 — reusable cinematic VFX recipes with smoke, shatter, fire, frost and rifts (real plates/shaders).
4. v0.4 — frame review and automated render quality reporting.
5. v1.0 — end-to-end reproducible evaluation on a complete original music video.

## Guardrails

Keep the original audio intact; don't invent lyric times; use licensed media; do not spend credits or upload files without approval; do not replace OpenFilm's native timeline; check actual renders before declaring success.

MIT licensed.

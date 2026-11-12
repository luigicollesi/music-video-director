---
name: music-video-director
description: Orchestrate editable music videos in OpenFilm from an original song, lyrics, images and footage. Use for symbolic storyboards, precise lyric timing, kinetic typography, cinematic VFX planning, local-first production and render QA.
license: MIT
---

# Music Video Director

Direct and produce music videos with OpenFilm as the source-of-truth editor. This skill is an orchestrator, not a second video editor. Load only the reference relevant to the current phase.

## Production contract

- Keep the supplied master audio unchanged unless explicitly authorized. The soundtrack sets the timeline; never infer exact timestamps from BPM.
- Supplied lyrics are authoritative. Align words to the recording and mark uncertain timings rather than inventing them.
- Preserve visual symbolism and focal subjects even during visually dense, extravagant sequences. Increase effects in negative space or instrumental moments.
- Favor footage, real VFX plates, particle simulations, shaders and well-composited assets over simplistic shapes pretending to be photorealistic effects. Quality outranks effect count.
- Keep the film editable in native `film.html` tracks and deterministic HTML shots. A shot's `window.film.frame(t)` must be reproducible for arbitrary, out-of-order times.
- Use only authorized/licensed media. Record URLs, license, attribution and permission for each external asset.
- Never spend credits, generate paid assets, upload private media to third parties or download copyrighted footage without explicit approval.
- Never claim a render passed review without actually inspecting it.

## Phase 0: Environment and available capabilities

When running inside OpenFilm Desktop, use the executable/path provided by the app. Do not invoke `npx openfilm@latest`, launch a second Studio, or switch to Remotion/Scenario as the editor. Read the local OpenFilm manual and `openfilm skill edit`, `openfilm skill media`, and optionally `openfilm skill canvas`.

Discover installed complementary skills for this session. Scenario skills are advice until the Scenario MCP is actually connected; do not assume paid model calls are available or permitted. Prefer OpenFilm and local FFmpeg.

## Phase 1: Asset and audio intake

- Read the user's source files and existing project's instructions. Inspect actual images and footage, not filenames alone.
- Run `python3 <skill-folder>/scripts/inspect_media.py <assets-folder> --output <project>/analysis/media.json` when Python 3 and FFprobe are available.
- Record each asset's shot content, symbols, rights, dimensions, orientation, duration, frame rate and usable segments. Keep original filenames intact.
- Determine actual song duration, sections, transitions, phrasing and energy map. Match lyric cues by listening/visual inspection or validated alignment tools. A waveform is not a transcript.

## Phase 2: Direction

Read `references/direction.md`. Author `analysis/creative-brief.md`, `analysis/timing.json`, `analysis/asset-ledger.csv` and `analysis/shot-plan.md`. The plan must map each lyrical moment to symbolism, source media, shots, text cues, camera motion, VFX treatment and expected screen readability. Do not create non-existent source assets.

## Phase 3: Production

Read `references/effects.md`. Establish a controlled visual vocabulary with contrasting levels of intensity. Reuse relevant assets; blend VFX with depth, lighting, masking, alpha and motion blur. Choose OpenFilm's native library, real overlay plates or local generators as appropriate. Keep text orthography correct, respect the exact sung onset and protect faces and narrative details.

Build the first representative scenes and inspect them with the app-provided `openfilm look` before scaling to the full song. Iterate only on failed intervals. Keep full-length audio continuous.

## Phase 4: Review and delivery

Read `references/quality-gates.md`. Use `openfilm look`, FFprobe, representative frame samples, playback checks and export validation. Verify timings, lyric display, narrative consistency, legibility, missing assets, determinism, audio duration, visual artifacts and source rights. Report what was measured and what remains uncertain.

Deliver an editable OpenFilm project, export if requested, source ledger, timing plan and QA report. Never state that content was rendered, generated or tested when the corresponding tool did not run.

## Optional complementary skills

- `scenario-kinetic-music-video`: concepts for sung-onset typography; implement locally unless Scenario use is approved.
- `scenario-motion-loops`: local deterministic Canvas loop patterns.
- `scenario-storyboards`, `scenario-asset-analysis`: planning and catalog patterns.
- `scenario-quality-gate`, `scenario-refine-loop`: review patterns.
- `scenario-video-editing`, `scenario-video-color-grade`: adapt via OpenFilm/FFmpeg first.
- `scenario-video-assembly`: reference only; OpenFilm remains the timeline authority.
- `scenario-seedance-music-video`: only if its service, access and spending are explicitly approved.

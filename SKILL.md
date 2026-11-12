---
name: music-video-director
description: Direct and refine editable music videos in Agente Videomaker (OpenFilm engine) from audio, lyrics and supplied media; selectively use local VFX, timing and QA helpers without duplicating the editor or invoking paid Scenario services.
license: MIT
---

# Music Video Director

Own the *creative decisions and final integration*, not every specialist operation. Use the running Agente Videomaker/OpenFilm editor as the single timeline and render authority. Read `references/routing.md` **only when the task needs another skill**.

## Fast path (default)

1. Determine the requested change and the actual project state. Do not repeat existing analysis, inventory, transcription, storyboard or render unless their inputs changed.
2. Use built-in OpenFilm tools and already-produced assets first. Read its `edit` instructions only when needed; use `media` or `canvas` only for relevant tasks. Inside Desktop, use the app-provided CLI; never launch a second Studio or run `npx openfilm@latest`.
3. Make the smallest useful change and inspect the affected interval with `openfilm look` when available. Do not render or recheck unaffected parts.
4. If the native path is genuinely insufficient, consult **at most one complementary skill for that specific subtask**. Its output is input to the same OpenFilm project, not a new project or competing timeline.
5. Keep a short record of chosen method, evidence, unresolved issues and reused assets. Only create full planning files when the task is full-film production or requests them.

## Routing contract

- Complementary skills are **optional**. Installed is not the same as accessible, authorized, cost-free or useful.
- Match the **requested operation**, not a keyword such as “music video.” Don't load all skills, recursively load their dependencies, or call an MCP tool just to see whether it might help.
- Before opening another skill, identify its exact expected deliverable, the missing native capability, and whether it reuses current inputs. If none is concrete, skip it.
- Prefer a short, relevant subsection or local script over reading an entire large skill. Never copy the specialist's whole pipeline into the main plan.
- For a local helper, inspect its requirements and invocation before executing. Test on a small sample; avoid costly full-length conversions.
- Scenario generation, analysis, Quality Gate, uploads and cloud editing may require connected MCP, authorization, credits or Enterprise access. No paid call or private upload without explicit consent. Offline fallback: OpenFilm/FFmpeg or report a limitation.
- Preserve users' approved media and original music master. Supplied lyrics are authoritative; never infer verified timestamps from tempo alone.

## Only for a new full-length music video

- Inventory assets once using `scripts/inspect_media.py` if metadata is missing; this script uses FFprobe and **does not** understand visual content.
- Build one compact asset ledger, section/timing map and shot plan. Consult `references/direction.md` if narrative decisions are genuinely unresolved, and `references/media-analysis.md` when timing metadata needs explanation.
- Validate the timing structure with `scripts/validate_timing.py`. The validator cannot verify sung onsets.
- Produce and approve a representative sequence, then reuse the visual vocabulary and existing shots. Maintain one continuous master soundtrack.
- Read `references/effects.md` only for advanced custom treatments. Focus on cinematic footage, plates, masking, lighting and compositing rather than basic shapes presented as photorealistic VFX.

## Review and delivery

Review changed shots and transitions first. For final delivery, consult `references/quality-gates.md` and inspect the *actual* output. Report measured checks separately from unverified assumptions. Preserve editable `film.html` shots and deterministic `window.film.frame(t)` behavior; use licensed media only.

**Stop condition:** if the project already satisfies the requested change and the relevant interval passes review, deliver. Do not invoke other skills to “improve” a passing result.

# Selective orchestration — one specialist per concrete subtask

This is a **decision table**, not a list of skills to load. The default choice in every row is the platform's existing editor, FFmpeg or an already available asset. Inspect the exact installed skill name in the current session: inside the platform, names can be namespaced (for example `local-...` or `scenario-labs-...`). Do not assume the `npx skills list` name is the same as the name presented to the agent.

| Missing capability / task | Optional specialist | Precise output to reuse in OpenFilm | Do not invoke when |
| --- | --- | --- | --- |
| Seamless Canvas background or reusable animated loop | `scenario-motion-loops` | Deterministic loop HTML or rendered overlay with correct period | Static image/parallax or native OpenFilm loop is already enough |
| Nontrivial cinematic grade or LUT matching | `scenario-video-color-grade` | A local `.cube` LUT or graded preview from its local scripts | Native correction already achieves the look; numpy/scipy/Pillow unavailable and not worth adding |
| Complex sung-onset kinetic typography | `scenario-kinetic-music-video` | Specific timing/type-animation pattern, not its entire Scenario/three.js production pipeline | Simple title animation, or user's lyric cues are already adequate |
| Existing audio needs section/cut analysis | `scenario-seedance-music-video` | *Only* a local analysis artifact from its `scripts/song.py` after dependency review | No need for beat analysis, or native timing is already verified |
| Continuity-heavy cast / shot-board problem | `scenario-storyboards` | A concise reference/shot-consistency method | No shared character or existing storyboard is sufficient |
| Specific repeated output failure | `scenario-refine-loop` | Small rubric, root cause, one-change fix, stop threshold | A simple inspect-and-fix cycle is enough |
| Assets already in Scenario and need paid analysis/control maps | `scenario-asset-analysis` | One specifically requested analysis/map result | Local images or visual inspection suffice; no MCP/credits |
| Assets already on Scenario need cloud post-processing/keying | `scenario-video-editing` | One processed clip or mask | FFmpeg, native effects or local code suffice |
| Scenario Enterprise image QA explicitly requested | `scenario-quality-gate` | Enterprise score/diagnostics for an image | Any routine frame QA; service/entitlement is unverified |
| Export cannot be made with platform and user explicitly requests Scenario composition | `scenario-video-assembly` | External assembly artifact, clearly secondary | **Normal music-video work:** never build a second timeline |

## Decision procedure

1. **Reuse**: does the requested artifact already exist and meet the requested criteria? If yes, stop.
2. **Native**: can OpenFilm, its built-in effects, FFmpeg or a short local transformation produce it at the required quality? If yes, use that.
3. **Specific gap**: select exactly one relevant specialist with a named output, expected input and acceptable local dependencies. If two match, use the narrower one.
4. **Cost and dependencies**: verify files actually exist and tools work; never assume the external service is connected. Require approval before paid generation or upload.
5. **Return to editor**: import only the useful result and validate the changed interval. Do not inherit alternate project structures, competing render engines or every quality gate from the specialist.

It is valid to use *different* specialists on different substasks in a whole film; the one-per-subtask limit prevents redundant pipelines, not useful specialization. Prefer no specialist for straightforward work.

## Context and execution budget

- No proactive reading of ten skill files.
- Do not eagerly run `--help`, `pip install`, MCP discovery, environment checks or full-media analysis for unused skills.
- A second specialist for the **same issue** needs evidence the first option failed and a new deliverable/approach; otherwise stop or ask for a tradeoff.
- Read only the files actually needed; don't produce duplicate ledgers, shot lists, transcripts, timelines, or QA reports.
- If a helper's setup costs more than a small local edit, skip it.
- Report the chosen helper and *why* it saved work, or say native tools sufficed.

## Scenario-specific boundaries

- `scenario-quality-gate` is documented as an **Enterprise image** quality gate, not an ordinary video review tool.
- `scenario-video-assembly` uses Scenario compositing services. It is not a substitute for OpenFilm timeline editing.
- `scenario-asset-analysis` uses paid Scenario tool calls; no offline automatic image semantic analysis is supplied by this skill.
- `scenario-storyboards` usually describes Scenario image-generation workflows; reuse only planning/continuity methods without MCP.
- `scenario-kinetic-music-video` contains a substantial independent engine; **extract techniques only**, unless the user explicitly opts into an alternative rendering workflow.
- `scenario-motion-loops` and `scenario-video-color-grade` include local code, but require their own dependencies. Do not treat their scripts as zero-cost in setup time.
- `scenario-seedance-music-video` has local audio-analysis code, but its cloud generation phase is separate and not automatically authorized.

None of these skills can, by mere installation, guarantee new photorealistic VFX. That requires real footage/plates, capable shader/compositing work, or separately authorized generation.

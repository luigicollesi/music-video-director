# Efficiency audit (qualitative, pre-benchmark)

## Baseline inspection

The previous orchestrator listed all ten Scenario skills at the end of `SKILL.md`, advised discovery up front and prescribed full production artifacts for every request. It did not define dispatch triggers, cost/credit gates or outputs for each handoff.

Inspection of the installed copies in `agente-videomaker/.agents/skills/` identified:

- Most Scenario skills describe their own extensive workflows, external calls and cross-skill dependencies. Reading them all duplicates planning and consumes context.
- `scenario-quality-gate` targets an Enterprise image-quality tool. It cannot replace local video QA.
- `scenario-video-assembly` runs a separate Scenario compositor, creating a conflicting second editor.
- `scenario-kinetic-music-video` has a full Scenario-plus-code engine; importing all of it into an OpenFilm edit is expensive.
- `scenario-motion-loops`, `scenario-video-color-grade` and `scenario-seedance-music-video` include potentially useful local helpers, subject to dependencies.
- `scenario-asset-analysis` and `scenario-video-editing` require actual connected Scenario services for their cloud features.

## Expected result of the lean router

| Measure | Old behavior risk | Lean policy |
| --- | --- | --- |
| Loaded specialist instructions | Up to ten large skills and their references | Zero by default, one for the particular gap |
| Duplicate timelines | Scenario assembly plus OpenFilm possible | OpenFilm is sole production authority |
| Duplicated planning docs | Full brief + ledger + board even for tiny edits | Full artifacts only on full-film creation |
| Unapproved spending | Cloud tools casually discovered | External paid calls explicitly gated |
| QA scope | Entire film repeated for small edits | Only changed range; full-film review at delivery |

These are **design expectations**, not measured cost or latency savings. A meaningful evaluation must compare equivalent tasks in the same agent/model with identical assets, record tokens used, tool calls, elapsed time, exported correctness and revision count. Do not promise a percent speedup without measurements.

## Suggested A/B tests

1. **Minor edit:** change one lyric overlay on an existing sequence; compare total calls and changed-only review.
2. **Background loop:** create one seamless 12-second animated bridge; compare native attempt against optional loop helper.
3. **Color treatment:** grade an existing 10-second clip; compare native grading against a dedicated LUT when justified.
4. **Full film:** use an approved original song, storyboard and assets; ensure only one timeline and no unapproved Scenario calls.

For each task log: selected specialist (or none), how many skill files were read, external calls/credits, time to first correct preview, rework count, and subjective quality assessed on actual frames. Reject the orchestrator if it increases overhead without a corresponding quality or reliability gain.

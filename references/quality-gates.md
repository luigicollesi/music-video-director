# Music video quality gates

A production cannot be marked delivered merely because the timeline renders.

1. **Asset integrity:** validate every referenced path and its duration; confirm licenses and source URLs. Never assume arbitrary online footage is free to reuse.
2. **Audio integrity:** measure output duration; audition start, middle, transitions and end; original master stays untouched unless authorized.
3. **Lyrics:** check spelling against supplied master text and sample actual entry/exit onsets. Confidence must distinguish verified from estimated.
4. **Visual grammar:** inspect opening/mid/closing frames in every scene plus transition boundary frames. Evaluate readability, symbolism and variation.
5. **VFX craftsmanship:** inspect mask halos, depth, shadows, motion blur, mismatched resolution, clipping, abrupt jumps and frame flicker.
6. **OpenFilm determinism:** use `openfilm look`; investigate any nondeterministic output, missing fonts and truncated text.
7. **Comfort:** identify harsh full-screen flashes and continuous rapid-flicker patterns. Reduce/replace potentially photosensitive effects.
8. **Export:** use FFprobe to inspect container, codecs, duration, fps, dimensions and audio. Export must include the intended continuous soundtrack.
9. **Reporting:** write `analysis/qa-report.md` with checks actually run, evidence, issues and fixes. A skipped check is not a pass.

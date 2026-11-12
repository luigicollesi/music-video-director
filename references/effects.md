# Cinematic VFX and motion treatments

Choose an effect based on what the line means, what the music does and what remains readable. Browse OpenFilm's effects and transitions before inventing a new implementation.

## Burning and ash

Use high-resolution fire/smoke plates, alpha mattes, animated luminance masks, edge distortion and motivated lighting. Words can emerge from burning footage or disintegrate into ember particles. A flat orange SVG gradient is not photorealistic fire.

## Frost and fragmentation

Combine frost textures, crystalline cracks, displacement and shatter masks whose fragments follow plausible motion. Align transitions to impacts. Preserve face recognizability and avoid arbitrary jagged polygons masquerading as physical 3D shards.

## Rift and screen tear

Layer foreground and background footage through an animated matte. Add differentiated parallax, rim lighting, displacement and shadow; place the revealing subject where it stays readable.

## Text motion

Use phrase-level anchoring and optional per-word onset. Words may fly in, burn, freeze, smear, fragment, rotate or emerge from occluding footage. Display canonical spelling and accents. Never allow excessive text density to make a narrative image unreadable.

## Camera and composition

Use parallax, intentional scale changes, handheld motion only when motivated, depth-of-field, lens flare where lighting warrants, and controlled chromatic distortion. The movement must be deterministic at every time value.

## Technical recipe record

For each custom effect track: source plate/path, resolution, alpha/transparency behavior, mask, animation function, visible duration, frame cost and fallback. Prefer a reusable native OpenFilm effect where it reaches the target quality.

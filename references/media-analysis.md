# Local asset inventory

Use `scripts/inspect_media.py` with Python 3 and system FFprobe. It reads metadata only; it does not recognize faces, identify narrative content, detect beats, transcribe, align vocals or upload media.

```bash
python3 scripts/inspect_media.py /path/to/assets --output /path/to/project/analysis/media.json
```

Review original images and representative video frames separately. Enrich each entry in `analysis/asset-ledger.csv` with symbolism, source/creator, license or written permission, attribution, allowed modifications, narrative relevance and selected time range.

A file is not necessarily suitable because the resolution is high: evaluate compression artifacts, motion quality, brightness, framing, focal subject, transparency and consistency with the project's visual direction.

## Timing schema

The JSON format described in `references/timing-example.json` is an interchange contract for the director and the validator. Times are in seconds from the actual master start, not relative to sections. An unverified onset is explicitly marked `verified: false`; merely setting a timestamp does not make it accurate.

Validate with:

```bash
python3 scripts/validate_timing.py /path/to/project/analysis/timing.json
```

This checks structural consistency only. It cannot prove whether a word is sung at the stated second; that requires audio review.

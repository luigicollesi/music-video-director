#!/usr/bin/env python3
"""Local media metadata inventory using FFprobe; no uploads or Python dependencies."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".mp3", ".wav", ".flac", ".m4a", ".ogg", ".aac", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}


def probe(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
        capture_output=True, text=True, timeout=30, check=False,
    )
    if result.returncode:
        return {"error": result.stderr.strip() or f"ffprobe failed ({result.returncode})"}
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"error": f"invalid ffprobe JSON: {exc}"}
    streams = []
    for s in data.get("streams", []):
        streams.append({k: s.get(k) for k in ("codec_type", "codec_name", "width", "height", "r_frame_rate", "sample_rate", "channels", "duration") if s.get(k) is not None})
    return {"duration": data.get("format", {}).get("duration"), "streams": streams}


def inventory(root):
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    records = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXTENSIONS or p.is_symlink():
            continue
        rec = {"path": str(p.relative_to(root)), "bytes": p.stat().st_size}
        try:
            rec.update(probe(p))
        except (OSError, subprocess.TimeoutExpired) as exc:
            rec["error"] = str(exc)
        records.append(rec)
    return {"root": str(root), "assets": records, "count": len(records)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assets", help="directory containing local audio, images and video")
    parser.add_argument("--output", help="write JSON to this path (otherwise stdout)")
    args = parser.parse_args(argv)
    try:
        result = inventory(args.assets)
    except ValueError as exc:
        parser.error(str(exc))
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        out = Path(args.output).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
        print(f"Inspected {result['count']} media files; wrote {out}", file=sys.stderr)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()

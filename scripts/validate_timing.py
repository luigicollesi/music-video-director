#!/usr/bin/env python3
"""Validate structural consistency of a music-video timing JSON; not an audio aligner."""
import argparse
import json
import math
import sys
from pathlib import Path


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate(data):
    issues = []
    if not isinstance(data, dict):
        return ["root must be an object"]
    if data.get("schema_version") != 1:
        issues.append("schema_version must be 1")
    audio = data.get("audio")
    if not isinstance(audio, dict) or not finite_number(audio.get("duration_seconds")) or audio["duration_seconds"] <= 0:
        issues.append("audio.duration_seconds must be a positive finite number")
        duration = None
    else:
        duration = audio["duration_seconds"]

    sections = data.get("sections")
    if not isinstance(sections, list) or not sections:
        issues.append("sections must be a nonempty list")
        sections = []
    ids = set()
    prev_end = None
    for i, s in enumerate(sections):
        tag = f"sections[{i}]"
        if not isinstance(s, dict):
            issues.append(f"{tag} must be an object")
            continue
        identifier = s.get("id")
        if not isinstance(identifier, str) or not identifier:
            issues.append(f"{tag}.id must be a nonempty string")
        elif identifier in ids:
            issues.append(f"duplicate section id {identifier}")
        else:
            ids.add(identifier)
        start, end = s.get("start"), s.get("end")
        if not finite_number(start) or not finite_number(end) or start < 0 or end <= start:
            issues.append(f"{tag} needs a valid start/end interval")
            continue
        if duration is not None and end > duration + 1e-4:
            issues.append(f"{tag} exceeds master duration")
        if prev_end is not None and start < prev_end - 1e-4:
            issues.append(f"{tag} overlaps the previous section")
        prev_end = end

    lyrics = data.get("lyrics", [])
    if not isinstance(lyrics, list):
        issues.append("lyrics must be a list")
        lyrics = []
    for i, cue in enumerate(lyrics):
        tag = f"lyrics[{i}]"
        if not isinstance(cue, dict):
            issues.append(f"{tag} must be an object")
            continue
        if not isinstance(cue.get("text"), str) or not cue["text"].strip():
            issues.append(f"{tag}.text must be a nonempty string")
        start, end = cue.get("start"), cue.get("end")
        if not finite_number(start) or not finite_number(end) or start < 0 or end <= start:
            issues.append(f"{tag} needs a valid start/end interval")
        elif duration is not None and end > duration + 1e-4:
            issues.append(f"{tag} exceeds master duration")
        if cue.get("section") not in ids:
            issues.append(f"{tag}.section must refer to a section id")
        if not isinstance(cue.get("verified"), bool):
            issues.append(f"{tag}.verified must be a boolean")
    return issues


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read timing data: {exc}", file=sys.stderr)
        return 2
    issues = validate(data)
    if issues:
        for issue in issues:
            print(f"ERROR: {issue}", file=sys.stderr)
        return 1
    print("Timing structure PASS (audio alignment not verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

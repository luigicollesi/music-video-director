import importlib.util
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("validate_timing", Path(__file__).parents[1] / "scripts" / "validate_timing.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def sample():
    return {
        "schema_version": 1,
        "audio": {"path": "master.wav", "duration_seconds": 20},
        "sections": [{"id": "intro", "start": 0, "end": 5}, {"id": "verse", "start": 5, "end": 20}],
        "lyrics": [{"text": "hello", "start": 6, "end": 7, "section": "verse", "verified": False}],
    }


class TimingTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(mod.validate(sample()), [])

    def test_overlapping_sections(self):
        data = sample()
        data["sections"][1]["start"] = 4
        self.assertTrue(any("overlaps" in x for x in mod.validate(data)))

    def test_exceeds_audio(self):
        data = sample()
        data["lyrics"][0]["end"] = 21
        self.assertTrue(any("exceeds" in x for x in mod.validate(data)))

    def test_unknown_section(self):
        data = sample()
        data["lyrics"][0]["section"] = "missing"
        self.assertTrue(any("section id" in x for x in mod.validate(data)))

    def test_boolean_timestamps_are_invalid(self):
        data = sample()
        data["lyrics"][0]["start"] = True
        self.assertTrue(any("valid start/end" in x for x in mod.validate(data)))

    def test_unverified_cue_is_allowed(self):
        data = sample()
        data["lyrics"][0]["verified"] = False
        self.assertEqual(mod.validate(data), [])


if __name__ == "__main__":
    unittest.main()

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
ROUTING = (ROOT / "references" / "routing.md").read_text(encoding="utf-8")


class OrchestrationContractTests(unittest.TestCase):
    def test_default_is_native_not_scenario(self):
        self.assertIn("Use built-in OpenFilm tools", SKILL)
        self.assertIn("at most one complementary skill for that specific subtask", SKILL)
        self.assertIn("The default choice in every row", ROUTING)

    def test_no_bulk_load_instruction(self):
        self.assertIn("Don't load all skills", SKILL)
        self.assertIn("No proactive reading of ten skill files", ROUTING)

    def test_require_explicit_cost_approval(self):
        self.assertIn("No paid call or private upload without explicit consent", SKILL)
        self.assertIn("Enterprise image", ROUTING)

    def test_openfilm_is_single_editor(self):
        self.assertIn("single timeline and render authority", SKILL)
        self.assertIn("not a substitute for OpenFilm timeline editing", ROUTING)

    def test_ten_scenario_skills_have_targeted_routing(self):
        names = set(re.findall(r"`(scenario-[a-z-]+)`", ROUTING))
        expected = {
            "scenario-asset-analysis", "scenario-kinetic-music-video",
            "scenario-motion-loops", "scenario-quality-gate",
            "scenario-refine-loop", "scenario-seedance-music-video",
            "scenario-storyboards", "scenario-video-assembly",
            "scenario-video-color-grade", "scenario-video-editing",
        }
        self.assertEqual(names, expected)


if __name__ == "__main__":
    unittest.main()

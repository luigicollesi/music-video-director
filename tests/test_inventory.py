import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import importlib.util

SPEC = importlib.util.spec_from_file_location("inspect_media", Path(__file__).parents[1] / "scripts" / "inspect_media.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class InventoryTests(unittest.TestCase):
    def test_inventory_is_recursive_and_ignores_non_media(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "nested").mkdir()
            (root / "nested" / "film.mp4").write_bytes(b"fake video")
            (root / "song.wav").write_bytes(b"fake audio")
            (root / "notes.txt").write_text("ignore")
            with patch.object(mod, "probe", return_value={"duration": "12.5", "streams": []}) as mocked:
                result = mod.inventory(root)
            self.assertEqual(result["count"], 2)
            self.assertEqual([x["path"] for x in result["assets"]], ["nested/film.mp4", "song.wav"])
            self.assertEqual(mocked.call_count, 2)

    def test_probe_failure_does_not_abort_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "bad.webm").write_bytes(b"invalid")
            with patch.object(mod, "probe", return_value={"error": "invalid media"}):
                result = mod.inventory(tmp)
            self.assertEqual(result["assets"][0]["error"], "invalid media")

    def test_missing_folder(self):
        with self.assertRaises(ValueError):
            mod.inventory("/unlikely/nonexistent/music-video-director-test-folder")


if __name__ == "__main__":
    unittest.main()

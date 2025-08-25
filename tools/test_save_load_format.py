"""Quick test harness for the save/load format changes.
Run this from the repo root with the virtualenv active.
"""
from pathlib import Path
import sys, os
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))
# Also add the src folder so imports like `windows.popup` (which are top-level in the app)
# resolve when running tests from the tools directory.
sys.path.insert(0, str(repo_root / 'src'))
import tempfile
import json

from src.utils.record_file_management import RecordFileManagement


class Dummy:
    def __init__(self):
        self.macro = type(
            "M",
            (),
            {
                "macro_events": {
                    "events": [
                        {"type": "cursorMove", "timestamp": 0, "x": 1, "y": 2}
                    ]
                },
                "playback": False,
            },
        )()
        self.settings = type(
            "S",
            (),
            {
                "settings_dict": {
                    "Saving": {"Compact_json": True},
                    "Playback": {},
                    "Minimization": {},
                    "After_Playback": {},
                }
            },
        )()
        self.menu = type(
            "MB",
            (),
            {
                "text_config": {},
                "file_menu": type("F", (), {"entryconfig": lambda *a, **k: None})(),
            },
        )()
        self.text_content = {"file_menu": {}, "global": {}}
        self.prevent_record = False
        self.macro_saved = True
        self.macro_recorded = True
        # Current file path (None or str)
        self.current_file = None


# Create tempfile and test both legacy and wrapper
root = Dummy()
manager = RecordFileManagement(root, root.menu)

# Test legacy write (.pmr)
with tempfile.NamedTemporaryFile(suffix=".pmr", delete=False) as tmpf:
    root.current_file = tmpf.name
    manager.save_macro()
    tmp_path = Path(tmpf.name)
    with open(tmp_path, "r", encoding="utf-8") as r:
        loaded = json.load(r)
    assert "events" in loaded and "payload" not in loaded

# Test wrapped write (.pmr2)
with tempfile.NamedTemporaryFile(suffix=".pmr2", delete=False) as tmpf:
    root.current_file = tmpf.name
    manager.save_macro()
    tmp_path = Path(tmpf.name)
    with open(tmp_path, "r", encoding="utf-8") as r:
        loaded = json.load(r)
    assert loaded.get("format") == "pmr" and "payload" in loaded

print("save/load format tests passed")

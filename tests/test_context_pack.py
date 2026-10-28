"""Tests for the context pack builder. Uses made-up data only (Level 0).

Run from the repo root:  PYTHONPATH=src python3 -m unittest discover tests
"""

import copy
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from mike_os import context_pack as cp
from mike_os.notion_client import simplify_page

FIXTURE = Path(__file__).parent / "fixtures" / "synthetic_project.json"
NOW = datetime(2026, 1, 10, tzinfo=timezone.utc)
FRESH_NOW = datetime(2026, 1, 3, tzinfo=timezone.utc)


def load():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class FingerprintTests(unittest.TestCase):
    def test_same_records_same_fingerprint_regardless_of_order(self):
        a, b = load(), load()
        b["linked"]["decisions"].append(copy.deepcopy(b["linked"]["work_queue"][0]))
        a["linked"]["decisions"].insert(0, copy.deepcopy(a["linked"]["work_queue"][0]))
        self.assertEqual(cp.fingerprint(a), cp.fingerprint(b))

    def test_linked_record_change_changes_fingerprint(self):
        before, after = load(), load()
        after["linked"]["work_queue"][0]["properties"]["Status"] = "Done"
        self.assertNotEqual(cp.fingerprint(before), cp.fingerprint(after))

    def test_project_edit_time_changes_fingerprint(self):
        before, after = load(), load()
        after["project"]["last_edited"] = "2026-01-05T10:00:00Z"
        self.assertNotEqual(cp.fingerprint(before), cp.fingerprint(after))


class WritePackTests(unittest.TestCase):
    def test_rerun_with_same_records_does_not_rewrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path, changed = cp.write_pack(load(), Path(tmp), NOW, "v0.5")
            self.assertTrue(changed)
            first = path.read_text()
            path, changed = cp.write_pack(load(), Path(tmp), datetime(2026, 1, 11, tzinfo=timezone.utc), "v0.5")
            self.assertFalse(changed)
            self.assertEqual(first, path.read_text())

    def test_changed_gap_rules_rewrite_pack(self):
        with tempfile.TemporaryDirectory() as tmp:
            path, _ = cp.write_pack(load(), Path(tmp), NOW, "v0.5")
            path.write_text(path.read_text().replace("## Gaps", "## Old gap rules"))
            _, changed = cp.write_pack(load(), Path(tmp), NOW, "v0.5")
            self.assertTrue(changed)

    def test_changed_records_rewrite_pack(self):
        with tempfile.TemporaryDirectory() as tmp:
            cp.write_pack(load(), Path(tmp), NOW, "v0.5")
            changed_snapshot = load()
            changed_snapshot["linked"]["skills"][0]["properties"]["Status"] = "Approved"
            _, changed = cp.write_pack(changed_snapshot, Path(tmp), NOW, "v0.5")
            self.assertTrue(changed)


class GapTests(unittest.TestCase):
    def test_fresh_project_flags_only_structural_gaps(self):
        gaps = " ".join(cp.find_gaps(load(), FRESH_NOW))
        self.assertIn("No review date", gaps)
        self.assertIn("No session recaps", gaps)
        self.assertIn("Example Outline Skill", gaps)
        self.assertNotIn("No activity", gaps)
        self.assertNotIn("untouched", gaps)

    def test_stale_project_and_open_items_flagged(self):
        stale = load()
        gaps = " ".join(cp.find_gaps(stale, datetime(2026, 2, 1, tzinfo=timezone.utc)))
        self.assertIn("No activity since 2026-01-02", gaps)
        self.assertIn("Collect reference links", gaps)

    def test_recent_skill_edit_does_not_hide_stale_project(self):
        snapshot = load()
        snapshot["linked"]["skills"][0]["last_edited"] = "2026-01-31T09:00:00Z"
        gaps = " ".join(cp.find_gaps(snapshot, datetime(2026, 2, 1, tzinfo=timezone.utc)))
        self.assertIn("No activity since 2026-01-02", gaps)

    def test_missing_next_action_and_manager_flagged(self):
        snapshot = load()
        snapshot["project"]["properties"]["Next Action"] = None
        snapshot["project"]["properties"]["Operating Manager"] = None
        gaps = " ".join(cp.find_gaps(snapshot, FRESH_NOW))
        self.assertIn("stalled", gaps)
        self.assertIn("No Operating Manager", gaps)

    def test_both_vertical_needs_justification(self):
        snapshot = load()
        snapshot["project"]["properties"]["Vertical"] = "Both"
        self.assertIn("Both Justification", " ".join(cp.find_gaps(snapshot, FRESH_NOW)))


class SensitivityTests(unittest.TestCase):
    def test_health_always_refused(self):
        snapshot = load()
        snapshot["project"]["properties"]["Area"] = "Health"
        with self.assertRaises(cp.PackRefused):
            cp.check_sensitivity(snapshot, allow_personal=True)

    def test_personal_needs_opt_in(self):
        snapshot = load()
        snapshot["project"]["properties"]["Vertical"] = "Personal"
        with self.assertRaises(cp.PackRefused):
            cp.check_sensitivity(snapshot)
        cp.check_sensitivity(snapshot, allow_personal=True)


class RenderTests(unittest.TestCase):
    def test_render_includes_sources_and_provenance(self):
        text = cp.render(load(), NOW, "v0.5")
        self.assertIn("status: DRAFT", text)
        self.assertIn("https://www.notion.so/bbbb0000000000000000000000000001", text)
        self.assertIn(f"source_fingerprint: {cp.fingerprint(load())}", text)
        self.assertIn("## Session recaps\n\nNone linked.", text)

    def test_pipe_in_value_does_not_break_table(self):
        snapshot = load()
        snapshot["project"]["properties"]["Outcome"] = "A | B"
        self.assertIn("A \\| B", cp.render(snapshot, NOW, "v0.5"))


class SimplifyPageTests(unittest.TestCase):
    def test_notion_api_page_converted(self):
        page = {
            "id": "aaaa0000-0000-0000-0000-000000000001",
            "url": "https://www.notion.so/x",
            "last_edited_time": "2026-01-01T10:00:00.000Z",
            "properties": {
                "Name": {"type": "title", "title": [{"plain_text": "Example "}, {"plain_text": "Plan"}]},
                "Status": {"type": "select", "select": {"name": "In Progress"}},
                "Notes": {"type": "rich_text", "rich_text": []},
                "Review Date": {"type": "date", "date": None},
                "Project": {"type": "relation", "relation": [{"id": "bbbb0000-0000-0000-0000-000000000001"}]},
                "Task ID": {"type": "unique_id", "unique_id": {"prefix": "LLM-", "number": 17}},
            },
        }
        result = simplify_page(page)
        self.assertEqual(result["id"], "aaaa0000000000000000000000000001")
        self.assertEqual(result["properties"]["Name"], "Example Plan")
        self.assertEqual(result["properties"]["Status"], "In Progress")
        self.assertIsNone(result["properties"]["Notes"])
        self.assertIsNone(result["properties"]["Review Date"])
        self.assertEqual(result["properties"]["Project"], ["bbbb0000000000000000000000000001"])
        self.assertEqual(result["properties"]["Task ID"], "LLM-17")


if __name__ == "__main__":
    unittest.main()

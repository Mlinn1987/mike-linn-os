"""Builds a one-page context pack for a Mike OS project.

A context pack summarizes a project's current state from Notion, with a link
to the source of every fact and a list of gaps worth fixing. The same records
and rules always produce the same pack, so an unchanged project never
creates a new version.

Run it (from the repo root):

    PYTHONPATH=src python3 -m mike_os.context_pack <project-id>

Options:
    --snapshot FILE       Build from a saved snapshot instead of live Notion.
    --save-snapshot FILE  Save the records read from Notion (keep out of the repo).
    --out-dir DIR         Where to write the pack (default docs/context-packs).
    --allow-personal      Allow Personal-vertical projects. Health is never allowed.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from mike_os import __version__
from mike_os.config import REPO_ROOT, load_config

STALE_DAYS = 14
OPEN_STATUSES = {"Not Started", "In Progress", "Needs Review", "Upcoming", "Blocked", "Draft", "Queued", "Reviewing"}

# Each Notion store linked to Projects: its config key, relation property,
# title property, and the fields shown in the pack.
LINKED_STORES = {
    "decisions": ("decisions_and_activity", "Project", "Entry", ["Date", "Type"]),
    "session_recaps": ("session_recaps", "Project", "Recap", ["Created"]),
    "work_queue": ("work_queue", "Project", "Action", ["Status", "Priority", "Due"]),
    "llm_tasks": ("llm_task_log", "Related Project", "Task", ["Status", "Task Type"]),
    "skills": ("skills_registry", "Related Project", "Skill name", ["Status", "Approved Version", "Steward"]),
    "qa": ("cross_model_qa", "Project", "QA Request", ["Status", "Verdict"]),
}

STORE_HEADINGS = {
    "decisions": "Decisions and activity",
    "session_recaps": "Session recaps",
    "work_queue": "Work Queue",
    "llm_tasks": "LLM tasks",
    "skills": "Skills",
    "qa": "Cross-Model QA",
}

PROJECT_FIELDS = [
    "Outcome", "Current Milestone", "Next Action", "Operating Manager", "Status",
    "Portfolio", "Priority", "Vertical", "Area", "Both Justification", "Review Date",
]


class PackRefused(Exception):
    """The project holds data that must not leave Notion."""


def read_snapshot(client, config: dict, project_id: str) -> dict:
    """Reads a project and everything linked to it from Notion."""
    project_id = project_id.replace("-", "")
    stores = config["stores"]
    return {
        "project": client.get_page(project_id),
        "linked": {
            key: client.query_related(stores[store]["data_source_id"], relation, project_id)
            for key, (store, relation, _, _) in LINKED_STORES.items()
        },
    }


def check_sensitivity(snapshot: dict, allow_personal: bool = False) -> None:
    props = snapshot["project"]["properties"]
    if props.get("Area") == "Health":
        raise PackRefused("Health projects are Level 2 and stay in Notion.")
    if props.get("Vertical") == "Personal" and not allow_personal:
        raise PackRefused("Personal project: rerun with --allow-personal if it holds no Level 2 detail.")


def fingerprint(snapshot: dict) -> str:
    """A hash of every record the pack draws on, linked records included."""
    canonical = json.dumps(
        {"project": snapshot["project"], "linked": {k: sorted(v, key=lambda r: r["id"]) for k, v in snapshot["linked"].items()}},
        sort_keys=True,
    )
    return hashlib.sha256(canonical.encode()).hexdigest()


def _parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def find_gaps(snapshot: dict, now: datetime) -> list[str]:
    props = snapshot["project"]["properties"]
    linked = snapshot["linked"]
    gaps = []

    if not props.get("Next Action"):
        gaps.append("**No primary Next Action.** Under Mike OS rules the project counts as stalled.")
    if not props.get("Operating Manager"):
        gaps.append("**No Operating Manager.** Nobody owns updates to this project.")
    if not props.get("Current Milestone"):
        gaps.append("**No current milestone.**")
    if props.get("Vertical") == "Both" and not props.get("Both Justification"):
        gaps.append("**Vertical is Both but there is no Both Justification.**")

    # Skills are shared across projects and edited for their own reasons
    # (the daily check-in skill changes every morning), so they don't count
    # as activity on this project.
    edits = [_parse_time(snapshot["project"]["last_edited"])]
    edits += [_parse_time(r["last_edited"]) for key, records in linked.items() if key != "skills" for r in records]
    latest = max((e for e in edits if e), default=None)
    if latest and (now - latest).days > STALE_DAYS:
        gaps.append(f"**No activity since {latest.date()}** (over {STALE_DAYS} days). Nothing on the project or its linked work has changed.")

    if props.get("Portfolio") == "Active" and not props.get("Review Date"):
        gaps.append("**No review date** on an Active project.")
    if not linked["session_recaps"]:
        gaps.append("**No session recaps** are linked to this project.")

    for skill in linked["skills"]:
        if skill["properties"].get("Status") == "Draft":
            gaps.append(f"**Skill still in draft:** {_title(skill, 'Skill name')}.")

    for key in ("work_queue", "llm_tasks", "qa"):
        _, _, title_prop, _ = LINKED_STORES[key]
        for record in linked[key]:
            edited = _parse_time(record["last_edited"])
            if record["properties"].get("Status") in OPEN_STATUSES and edited and (now - edited).days > STALE_DAYS:
                gaps.append(
                    f"**Open {STORE_HEADINGS[key]} item untouched since {edited.date()}:** "
                    f"{_title(record, title_prop)} ({record['properties']['Status']})."
                )
    return gaps


def _title(record: dict, title_prop: str) -> str:
    return record["properties"].get(title_prop) or "(untitled)"


def _cell(value) -> str:
    if value is None or value == [] or value == "":
        return "—"
    if isinstance(value, list):
        value = ", ".join(map(str, value))
    return str(value).replace("|", "\\|").replace("\n", " ")


def _sort_key(record: dict, fields: list[str]):
    date = record["properties"].get(fields[0]) if fields[0] in ("Date", "Created", "Due") else None
    return (date or record["last_edited"] or "", record["id"])


def render(snapshot: dict, now: datetime, constitution_version: str) -> str:
    project = snapshot["project"]
    props = project["properties"]
    name = props.get("Name") or "(untitled project)"
    fp = fingerprint(snapshot)

    lines = [
        "---",
        f"pack: {slug(name)}",
        f"pack_version: {fp[:12]}",
        f"source_fingerprint: {fp}",
        f"generated_at: {now.isoformat(timespec='seconds')}",
        f"generator: mike_os.context_pack {__version__}",
        f"constitution_version: {constitution_version}",
        "status: DRAFT — generated; not delivered or applied anywhere",
        "sensitivity: Level 1 (internal)",
        "---",
        "",
        f"# Context pack: {name}",
        "",
        "> Generated from live Notion records. Notion remains the primary home for this project; this pack is a copy.",
        "",
        "## Project record",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Project | [{_cell(name)}]({project['url']}) (`{project['id']}`) |",
        f"| Record last edited | {_cell(project['last_edited'])} |",
    ]
    lines += [f"| {field} | {_cell(props.get(field))} |" for field in PROJECT_FIELDS]

    for key, (_, _, title_prop, fields) in LINKED_STORES.items():
        records = sorted(snapshot["linked"][key], key=lambda r: _sort_key(r, fields), reverse=True)
        lines += ["", f"## {STORE_HEADINGS[key]}", ""]
        if not records:
            lines.append("None linked.")
            continue
        lines.append("| " + " | ".join(["Record"] + fields + ["Last edited"]) + " |")
        lines.append("|" + "---|" * (len(fields) + 2))
        for r in records:
            cells = [f"[{_cell(_title(r, title_prop))}]({r['url']})"]
            cells += [_cell(r["properties"].get(f)) for f in fields]
            cells.append(_cell(r["last_edited"]))
            lines.append("| " + " | ".join(cells) + " |")

    gaps = find_gaps(snapshot, now)
    lines += ["", "## Gaps", ""]
    lines += [f"{i}. {gap}" for i, gap in enumerate(gaps, 1)] if gaps else ["No gaps found by the automatic checks."]
    lines += [
        "",
        "## Provenance",
        "",
        "Read from Notion at the generated_at time above. "
        "Linked records are those whose relation property points at this project. "
        "The fingerprint covers the project and every linked record, so a change to any of them produces a new pack version.",
        "",
    ]
    return "\n".join(lines)


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _without_timestamp(text: str) -> str:
    return re.sub(r"^generated_at: .*$", "", text, count=1, flags=re.MULTILINE)


def write_pack(snapshot: dict, out_dir: Path, now: datetime, constitution_version: str) -> tuple[Path, bool]:
    """Writes the pack unless an identical one exists. Returns (path, changed).

    Packs are compared with their timestamps removed, so a rerun on the same
    records is a no-op, but a change to the records or to the gap rules is not.
    """
    path = out_dir / f"{slug(snapshot['project']['properties'].get('Name') or snapshot['project']['id'])}.md"
    text = render(snapshot, now, constitution_version)
    if path.exists() and _without_timestamp(path.read_text(encoding="utf-8")) == _without_timestamp(text):
        return path, False
    out_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a Mike OS context pack from Notion.")
    parser.add_argument("project_id")
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--save-snapshot", type=Path)
    parser.add_argument("--out-dir", type=Path, default=REPO_ROOT / "docs" / "context-packs")
    parser.add_argument("--allow-personal", action="store_true")
    args = parser.parse_args(argv)

    config = load_config()
    if args.snapshot:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    else:
        from mike_os.notion_client import NotionClient

        snapshot = read_snapshot(NotionClient(), config, args.project_id)
    if args.save_snapshot:
        args.save_snapshot.write_text(json.dumps(snapshot, indent=2, sort_keys=True), encoding="utf-8")

    try:
        check_sensitivity(snapshot, args.allow_personal)
    except PackRefused as e:
        print(f"Refused: {e}", file=sys.stderr)
        return 2

    path, changed = write_pack(snapshot, args.out_dir, datetime.now(timezone.utc), config["constitution_version"])
    print(f"{'Wrote' if changed else 'Unchanged'}: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Notion integration

**Status:** First slice built: read-only context packs. Tested with made-up data, and run once on live records that Claude read through its own Notion connection. **Not yet run against the Notion API**, because no `NOTION_TOKEN` exists yet.

**Purpose:** Read live Mike OS state (projects, tasks, decisions, recaps) and produce compact context packs and read-only backups.

## Context packs

```
PYTHONPATH=src python3 -m mike_os.context_pack <project-id>
```

- Reads the project and every record linked to it in Decisions & Activity, Session Recaps, Work Queue, LLM Task Log, Skills Registry and Cross-Model QA.
- Writes `docs/context-packs/<project-name>.md`, with a link to the source of every fact and a list of gaps.
- Rerunning on unchanged records changes nothing. A change to any linked record produces a new pack version.
- Refuses Health projects (Level 2). Personal projects need `--allow-personal`.
- `--snapshot FILE` builds from saved records instead of live Notion. Snapshots are real data: keep them outside the repo.

Code: `src/mike_os/context_pack.py` (builder) and `src/mike_os/notion_client.py` (API reader). Tests: `PYTHONPATH=src python3 -m unittest discover tests`.

## Access needed

A Notion **integration token**: a private key that lets a script read your workspace.

1. Go to https://www.notion.so/profile/integrations and create an internal integration with **read content** access only.
2. In Notion, open each Mike OS database (Projects, Decisions & Activity, Session Recaps, Work Queue, LLM Task Log, Skills Registry, Cross-Model QA), then **⋯ → Connections** and add the integration.
3. Save the token as `NOTION_TOKEN` in the cloud environment's secrets. Never put it in the repo or in Notion.

Database IDs are in `config/notion-sources.example.yaml`.

**May:** Read records and fetch schemas.
**Not yet:** Write to any database.

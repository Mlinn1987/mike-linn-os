# Notion integration

**Status:** Not started. **First build target.**

**Purpose:** Read live Mike OS state (projects, tasks, decisions, recaps) and produce compact context packs and read-only backups.

**First slice:** A read-only context pack for one project (Cross-Model Context Sync), with links to the source records and read times.

**Access needed:** A Notion integration token with read access to the Mike OS databases. Database IDs are in `config/notion-sources.example.yaml`.

**May:** Read records and fetch schemas.
**Not yet:** Write to any database. That needs ownership checks and Mike's approval first.

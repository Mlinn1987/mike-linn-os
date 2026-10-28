# src

Shared Python code, in the `mike_os` package.

| Module | Purpose |
|---|---|
| `mike_os/config.py` | Loads `config/notion-sources.example.yaml` |
| `mike_os/notion_client.py` | Read-only Notion API client |
| `mike_os/context_pack.py` | Builds project context packs |

Run anything with `PYTHONPATH=src python3 -m mike_os.<module>` from the repo root, or install once with `pip install -e .`.

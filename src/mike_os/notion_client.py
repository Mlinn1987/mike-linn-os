"""Read-only Notion API client for building context packs.

Needs a Notion integration token in the NOTION_TOKEN environment variable
(see .env.example). It only reads. Nothing here writes to Notion.

Records are converted to a simple shape so the pack builder never depends on
Notion's API format:

    {"id": ..., "url": ..., "last_edited": ..., "properties": {name: value}}
"""

import json
import os
import urllib.error
import urllib.request

API_URL = "https://api.notion.com/v1"
API_VERSION = "2025-09-03"  # The version that introduced data sources.


class NotionError(RuntimeError):
    pass


class NotionClient:
    def __init__(self, token: str | None = None):
        self.token = token or os.environ.get("NOTION_TOKEN")
        if not self.token:
            raise NotionError(
                "NOTION_TOKEN is not set. Create a Notion integration, share the "
                "Mike OS databases with it, and put its token in environment secrets."
            )

    def _request(self, method: str, path: str, body: dict | None = None) -> dict:
        request = urllib.request.Request(
            f"{API_URL}{path}",
            method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Notion-Version": API_VERSION,
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as e:
            raise NotionError(f"Notion {method} {path} failed: {e.code} {e.read().decode()}") from e

    def get_page(self, page_id: str) -> dict:
        return simplify_page(self._request("GET", f"/pages/{page_id}"))

    def query_related(self, data_source_id: str, relation_property: str, page_id: str) -> list[dict]:
        """Every record in a data source whose relation property links to page_id."""
        body = {"filter": {"property": relation_property, "relation": {"contains": page_id}}}
        records = []
        while True:
            result = self._request("POST", f"/data_sources/{data_source_id}/query", body)
            records += [simplify_page(page) for page in result["results"]]
            if not result.get("has_more"):
                return records
            body["start_cursor"] = result["next_cursor"]


def simplify_page(page: dict) -> dict:
    return {
        "id": page["id"].replace("-", ""),
        "url": page.get("url"),
        "last_edited": page.get("last_edited_time"),
        "properties": {name: _value(prop) for name, prop in page.get("properties", {}).items()},
    }


def _value(prop: dict):
    kind = prop.get("type")
    data = prop.get(kind)
    if kind in ("title", "rich_text"):
        return "".join(part.get("plain_text", "") for part in data) or None
    if kind in ("select", "status"):
        return data["name"] if data else None
    if kind == "multi_select":
        return [option["name"] for option in data]
    if kind == "date":
        return data["start"] if data else None
    if kind == "relation":
        return [item["id"].replace("-", "") for item in data]
    if kind in ("url", "checkbox", "number", "created_time", "last_edited_time"):
        return data
    if kind == "unique_id":
        return f"{data.get('prefix') or ''}{data['number']}" if data else None
    return None

# Decision: Repo becomes a supplemental source of truth

- **Date:** 2026-10-23
- **Status:** Approved by Mike in a Claude Code session, 2026-10-23
- **Proposed by:** Claude (Claude Code)
- **Notion log:** Recorded in Decisions & Activity

## Decision

The GitHub repo becomes a second source of truth alongside Notion, so the system doesn't depend on one tool. To prevent conflicts, **every kind of information has exactly one primary home**:

| Primary home: repo | Primary home: Notion |
|---|---|
| Governance (constitution, protocols, standards) | Projects, tasks, running to-do list |
| Skills and prompts | Approvals and Decisions & Activity |
| Code and integration config | Session recaps and briefings |
| Architecture docs | Anything updated daily |

The repo also keeps **read-only backups** of Notion databases. A backup never overrides Notion.

## Why

- Reduces reliance on Notion (outages, pricing changes, export limits).
- Rules and skills benefit from GitHub's full version history and change review.
- Daily operating state stays in Notion, which is easier to use and works well on mobile.

## Tradeoffs and follow-ups

- Moving governance and skills out of Notion means ChatGPT and Claude need to read them from the repo or from a synced copy. Until that path works, Notion keeps the current approved versions, and the repo versions are drafts.
- Backups include only Level 0–1 content. Health, financial and other Level 2 fields must be left out or redacted (see `2026-10-23-data-sensitivity-levels.md`).
- This changes Mike OS architecture, so it should also be recorded in Notion's Decisions & Activity with Mike as approver.

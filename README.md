# Mike Linn OS

> **Status: DRAFT — initial structure (2026-10-23).** Nothing here is deployed yet.

This repository is the code and governance home for **Mike OS**, Mike Linn's operating system for business and personal work. It works alongside Notion, ChatGPT and Claude.

## How it fits together

| Tool | Role |
|---|---|
| **Notion** | Primary home for live operating state: projects, tasks, approvals, recaps, briefings |
| **This repo (GitHub)** | Primary home for rules, skills, prompts, architecture docs, code and integration settings. It also keeps read-only backups of Notion. |
| **ChatGPT** | Operating interface: portfolio manager, morning briefing |
| **Claude** | Operating interface: reviewer, nightly readout, implementation through Claude Code |

Every kind of information has **exactly one primary home**. Any copy elsewhere is a backup or cache, never a competing version. See [docs/decisions/2026-10-23-source-of-truth-split.md](docs/decisions/2026-10-23-source-of-truth-split.md).

## What's where

| Folder | Purpose |
|---|---|
| `CLAUDE.md` | Startup rules Claude reads at the beginning of every session |
| `docs/architecture.md` | How the whole system works |
| `docs/decisions/` | Dated decisions, each marked **Approved** or **Proposal** |
| `docs/handoffs/` | Handoff documents received from other models, kept as reference |
| `docs/context-packs/` | One-page project summaries generated from Notion, each with source links |
| `governance/` | *(coming)* Constitution, protocols and standards, once moved over from Notion |
| `skills/` | *(coming)* Approved skills and reusable prompts |
| `config/` | Settings such as Notion database IDs. **Never passwords or keys.** |
| `integrations/` | One folder per connected tool (Notion, YouTube, Wix, Gemini, email, analytics) |
| `src/` | Shared code used by more than one integration |
| `schemas/` | Data shapes the code checks against |
| `tests/` | Tests, using **made-up** example data only |
| `backups/notion/` | Read-only backups of Notion (Level 0–1 content only) |

## Ground rules

- **Data sensitivity:** follow the four levels in [docs/decisions/2026-10-23-data-sensitivity-levels.md](docs/decisions/2026-10-23-data-sensitivity-levels.md). Health, finances, family details and other Level 2 material stay in Notion. Secrets never go in this repo.
- **Saving to GitHub:** see [docs/decisions/2026-10-23-github-change-permissions.md](docs/decisions/2026-10-23-github-change-permissions.md).

## Integration status

| Integration | Status |
|---|---|
| Notion | Not started — first build target |
| YouTube | Not started |
| Wix | Not started |
| Gemini | Not started |
| Email | Not started |
| Analytics | Not started |

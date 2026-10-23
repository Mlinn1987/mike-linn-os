# Mike OS architecture

> **Status: DRAFT.** This summarizes the ChatGPT handoff of 2026-10-23 (`docs/handoffs/2026-10-23-chatgpt-architecture-handoff.md`) plus decisions approved on 2026-10-23. The full handoff holds the detail and the source links. Where they differ, the decisions in `docs/decisions/` take precedence.

## What Mike OS is

A shared operating system for Mike's business and personal work. Notion holds live operating state. This repo holds the rules, skills and code. ChatGPT and Claude are operating interfaces with separately assigned jobs. Their project files and private memory are caches, not sources of truth.

## Sources of truth

| Information | Primary home | Copies |
|---|---|---|
| Projects, Work Queue, Running To-Do List | Notion | Repo backups (read-only) |
| Decisions & Activity, approvals | Notion | Repo backups (read-only) |
| Session Recaps, briefings, readouts | Notion | Repo backups (read-only) |
| Constitution, protocols, standards | **Repo** *(after migration from Notion)* | Notion links |
| Skills and prompts | **Repo** *(after migration)* | ChatGPT and Claude project files |
| Architecture, integration code and config | Repo | — |

## Project hierarchy

**Goal → Project → Milestone → Workflow → Next Action**

Every active project has one current milestone and one primary Next Action. If the primary action is missing, the project is stalled.

These fields stay independent: **Status** (Not Started / In Progress / Needs Review / Done), **Portfolio** (Active / Next / Maintain / Waiting / Backlog / Paused / Complete), **Priority** (P0–P3), **Vertical** (Business / Personal / Both), and **Area**.

Areas: Velocity, AI Lab, Creator, Doctronic, Health, Properties, Chaotic Good, Personal, Admin.

## Roles

| Scope | Assignment |
|---|---|
| Portfolio and weekly review | ChatGPT manages; Claude reviews |
| Mike OS v1 | ChatGPT (P0) |
| Cross-Model Context Sync | Claude (P1) |
| Morning briefing, 9:00 AM Pacific (11:00 AM follow-up) | ChatGPT |
| Nightly readout, 9:00 PM Pacific | Claude |
| Every other project | Read its Operating Manager field in Notion |

Mike assigns one Operating Manager per project, and the other model reviews. Changing a manager requires Mike's approval and a recorded handoff.

## Authority

Constitution v0.5 defines four levels: A0 observe, A1 organize facts, A2 reversible internal execution, and A3 consequential external action (closed). Repo-specific permissions are set in `docs/decisions/2026-10-23-github-change-permissions.md`.

## Integrations

Each tool gets its own folder in `integrations/`. Shared code lives in `src/`. Build order and status are tracked in `integrations/README.md`.

## Known open issues (from the handoff)

1. Native schedule routing, notification delivery and fresh-session retrieval are unverified.
2. Cross-Model Context Sync deployment claims haven't been reproduced.
3. The Decisions & Activity "Approved By" field doesn't list Mike as an option.
4. Business / Personal / Both context isolation hasn't been validated in live sessions.

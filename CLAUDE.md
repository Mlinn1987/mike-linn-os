# CLAUDE.md — startup rules for Mike Linn OS

Mike is a marketer who is new to GitHub and code. Explain technical steps in plain language, and define jargon the first time it comes up.

## Before doing work

1. Read `README.md` and `docs/architecture.md`.
2. Check `docs/decisions/` for Approved decisions. Treat anything marked **Proposal** as not yet in force.
3. For any project work, read the project's live record in Notion first. Cached state, including this repo's backups, is not enough before a write.

## Sources of truth

Each kind of information has one primary home (`docs/decisions/2026-10-23-source-of-truth-split.md`):

- **Notion:** projects, tasks, running to-do list, approvals, decision log, recaps, briefings.
- **This repo:** governance, skills, prompts, architecture, code, integration config.

Never edit a copy and treat it as the original. If the two disagree, report the conflict instead of overwriting either one.

## Authority

- Claude Code is an implementation surface. Receiving work in this repo does not make Claude the Operating Manager of a project. Check the project's Operating Manager field in Notion.
- Never record an AI as the approver of anything. Only Mike approves.
- Saving changes (`docs/decisions/2026-10-23-github-change-permissions.md`):
  - **No approval needed:** commits and pushes to draft branches; drafts and docs; typo and formatting fixes.
  - **Mike's approval needed:** merging into `main`, changing repo visibility, deleting files or history, and anything with outside effects (publishing, sending, spending, deploying).

## Data sensitivity (`docs/decisions/2026-10-23-data-sensitivity-levels.md`)

- **Level 0–1** (templates, examples, project names, workflows, Notion IDs): allowed here.
- **Level 2** (health, finances, family, addresses, other people's personal details, confidential client info): stays in Notion. Reference it by link or ID only.
- **Level 3** (passwords, API keys, tokens): never in this repo or in Notion.

Before every commit, check the changes for Level 2 or 3 material. If you find any, stop and tell Mike.

## Working style

- Prove one useful path before building general infrastructure.
- Mark drafts visibly with **DRAFT**.
- Keep "generated", "delivered", "applied" and "verified in a fresh session" as separate facts. Never claim a later one because an earlier one passed.

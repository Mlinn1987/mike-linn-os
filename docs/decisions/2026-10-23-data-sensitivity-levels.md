# Decision: Four data sensitivity levels

- **Date:** 2026-10-23
- **Status:** Approved by Mike in a Claude Code session, 2026-10-23
- **Proposed by:** Claude (Claude Code)
- **Notion log:** Not yet recorded in Decisions & Activity

## Decision

| Level | Examples | Rule |
|---|---|---|
| **0: Safe to share** | Templates, made-up examples, code | Allowed anywhere |
| **1: Internal** | Project names, workflows, Notion database IDs, business rules | Allowed in this private repo |
| **2: Sensitive** | Health, finances, family, home addresses, other people's personal details, confidential client information | Stays in Notion. The repo references it by link or ID only. |
| **3: Secrets** | Passwords, API keys, access tokens | Never in the repo or in Notion. Kept in a secure settings store, such as environment secrets. |

## Why a private repo still needs limits

- It can be made public by accident.
- Every connected tool, integration and collaborator can read all of it.
- Deleting a file doesn't remove it from Git history.
- A provider breach is unlikely but possible.

## Follow-ups

- Add an automatic check that blocks commits containing likely Level 2 or 3 content.
- Notion backups must leave out or redact Level 2 fields.

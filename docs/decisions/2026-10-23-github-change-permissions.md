# Decision: Standing permission for saving changes to this repo

- **Date:** 2026-10-23
- **Status:** Approved by Mike in a Claude Code session, 2026-10-23
- **Proposed by:** Claude (Claude Code)
- **Notion log:** Not yet recorded in Decisions & Activity

## Decision

Constitution v0.5 lists "commit" as a closed A3 consequential action. For this private repo, Mike grants a standing permission that narrows that:

| No approval needed | Mike's approval needed |
|---|---|
| Commits and pushes to draft branches | Merging into `main` |
| Drafts and documentation | Changing repo visibility (e.g. making it public) |
| Typo and formatting fixes | Deleting files or rewriting history |
| | Anything with outside effects: publishing, sending, spending, deploying |

## Why

- Commits to a private repo are reversible, because Git keeps every version.
- A private commit publishes nothing to anyone.
- Cloud sessions are wiped when they end, so unsaved work is lost.

## Scope

This applies only to this repository. It doesn't reopen A3 elsewhere in Mike OS.

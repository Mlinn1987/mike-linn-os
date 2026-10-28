# Decision: Act on Mike's requests without re-asking

- **Date:** 2026-10-28
- **Status:** Approved by Mike in a Claude Code session, 2026-10-28
- **Proposed by:** Mike
- **Replaces:** `2026-10-23-github-change-permissions.md`
- **Notion log:** Recorded in Decisions & Activity

## Decision

When Mike asks for something, Claude does it, including merging into `main` and writing to Notion. A request is the approval. Claude doesn't ask again for permission it already has.

Claude stops and asks only in two cases:

| Contextual uncertainty | Truly dangerous actions |
|---|---|
| The request is unclear, or could reasonably mean two different things | Deleting files, pages, databases or branches |
| Sources conflict (Notion vs. repo, or a record changed since it was read) | Rewriting or force-pushing history |
| The change goes beyond what Mike asked for and would change how the system works | Making the repo, or anything else, public |
| Something unexpected turns up mid-task | Outside effects: publishing, sending, spending, deploying |
| | Handling Level 2 or 3 data (see `2026-10-23-data-sensitivity-levels.md`) |

Routine work that follows directly from a request needs no separate approval: commits, pushes, branches, pull requests, merges, docs, and Notion updates.

## Why

Asking again for something Mike has already requested adds friction without adding safety. Git keeps every version, so repo changes can be undone. The real risks are irreversible or public actions, and those still need a check.

## How it's enforced

`.claude/settings.json` in this repo allows Git commands, GitHub calls for this repo and Notion tools without a prompt. It still prompts for force pushes, branch and history deletion, `rm -rf`, and Notion deletes and moves.

## Scope

Mike OS work done through this repo and the Mike OS Notion workspace. It doesn't change Operating Manager assignments, and it doesn't let an AI approve anything on Mike's behalf.

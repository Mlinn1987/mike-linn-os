# Integrations

> **Status: DRAFT.** One folder per connected tool. Each folder's README covers what the integration is for, what access it needs, and what it may and may not do.

## Build order

| # | Integration | Status | Why this order |
|---|---|---|---|
| 1 | [Notion](notion/) | Not started | Everything else reads from or reports to Notion |
| 2 | [YouTube](youtube/) | Not started | Core Creator pipeline |
| 3 | [Gemini](gemini/) | Not started | Video-specialist model for the Creator pipeline |
| 4 | [Analytics](analytics/) | Not started | Measures results across YouTube and websites |
| 5 | [Wix](wix/) | Not started | Websites and landing pages |
| 6 | [Email](email/) | Not started | Sending is an outside effect, so it comes last |

The order is a proposal and can change.

## Rules for every integration

- **Read before write.** Start each integration read-only, and add writing only after reading works.
- **Keys stay out of the repo.** Put variable names in `.env.example`. Real values go in environment secrets.
- **Outside effects need Mike's approval:** publishing, sending, spending, or changing anything public.
- **Level 2 data** passes through without being saved here (see `docs/decisions/2026-10-23-data-sensitivity-levels.md`).

# Decision: Standardize on Python

- **Date:** 2026-10-23
- **Status:** Approved by Mike in a Claude Code session, 2026-10-23
- **Proposed by:** Claude (Claude Code)
- **Notion log:** Recorded in Decisions & Activity

## Decision

Use **Python** for shared code and most integrations. Use JavaScript only where a platform requires it. Wix Velo, Wix's coding tool, is the likely exception, and that code would live in `integrations/wix/`.

## Why

- Python is beginner-friendly and easy to read.
- It has official or well-supported libraries for Notion, YouTube, Gemini, Gmail and Google Analytics.
- One main language keeps shared code, tests and setup simple.

## Tradeoff

Wix work may need a second language. That cost stays contained to one folder.

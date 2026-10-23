---
pack: cross-model-context-sync
pack_version: 2026-10-23.01
status: DRAFT — first manual prototype; generated, not delivered or applied anywhere
generated_at: 2026-10-23
generated_by: Claude (Claude Code), read-only Notion reads
constitution_version: v0.5
sensitivity: Level 1 (internal)
---

# Context pack: Cross-Model Context Sync

> A one-page summary of this project's current state, built from live Notion records. Every fact links to its source. Notion remains the primary home for this project. Nothing in Notion was changed to build this pack.

## Project record

| Field | Value |
|---|---|
| Project | [Cross-Model Context Sync](https://app.notion.com/p/3d3d5ca6aed281919a96dbe3c519a041) (`3d3d5ca6-aed2-8191-9a96-dbe3c519a041`) |
| Record last edited | 2026-09-14T02:25:15Z — **39 days before this pack** |
| Outcome | Claude and ChatGPT both stay current with Mike's project state via Notion as the single source of truth, without Mike manually repeating context between them. |
| Current milestone | Claude-side context cache built: 6 synced docs, a 12-hour Notion reconciliation trigger in the Mike Linn Project, and the Running To-Do List cross-model check-in. ChatGPT-side project context configuration and refresh verification still pending. |
| Primary Next Action | Verify each platform's project context actually refreshes from Notion and reports which version it loaded before substantive work. ChatGPT to configure its own project context and skills from the same Notion records. |
| Operating Manager / Reviewer | Claude / ChatGPT (reviewer derived) |
| Status · Portfolio · Priority | In Progress · Active · P1 |
| Vertical · Area | Both · AI Lab |
| Both justification | Maintains shared model context and routing across both verticals. |
| Review date | Not set |

## Decisions and activity (linked to this project)

| Date | Entry | Type |
|---|---|---|
| 2026-09-14 | [[Mike] Run the Claude nightly round-trip verification today](https://app.notion.com/3dbd5ca6aed28142a393c07f329de7fa) | Decision |
| 2026-09-13 | [[ChatGPT] Cross-platform handoff package 2026-09-13.02 created](https://app.notion.com/3dbd5ca6aed281bb9b66f451d05cb809) | Progress |
| 2026-09-06 | [[Claude] Skills Registry created](https://app.notion.com/3d3d5ca6aed2819884e5d43b9ca01053) | Change |
| 2026-09-06 | [[Claude] Responsibility split agreed for the Notion↔model context integration](https://app.notion.com/3d3d5ca6aed281349ca5d2fec8a6baf4) | Decision |
| 2026-09-05 | [[Claude] Velocity context pack 2026-09-05.01 generated](https://app.notion.com/3d3d5ca6aed281968383cb12c41c734c) | Progress |

**Agreed role split (2026-09-06):** Claude maintains the Notion integration and its own project context and skills. ChatGPT configures its own context and skills from the same Notion records and reviews the integration. Notion holds approved state. Mike approves governing changes.

## Skills linked to this project

| Skill | Status | Approved version | Steward |
|---|---|---|---|
| [Cross-Model Notion Sync](https://app.notion.com/3d3d5ca6aed28176b4d4eb2b97735c5c) | **Draft** | "0.1 (draft — not yet through Rule 5 approval or cross-model QA)" | Claude |
| [Running To-Do Check-in](https://app.notion.com/3d3d5ca6aed281948a3de9285c5662ae) | Approved | 1.2 (Mike, 2026-09-12) | ChatGPT |

## Related open tasks (LLM Task Log, not linked to any project)

| Task | Status | Last edited |
|---|---|---|
| [LLM-17: Claude adopt account-wide briefing connection standard v0.2](https://app.notion.com/3d9d5ca6aed281d88348dcf69e0fdb72) | Blocked | 2026-09-14 |
| [LLM-8: Observe Claude's first scheduled briefing review on September 9](https://app.notion.com/3d5d5ca6aed281c698d8c8b6f8abc7b2) | In Progress | 2026-09-09 |
| [LLM-3: Verify the first scheduled Claude briefing review](https://app.notion.com/3d4d5ca6aed281d68312c28335629143) | Blocked | 2026-09-07 |

## Empty: nothing linked

- Session Recaps: **none**
- Work Queue: **none**
- Cross-Model QA: **none**

---

## Gap list

Ordered by importance. **Proposals only.** Claude is this project's Operating Manager in Notion, but changing records needs a separate, deliberate step, and some changes need Mike's approval.

1. **The Outcome conflicts with today's decision.** It says "Notion as the single source of truth", but Mike approved the repo as a supplemental source of truth on 2026-10-23. *Proposal:* reword to "Notion and the Mike OS repo, each the primary home for its defined content." This is a governing change, so it needs Mike's approval.
2. **The project has stalled for 39 days.** The record, its milestone and every linked item stop at 2026-09-14. No recap, Work Queue item or QA record explains the gap. The Next Action is still valid but has no owner on the ChatGPT side, and no date.
3. **The "6 synced docs + 12-hour trigger" claim can't be verified from Notion.** The milestone reports it, but no record shows a run log, the last successful run, or which docs are included. The handoff flags the same gap.
4. **There's no refresh evidence on either side.** No record shows either platform reporting which Notion version it loaded, which is the core of the Next Action. Generated, delivered, applied and fresh-session-verified remain unproven for both platforms.
5. **The core skill is still a draft.** Cross-Model Notion Sync hasn't been through cross-model QA (Protocol A) or Mike's approval.
6. **Three related tasks aren't linked to any project,** and two look abandoned. LLM-3 and LLM-8 haven't been touched since 2026-09-07 and 2026-09-09. LLM-17 is Blocked, waiting on a Claude session that can edit Claude's own scheduled-task instructions. *Proposal:* link all three to this project, and close or refresh LLM-3 and LLM-8.
7. **The round-trip test result isn't linked here.** The 2026-09-14 test decision is linked, but its outcome (per the handoff, recorded in the 2026-09-15 check-in log) isn't.
8. **The Velocity pack 2026-09-05.01 was never confirmed as applied.** It was generated under Constitution v0.4, now superseded, and marked "not yet applied; Mike uploads it."
9. **No review date is set** for an Active P1 project.

## Suggested primary next action

Mike decides on gap 1 (rewording the Outcome). Then Claude, as Operating Manager, updates this project's milestone and Next Action to reflect the repo-based approach. The next step after that is a repeatable version of this pack, compared against the Claude Project Knowledge documents to check whether they are current.

## Provenance

| Source | Read at | Source last edited |
|---|---|---|
| Project record | 2026-10-23 | 2026-09-14T02:25:15Z |
| Decisions & Activity (filtered by project) | 2026-10-23 | — |
| Skills Registry (filtered by project) | 2026-10-23 | — |
| LLM Task Log (open tasks matching sync / context / Claude, or ID 17) | 2026-10-23 | LLM-17: 2026-09-14T18:25:44Z |
| Session Recaps, Work Queue, Cross-Model QA (filtered by project) | 2026-10-23 | No rows |

---
title: "Mike OS / Mike Linn — Architecture and Claude Code Repository Handoff"
status: "DRAFT — evidence-based handoff; proposed repo design is not adopted governance"
version: "2026-10-23.01"
prepared_on: "2026-10-23"
timezone: "America/Los_Angeles"
canonical_state: "Notion"
intended_consumer: "Claude Code / GitHub repository"
---

# Mike OS / Mike Linn — Architecture and Claude Code Repository Handoff

## 1. Read this first

Mike OS is Mike Linn's shared operating system for business and personal execution. Notion holds canonical projects, work, decisions, approvals, recaps, skills, and handoffs. ChatGPT and Claude are operating interfaces with separately assigned responsibilities; their project files and private memory are caches.

This document transfers architectural context to Claude Code and a future GitHub repository. It does not establish that a repository, GitHub integration, generator, native project updater, or new schedule exists. It does not transfer project ownership to Claude Code. Repository recommendations below are proposals for implementation, distinct from approved operating rules.

**Primary implementation direction:** preserve the working Notion system; make its context retrieval, provenance, verification, and handoffs easier to execute and inspect. Avoid building a replacement operating system.

### Evidence and coverage

Prepared from the supplied `mike-os--chatgpt-handoff.md`, live reads of the Notion sources listed at the end, and the conversation context supplied with this request. Live reads occurred October 23, 2026. This is a synthesis of available structural evidence, not an exhaustive export of every ChatGPT/Claude conversation or Notion record.

“Verified read” means the record was retrieved successfully. It does not mean its historical implementation claims were independently reproduced. Some Notion pages carry unverified native verification metadata despite explicitly documenting Mike's approval; those are separate concepts.

No Claude account, Claude Code installation, GitHub repository, notification delivery, or native scheduler configuration was inspected. This session performed Notion reads, not a new Notion write-capability test. Historical write and round-trip results below are attributed to their records.

## 2. Identity, scope, and platform boundaries

| Name | Meaning |
|---|---|
| Mike OS | The operating system and canonical Notion workspace |
| Mike OS v1 | Existing system project; preserve stable ID `3d2d5ca6-aed2-816c-9f14-d613bbccde30` |
| Mike Linn in ChatGPT | Designated October 12 as the broader ChatGPT home for portfolio planning and continuity |
| Morning Briefing in ChatGPT | Dedicated conversational briefing home established October 19 within the broader Mike OS / Mike Linn ecosystem |
| Mike Linn in Claude | Historical Claude platform project reference; separate native storage from ChatGPT |
| Claude Code / GitHub repo | Intended implementation consumer of this document; deployment and authority are not established by this handoff |

The October 19 Morning Briefing specialization supplements the October 12 broader identity mapping. It does not create a second canonical task store or prove schedules route into that ChatGPT project.

### Portfolio coverage

Canonical Areas currently exposed in the Projects schema: Velocity, AI Lab, Creator, Doctronic, Health, Properties, Chaotic Good, Personal, and Admin.

These span agency/client work, AI production systems, creator/video pipelines, Doctronic content work, property/rental work, personal work, health/athletic work, and shared administration. Active scope and priorities must be read from Notion rather than inferred from historical conversation activity.

The supplied Admin handoff covers Mike OS v1 and Writing Rules, not the entire portfolio. The September cross-platform package groups context into seven friendly platform homes: Mike OS, Velocity Agency, AI Production Systems, Creator, Doctronic, Properties, and Health and Athletic Performance. Friendly names map to canonical Areas and stable project IDs; they are not a new database taxonomy.

## 3. Existing architecture

### Canonical hierarchy

**Goal → Project → Milestone → Workflow → Next Action**

Every active project has one current milestone and one primary Next Action. Recaps may include up to two secondary actions. A missing primary action means the project is stalled.

Notion navigation has four main surfaces:

1. Business: filtered Business and Both records.
2. Personal: filtered Personal and Both records.
3. Shared OS: governance, shared projects, skills, QA, and operating documentation.
4. System Databases: underlying authoritative databases and retained legacy material.

Business and Personal use shared databases with filtered views, not independent copies. Legacy Project Portals and superseded constitutions remain for lineage; they are not the normal operating entry point.

### Authority and ownership

| Scope | Operating assignment |
|---|---|
| Portfolio / weekly review | ChatGPT manager; Claude reviewer |
| Mike OS v1 | ChatGPT; P0; In Progress; Both; Admin |
| Cross-Model Context Sync | Claude; P1; In Progress; Both; AI Lab |
| Morning dialogue | ChatGPT daily |
| Nightly readout | Claude daily |
| Any other project | Read its live Operating Manager field |

Mike assigns one Operating Manager per project. The other model is reviewer. A model cannot acquire ownership merely by receiving the work in a chat or repo. A mid-project change requires Mike's approval, outgoing recap and current state, incoming live read before first write, and an attributed decision log naming both models.

Claude's ownership of the integration does not replace ChatGPT's portfolio assignment or underlying project managers. Claude Code should initially act as a bounded implementation surface, subject to the applicable role and task authorization.

### Existing authority ceiling

The approved Constitution v0.5 defines A0 observation, A1 factual organization, A2 reversible internal execution, and **A3 closed** for consequential external action. Its examples include publish, send, spending beyond budget, commit, important deletion, and major strategic action. Service/model use within a Mike-approved budget is carved out.

A repo is not evidence of a reopened A3 category. Before executing commits, pushes, merges, publishing, paid commitments, or other consequential steps under Mike OS, resolve the applicable current authorization against live governance. Do not silently reinterpret the historical “commit” wording. This handoff authorizes no such action.

Working drafts and routine factual updates do not require new governing approval. Permanent methods, material schema changes, strategic decisions, authority changes, or rules governing future behavior require Mike's approval. Mark draft artifacts visibly.

### Shared-state write rules

- Assigned manager owns factual/reversible Projects, Work Queue, Session Recaps, and Knowledge & Entities updates.
- Manager/producer may prepare QA request fields.
- Reviewer alone owns findings, disagreements, verdict, and reviewer analysis.
- Decisions & Activity is append-only and attributed.
- Non-owners propose changes rather than overwrite.
- Re-read affected records before material writes; cached session state is insufficient.
- Never substitute an AI's identity for Mike's approval.

## 4. Data model and stable integration targets

The following database and collection IDs were exposed by live Notion records. Database IDs and data-source IDs are different; use the correct one for the connector/API operation. Fetch full schemas before building write adapters.

| Store | Database ID | Data-source ID |
|---|---|---|
| Projects | 39c595087f9444d0b973d07e94d92e68 | b0a1d720-0fc3-40b2-8347-db095ea329f9 |
| Knowledge & Entities | 29c421b2e5ca46e795cbbbcb83e4b7b5 | 4965855b-5e82-4d51-9e87-d001ab7b5fee |
| Work Queue | 7c9cdf4488c64e66b774ecffe3c6ae41 | 93c79a4b-42b1-4d1d-ac7a-88ae4a170b08 |
| Decisions & Activity | 03d71bc67f73470183e88fbc5fdd388d | d71bc75b-6af7-4a8d-ad2f-93b16ef30489 |
| Session Recaps | ec509c2f23fe4b149eb15f7463b7c549 | d934eadd-280b-4235-a624-644671cdb12b |
| Running To-Do List | 97cac64a7bde4824ba5515dfa3bb9880 | 4b4510d6-17b3-4b7c-954c-59b9b4f81f91 |
| LLM Task Log | 165e3c822c854f868ff9cf25c25a1b7a | 2897c4aa-ad1c-494e-9cf6-902c29792c2d |
| Skills Registry | af3faa0db7f0438eaa25ed599f1437bf | 021f5112-1d05-45ed-8b2d-effd45b0374a |
| Cross-Model QA | efc3ef9c6dac4047855fa9c9b2b087dc | f5990036-b108-4dc5-8e76-7202081ab55e |

Projects exposes Name, Outcome, Current Milestone, Next Action, Operating Manager, Area, Vertical, Both Justification, Priority, Status, Portfolio, Notes, Related Entities, and Review Date.

Keep these independent:

- **Status:** Not Started / In Progress / Needs Review / Done.
- **Portfolio:** Active / Next / Maintain / Waiting / Backlog / Paused / Complete.
- **Priority:** P0 / P1 / P2 / P3.
- **Vertical:** Business / Personal / Both.
- **Area:** domain classification.

LLM Task Log has its own lifecycle: Upcoming / In Progress / Blocked / Done / Cancelled; Task Type includes Work / Review / Sync / Maintenance. Do not normalize all stores into one status enum. Running-list conversation terms such as “queued” also need explicit schema mapping.

Skills Registry separates Draft/Approved status, Approved Version, Steward, Related Project, and platform-specific implementation fields. A populated “Approved Version” string does not override Status=Draft: Cross-Model Notion Sync explicitly remains draft.

Briefing Checkpoint is a compact continuity cache, not a Current State database. The September 7 efficiency decision explicitly rejects creating a parallel Current State database. Manager Approvals are surfaced from Decisions & Activity, not assumed to be a separate authoritative database.

## 5. Business / Personal separation

Approved September 6: retain shared databases, add Vertical, preserve Area, and use filtered hubs. The implementation record reports 19 projects classified and 60 linked records propagated at that time; those are historical migration counts, not today's totals.

Both mode retrieves summaries first and details only when necessary. Before assigning Both, identify the Business outcome, Personal outcome, why two linked projects are insufficient, and record the justification.

Health detail stays Personal. Only a sanitized operational effect may cross into Business. A broadly accessible implementation repo should contain the operating rules and synthetic examples rather than raw personal records. Repository visibility has not been established; do not treat this handoff as permission to publish private workspace exports.

The architecture record still names live Business, Personal, and Both session validation as remaining work. Do not equate completed schema migration with validated context isolation.

## 6. Daily briefing and cross-model handoff

The approved daily contract supersedes the former odd/even operator rotation.

| Routine | Owner | Intended local timing | Behavior |
|---|---|---|---|
| Morning invitation | ChatGPT | 9:00 AM America/Los_Angeles | Interactive, one actionable decision at a time |
| Conditional follow-up | ChatGPT | 11:00 AM | Once, only if not Completed or Missed |
| Nightly readout | Claude | Default 9:00 PM | Quiet, noninteractive, Check→Expand |

Morning inputs: latest successful Claude Nightly Readout, live Running To-Do items and notes, current project links, Manager Approvals, and shared dated check-in log. Verify important readout claims against canonical records.

Show a concise overview of all outstanding running-list items, including future-dated and undated deferrals. Display resume dates, respect them, and walk decisions one at a time. Future visibility does not mean reopening a deferred decision early.

Nod approvals remain one-line by default; Mike Review items receive a concise explanation. Capture additions, completions, deferrals, decisions, and attribution as the session proceeds.

Silence is unconfirmed. A declined or unanswered 9:00 invitation still permits the one 11:00 follow-up. Explicit decline of that follow-up produces Missed; completion produces Completed. Either suppresses further daily prompting. A completed briefing does not complete unfinished tasks.

Claude's nightly readout covers changes since the previous successful run, completed/open work, contradictions, blockers, decisions, up to three recommended focus items, exact morning inputs, source links, coverage window, and run evidence. A no-change run leaves a short record. Models communicate through Notion; direct private-memory sharing is not assumed.

### Delivery and connection assurance

Native ChatGPT scheduled tasks are the preferred account-wide trigger. Codex morning automation was designated temporary backup pending an end-to-end native test. Claude schedules, Codex automations, and native ChatGPT tasks are separate systems.

Each run checks intended account/workspace, a known canonical record, latest readout, and write capability before claiming synchronization. Failure should produce evidence, retry/fallback, and provisional work where useful. Application restart is not a daily context-clearing mechanism.

The shared dated check-in log suppresses duplicates across surfaces. A configured task, an issued invitation, successful Notion access, native project routing, and delivered phone/desktop notification are separate verification facts.

## 7. Structural evolution and notable occurrences

| Date / period | Event | Repository implication |
|---|---|---|
| Early September | Constitution lineage: v0.1's 20 rules → condensed v0.2 → ChatGPT v0.3 → merged v0.4 after Claude QA → approved v0.5 | Preserve lineage without loading superseded drafts as active instructions |
| September 5 | A3 closed; explicit project-level manager assignment; formal switching handoff; protected reviewer fields | Authority and ownership checks belong at action boundaries |
| September 6 | Business/Personal/Both architecture and sidebar/status workflow approved and implemented | Preserve shared stores, independent Status/Portfolio axes, and context separation |
| September 7 | Efficiency decisions approved | Reuse current stores; minimize context; use deterministic checks and delta review; avoid generalized infrastructure before demonstrated ROI |
| September 9 | Daily ChatGPT morning / Claude nightly division approved; odd/even rotation retired | Remove obsolete rotation logic from any imported instructions |
| September 12 | Account-wide delivery/connection assurance and check-in v1.2 recorded | Native task migration needs separate delivery, read, write, and Claude-observation evidence |
| September 13–14 | Seven paired platform handoffs packaged as 2026-09-13.02 | Generated packages are transport artifacts, not proof of native installation |
| September 14 | LLM-17 records partial v0.2 adoption and remains Blocked | Do not mark standing Claude schedule instructions updated without Claude-authored evidence |
| September 15 check-in log | Records Claude detection of a September 14 ChatGPT decision and closure of a recurring-review round-trip task | Some round-trip evidence exists; it does not prove every native delivery or project-refresh path |
| October 11 | Future and undated deferrals explicitly included in outstanding-list overview | Do not filter them out merely because not actionable today |
| October 12 | Mike Linn designated ChatGPT home; stable Mike OS v1 retained | Preserve aliases and IDs; avoid duplicate projects |
| October 13 | One-time identity/handoff reconciliation completed; September file repaired | Do not repeatedly redo reconciliation without a material change |
| October 19 | Morning Briefing established as dedicated ChatGPT conversational home | Broader home and briefing home coexist; routing still requires evidence |
| October 23 | This repo-oriented handoff prepared | Import as working context; recommendations remain draft |

### Defects and tensions to preserve explicitly

1. Native project installation, URL/ID, fresh-session retrieval, scheduler routing, and notification delivery were explicitly unverified in the October 13 reconciliation. The October 19 project designation alone does not close them.
2. Cross-Model Context Sync reports six Claude documents and a 12-hour trigger. The linked draft still requests source/target links and first-run proof. These are reported implementation claims, not reproduced deployment evidence.
3. The early context-architecture draft retains v0.4 references. Current approved baseline is v0.5; do not mechanically import its stale version constants.
4. Decisions & Activity's Approved By select was documented as lacking Mike. Preserve explicit approval provenance; never select ChatGPT/Claude as a substitute. A schema repair is a proposal requiring the applicable approval.
5. Source fetches sometimes show a response “as of” time different from page_last_edited_at. Keep both provenance fields rather than inventing a single global revision.
6. Recent chat status replies are incomplete without item identities. Do not bulk-apply “done” or “queued” from a transcript without resolving their canonical records.

## 8. Integration inventory and confidence

| Integration | Supported by evidence | Boundary / next verification |
|---|---|---|
| ChatGPT ↔ Notion | Live reads succeeded here; historical reads/writes documented | Re-test authorized writes in the consuming runtime |
| Claude ↔ Notion | Recorded nightly outputs and observations of ChatGPT changes | Claude session must establish its own current connection |
| Native ChatGPT Projects / sources | Supplied file and approved identity mapping | Automatic file/instruction updates and fresh-session retrieval not established |
| Claude Project Knowledge | Paired handoffs and six-doc cache reported | Native install/refresh requires actual target evidence |
| Native scheduled tasks | Approved delivery target and historical schedule requests | No native configuration or delivery audit performed here |
| Codex automation | Temporary morning backup described in approved standard | Do not create a duplicate or pause it without checking migration evidence |
| Browser/web | Used when current external facts are required | Not a canonical project-state store |
| ChatGPT Library | Source transport and durable deliverables | Does not replace canonical Notion operating state |
| Claude Code / GitHub | Requested destination for implementation context | No repo URL, branch, codebase, credentials, or GitHub connection verified |
| Gemini / video tools | Conversation context describes a video-specialist role | Adjacent workflow, not verified core orchestration infrastructure |

Do not copy ChatGPT app credentials or assume its connector session is portable to Claude Code. Discover supported access in the target runtime and keep secrets outside source control.

## 9. Proposed repository design — not existing deployment

Keep the bootstrap small. Suggested files and responsibilities:

| Proposed path | Purpose |
|---|---|
| CLAUDE.md | Compact startup, canonical-source rule, role/authority checks, links to deeper docs |
| README.md | What the repo does, setup, supported commands, implementation status |
| docs/architecture.md | Architecture, ownership, vertical boundaries, source precedence |
| docs/decisions/ | Dated implementation decisions, distinguishing proposals from Mike-approved changes |
| config/notion-sources.example.yaml | Stable IDs, logical store mappings, timezone; no credentials |
| schemas/ | Locally validated contracts mapped to fetched live schemas |
| src/notion/ | Supported read adapter; authorized writes isolated behind ownership/freshness checks |
| src/context/ | Deterministic extraction, rendering, source fingerprinting, per-platform deltas |
| tests/fixtures/ | Synthetic records and meaningful contract/failure cases |
| .env.example / .gitignore | Variable names and exclusions for secrets/private caches |

These are suggested locations, not a request to create a generalized framework. Follow the approved efficiency policy: prove one useful path before adding infrastructure.

### Candidate context-pack contract

The earlier architecture draft proposes four layers: shared Project Schema, canonical Project Record, Context Pack Generator, and Sync Policy. This is a useful prototype direction, not an approved replacement architecture.

A compact pack should carry stable project ID and source URL; outcome/milestone/primary action; manager and derived reviewer; vertical/area; approved decisions separated from proposals; relevant constraints/blockers; latest recap and artifact links; approved skills/versions; and explicit missing values.

Candidate provenance fields:

- constitution_version, schema_version, source_revision.
- pack_version, generator_version, generated_at.
- source record IDs and source read/edit times.
- Per-target last_applied_pack_version, applied_at, verified_at, and failure reason.

These fields are a proposed contract, not a claim they exist in Notion. A source fingerprint must include relevant linked records, since the project timestamp alone can miss changed tasks or decisions. Unknown platform baselines require full refresh; otherwise compute delta against each platform's actual acknowledged baseline.

**Keep distinct:** generated → delivered → applied → retrieved in a fresh session. Never mark later stages successful merely because an earlier stage passed.

## 10. Claude Code startup and first implementation slice

1. Read this handoff, live Constitution v0.5, target project record, and applicable approved skills.
2. Identify target vertical, manager, current milestone, primary action, and latest recap. For this system handoff, Both/Admin is appropriate; retrieve personal details only when necessary.
3. Inspect the actual repository if supplied. Record its URL, branch, existing instructions, integration mechanism, and missing access. Do not assume a blank repo.
4. Establish read access to one known Notion record in Claude Code. Fetch relevant schemas; report missing capability accurately.
5. Build an isolated read-only prototype for one project: current canonical state → validated compact Markdown pack with source provenance.
6. Demonstrate identical inputs produce no duplicate changes, linked-record updates change the fingerprint, and two target baselines yield correct deltas.
7. Prototype failure handling for stale state, missing manager, schema mismatch, unavailable access, and application failure.
8. Only extend to authorized writes and delivery paths after ownership, actual platform capability, and applicable governing requirements are satisfied.
9. Present structural adoption proposals with what changed, why, evidence, benefit, and tradeoff. Obtain independent QA and Mike's governing approval where required.
10. Record meaningful work and a compact recap in the authorized canonical location, with one primary next action.

### Useful verification cases

- Business retrieval excludes Personal health detail; Both begins with summaries.
- No reviewer-owned field changes during producer write-back.
- Freshness conflict causes re-read/reconciliation rather than blind overwrite.
- Repeated run does not duplicate decisions, prompts, or readouts.
- Incomplete vs Completed vs Missed follows the briefing rules, including silence.
- Time handling uses America/Los_Angeles through DST.
- A generated pack whose application failed remains stale.
- Readout references resolve to canonical evidence; missing sources are visible.
- Full schemas, not guessed property names, drive API writes.

Independent review is required by Protocol A for qualifying P0/P1 reusable systems, new/material skills, consequential external assets, complex analysis, sensitive research, and workflow samples. Deterministic preflight helps but does not replace eligible semantic QA. The producer does not self-certify this handoff as an independent Pass.

## 11. Open structural work and next action

| Item | Current evidence | Smallest next step |
|---|---|---|
| Mike OS v1 validation | Live project still asks for Business, Personal, Both sessions | Find existing results or run the missing validation; preserve assignment |
| Claude standing v0.2 adoption / LLM-17 | Blocked; partial evidence recorded | Claude reads LLM-17 and updates/acknowledges its standing nightly instructions with evidence |
| Context-sync pilot | Draft design plus generated packages; target refresh incomplete | Prove one source-to-target refresh and fresh-session retrieval |
| Native morning migration | Desired native trigger; backup described | Audit delivery/read/dialogue/write/Claude-observation evidence before retiring backup |
| Approval attribution gap | Mike unavailable in documented Approved By select | Preserve original approval evidence and propose scoped repair |
| Repo bootstrap | Target named by user; actual repo unspecified | Give this document to Claude Code, inspect repo/access, begin read-only prototype |

**Primary next action:** Claude Code should read this document and the live Cross-Model Context Sync project, inspect the actual repo and Notion access, then produce a one-project read-only context-pack prototype and an evidence-based gap list. This is implementation preparation, not a manager reassignment.

## 12. Source register

The supplied file is package 2026-09-13.02, reconciled October 13. It is a working platform package, not independent deployment proof. Conversation context supplies adjacent workflow history; live linked records govern structural state.


- [📜 Mike OS Constitution v0.5 (APPROVED)](https://app.notion.com/p/3d2d5ca6aed281e69973fb0cb2546b36) — live read October 23; returned page edit time: 2026-09-07T04:11:04.022Z.
- [Mike OS v1](https://app.notion.com/p/3d2d5ca6aed2816c9f14d613bbccde30) — live read October 23; returned page edit time: 2026-10-13T16:25:21.900Z.
- [Mike OS → Mike Linn: ChatGPT handoff and canonical identity](https://app.notion.com/p/3f7d5ca6aed281b1a49efdce57e3c126) — live read October 23; returned page edit time: 2026-10-13T16:25:11.635Z.
- [🌅 Mike OS Daily Briefing and Nightly Readout Standard v0.2](https://app.notion.com/p/3d6d5ca6aed2812489a2d541a55e1d38) — live read October 23; returned page edit time: 2026-09-12T22:04:54.504Z.
- [Cross-Model Notion Sync](https://app.notion.com/p/3d3d5ca6aed28176b4d4eb2b97735c5c) — live read October 23; returned page edit time: 2026-09-14T02:25:42.862Z.
- [Cross-Model Context Sync](https://app.notion.com/p/3d3d5ca6aed281919a96dbe3c519a041) — live read October 23; returned page edit time: 2026-09-14T02:25:15.827Z.
- [🧭 Business and Personal Vertical Architecture v1.0 (APPROVED)](https://app.notion.com/p/3d4d5ca6aed2818385e4f28ba9d21c22) — live read October 23; returned page edit time: 2026-09-07T04:11:02.843Z.
- [Cross-Platform Project Handoff Library v2026-09-13.02](https://app.notion.com/p/3dbd5ca6aed2813685d0e27c589d4817) — live read October 23; returned page edit time: 2026-09-14T02:24:27.378Z.
- [🧭 Sidebar and Status Workflow v1.0 (APPROVED)](https://app.notion.com/p/3d4d5ca6aed28125a66cc05956f8b578) — live read October 23; returned page edit time: 2026-09-07T04:54:46.127Z.
- [⚙️ Mike OS Efficiency Decisions v0.1 (APPROVED)](https://app.notion.com/p/3d4d5ca6aed2817480f0f390a316601a) — live read October 23; returned page edit time: 2026-09-07T23:40:24.738Z.
- [Claude adopt account-wide briefing connection standard v0.2](https://app.notion.com/p/3d9d5ca6aed281d88348dcf69e0fdb72) — live read October 23; returned page edit time: 2026-09-14T18:25:44.153Z.
- [Mike OS cross-platform project context architecture — Claude handoff (DRAFT)](https://app.notion.com/p/3d3d5ca6aed2813fadb8d249c032a476) — live read October 23; returned page edit time: 2026-09-06T01:53:23.698Z.
- [Protocol A — Cross-Model QA](https://app.notion.com/p/3d2d5ca6aed281459c7ff23b00e3b79a) — live read October 23; returned page edit time: 2026-09-05T19:20:13.708Z.
- [Protocol B — Skill learning and versioning](https://app.notion.com/p/3d2d5ca6aed281b7910dceab41b594e7) — live read October 23; returned page edit time: 2026-09-05T19:20:13.708Z.
- [Running To-Do Check-in](https://app.notion.com/p/3d3d5ca6aed281948a3de9285c5662ae) — live read October 23; returned page edit time: 2026-10-23T16:52:00.560Z.
- [Mike OS root](https://app.notion.com/p/3d2d5ca6aed281cbb68ed8e5cf4c858d) — includes October 19 Morning Briefing designation.
- [System Databases](https://app.notion.com/p/3d4d5ca6aed281f7be8eda0b6a73f127) — database/data-source mappings read live.

No Notion schema, project ownership, schedule, or governing rule was changed while preparing this handoff. No independent reviewer verdict has yet been obtained.


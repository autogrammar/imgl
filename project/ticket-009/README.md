# Ticket 009: Pytest collection health with governance

- **ID**: ticket-009
- **Owner**: agent:codex
- **Status**: IN_PROGRESS
- **Workflow state**: PUBLICATION
- **Created**: 2026-10-02

## Goal and scope

Accept successful governance summaries containing `0 errors` while retaining pytest exit-code and actual collection/import failure checks.

## Acceptance criteria

- [x] AC-01: Collection health and the full IMGL test suite pass.
- [x] AC-02: Managed governance accepts the scoped application test repair.
- [ ] AC-03: Independent exact-head review and protected merge complete.

## Validation

Full product suite: 177 passed, 6 skipped using the existing IMGL environment against this worktree. Real collection checks now accept the governance success summary. Required nonzero exit-code and ModuleNotFoundError checks remain enforced. Managed governance passed. Protected publication pending.

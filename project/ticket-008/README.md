# Ticket 008: Adopt pinned Wellman validation and CI in IMGL

- **ID**: ticket-008
- **Owner**: agent:codex
- **Status**: IN_PROGRESS
- **Workflow state**: PUBLICATION
- **Created**: 2026-10-02

## Goal and scope

Enforce immutable Wellman metadata validation in CI, preserve existing product and governance checks, and repair the target-owned ticket index marker range required by its existing generator.

## Acceptance criteria

- [x] AC-01: Pinned Wellman requirements and repository-bound Docs metadata validate.
- [x] AC-02: Managed governance and ticket index generation pass without changing inherited product files.
- [ ] AC-03: Exact-head independent validation and protected merge complete.

## Validation and publication

Wellman 0.20.38 is pinned to independently merged source `73b4edcf3e74709734c755a4f68cbf328b7d6f5b` (wellmanifest/wellman PR25). Dependency-free `python -S scripts/check-wellman.py`, installed `git wellman check --root . --json`, and the managed governance gate pass without findings. After the separately merged IMGL PR15 collection-health repair, the full product suite passes: 177 passed, 6 skipped. Existing product changes in the primary checkout were preserved. Exact-head independent publication remains pending.

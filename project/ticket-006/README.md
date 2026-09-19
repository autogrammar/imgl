# Ticket 006: Publish pending SubLLM vision integration

- **Status**: DONE
- **Workflow state**: PUBLICATION
Allocation: https://github.com/autogrammar/imgl/issues/6.
SESSION_EXECUTION_AUTHORIZATION: user requests continuing fleet repairs, push and protected merge.

AC-01: Preserve the application integration of PR #1 while publishing from the canonical ticket worktree.
AC-02: Pass the current locked Python 3.10 and 3.13 matrix and obtain independent exact-head approval.
AC-03: Retire the superseded PR only after replacement merge, preserving dirty and legacy checkouts.

Validation: Python 3.13 isolated environment, identical CI installation and test commands: 154 passed, 11 pre-existing optional-dependency skips. The vision transport is mocked; no provider request was made. Source dependency subactor/subllm PR #25 is merged.

Current-main reconciliation: regenerate uv.lock for the pinned SubLLM dependency. Keep the existing locked matrix and its aggregate test gate; omit the superseded single-version ci.yml from PR #1 so it cannot create an ambiguous duplicate check name. Initial unlocked tests above are diagnostic; final validation uses the current main workflow.

Final local validation: uv lock --check and both locked Python 3.10/3.13 environments with dev, web and diagnose extras; 164 passed, 11 existing skips and one dependency deprecation warning per environment. No package version upgrades were requested.

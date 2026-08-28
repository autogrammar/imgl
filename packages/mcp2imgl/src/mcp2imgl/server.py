"""MCP stdio server — thin wrappers over dsl2imgl."""

from __future__ import annotations

import json
import os

_EXECUTE_ENV = "IMGL_MCP_ALLOW_EXECUTE"


def _require_execute(action: str) -> None:
    enabled = os.getenv(_EXECUTE_ENV, "").strip().lower() in {"1", "true", "yes", "on"}
    if not enabled:
        raise PermissionError(
            f"MCP desktop execution '{action}' is disabled; start the server with {_EXECUTE_ENV}=1"
        )


def run_stdio() -> None:
    from dsl2imgl import dispatch
    from nlp2imgl.to_dsl import apply_nl, to_dsl

    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise SystemExit("pip install mcp2imgl[mcp]") from exc

    mcp = FastMCP("mcp2imgl")

    @mcp.tool()
    def imgl_run_command(command: str) -> str:
        """Run one imgl DSL line."""
        _require_execute("imgl_run_command")
        return dispatch(command).to_json()

    @mcp.tool()
    def imgl_to_dsl(prompt: str, image: str = "screen.png", window: str = "") -> str:
        """Convert NL to DSL without executing."""
        return to_dsl(prompt, image=image, window=window or None)

    @mcp.tool()
    def imgl_apply_nl(prompt: str, image: str = "screen.png", window: str = "", execute: bool = False) -> str:
        """NL → DSL → dispatch."""
        if execute:
            _require_execute("imgl_apply_nl")
        result = apply_nl(prompt, image=image, window=window or None, execute=execute)
        return json.dumps(result.to_dict(), ensure_ascii=False)

    mcp.run()

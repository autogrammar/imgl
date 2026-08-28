"""Safety tests for mcp2imgl."""

import pytest

from mcp2imgl.server import _require_execute


def test_mcp_desktop_execution_requires_operator_capability(monkeypatch) -> None:
    monkeypatch.delenv("IMGL_MCP_ALLOW_EXECUTE", raising=False)
    with pytest.raises(PermissionError, match="IMGL_MCP_ALLOW_EXECUTE"):
        _require_execute("imgl_run_command")

    monkeypatch.setenv("IMGL_MCP_ALLOW_EXECUTE", "on")
    _require_execute("imgl_run_command")

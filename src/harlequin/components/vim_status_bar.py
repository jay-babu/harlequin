"""The query editor Vim mode status line."""

from __future__ import annotations

from typing import Any

from textual.widgets import Static


class VimStatusBar(Static):
    DEFAULT_CSS = """
    VimStatusBar {
        height: 1;
        width: 100%;
        color: $primary;
        padding: 0 1;
    }

    VimStatusBar.hide {
        display: none;
    }
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__("", **kwargs)

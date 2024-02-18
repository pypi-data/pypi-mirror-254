from __future__ import annotations

import ast

from flake8_no_nested_comprehensions import Plugin


def _results(s: str) -> set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_trivial_case() -> None:
    assert _results('') == set()


def test_nested_comprehension() -> None:
    ret = _results('[attr for style in styles for attr in {"testing", "set"}]')
    assert ret == {'1:0 CMP100 no nested comprehension'}


def test_allowed_comprehension() -> None:
    ret = _results('[style for style in {"testing", "set"}]')
    assert ret == set()

from __future__ import annotations

import ast
import importlib.metadata
from typing import Any
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    import argparse
    import flake8.options.manager
    from collections.abc import Generator


class Visitor(ast.NodeVisitor):
    def __init__(self, max_generators: int) -> None:
        self.problems: list[tuple[int, int]] = []
        self.max_generators = max_generators

        self.visit_ListComp = self._visit_max_generators
        self.visit_SetComp = self._visit_max_generators
        self.visit_GeneratorExp = self._visit_max_generators
        self.visit_DictComp = self._visit_max_generators

    def _visit_max_generators(self, node: ast.ListComp | ast.SetComp | ast.GeneratorExp | ast.DictComp) -> None:
        if len(node.generators) > self.max_generators:
            self.problems.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)
    max_generators = 1

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def add_options(manager: flake8.options.manager.OptionManager) -> None:  # pragma: no cover
        manager.add_option(
            '--max-comprehensions', type=int, metavar='n',
            default=1, parse_from_config=True,
            help='Maximum allowed generators in a single comprehension. (Default: %(default)s)',
        )

    @staticmethod
    def parse_options(options: argparse.Namespace) -> None:  # pragma: no cover
        Plugin.max_generators = options.max_comprehensions

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = Visitor(self.max_generators)
        visitor.visit(self._tree)
        for line, col in visitor.problems:
            yield line, col, 'CMP100 no nested comprehension', type(self)

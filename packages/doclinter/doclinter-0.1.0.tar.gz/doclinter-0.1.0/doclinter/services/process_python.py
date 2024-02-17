import ast
from os import error
from pathlib import Path
from pydoc import doc
from typing import Callable, Optional

from doclinter.core.rating import is_above_threshold, rate_text


def get_docstring_in_tree(tree: ast.Module):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if docstring := ast.get_docstring(node):
                yield docstring, node.lineno
        elif isinstance(node, ast.Module):
            if docstring := ast.get_docstring(node):
                yield docstring, None


def process_file(
    path: Path,
    max_ari_level: Optional[int],
    error_callback: Callable[[str, str], None],
) -> bool:
    if not max_ari_level:
        max_ari_level = 10

    file_path = str(path)
    with open(path, mode="r") as f:
        file_contents = f.read()

    try:
        tree = ast.parse(file_contents)
    except SyntaxError as e:
        error_callback(
            f"{file_path}:{e.lineno}",
            "SyntaxError: invalid syntax. doclint unable to analyse.",
        )
        exit(1)

    has_errors = False

    for docstring, line_number in get_docstring_in_tree(tree):
        difficulty = rate_text(docstring)
        if is_above_threshold(difficulty, max_ari_level):
            has_errors = True
            if line_number:
                error_callback(f"{file_path}:{line_number}", "Docstring too complex")
            else:
                error_callback(f"{file_path}:1", "Docstring too complex")

    return has_errors

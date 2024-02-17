from pathlib import Path
from typing import Optional
import click

from doclinter.services.process_python import process_file


def output(str: str):
    click.echo(str)


def output_error(location: str, error: str):
    click.echo(
        location + ": " + click.style("error: ", fg="red", bold=True) + error, err=True
    )


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option("-v", "--verbose", is_flag=True)
@click.option("--max-ari-level", type=int)
def analyse_file(files: str, max_ari_level: Optional[int], verbose: bool):
    """Analyse the complexity of a Python file's docstrings."""
    output_value = False

    for p in files:
        path = Path(p)
        if verbose:
            output(f"Checking {str(path)}")
        file_invalid = process_file(path, max_ari_level, output_error)
        if not output_value and file_invalid:
            output_value = True

    exit(output_value)


def main():
    analyse_file()

"""
Validate a given BIO file.
"""

from argparse import ArgumentParser
from pathlib import Path

from bio_parser.parse.validate import run


def _check_bio_ext(filename: str) -> Path:
    filepath = Path(filename)
    assert filepath.suffix == ".bio"
    return filepath


def add_validate_parser(subcommands):
    parser: ArgumentParser = subcommands.add_parser(
        "validate",
        help=__doc__,
        description=__doc__,
    )
    parser.set_defaults(func=run)

    parser.add_argument(
        "filepaths", help="Files to validate.", type=_check_bio_ext, nargs="*"
    )

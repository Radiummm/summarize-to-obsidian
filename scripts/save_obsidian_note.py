#!/usr/bin/env python3
"""Create a collision-safe Markdown note inside an Obsidian vault."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("--vault", required=True, help="Absolute path to the Obsidian vault root")
    command.add_argument("--filename", required=True, help="Markdown filename, e.g. 2026-08-13 - topic.md")
    command.add_argument("--source", required=True, help="Existing Markdown file to copy")
    command.add_argument("--folder", default="", help="Optional folder relative to the vault root")
    return command


def unique_path(destination: Path) -> Path:
    if not destination.exists():
        return destination
    for index in range(2, 10_000):
        candidate = destination.with_name(f"{destination.stem} ({index}){destination.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError("Unable to find an available filename")


def main() -> int:
    args = parser().parse_args()
    vault = Path(args.vault).expanduser().resolve()
    source = Path(args.source).expanduser().resolve()
    filename = Path(args.filename)

    if not vault.is_dir():
        raise ValueError(f"Vault directory does not exist: {vault}")
    if not source.is_file():
        raise ValueError(f"Source file does not exist: {source}")
    if filename.name != args.filename or filename.suffix.lower() != ".md":
        raise ValueError("--filename must be a plain Markdown filename, not a path")

    folder = Path(args.folder)
    if folder.is_absolute() or ".." in folder.parts:
        raise ValueError("--folder must be a relative path contained in the vault")

    destination_dir = vault / folder
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = unique_path(destination_dir / filename.name)
    shutil.copyfile(source, destination)
    print(destination)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)

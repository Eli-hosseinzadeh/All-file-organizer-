"""
utils.py
--------
General-purpose utility functions shared by both organizer.py and gui.py.

Keeping these helper functions in a separate module makes the main logic
in organizer.py cleaner, more readable, and focused on the core business
logic.
"""

import hashlib
import time
from pathlib import Path


def human_readable_size(num_bytes: int) -> str:
    """Convert a file size from bytes into a human-readable string (e.g., '2.3 GB')."""
    size = float(num_bytes)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def file_hash(path: Path, block_size: int = 65536) -> str:
    """
    Return the MD5 hash of a file's contents.

    This function is used to detect duplicate files (Version 2) by
    comparing file contents rather than filenames.
    """
    hasher = hashlib.md5()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, FileNotFoundError, OSError):
        # Return an empty hash if the file cannot be read,
        # allowing the program to continue without interruption.
        return ""


def file_age_days(path: Path) -> int:
    """Return the number of days since the file was last modified."""
    mtime = path.stat().st_mtime
    age_seconds = time.time() - mtime
    return int(age_seconds / 86400)


def unique_destination(dest_folder: Path, filename: str) -> Path:
    """
    If a file with the same name already exists in the destination folder,
    append a number to the filename to avoid overwriting it.

    Example:
        report.pdf -> report (1).pdf
    """
    dest = dest_folder / filename
    if not dest.exists():
        return dest

    stem = dest.stem
    suffix = dest.suffix
    counter = 1
    while dest.exists():
        dest = dest_folder / f"{stem} ({counter}){suffix}"
        counter += 1
    return dest
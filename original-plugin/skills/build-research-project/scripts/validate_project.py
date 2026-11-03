#!/usr/bin/env python3
"""Check the structure and integrity metadata of a generated research project.

This is not a statistical or scientific validation tool. It uses only Python's
standard library and never executes project scripts or downloads data.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath

REQUIRED_DIRS = [
    "research", "data/raw", "data/processed", "scripts", "results/tables",
    "results/figures", "results/validation", "logs", "report"
]
REQUIRED_FILES = [
    "README.md", "research/problem_statement.md", "research/research_questions.md",
    "research/analysis_protocol.md", "data/dataset_register.csv",
    "data/data_dictionary.csv", "logs/execution_status.md"
]
REPORT_SUFFIXES = {".pdf", ".docx", ".html", ".md"}
REGISTER_COLUMNS = {
    "dataset_id", "title", "producer", "landing_page", "licence",
    "accessed_utc", "local_path", "sha256", "redistribution_status"
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_relative(project: Path, value: str) -> Path | None:
    if not value or value == "NOT_RETAINED":
        return None
    rel = PurePosixPath(value)
    if rel.is_absolute() or ".." in rel.parts or "\\" in value:
        raise ValueError(f"Unsafe local_path in dataset register: {value!r}")
    path = project.joinpath(*rel.parts).resolve()
    if not path.is_relative_to(project.resolve()):
        raise ValueError(f"Dataset path escapes project directory: {value!r}")
    return path


def validate(project: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    checked: list[str] = []
    if not project.exists() or not project.is_dir():
        return {"status": "FAIL", "errors": ["Project path does not exist or is not a directory"],
                "warnings": [], "checked": []}

    for rel in REQUIRED_DIRS:
        if not (project / rel).is_dir():
            errors.append(f"Missing required directory: {rel}")
        else:
            checked.append(f"directory:{rel}")
    for rel in REQUIRED_FILES:
        p = project / rel
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"Missing or empty required file: {rel}")
        else:
            checked.append(f"file:{rel}")

    register = project / "data/dataset_register.csv"
    if register.is_file():
        try:
            with register.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                fields = set(reader.fieldnames or [])
                missing = sorted(REGISTER_COLUMNS - fields)
                if missing:
                    errors.append("Dataset register missing columns: " + ", ".join(missing))
                else:
                    for line, row in enumerate(reader, start=2):
                        local_path = (row.get("local_path") or "").strip()
                        recorded_hash = (row.get("sha256") or "").strip().lower()
                        try:
                            p = safe_relative(project, local_path)
                        except ValueError as exc:
                            errors.append(f"Dataset register line {line}: {exc}")
                            continue
                        if p is None:
                            if (row.get("redistribution_status") or "").strip() not in {
                                "NOT_REDISTRIBUTED", "UNKNOWN", "PUBLIC_DOWNLOAD_TERMS",
                                "RESTRICTED_OR_CLOSED", "REGISTRATION_OR_APPLICATION"
                            }:
                                warnings.append(f"Dataset register line {line}: no local file; confirm lawful access/retention reason")
                            continue
                        if not p.is_file():
                            errors.append(f"Dataset register line {line}: local file not found: {local_path}")
                            continue
                        if not recorded_hash:
                            warnings.append(f"Dataset register line {line}: local file has no SHA-256")
                        elif sha256(p) != recorded_hash:
                            errors.append(f"Dataset register line {line}: SHA-256 mismatch: {local_path}")
                        else:
                            checked.append(f"sha256:{local_path}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Could not read dataset register: {type(exc).__name__}: {exc}")

    reports_dir = project / "report"
    report_files = [p for p in reports_dir.iterdir() if p.is_file() and p.suffix.lower() in REPORT_SUFFIXES] if reports_dir.is_dir() else []
    if len(report_files) != 1:
        errors.append(f"Expected exactly one canonical report file; found {len(report_files)}")
    elif report_files[0].stat().st_size == 0:
        errors.append("Canonical report file is empty")
    else:
        checked.append(f"canonical_report:{report_files[0].relative_to(project).as_posix()}")

    raw_dir = project / "data/raw"
    if raw_dir.is_dir() and not any(p.is_file() for p in raw_dir.rglob("*")):
        warnings.append("No raw dataset files are present; verify that the project documents a lawful/technical reason and retrieval route")

    return {"status": "FAIL" if errors else "PASS", "project": str(project.resolve()),
            "errors": errors, "warnings": warnings, "checked": checked,
            "note": "Structural and checksum checks only; no statistical, methodological or scientific claims are validated."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="Path to the generated project directory")
    args = parser.parse_args()
    try:
        result = validate(args.project_dir)
    except Exception as exc:  # defensive CLI boundary; do not disclose file contents
        result = {"status": "FAIL", "errors": [f"Validator error: {type(exc).__name__}: {exc}"], "warnings": [], "checked": []}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

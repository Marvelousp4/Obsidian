#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


VAULT_ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = VAULT_ROOT / "10 Raw"
COMPILED_ROOT = VAULT_ROOT / "05 Knowledge" / "Compiled"
CONCEPT_ROOT = VAULT_ROOT / "05 Knowledge" / "Concepts"
REPORT_ROOT = VAULT_ROOT / "08 Reviews" / "Wiki Health"


@dataclass
class Finding:
    kind: str
    message: str


def today() -> str:
    return date.today().isoformat()


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text
    _, block, body = text.split("---\n", 2)
    data: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - ") and current_key:
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(line[4:])
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip()
    return data, body.strip()


def load_notes(root: Path) -> dict[Path, tuple[dict[str, object], str]]:
    notes: dict[Path, tuple[dict[str, object], str]] = {}
    for path in root.rglob("*.md"):
        if path.name in {"Raw Index.md", "Compiled Index.md", "Concept Index.md", "README.md"}:
            continue
        notes[path] = parse_frontmatter(path.read_text(encoding="utf-8"))
    return notes


def wiki_link_candidates(path: Path) -> set[str]:
    relative = path.relative_to(VAULT_ROOT).as_posix()
    stem = relative[:-3]
    return {stem, path.stem}


def extract_wikilinks(text: str) -> list[str]:
    matches = []
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0]
        matches.append(target)
    return matches


def unresolved_placeholders(text: str) -> list[str]:
    patterns = [r"\bTODO\b", r"\bTBD\b", r"_No .* found\._", r"- $"]
    found: list[str] = []
    for pattern in patterns:
        if re.search(pattern, text, re.M):
            found.append(pattern)
    return found


def generate_report(findings: list[Finding]) -> Path:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    path = REPORT_ROOT / f"{today()} Wiki Health.md"
    kind_counts: dict[str, int] = {}
    for finding in findings:
        kind_counts[finding.kind] = kind_counts.get(finding.kind, 0) + 1
    body = [
        "---",
        "type: review",
        "period: wiki_health",
        f"date: {today()}",
        "tags:",
        "  - review",
        "  - knowledge",
        "---",
        "",
        f"# Wiki Health - {today()}",
        "",
        "## Summary",
        "",
        f"- Total findings: {len(findings)}",
    ]
    for kind, count in sorted(kind_counts.items()):
        body.append(f"- {kind}: {count}")
    body.extend(["", "## Findings", ""])
    if findings:
        for finding in findings:
            body.append(f"- [{finding.kind}] {finding.message}")
    else:
        body.append("- No issues found.")
    path.write_text("\n".join(body) + "\n", encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a structural health check on the compiled wiki.")
    parser.parse_args()

    raw_notes = load_notes(RAW_ROOT)
    compiled_notes = load_notes(COMPILED_ROOT)
    concept_notes = load_notes(CONCEPT_ROOT)
    all_notes = {**raw_notes, **compiled_notes, **concept_notes}

    targets: set[str] = set()
    for path in all_notes:
        targets.update(wiki_link_candidates(path))

    findings: list[Finding] = []

    for path, (frontmatter, body) in raw_notes.items():
        compiled_note = str(frontmatter.get("compiled_note", "")).strip()
        if not compiled_note:
            findings.append(Finding("uncompiled_raw", f"{path.relative_to(VAULT_ROOT)} has no compiled note."))
        for placeholder in unresolved_placeholders(body):
            findings.append(Finding("raw_placeholder", f"{path.relative_to(VAULT_ROOT)} contains placeholder pattern `{placeholder}`."))

    for path, (frontmatter, body) in compiled_notes.items():
        compiled_from = str(frontmatter.get("compiled_from", "")).strip()
        if not compiled_from:
            findings.append(Finding("compiled_missing_source", f"{path.relative_to(VAULT_ROOT)} is missing `compiled_from`."))
        links = extract_wikilinks(body)
        if len(links) < 2:
            findings.append(Finding("weak_compiled_links", f"{path.relative_to(VAULT_ROOT)} links to fewer than two notes."))
        for placeholder in unresolved_placeholders(body):
            findings.append(Finding("compiled_placeholder", f"{path.relative_to(VAULT_ROOT)} contains placeholder pattern `{placeholder}`."))

    for path, (frontmatter, body) in concept_notes.items():
        links = extract_wikilinks(body)
        linked_sources = [link for link in links if link.startswith("05 Knowledge/Compiled/")]
        if len(linked_sources) < 1:
            findings.append(Finding("weak_concept_sources", f"{path.relative_to(VAULT_ROOT)} has no linked compiled source."))
        for placeholder in unresolved_placeholders(body):
            findings.append(Finding("concept_placeholder", f"{path.relative_to(VAULT_ROOT)} contains placeholder pattern `{placeholder}`."))

    for path, (_, body) in all_notes.items():
        for link in extract_wikilinks(body):
            if link not in targets:
                findings.append(Finding("broken_link", f"{path.relative_to(VAULT_ROOT)} links to missing note `[[{link}]]`."))

    report_path = generate_report(findings)
    print(report_path)


if __name__ == "__main__":
    main()

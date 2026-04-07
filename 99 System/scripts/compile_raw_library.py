#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


VAULT_ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = VAULT_ROOT / "10 Raw"
COMPILED_ROOT = VAULT_ROOT / "05 Knowledge" / "Compiled"
CONCEPT_ROOT = VAULT_ROOT / "05 Knowledge" / "Concepts"


@dataclass
class Note:
    path: Path
    frontmatter: dict[str, object]
    body: str


def today() -> str:
    return date.today().isoformat()


def slugify(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r'[\\/:*?"<>|]', "", text)
    return text or "Untitled"


def wiki_link(path: Path) -> str:
    relative = path.relative_to(VAULT_ROOT).as_posix()
    return f"[[{relative[:-3]}]]"


def extract_title(note: Note) -> str:
    for line in note.body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return note.path.stem


def parse_frontmatter_block(block: str) -> dict[str, object]:
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
            value = value.strip()
            if value == "[]":
                data[current_key] = []
            else:
                data[current_key] = value
    return data


def read_note(path: Path) -> Note:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, block, body = text.split("---\n", 2)
        return Note(path=path, frontmatter=parse_frontmatter_block(block), body=body.strip())
    return Note(path=path, frontmatter={}, body=text.strip())


def render_value(value: object) -> str:
    if isinstance(value, list):
        if not value:
            return " []"
        return "\n" + "\n".join(f"  - {item}" for item in value)
    if value is None:
        return ""
    text = str(value)
    if "\n" in text:
        lines = "\n".join(f"  {line}" for line in text.splitlines())
        return f" >-\n{lines}"
    return f" {text}"


def write_note(path: Path, frontmatter: dict[str, object], body: str) -> None:
    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}:{render_value(value)}")
    lines.extend(["---", "", body.strip(), ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def list_raw_notes() -> list[Path]:
    return sorted(
        path
        for path in RAW_ROOT.rglob("*.md")
        if path.name != "Raw Index.md"
    )


def infer_area(text: str, source_kind: str) -> str:
    if source_kind == "paper":
        return "research"
    if source_kind == "repo":
        return "research"
    corpus = text.lower()
    if any(token in corpus for token in ("work", "customer", "account", "deployment", "issue")):
        return "work"
    if any(token in corpus for token in ("health", "nutrition", "workout", "training", "sleep")):
        return "health"
    if any(token in corpus for token in ("finance", "stock", "portfolio", "cash")):
        return "finance"
    if any(token in corpus for token in ("research", "paper", "experiment", "hypothesis")):
        return "research"
    if source_kind == "repo":
        return "research"
    return "learning"


def infer_domain(text: str, source_kind: str) -> str:
    corpus = text.lower()
    if source_kind == "paper":
        return "paper_notes"
    if source_kind == "repo":
        return "codebase_digest"
    if "robot" in corpus or "sim2real" in corpus:
        return "robotics"
    if "llm" in corpus or "agent" in corpus:
        return "ai_systems"
    return source_kind


def nonempty_paragraphs(body: str) -> list[str]:
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", body) if chunk.strip()]
    return [chunk for chunk in chunks if not chunk.startswith("#")]


def normalize_text(text: str) -> str:
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    text = normalize_text(text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if len(part.strip()) > 20]


def pick_core_sentence(text: str) -> str:
    sentences = split_sentences(text)
    priority_patterns = (
        r"\bwe introduce\b",
        r"\bwe propose\b",
        r"\bthis work\b",
        r"\bthis paper\b",
        r"\bwe demonstrate\b",
        r"\bour method\b",
    )
    for pattern in priority_patterns:
        for sentence in sentences:
            if re.search(pattern, sentence, re.I):
                return sentence
    return sentences[0] if sentences else ""


def short_summary(title: str, text: str) -> str:
    sentence = pick_core_sentence(text)
    if not sentence:
        return f"This source needs a manual summary before it can be treated as compiled knowledge."
    sentence = re.sub(r"^(In this work,|This work|This paper)\s*", "", sentence, flags=re.I).strip()
    if len(sentence) > 260:
        sentence = sentence[:260].rsplit(" ", 1)[0] + "."
    return f"{title}: {sentence}"


def extract_takeaways(text: str) -> list[str]:
    sentences = split_sentences(text)
    selected: list[str] = []
    patterns = (
        r"\bintroduce\b",
        r"\bpropose\b",
        r"\bdemonstrate\b",
        r"\benable\b",
        r"\bensure\b",
        r"\bshow\b",
        r"\bcontribution\b",
    )
    for pattern in patterns:
        for sentence in sentences:
            if re.search(pattern, sentence, re.I) and sentence not in selected:
                selected.append(sentence)
            if len(selected) >= 3:
                break
        if len(selected) >= 3:
            break
    if len(selected) < 3:
        for sentence in sentences:
            if sentence not in selected:
                selected.append(sentence)
            if len(selected) >= 3:
                break
    takeaways: list[str] = []
    for sentence in selected[:3]:
        sentence = sentence.strip()
        if len(sentence) > 220:
            sentence = sentence[:220].rsplit(" ", 1)[0] + "."
        takeaways.append(sentence)
    while len(takeaways) < 3:
        takeaways.append("Manual synthesis needed before this source should drive decisions.")
    return takeaways


def extract_section(body: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\s*(.*?)(\n## |\Z)"
    match = re.search(pattern, body, re.S)
    if not match:
        return ""
    return match.group(1).strip()


def compile_text(note: Note) -> str:
    for heading in ("Raw Markdown", "README"):
        section = extract_section(note.body, heading)
        if section:
            return section
    return note.body


def extract_concepts(title: str, body: str) -> list[str]:
    ignored = {
        "source",
        "raw markdown",
        "readme",
        "repo tree",
        "linked source",
        "actionable takeaways",
    }
    concepts: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            concept = line[3:].strip()
            if concept.lower() not in ignored:
                concepts.append(concept)
    title_tokens = re.split(r"[-:|/]", title)
    for token in title_tokens:
        token = token.strip()
        if len(token) >= 4:
            concepts.append(token)
    deduped: list[str] = []
    seen: set[str] = set()
    for concept in concepts:
        normalized = concept.lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(concept)
    return deduped[:6]


def deterministic_compile(note: Note) -> dict[str, object]:
    title = extract_title(note)
    source_kind = str(note.frontmatter.get("source_kind", "web"))
    source_body = compile_text(note)
    area = infer_area(source_body, source_kind)
    domain = infer_domain(source_body, source_kind)
    concepts = extract_concepts(title, source_body)
    entry = (
        f"{title} is a source-derived note compiled from {wiki_link(note.path)}. "
        f"It belongs to the {area} area and currently sits in the {domain} domain."
    )
    takeaways = extract_takeaways(source_body)
    return {
        "title": title,
        "area": area,
        "domain": domain,
        "_compiler": "deterministic",
        "summary": short_summary(title, source_body),
        "encyclopedia_entry": entry,
        "key_concepts": concepts,
        "why_it_matters": f"This source is worth keeping because it can be turned into reusable knowledge instead of remaining trapped as raw input.",
        "actionable_takeaways": takeaways,
    }


def ollama_available() -> bool:
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    return result.returncode == 0


def extract_json_block(text: str) -> dict[str, object]:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object returned")
    return json.loads(text[start : end + 1])


def compile_with_ollama(note: Note, model: str) -> dict[str, object]:
    prompt = f"""
You are compiling one raw markdown source into a structured wiki note.
Return JSON only with these keys:
title, area, domain, summary, encyclopedia_entry, key_concepts, why_it_matters, actionable_takeaways.
Rules:
- area should be one of: work, health, finance, learning, research, personal
- key_concepts should be a short list of string concept names
- actionable_takeaways should be a short list of string bullets

RAW NOTE TITLE: {extract_title(note)}

RAW NOTE BODY:
{note.body[:12000]}
""".strip()
    result = subprocess.run(
        ["ollama", "run", model, prompt],
        check=True,
        capture_output=True,
        text=True,
    )
    data = extract_json_block(result.stdout)
    data["_compiler"] = f"ollama:{model}"
    if not isinstance(data.get("key_concepts"), list):
        data["key_concepts"] = []
    if not isinstance(data.get("actionable_takeaways"), list):
        data["actionable_takeaways"] = []
    return data


def choose_provider(provider: str) -> str:
    if provider != "auto":
        return provider
    return "ollama" if ollama_available() else "none"


def compile_note(note: Note, provider: str, model: str) -> dict[str, object]:
    if provider == "ollama":
        try:
            return compile_with_ollama(note, model)
        except Exception:
            return deterministic_compile(note)
    return deterministic_compile(note)


def safe_note_path(root: Path, title: str) -> Path:
    path = root / f"{slugify(title)}.md"
    counter = 2
    while path.exists():
        path = root / f"{slugify(title)} {counter}.md"
        counter += 1
    return path


def paths_from_wikilink_list(values: object) -> list[Path]:
    if not isinstance(values, list):
        return []
    paths: list[Path] = []
    for value in values:
        link = str(value).strip()
        if link.startswith("[[") and link.endswith("]]"):
            target = link[2:-2].split("|", 1)[0].split("#", 1)[0]
            path = VAULT_ROOT / f"{target}.md"
            if path.exists():
                paths.append(path)
    return paths


def quality_gate(data: dict[str, Any], concept_paths: list[Path], linked_source_count: int) -> list[str]:
    failures: list[str] = []
    summary = normalize_text(str(data.get("summary", "")))
    takeaways = data.get("actionable_takeaways", [])
    concepts = data.get("key_concepts", [])
    compiler = str(data.get("_compiler", "deterministic"))
    if compiler == "deterministic":
        failures.append("deterministic fallback is draft-only; rerun with a real LLM compiler")
    if not summary:
        failures.append("missing summary")
    if len(summary.split()) > 80:
        failures.append("summary longer than 80 words")
    if "\n" in str(data.get("summary", "")):
        failures.append("summary contains line breaks")
    if re.search(r"\bAbstract[—-]|\bI\.\s+I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N\b", summary, re.I):
        failures.append("summary appears to copy raw paper text")
    if not isinstance(takeaways, list) or len([item for item in takeaways if str(item).strip()]) < 3:
        failures.append("fewer than three takeaways")
    if not isinstance(concepts, list) or len([item for item in concepts if str(item).strip()]) < 2:
        failures.append("fewer than two concept candidates")
    if len(concept_paths) < 2:
        failures.append("fewer than two concept notes")
    if linked_source_count < 1:
        failures.append("missing linked source")
    return failures


def update_raw_note(note: Note, compiled_path: Path, concept_paths: list[Path], status: str, failures: list[str]) -> None:
    note.frontmatter["capture_status"] = status
    note.frontmatter["compiled_note"] = wiki_link(compiled_path)
    note.frontmatter["compiled_on"] = today()
    note.frontmatter["concept_notes"] = [wiki_link(path) for path in concept_paths]
    if failures:
        note.frontmatter["compile_quality"] = "failed"
        note.frontmatter["compile_failures"] = failures
    else:
        note.frontmatter["compile_quality"] = "passed"
        note.frontmatter.pop("compile_failures", None)
    write_note(note.path, note.frontmatter, note.body)


def mark_raw_failed(note: Note, failures: list[str]) -> None:
    note.frontmatter["capture_status"] = "needs_compile"
    note.frontmatter["compile_quality"] = "failed"
    note.frontmatter["compile_failures"] = failures
    write_note(note.path, note.frontmatter, note.body)


def set_compiled_quality(path: Path, status: str, failures: list[str]) -> None:
    if not path.exists():
        return
    note = read_note(path)
    note.frontmatter["compile_quality"] = status
    if failures:
        note.frontmatter["compile_failures"] = failures
    else:
        note.frontmatter.pop("compile_failures", None)
    write_note(path, note.frontmatter, note.body)


def update_raw_note_legacy(note: Note, compiled_path: Path, concept_paths: list[Path]) -> None:
    note.frontmatter["capture_status"] = "compiled"
    note.frontmatter["compiled_note"] = wiki_link(compiled_path)
    note.frontmatter["compiled_on"] = today()
    note.frontmatter["concept_notes"] = [wiki_link(path) for path in concept_paths]
    write_note(note.path, note.frontmatter, note.body)


def create_compiled_note(note: Note, data: dict[str, object], force: bool) -> tuple[Path, list[Path]]:
    existing_link = str(note.frontmatter.get("compiled_note", "")).strip()
    if existing_link:
        relative = existing_link[2:-2] + ".md"
        compiled_path = VAULT_ROOT / relative
        if compiled_path.exists() and not force:
            return compiled_path, paths_from_wikilink_list(note.frontmatter.get("concept_notes"))
        if compiled_path.exists() and force:
            concept_paths = create_or_update_concepts(data, compiled_path)
            target_path = compiled_path
        else:
            target_path = safe_note_path(COMPILED_ROOT, str(data["title"]))
            concept_paths = create_or_update_concepts(data, target_path)
    else:
        target_path = safe_note_path(COMPILED_ROOT, str(data["title"]))
        concept_paths = create_or_update_concepts(data, target_path)

    body_lines = [
        f"# {data['title']}",
        "",
        "## One-Line Summary",
        "",
        str(data["summary"]).strip(),
        "",
        "## Encyclopedia Entry",
        "",
        str(data["encyclopedia_entry"]).strip(),
        "",
        "## Key Concepts",
        "",
    ]
    if concept_paths:
        body_lines.extend(f"- {wiki_link(path)}" for path in concept_paths)
    else:
        body_lines.append("- ")
    body_lines.extend(
        [
            "",
            "## Why It Matters",
            "",
            str(data["why_it_matters"]).strip(),
            "",
            "## Actionable Takeaways",
            "",
        ]
    )
    takeaways = data.get("actionable_takeaways", [])
    if isinstance(takeaways, list) and takeaways:
        body_lines.extend(f"- {item}" for item in takeaways)
    else:
        body_lines.append("- ")
    body_lines.extend(
        [
            "",
            "## Linked Source",
            "",
            f"- {wiki_link(note.path)}",
        ]
    )
    frontmatter = {
        "type": "knowledge",
        "area": data.get("area", "learning"),
        "domain": data.get("domain", "raw_compile"),
        "source": wiki_link(note.path),
        "source_type": "raw_source",
        "compiled_from": wiki_link(note.path),
        "created": today(),
        "updated": today(),
        "tags": ["knowledge", "compiled"],
    }
    write_note(target_path, frontmatter, "\n".join(body_lines))
    return target_path, concept_paths


def create_or_update_concepts(data: dict[str, object], compiled_path: Path) -> list[Path]:
    concept_paths: list[Path] = []
    raw_concepts = data.get("key_concepts", [])
    if not isinstance(raw_concepts, list):
        return concept_paths
    for concept in raw_concepts:
        title = str(concept).strip()
        if not title:
            continue
        path = CONCEPT_ROOT / f"{slugify(title)}.md"
        if path.exists():
            note = read_note(path)
            sources = extract_wikilinks(note.body)
            sources.add(wiki_link(compiled_path))
            note.frontmatter["source_count"] = str(len(sources))
            note.frontmatter["updated"] = today()
            body = note.body
            if "## Linked Sources" in body:
                body = re.sub(
                    r"## Linked Sources\s*(.*?)(\n## |\Z)",
                    "## Linked Sources\n\n" + "\n".join(f"- {link}" for link in sorted(sources)) + r"\2",
                    body,
                    flags=re.S,
                )
            else:
                body += "\n\n## Linked Sources\n\n" + "\n".join(f"- {link}" for link in sorted(sources))
            write_note(path, note.frontmatter, body)
        else:
            frontmatter = {
                "type": "concept",
                "area": data.get("area", "learning"),
                "domain": data.get("domain", "raw_compile"),
                "source_count": "1",
                "updated": today(),
                "tags": ["concept"],
            }
            body = "\n".join(
                [
                    f"# {title}",
                    "",
                    "## Definition",
                    "",
                    f"{title} is a concept extracted from {wiki_link(compiled_path)}.",
                    "",
                    "## Why It Matters",
                    "",
                    f"This concept appears in the compiled knowledge note {wiki_link(compiled_path)} and should accumulate sources over time.",
                    "",
                    "## Linked Sources",
                    "",
                    f"- {wiki_link(compiled_path)}",
                    "",
                    "## Related Concepts",
                ]
            )
            write_note(path, frontmatter, body)
        concept_paths.append(path)
    return concept_paths


def extract_wikilinks(text: str) -> set[str]:
    return {f"[[{match.group(1)}]]" for match in re.finditer(r"\[\[([^\]]+)\]\]", text)}


def process_notes(provider: str, model: str, only_uncompiled: bool, limit: int | None, force: bool) -> None:
    notes = [read_note(path) for path in list_raw_notes()]
    processed = 0
    for note in notes:
        if only_uncompiled and str(note.frontmatter.get("capture_status", "")).strip() == "compiled" and not force:
            continue
        data = compile_note(note, provider, model)
        compiled_path, concept_paths = create_compiled_note(note, data, force=force)
        failures = quality_gate(data, concept_paths, linked_source_count=1)
        if failures:
            mark_raw_failed(note, failures)
            set_compiled_quality(compiled_path, "failed", failures)
            print(f"needs_compile\t{note.path.relative_to(VAULT_ROOT)}\t{'; '.join(failures)}")
        else:
            update_raw_note(note, compiled_path, concept_paths, "compiled", failures)
            set_compiled_quality(compiled_path, "passed", failures)
            print(f"compiled\t{note.path.relative_to(VAULT_ROOT)}\t{compiled_path.relative_to(VAULT_ROOT)}")
        processed += 1
        if limit and processed >= limit:
            break


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile raw markdown notes into a structured wiki.")
    parser.add_argument("--provider", default="auto", choices=["auto", "ollama", "none"])
    parser.add_argument("--model", default="qwen2.5:7b")
    parser.add_argument("--only-uncompiled", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    provider = choose_provider(args.provider)
    process_notes(provider, args.model, args.only_uncompiled, args.limit, args.force)


if __name__ == "__main__":
    main()

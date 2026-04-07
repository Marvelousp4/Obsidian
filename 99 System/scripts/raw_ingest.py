#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import subprocess
from datetime import date
from pathlib import Path

from pypdf import PdfReader


VAULT_ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = VAULT_ROOT / "10 Raw"


def slugify(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r'[\\/:*?"<>|]', "", text)
    return text or "Untitled"


def title_from_path(path: Path) -> str:
    title = path.stem.replace("_", " ").replace("-", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title or "Untitled"


def today() -> str:
    return date.today().isoformat()


def wiki_link(path: Path) -> str:
    relative = path.relative_to(VAULT_ROOT).as_posix()
    return f"[[{relative[:-3]}]]"


def portable_path(path: Path) -> str:
    try:
        return path.relative_to(VAULT_ROOT).as_posix()
    except ValueError:
        return path.name


def yaml_value(value: str | list[str] | None) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        if not value:
            return "[]"
        rendered = "\n".join(f"  - {item}" for item in value)
        return f"\n{rendered}"
    if "\n" in value:
        lines = "\n".join(f"  {line}" for line in value.splitlines())
        return f">-\n{lines}"
    return value


def render_frontmatter(data: dict[str, str | list[str] | None]) -> str:
    lines = ["---"]
    for key, value in data.items():
        rendered = yaml_value(value)
        if rendered.startswith("\n"):
            lines.append(f"{key}:{rendered}")
        else:
            lines.append(f"{key}: {rendered}")
    lines.append("---")
    return "\n".join(lines)


def ensure_output(folder: str, title: str) -> Path:
    output_dir = RAW_ROOT / folder
    output_dir.mkdir(parents=True, exist_ok=True)
    base = f"{today()} - {slugify(title)}.md"
    path = output_dir / base
    counter = 2
    while path.exists():
        path = output_dir / f"{today()} - {slugify(title)} {counter}.md"
        counter += 1
    return path


def write_raw_note(
    output_path: Path,
    *,
    title: str,
    source_kind: str,
    source_path: str | None,
    source_url: str | None,
    repo_url: str | None,
    body_sections: list[tuple[str, str]],
) -> None:
    frontmatter = render_frontmatter(
        {
            "type": "raw_source",
            "source_kind": source_kind,
            "capture_status": "inbox",
            "captured": today(),
            "source_path": source_path or "",
            "source_url": source_url or "",
            "repo_url": repo_url or "",
            "compiled_note": "",
            "tags": ["raw", source_kind],
        }
    )
    body = [frontmatter, "", f"# {title}", ""]
    for heading, content in body_sections:
        body.extend([f"## {heading}", "", content.strip(), ""])
    output_path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        pages.append((page.extract_text() or "").strip())
    text = "\n\n".join(page for page in pages if page)
    return text.strip()


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def repo_remote(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "remote", "get-url", "origin"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def repo_head(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def repo_tree(path: Path, max_depth: int = 2) -> str:
    lines: list[str] = []
    root_depth = len(path.parts)
    for root, dirs, files in os.walk(path):
        current = Path(root)
        rel = current.relative_to(path)
        depth = len(current.parts) - root_depth
        if depth > max_depth:
            dirs[:] = []
            continue
        if rel != Path("."):
            indent = "  " * depth
            lines.append(f"{indent}{rel.name}/")
        for file_name in sorted(files):
            if file_name.startswith(".git"):
                continue
            indent = "  " * (depth + 1)
            lines.append(f"{indent}{file_name}")
    return "\n".join(lines[:300]).strip()


def repo_readme(path: Path) -> str:
    for candidate in ("README.md", "readme.md", "README.MD"):
        readme = path / candidate
        if readme.exists():
            return read_text_file(readme)
    return ""


def default_folder(kind: str) -> str:
    return {
        "web": "Web",
        "paper": "Papers",
        "repo": "Repos",
        "note": "Inbox",
    }.get(kind, "Inbox")


def ingest_markdown(args: argparse.Namespace) -> None:
    source = Path(args.source).expanduser().resolve()
    title = args.title or title_from_path(source)
    folder = args.folder or default_folder(args.kind)
    output_path = ensure_output(folder, title)
    raw_text = read_text_file(source)
    write_raw_note(
        output_path,
        title=title,
        source_kind=args.kind,
        source_path=portable_path(source),
        source_url=args.source_url,
        repo_url=None,
        body_sections=[
            ("Source", f"- Original file: `{portable_path(source)}`\n- Why keep this:"),
            ("Raw Markdown", raw_text),
        ],
    )
    print(output_path)


def ingest_pdf(args: argparse.Namespace) -> None:
    source = Path(args.source).expanduser().resolve()
    title = args.title or title_from_path(source)
    folder = args.folder or default_folder("paper")
    output_path = ensure_output(folder, title)
    text = extract_pdf_text(source)
    write_raw_note(
        output_path,
        title=title,
        source_kind="paper",
        source_path=portable_path(source),
        source_url=args.source_url,
        repo_url=None,
        body_sections=[
            ("Source", f"- Original file: `{portable_path(source)}`\n- Why keep this:"),
            ("Raw Markdown", text or "_No extractable text found in this PDF._"),
        ],
    )
    print(output_path)


def ingest_repo(args: argparse.Namespace) -> None:
    source = Path(args.source).expanduser().resolve()
    title = args.title or title_from_path(source)
    folder = args.folder or default_folder("repo")
    output_path = ensure_output(folder, title)
    remote = repo_remote(source)
    commit = repo_head(source)
    readme = repo_readme(source)
    tree = repo_tree(source)
    source_block = [
        f"- Repo path: `{portable_path(source)}`",
        f"- Remote: {remote or 'N/A'}",
        f"- HEAD: `{commit or 'N/A'}`",
        "- Why keep this:",
    ]
    body_sections = [
        ("Source", "\n".join(source_block)),
        ("README", readme or "_No README found._"),
        ("Repo Tree", f"```text\n{tree or '(empty)'}\n```"),
    ]
    write_raw_note(
        output_path,
        title=title,
        source_kind="repo",
        source_path=portable_path(source),
        source_url=None,
        repo_url=remote,
        body_sections=body_sections,
    )
    print(output_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn source material into markdown raw notes.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    markdown_parser = subparsers.add_parser("markdown", help="Ingest a markdown or text file.")
    markdown_parser.add_argument("source")
    markdown_parser.add_argument("--kind", default="web", choices=["web", "note"])
    markdown_parser.add_argument("--title")
    markdown_parser.add_argument("--folder")
    markdown_parser.add_argument("--source-url")
    markdown_parser.set_defaults(func=ingest_markdown)

    pdf_parser = subparsers.add_parser("pdf", help="Extract a PDF into a raw markdown note.")
    pdf_parser.add_argument("source")
    pdf_parser.add_argument("--title")
    pdf_parser.add_argument("--folder")
    pdf_parser.add_argument("--source-url")
    pdf_parser.set_defaults(func=ingest_pdf)

    repo_parser = subparsers.add_parser("repo", help="Create a repo digest raw note.")
    repo_parser.add_argument("source")
    repo_parser.add_argument("--title")
    repo_parser.add_argument("--folder")
    repo_parser.set_defaults(func=ingest_repo)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

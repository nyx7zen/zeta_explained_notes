"""Build Claude.ai web request files for one lecture.

This script does not call Claude.ai and does not create a zip archive. It writes
small Markdown request files that tell the user which project files to upload
and what to ask Claude.ai to do.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOCAL_DIR = PROJECT_ROOT / "local"
TASKS_DIR = PROJECT_ROOT / "tasks"


def normalize_lecture_id(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    if not digits:
        raise ValueError(f"Invalid lecture id: {value!r}")
    return digits.zfill(3)


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp949"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def find_lecture_entry(lecture_id: str) -> dict[str, str]:
    list_path = PROJECT_ROOT / "LECTURE_LIST.yml"
    if not list_path.exists():
        return {}

    text = read_text(list_path)
    current: dict[str, str] | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        id_match = re.match(r'-\s+id:\s*"([^"]+)"', line)
        if id_match:
            if current and current.get("id") == lecture_id:
                return current
            current = {"id": id_match.group(1)}
            continue

        if current is None:
            continue

        field_match = re.match(r'(title_ko|title_en|url):\s*"([^"]*)"', line)
        if field_match:
            current[field_match.group(1)] = field_match.group(2)

    if current and current.get("id") == lecture_id:
        return current
    return {}


def required_paths(lecture_id: str) -> dict[str, Path]:
    lecture_dir = LOCAL_DIR / f"lec-{lecture_id}"
    return {
        "slides_pdf": lecture_dir / f"lec-{lecture_id}_slides.pdf",
        "transcript": lecture_dir / f"lec-{lecture_id}.cleaned.txt",
        "description": lecture_dir / f"lec-{lecture_id}_desc.txt",
        "lecture_list": PROJECT_ROOT / "LECTURE_LIST.yml",
        "writing_prompt": TASKS_DIR / "prompt.md",
        "example_notes": PROJECT_ROOT / "docs" / "contents" / "lec-001" / "lec-001_notes.md",
    }


def missing_files(paths: dict[str, Path]) -> list[Path]:
    return [path for path in paths.values() if not path.exists()]


def rel(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def build_readme(lecture_id: str, paths: dict[str, Path], meta: dict[str, str]) -> str:
    title = meta.get("title_en") or f"Lecture {lecture_id}"
    url = meta.get("url") or "(not found)"
    attach_lines = "\n".join(f"- `{rel(path)}`" for path in paths.values())
    return f"""
# Claude.ai Web Bundle: lec-{lecture_id}

Lecture: **{title}**

Source: {url}

This folder contains prompt files for reducing Claude.ai Pro usage. It does not
call Claude.ai and it does not create an archive.

## Recommended Low-Usage Workflow

1. Open `01_source_digest_request.md` and paste it into Claude.ai.
2. Attach only the source files listed in that request.
3. Save Claude's output as `local/lec-{lecture_id}/claude_web_bundle/source_digest.md`.
4. Use `02_notes_from_digest_request.md` with `source_digest.md` to create the final notes.
5. Use `03_review_request.md` only for targeted review of uncertain formulas or sections.

## Project Files

{attach_lines}

## Why This Helps

The expensive multimodal step is limited to extracting a compact source digest
from the PDF and transcript. The final writing step can then work from the much
smaller digest instead of repeatedly re-reading the full PDF and full transcript.
"""


def build_digest_request(lecture_id: str, paths: dict[str, Path], meta: dict[str, str]) -> str:
    title = meta.get("title_en") or f"Lecture {lecture_id}"
    url = meta.get("url") or "(not found)"
    return f"""
# Request 1: Create a Compact Source Digest

You are helping prepare Korean lecture notes for a mathematics course.

Lecture id: {lecture_id}
Lecture title: {title}
Source URL: {url}

Attach these files:

- `{rel(paths["slides_pdf"])}`
- `{rel(paths["transcript"])}`
- `{rel(paths["description"])}`
- `{rel(paths["lecture_list"])}`

Do not write the final lecture notes yet.

Read the attached slide PDF visually and the transcript carefully. Create a
compact source digest that will be used later to write `lec-{lecture_id}_notes.md`.

Output in Markdown with exactly these sections:

## Lecture Metadata

- English title
- Korean title if available
- Source URL
- One-sentence learning goal in Korean

## Section Outline

List 5-10 major sections in lecture order. For each section include:

- short English label
- Korean section title candidate
- related slide/page numbers if visible
- related transcript phrases or timestamps if available

## Slide Formulas

Extract every important formula from the PDF as LaTeX. Use `$...$` for inline
math and `$$...$$` for display math. Preserve symbols exactly. If uncertain,
mark it with `[확인 필요]`.

For each formula include:

- slide/page number if visible
- LaTeX
- one Korean sentence explaining its role

## Transcript Concepts

Summarize the main mathematical explanations from the transcript in Korean.
Include definitions, proof ideas, warnings, historical notes, and examples.
Keep this compact.

## Figure Candidates

List visual figures or graphs that should become placeholders in the final
notes. For each item include:

- suggested filename `images/fig-{lecture_id}-YYY.png`
- caption title in Korean
- 2-3 Korean sentences explaining the figure

## Risk Checklist

List formulas, terms, or slide readings that are uncertain and should be checked
manually.

Important constraints:

- Do not invent formulas not visible in the PDF or strongly supported by the transcript.
- Prefer compact, factual extraction over polished prose.
- Keep the output much shorter than the transcript.
- The final notes will be written in a later step, so avoid long paragraphs.
"""


def build_notes_request(lecture_id: str, paths: dict[str, Path], meta: dict[str, str]) -> str:
    title = meta.get("title_en") or f"Lecture {lecture_id}"
    url = meta.get("url") or "(not found)"
    digest_path = LOCAL_DIR / f"lec-{lecture_id}" / "claude_web_bundle" / "source_digest.md"
    return f"""
# Request 2: Write Final Notes From the Source Digest

You are writing `docs/contents/lec-{lecture_id}/lec-{lecture_id}_notes.md`.

Lecture id: {lecture_id}
Lecture title: {title}
Source URL: {url}

Attach these files:

- `{rel(paths["writing_prompt"])}`
- `{rel(paths["example_notes"])}`
- `{rel(paths["description"])}`
- `{rel(paths["lecture_list"])}`
- `{rel(digest_path)}`

Use `source_digest.md` as the primary source. Use `prompt.md` and
`lec-001_notes.md` for style, structure, Korean tone, formula formatting, figure
placeholder format, Summary, and Review Questions.

Write the complete final Markdown document for:

`docs/contents/lec-{lecture_id}/lec-{lecture_id}_notes.md`

Requirements:

- Korean explanatory prose.
- Preserve important mathematical terms in English when they are standard proper
  nouns or theorem names.
- Use `$...$` for inline formulas.
- Use `equation`, `align*`, or plain `$$...$$` according to the project rules.
- Include figure placeholders only for figures listed in the digest.
- Include Summary and Review Questions as the last two sections.
- Do not mention that this was generated from a digest.
- If a formula is marked `[확인 필요]`, either avoid relying on it or keep the
  marker in a short comment for manual review.
"""


def build_review_request(lecture_id: str, paths: dict[str, Path]) -> str:
    notes_path = PROJECT_ROOT / "docs" / "contents" / f"lec-{lecture_id}" / f"lec-{lecture_id}_notes.md"
    return f"""
# Request 3: Targeted Review

Review the draft notes for lecture {lecture_id}.

Attach these files:

- `{rel(paths["slides_pdf"])}`
- `{rel(paths["transcript"])}`
- `{rel(notes_path)}`

Focus only on high-risk issues:

- formulas that differ from the slide PDF
- missing important formulas from the PDF
- incorrect mathematical claims
- transcript points that were omitted but are important
- figure placeholders that do not correspond to actual visuals

Return a concise checklist of fixes. Do not rewrite the entire document unless a
specific section is seriously wrong.
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Claude.ai web prompt files for one lecture."
    )
    parser.add_argument("lecture_id", help="Lecture id, e.g. 001 or 1")
    args = parser.parse_args()

    lecture_id = normalize_lecture_id(args.lecture_id)
    paths = required_paths(lecture_id)
    meta = find_lecture_entry(lecture_id)
    bundle_dir = LOCAL_DIR / f"lec-{lecture_id}" / "claude_web_bundle"

    missing = missing_files(paths)
    if missing:
        print("Warning: some expected files are missing:")
        for path in missing:
            print(f"  - {rel(path)}")

    write(bundle_dir / "README.md", build_readme(lecture_id, paths, meta))
    write(bundle_dir / "01_source_digest_request.md", build_digest_request(lecture_id, paths, meta))
    write(bundle_dir / "02_notes_from_digest_request.md", build_notes_request(lecture_id, paths, meta))
    write(bundle_dir / "03_review_request.md", build_review_request(lecture_id, paths))

    print(f"Created Claude.ai web bundle: {rel(bundle_dir)}")
    print("Start with: 01_source_digest_request.md")


if __name__ == "__main__":
    main()

"""Build OCR benchmark prompt files for comparing PDF-to-Markdown tools."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOCAL_DIR = PROJECT_ROOT / "local"


def normalize_lecture_id(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    if not digits:
        raise ValueError(f"Invalid lecture id: {value!r}")
    return digits.zfill(3)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def common_prompt(lecture_id: str, slides_pdf: Path) -> str:
    return f"""
# PDF OCR Benchmark Request

You are testing PDF-to-Markdown OCR quality for a mathematics lecture.

Input file:

- `{rel(slides_pdf)}`

Task:

Extract only the visible content from the attached image-based slide PDF.

Output a Markdown document with this exact structure:

```markdown
# lec-{lecture_id} Slides OCR

## Page 1

### English Text

...

### Formulas

1. `display`

$$
...
$$

2. `inline`

`$...$`

### Uncertain Items

- ...

## Page 2
...
```

Rules:

- Preserve page order.
- Extract English text as written on the slides.
- Convert every mathematical expression to LaTeX.
- Use `$...$` for inline math.
- Use `$$...$$` for display math.
- Do not translate, summarize, or explain.
- Do not add formulas that are not visible.
- If a symbol is unclear, write `[uncertain: ...]`.
- If a page has no formulas, write `None`.
- If a page has no English text, write `None`.
- Keep diagrams and graphs as short notes under `Uncertain Items`; do not invent captions.

The goal is faithful OCR, not polished lecture notes.
"""


def scoring_sheet(lecture_id: str) -> str:
    return f"""
# OCR Benchmark Scores: lec-{lecture_id}

Use the same slide PDF and the same prompt for each system.

Source PDF:

```text
local/lec-{lecture_id}/lec-{lecture_id}_slides.pdf
```

## Systems

| System | Output File | Notes |
|---|---|---|
| Claude.ai web | `claude_ai_web.md` | |
| ChatGPT web | `chatgpt_web.md` | |
| Gemini web | `gemini_web.md` | |
| Claude Code CLI | `claude_code_cli.md` | |
| Codex CLI | `codex_cli.md` | |
| Open-source model | `opensource.md` | |

## Score Rubric

Score each category from 0 to 5.

| Category | Claude.ai web | ChatGPT web | Gemini web | Claude Code CLI | Codex CLI | Open-source |
|---|---:|---:|---:|---:|---:|---:|
| Page order preserved | | | | | | |
| English text accuracy | | | | | | |
| Inline formula accuracy | | | | | | |
| Display formula accuracy | | | | | | |
| Symbol fidelity | | | | | | |
| Fraction/superscript/subscript fidelity | | | | | | |
| Multi-line derivation fidelity | | | | | | |
| Uncertainty marking | | | | | | |
| Markdown cleanliness | | | | | | |
| Easy to use in CLI pipeline | | | | | | |
| **Total / 50** | | | | | | |

## Error Log

Record concrete examples, not impressions.

| Page | System | Expected | Actual | Severity |
|---:|---|---|---|---|
| | | | | |

## CLI Capability Notes

Use this section to record whether the CLI can read the PDF/image directly or
whether it needs an external OCR tool.

| CLI | Direct PDF/image OCR worked? | External tool used | Command / Notes |
|---|---|---|---|
| Claude Code CLI | | | |
| Codex CLI | | | |

## Decision

Recommended OCR source:

```text
TBD
```

Reason:

```text
TBD
```
"""


def readme(lecture_id: str, slides_pdf: Path) -> str:
    return f"""
# OCR Benchmark Bundle: lec-{lecture_id}

This folder is for comparing web-based multimodal tools and open-source OCR on
the same image-based lecture PDF.

## Files

- `common_pdf_ocr_prompt.md`: paste the same prompt into each web tool.
- `cli_pdf_ocr_prompt.md`: use this prompt when testing Claude Code or Codex.
- `score_sheet.md`: fill in scores after saving each output.
- `outputs/`: save model outputs here.

## Source

```text
{rel(slides_pdf)}
```

## Suggested Output Files

```text
local/lec-{lecture_id}/ocr_benchmark/outputs/claude_ai_web.md
local/lec-{lecture_id}/ocr_benchmark/outputs/chatgpt_web.md
local/lec-{lecture_id}/ocr_benchmark/outputs/gemini_web.md
local/lec-{lecture_id}/ocr_benchmark/outputs/claude_code_cli.md
local/lec-{lecture_id}/ocr_benchmark/outputs/codex_cli.md
local/lec-{lecture_id}/ocr_benchmark/outputs/opensource.md
```

Use the exact same prompt and PDF for every system. Do not ask follow-up
questions during the first pass; follow-ups hide OCR weaknesses.
"""


def cli_prompt(lecture_id: str, slides_pdf: Path) -> str:
    output_path = LOCAL_DIR / f"lec-{lecture_id}" / "ocr_benchmark" / "outputs"
    return f"""
# CLI OCR Benchmark Request

Target input:

```text
{rel(slides_pdf)}
```

Task:

Try to extract visible English text and mathematical formulas from the PDF into
Markdown. Save the result to one of these files, depending on the CLI being
tested:

```text
{rel(output_path / "claude_code_cli.md")}
{rel(output_path / "codex_cli.md")}
```

Use this exact Markdown structure:

```markdown
# lec-{lecture_id} Slides OCR

## Page 1

### English Text

...

### Formulas

1. `display`

$$
...
$$

2. `inline`

`$...$`

### Uncertain Items

- ...
```

Rules:

- Preserve page order.
- Extract English text as written on the slides.
- Convert every mathematical expression to LaTeX.
- Do not translate, summarize, or explain.
- If the CLI cannot directly inspect the PDF/image visually, say so at the top
  under `## Capability Note`, then use an available local OCR tool only if one is
  already installed.
- Do not use paid APIs for this benchmark.
- Do not invent formulas.
- Mark unclear symbols with `[uncertain: ...]`.

After saving the output file, report which method was used:

- direct CLI multimodal reading
- local OCR library/tool
- unable to complete
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a benchmark bundle for PDF OCR model comparison."
    )
    parser.add_argument("lecture_id", help="Lecture id, e.g. 001 or 1")
    args = parser.parse_args()

    lecture_id = normalize_lecture_id(args.lecture_id)
    lecture_dir = LOCAL_DIR / f"lec-{lecture_id}"
    slides_pdf = lecture_dir / f"lec-{lecture_id}_slides.pdf"
    bundle_dir = lecture_dir / "ocr_benchmark"

    if not slides_pdf.exists():
        print(f"Warning: missing source PDF: {rel(slides_pdf)}")

    write(bundle_dir / "README.md", readme(lecture_id, slides_pdf))
    write(bundle_dir / "common_pdf_ocr_prompt.md", common_prompt(lecture_id, slides_pdf))
    write(bundle_dir / "cli_pdf_ocr_prompt.md", cli_prompt(lecture_id, slides_pdf))
    write(bundle_dir / "score_sheet.md", scoring_sheet(lecture_id))
    (bundle_dir / "outputs").mkdir(parents=True, exist_ok=True)

    print(f"Created OCR benchmark bundle: {rel(bundle_dir)}")
    print("Use common_pdf_ocr_prompt.md with each system.")


if __name__ == "__main__":
    main()

# OCR Model Comparison

This test compares tools for the narrow task needed by this project:

```text
image-based lecture PDF -> English text + LaTeX formulas -> Markdown
```

The goal is not to compare general writing quality. The best tool is the one
that produces the most faithful reusable Markdown source for later CLI-based
note generation.

## Test Targets

1. Claude.ai web
2. ChatGPT web
3. Gemini web
4. Claude Code CLI
5. Codex CLI
6. Open-source model

## Create A Test Bundle

```powershell
& "C:\winpython\WPy64-312101\python\python.exe" -m src.pipeline.build_ocr_benchmark_bundle 001
```

This creates:

```text
local/lec-001/ocr_benchmark/
  README.md
  common_pdf_ocr_prompt.md
  cli_pdf_ocr_prompt.md
  score_sheet.md
  outputs/
```

## Run The Test

For each web tool:

1. Open `common_pdf_ocr_prompt.md`.
2. Paste the prompt into the web tool.
3. Attach `local/lec-NNN/lec-NNN_slides.pdf`.
4. Save the response under `outputs/`.
5. Do not ask follow-up questions during the first pass.

Suggested output filenames:

```text
outputs/claude_ai_web.md
outputs/chatgpt_web.md
outputs/gemini_web.md
outputs/claude_code_cli.md
outputs/codex_cli.md
outputs/opensource.md
```

## CLI Test

Use `cli_pdf_ocr_prompt.md` for Claude Code and Codex. The CLI test should
record one of three outcomes:

- direct CLI multimodal PDF/image reading worked
- direct reading did not work, but a local OCR tool produced Markdown
- unable to complete without installing extra tools or using a paid API

For fairness, do not let the CLI use Claude.ai web, ChatGPT web, Gemini web, or
paid OCR APIs during this benchmark.

## Score

Fill in `score_sheet.md`.

The key categories are:

- English text accuracy
- inline formula accuracy
- display formula accuracy
- symbol fidelity
- fraction/superscript/subscript fidelity
- multi-line derivation fidelity
- Markdown cleanliness
- ease of use in a CLI pipeline
- whether direct CLI multimodal reading works

## Recommended Decision Rule

Choose the model that wins on formula fidelity unless its Markdown is unusable.
English text can often be repaired from the transcript, but incorrect LaTeX
formulas are expensive to detect later.

For CLI tools, distinguish two different scores:

- OCR quality: how good the extracted Markdown is
- automation quality: how reproducible the workflow is from a command line

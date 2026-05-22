# Claude.ai Web Workflow

This workflow reduces Claude.ai Pro usage by separating multimodal extraction
from final note writing.

## Problem

Sending the full writing prompt, transcript, description, lecture list, and
slide PDF in one request makes Claude.ai spend usage on three tasks at once:

- reading the image PDF
- reading the full transcript
- writing and polishing the final notes

For several lectures in a row, this can exhaust the Claude.ai Pro usage window.

## Recommended Workflow

Generate request files:

```powershell
python -m src.pipeline.build_claude_web_bundle 001
```

Then open:

```text
local/lec-001/claude_web_bundle/
```

Use the files in this order:

1. `01_source_digest_request.md`
2. `02_notes_from_digest_request.md`
3. `03_review_request.md`

## Step 1: Source Digest

Paste `01_source_digest_request.md` into Claude.ai and attach:

- `local/lec-NNN/lec-NNN_slides.pdf`
- `local/lec-NNN/lec-NNN.cleaned.txt`
- `local/lec-NNN/lec-NNN_desc.txt`
- `LECTURE_LIST.yml`

Save Claude's output as:

```text
local/lec-NNN/claude_web_bundle/source_digest.md
```

This is the only step that needs the full image PDF.

## Step 2: Final Notes

Paste `02_notes_from_digest_request.md` into Claude.ai and attach:

- `tasks/prompt.md`
- `docs/contents/lec-001/lec-001_notes.md`
- `local/lec-NNN/lec-NNN_desc.txt`
- `LECTURE_LIST.yml`
- `local/lec-NNN/claude_web_bundle/source_digest.md`

The source digest is much smaller than the full PDF plus transcript, so this
step should use less context.

## Step 3: Targeted Review

Use `03_review_request.md` only when the draft has risky formulas or unclear
figures. Ask Claude.ai to return a checklist of fixes instead of rewriting the
whole document.

## Notes

This does not bypass Claude.ai limits. It reduces repeated usage by avoiding
full PDF and transcript re-reading after the source digest is created.

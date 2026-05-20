# Project Folder Structure

```
zeta_explained_notes/
├── CLAUDE.md
├── README.md
├── LECTURE_LIST.yml
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml
├── tasks/
│   ├── guide.md
│   ├── pipeline.md
│   ├── prompt.md
│   ├── structure.md
│   └── workflow.md
├── docs/
│   ├── _config.yml
│   ├── _toc.yml
│   ├── intro.md
│   ├── lecture_list.md
│   ├── references.bib
│   ├── _static/
│   │   └── custom.css
│   └── contents/
│       └── lec-NNN/
│           ├── lec-NNN_notes.md
│           ├── lec-NNN_figures.ipynb
│           └── images/
│               └── fig-NNN-YYY.png
├── src/
│   ├── __init__.py
│   ├── notebook/
│   │   └── __init__.py
│   └── pipeline/
│       ├── __init__.py
│       ├── LECTURE_URLS.py
│       ├── clean_vtt.py
│       ├── create_lecture_desc.py
│       ├── create_lecture_slides.py
│       ├── create_lecture_text.py
│       ├── extract_frames.py
│       └── images_to_pdf.py
└── local/                          ← .gitignore 제외
    └── lec-NNN/
        ├── lec-NNN.en.raw.vtt
        ├── lec-NNN.en.vtt
        ├── lec-NNN.cleaned.txt
        ├── lec-NNN.mp4
        ├── lec-NNN_desc.txt
        └── lec-NNN_slides.pdf
```
# Pipeline Guide

이 문서는 Zeta Explained Course Notes 프로젝트의 환경 구축과
파이프라인 개요를 설명한다.

- 폴더/파일 구조: `tasks/structure.md` 참조
- 강의별 작업 절차: `tasks/workflow.md` 참조

---

## 1. 환경 구축

### 1-1. yt-dlp

YouTube 자막 및 동영상 다운로드에 사용한다.

```bash
pip install yt-dlp
pip install -U yt-dlp       # 업데이트
yt-dlp --version            # 버전 확인
```

### 1-2. Deno (JavaScript Runtime)

yt-dlp가 YouTube에서 일부 포맷을 추출할 때 필요하다.

```bash
winget install DenoLand.Deno
deno --version
```

### 1-3. ffmpeg

동영상 처리에 필요하다.

```bash
winget install Gyan.FFmpeg
ffmpeg -version
```

### 1-4. OpenCV

장면 변화 감지 기반 프레임 추출에 사용한다.

```bash
pip install opencv-python
```

### 1-5. Pillow

프레임 이미지 → PDF 변환에 사용한다.

```bash
pip install Pillow
```

### 1-6. PyYAML

`LECTURE_LIST.yml` 읽기에 사용한다.

```bash
pip install pyyaml
```

> 설치 후 터미널을 재시작해야 PATH가 적용된다.

---

## 2. 파이프라인 개요

Stage 1, 2, 3은 서로 독립적으로 실행 가능하다.
Stage 4는 Stage 1, 2, 3이 모두 완료된 후 진행한다.
Stage 5는 Stage 4 완료 후 사용자가 수동으로 진행한다.

```
LECTURE_LIST.yml
    │
    ├── Stage 1 (자막 추출)      ──────────────────────┐
    │                                                  │
    ├── Stage 2 (동영상 + PDF)   ──────────────────────┤
    │                                                  │
    └── Stage 3 (더보기 추출)    ──────────────────────┤
                                                       │
                                              Stage 4 (노트 작성)
                                              Claude Code / 웹 AI
                                                       │
                                              lec-NNN_notes.md
                                              (그래프 플레이스홀더 포함)
                                                       │
                                              Stage 5 (그래프 이미지 작업)
                                                       │
                                              docs/contents/lec-NNN/images/
                                              lec-NNN_figures.ipynb
```

---

## 3. 파일 네이밍 규칙

| 파일 | 경로 | 생성 주체 |
|------|------|-----------|
| `LECTURE_LIST.yml` | 루트 | 수동 관리 |
| `lec-NNN.en.raw.vtt` | `local/lec-NNN/` | Stage 1 |
| `lec-NNN.en.vtt` | `local/lec-NNN/` | Stage 1 |
| `lec-NNN.cleaned.txt` | `local/lec-NNN/` | Stage 1 |
| `lec-NNN.mp4` | `local/lec-NNN/` | Stage 2 |
| `lec-NNN_slides.pdf` | `local/lec-NNN/` | Stage 2 |
| `lec-NNN_desc.txt` | `local/lec-NNN/` | Stage 3 |
| `lec-NNN_notes.md` | `docs/contents/lec-NNN/` | Stage 4 |
| `fig-NNN-YYY.png` | `docs/contents/lec-NNN/images/` | Stage 5 |
| `lec-NNN_figures.ipynb` | `docs/contents/lec-NNN/` | Stage 5 |

---

## 4. Jupyter Book 빌드

```bash
# 1. Clean
jupyter-book clean docs/

# 2. Build
jupyter-book build docs/
```

로컬 확인:

```cmd
# CMD
start docs\_build\html\index.html

# PowerShell
Start-Process docs\_build\html\index.html
```

```bash
# WSL
explorer.exe docs/_build/html/index.html
```

GitHub에 push하면 GitHub Actions가 자동으로 빌드 및 배포한다.
`.github/workflows/deploy.yml` 참조.
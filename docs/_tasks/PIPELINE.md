# Pipeline Guide

이 문서는 Zeta Explained Course Notes 프로젝트의 환경 구축,
폴더/파일 구조, 파일 네이밍 규칙, 그리고 강의별 작업 파이프라인을 설명한다.

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

> 설치 후 터미널을 재시작해야 PATH가 적용된다.

---

## 2. 폴더 / 파일 구조

```bash
zeta_explained_notes/
│
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── README.md                        ← 강의 소개, Lecture List
├── PIPELINE.md                      ← 이 문서
├── PROMPT.md                        ← 새 대화창용 노트 작성 instruction
├── setup.py                         ← src 패키지 editable 설치
│
├── src/
│   ├── __init__.py
│   ├── pipeline/                    ← 자막·이미지 처리 스크립트
│   │   ├── lectures.py              # 강의 URL 리스트
│   │   ├── create_lecture_text.py   # Stage 1 실행
│   │   ├── create_lecture_slides.py # Stage 2 실행
│   │   ├── clean_vtt.py             # 유틸: vtt 정제
│   │   ├── extract_frames.py        # 유틸: 프레임 추출
│   │   └── images_to_pdf.py         # 유틸: 이미지 → PDF
│   └── notebook/                    ← Jupyter notebook 수치해석·시각화
│       ├── __init__.py
│       ├── plot_utils.py
│       ├── math_utils.py
│       └── notebook_utils.py
│
├── docs/                            ← GitHub 공유 O
│   ├── _config.yml
│   ├── _toc.yml
│   ├── references.bib
│   ├── _static/
│   │   └── custom.css
│   └── contents/
│       ├── index.md
│       ├── lec-001/
│       │   ├── lec-001_notes.md
│       │   ├── lec-001_plots.ipynb  ← 필요시만
│       │   └── images/              ← 강의 그래프 이미지
│       │       ├── fig-001-001.png
│       │       └── ...
│       └── ...
│
└── local/                           ← GitHub 공유 X (.gitignore)
    ├── lec-001/
    │   ├── lec-001.en.raw.vtt       ← yt-dlp 원본 자막
    │   ├── lec-001.en.vtt           ← 정제본 (동영상 플레이어 자동 로드)
    │   ├── lec-001.cleaned.txt      ← 문서 작성용 정제 텍스트
    │   ├── lec-001.mp4              ← 동영상
    │   ├── lec-001_slides.pdf       ← 슬라이드 PDF
    │   └── frames/                  ← 추출된 슬라이드 이미지
    │       ├── frame_0001.png
    │       └── ...
    └── ...
```

---

## 3. 파일 네이밍 규칙

| 파일 | 경로 | 생성 방법 |
|------|------|-----------|
| `lec-NNN.en.raw.vtt` | `local/lec-NNN/` | yt-dlp 자막 추출 (원본) |
| `lec-NNN.en.vtt` | `local/lec-NNN/` | clean_vtt.py (정제본, 자동 로드) |
| `lec-NNN.cleaned.txt` | `local/lec-NNN/` | clean_vtt.py (문서 작성용) |
| `lec-NNN.mp4` | `local/lec-NNN/` | yt-dlp 동영상 다운로드 |
| `lec-NNN_slides.pdf` | `local/lec-NNN/` | images_to_pdf.py |
| `frames/frame_XXXX.png` | `local/lec-NNN/frames/` | extract_frames.py |
| `lec-NNN_notes.md` | `docs/contents/lec-NNN/` | Stage 3 문서 작성 |
| `fig-NNN-YYY.png` | `docs/contents/lec-NNN/images/` | 사용자 수동 저장 |
| `lec-NNN_plots.ipynb` | `docs/contents/lec-NNN/` | 필요시만 |

---

## 4. 파이프라인

Stage 1과 Stage 2는 서로 독립적이므로 동시에 진행 가능하다.
Stage 3은 Stage 1과 Stage 2가 모두 완료된 후 진행한다.
Stage 4는 Stage 3 완료 후 사용자가 수동으로 진행한다.

```
YouTube URL
    │
    ├── Stage 1 (자막)     ─────────────────────────┐
    │                                               │
    └── Stage 2 (슬라이드) ─────────────────────────┤
                                                    │
                                             Stage 3 (문서 작성)
                                                    │
                                             lec-NNN_notes.md
                                             (그래프 플레이스홀더 포함)
                                                    │
                                             Stage 4 (그래프 이미지 저장)
                                                    │
                                             docs/contents/lec-NNN/images/
```

---

## 5. Stage 1: 자막 생성

**입력**: YouTube URL
**출력**: `lec-NNN.en.raw.vtt`, `lec-NNN.en.vtt`, `lec-NNN.cleaned.txt`

### 실행

`src/pipeline/create_lecture_text.py` 상단의 `LECTURES` 리스트에서
처리할 강의의 주석을 해제한 후 실행한다.

```python
# create_lecture_text.py 내 LECTURES 리스트 예시
LECTURES = [
    ("lec-002", "https://youtu.be/VIDEO_ID"),
    # ("lec-003", "https://youtu.be/VIDEO_ID"),
]
```

```bash
python src/pipeline/create_lecture_text.py
```

### 완료 체크리스트

```
□ local/lec-NNN/lec-NNN.en.raw.vtt    ← yt-dlp 원본
□ local/lec-NNN/lec-NNN.en.vtt        ← 정제본 (자동 로드)
□ local/lec-NNN/lec-NNN.cleaned.txt   ← 문서 작성용
```

---

## 6. Stage 2: 슬라이드 생성

**입력**: YouTube URL
**출력**: `lec-NNN.mp4`, `frames/*.png`, `lec-NNN_slides.pdf`

### 실행

`src/pipeline/create_lecture_slides.py` 상단의 `LECTURES` 리스트에서
처리할 강의의 주석을 해제한 후 실행한다.

```python
# create_lecture_slides.py 내 LECTURES 리스트 예시
LECTURES = [
    ("lec-002", "https://youtu.be/VIDEO_ID"),
    # ("lec-003", "https://youtu.be/VIDEO_ID"),
]
```

```bash
python src/pipeline/create_lecture_slides.py
```

### 프레임 추출 설정

| 설정 | 값 | 설명 |
|------|-----|------|
| `FRAME_THRESHOLD` | `0.001` | 장면 변화 감지 임계값 |

### PDF 검토 (사용자 작업)

생성된 `lec-NNN_slides.pdf`에서 불필요한 페이지를 삭제한다.

- 필기가 많이 겹친 슬라이드
- 동일 슬라이드 중복 페이지
- 강의 내용과 무관한 페이지 (피드백 슬라이드 등)

### 완료 체크리스트

```
□ local/lec-NNN/lec-NNN.mp4
□ local/lec-NNN/frames/frame_XXXX.png  (N장)
□ local/lec-NNN/lec-NNN_slides.pdf     (불필요 페이지 삭제 완료)
```

---

## 7. Stage 3: 문서 작성

**입력**: `lec-NNN.cleaned.txt`, `lec-NNN_slides.pdf`
**출력**: `lec-NNN_notes.md` (그래프 플레이스홀더 포함)

### 실행 절차

```
1. 새 Claude 대화창 열기
2. PROMPT.md 내용 전체를 첫 메시지로 붙여넣기
3. lec-NNN.cleaned.txt 첨부 (또는 내용 붙여넣기)
4. lec-NNN_slides.pdf 첨부
5. Claude가 lec-NNN_notes.md 초안 생성
   (자막과 슬라이드에서 그래프가 등장하는 섹션에 플레이스홀더 자동 삽입)
6. 검토 및 수정
7. docs/contents/lec-NNN/lec-NNN_notes.md 저장
8. _toc.yml 업데이트
```

### 완료 체크리스트

```
□ docs/contents/lec-NNN/lec-NNN_notes.md
□ 그래프 플레이스홀더 삽입 여부 확인
□ docs/_toc.yml 업데이트
□ (선택) docs/contents/lec-NNN/lec-NNN_plots.ipynb
```

---

## 8. Stage 4: 그래프 이미지 저장 (사용자 수동 작업)

**입력**: `local/lec-NNN/lec-NNN_slides.pdf`, `lec-NNN_notes.md`의 플레이스홀더
**출력**: `docs/contents/lec-NNN/images/fig-NNN-YYY.png`

### 실행 절차

```
1. lec-NNN_notes.md에서 플레이스홀더 목록 확인
   예: fig-001-001.png, fig-001-002.png, ...

2. lec-NNN_slides.pdf에서 해당 그래프 페이지 선별

3. 그래프 영역 크롭 및 저장
   저장 경로: docs/contents/lec-NNN/images/fig-NNN-YYY.png
   파일명 규칙: fig-{lec_id}-{순번}.png (순번 3자리)

4. 저장 완료 후 lec-NNN_notes.md 확인
   플레이스홀더 경로와 실제 파일명이 일치하는지 확인
```

### 파일명 규칙

```
fig-001-001.png   ← lec-001의 첫 번째 그래프
fig-001-002.png   ← lec-001의 두 번째 그래프
fig-002-001.png   ← lec-002의 첫 번째 그래프
```

### 완료 체크리스트

```
□ docs/contents/lec-NNN/images/ 폴더 생성
□ fig-NNN-YYY.png 파일 저장 (플레이스홀더 수만큼)
□ lec-NNN_notes.md의 플레이스홀더 경로와 파일명 일치 확인
```

---

## 9. Jupyter Book 빌드

```bash
# 빌드
jupyter-book build docs/

# 로컬 확인
open docs/_build/html/index.html   # Mac
start docs/_build/html/index.html  # Windows
```

GitHub에 push하면 GitHub Actions가 자동으로 빌드 및 배포한다.
`.github/workflows/deploy.yml` 참조.
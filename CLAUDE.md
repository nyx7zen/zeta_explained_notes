# CLAUDE.md

이 파일은 Claude Code가 `zeta_explained_notes` 프로젝트의 컨텍스트를 인식하기 위한
설정 파일이다. 모든 작업은 이 파일의 지침을 우선 따른다.

---

## 프로젝트 개요

YouTube "Zeta Explained" 재생목록의 강의 노트를 작성하는 프로젝트이다.
Riemann zeta function을 기초부터 Riemann hypothesis까지 단계적으로 학습하며,
강의별로 `lec-NNN_notes.md` 파일을 생성하여 Jupyter Book으로 배포한다.

- GitHub: `nyx7zen/zeta_explained_notes`
- 배포: https://nyx7zen.github.io/zeta_explained_notes/
- 참고문헌: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

---

## 파이프라인 개요

| Stage | 내용 | 수행 주체 |
|-------|------|-----------|
| 1 | 자막 추출·정제 → `lec-NNN.cleaned.txt` | 사용자 (터미널) |
| 2 | 동영상 다운로드 + 슬라이드 PDF 생성 | 사용자 (터미널) |
| 3 | 더보기(Description) 추출 → `lec-NNN_desc.txt` | 사용자 (터미널) |
| 4 | `lec-NNN_notes.md` 생성 | Claude Code |
| 5 | 그래프 이미지 저장 + `lec-NNN_figures.ipynb` 작업 | 사용자 |

Claude Code는 Stage 4만 담당한다.

---

## Stage 4: 강의 노트 작성

### 요청 형식

사용자가 "NNN강 문서를 만들어 주세요" 라고 요청하면 아래 절차를 따른다.

### 입력 파일 (읽기)

```
local/lec-NNN/lec-NNN.cleaned.txt    <- 자막 정제 텍스트
local/lec-NNN/lec-NNN_desc.txt       <- YouTube 더보기 내용
local/lec-NNN/lec-NNN_slides.pdf     <- 슬라이드 캡처 PDF
```

### 참조 파일 (스타일 기준)

아래 파일을 참조하여 수준, 문체, 수식 표현, 섹션 구성을 동일하게 유지한다.

```
docs/contents/lec-001/lec-001_notes.md
docs/contents/lec-002/lec-002_notes.md
docs/contents/lec-003/lec-003_notes.md
```

특히 `lec-001_notes.md`가 기준 예시이다. 다음을 반드시 확인한다.

- 제목 형식 및 1줄 요약 위치
- 수식 넘버링 비율 (핵심 수식 위주)
- `align*` 환경의 사용 방식 (증명 전개)
- Summary의 불릿 스타일 (이모지 없음)
- Review Questions의 질문 유형과 수 (8~10개)
- `> **주의**:` 블록의 사용 방식
- 그래프 플레이스홀더 형식 및 Figure 설명 수준

### 출력 파일 (생성)

```
docs/contents/lec-NNN/lec-NNN_notes.md
```

출력 전에 `docs/contents/lec-NNN/` 폴더가 존재하는지 확인한다.
폴더가 없으면 생성한 후 파일을 작성한다.

---

## 문서 구조

```markdown
# 강의 제목 (영어 원문, 번호 제외)

> 핵심 목표 1문장 요약

- **Source**: [Zeta Explained #NNN](https://youtu.be/VIDEO_ID)
- **Reference**: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

**Overview**

(lec-NNN_desc.txt의 강의 목적·범위 설명 — 한국어, 교과서체, 영어 키워드 유지)

**Contents**

(lec-NNN_desc.txt의 타임스탬프 제거 후 불릿 리스트 — 한국어, 수학 키워드 영어 유지)

---

## 1. [내용 섹션]
## 2. [내용 섹션]
...
## N. Summary
## N+1. Review Questions
```

---

## 언어 및 문체 원칙

- 설명은 한국어로 작성한다.
- 수학 용어는 한국어로 번역하여 사용한다.
  - 예: 해석적 연속, 자명한 영점, 임계 띠, 극점, 수렴
- 다음 고유명사·전문 용어는 영어 표기를 유지한다.
  - 인명 및 인명이 포함된 정리·함수명: Riemann hypothesis, Euler product,
    Dirichlet series, Weierstrass factorization, Hardy Z-function 등
  - 국제적으로 고유명사로 굳어진 개념: Jupyter Book, GitHub, LaTeX 등
- 처음 등장하는 용어는 한국어(영어) 병기를 허용한다.
  - 예: 해석적 연속(analytic continuation), 임계 띠(critical strip)
- 과도한 영어 표기를 최소화하고 부드러운 수학적 서술로 다듬는다.

---

## 수식 작성 원칙

### Inline 수식

- `$...$` 형식만 사용한다. `\(...\)` 형식은 사용하지 않는다.
- 수식 내부에서 줄바꿈을 허용하지 않는다.

### Display 수식 — 3가지 환경

**[1] 핵심 정의 / 핵심 결과 → `equation` (넘버링 O)**

```latex
$$
\begin{equation}
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
\end{equation}
$$
```

**[2] 증명 전개 (여러 줄) → `align*` (넘버링 X)**

```latex
$$
\begin{align*}
f(x) &= \cdots \\
     &= \cdots
\end{align*}
$$
```

**[3] 단순 표현 / 예시 → `$$...$$` (넘버링 X)**

```latex
$$
s = \tfrac{1}{2} \pm 14.13i, \quad \ldots
$$
```

넘버링 비율은 `lec-001_notes.md`를 기준으로 한다.

---

## 그래프 처리 원칙

### 그래프 식별 기준

자막에서 아래 표현이 등장하거나, 슬라이드 PDF에 시각적 요소(좌표계, 곡선, 음영 등)가
있는 경우 그래프가 포함된 것으로 판단한다.

- "as you can see", "shown here", "this graph shows", "let's look at"
- "the blue curve", "the red line", "plot", "graph", "figure", "diagram"
- "increasing", "decreasing", "converges to", "approaches"

### 플레이스홀더 형식

```markdown
![alt text](images/fig-NNN-YYY.png)

**Figure N.** 캡션 제목
설명 (2~5문장, 논문 Figure caption 스타일).
```

- `NNN`: 강의 번호 3자리, `YYY`: 강의 내 등장 순서 3자리
- `**Figure N.**`의 N은 문서 내 그림 순서 번호 (강의 번호 포함하지 않음)
- 설명은 그래프의 대상, 축의 의미, 주요 특징, 본문 수식과의 연관성을 포함한다.

---

## 자막 오류 보정

| 자막 오류 | 올바른 표현 |
|-----------|-------------|
| remon, reman, riman | Riemann |
| oiler, Oiler | Euler |
| tailaylor | Taylor |
| McLaren | Maclaurin |
| buyer stress | Weierstrass |
| number file | Numberphile |
| complex plain | complex plane |
| analytic continues | analytic continuation |
| converts | converges |
| serious | series |
| primer number | prime number |

---

## 파일 네이밍 규칙

| 파일 | 경로 |
|------|------|
| `lec-NNN.en.raw.vtt` | `local/lec-NNN/` |
| `lec-NNN.en.vtt` | `local/lec-NNN/` |
| `lec-NNN.cleaned.txt` | `local/lec-NNN/` |
| `lec-NNN.mp4` | `local/lec-NNN/` |
| `lec-NNN_desc.txt` | `local/lec-NNN/` |
| `lec-NNN_slides.pdf` | `local/lec-NNN/` |
| `lec-NNN_notes.md` | `docs/contents/lec-NNN/` |
| `fig-NNN-YYY.png` | `docs/contents/lec-NNN/images/` |
| `lec-NNN_figures.ipynb` | `docs/contents/lec-NNN/` |
| `LECTURE_LIST.yml` | `./` |

`local/` 폴더는 `.gitignore`에 의해 GitHub에 공유되지 않는다.

---

## 내용 누락 방지 체크리스트

생성 전 아래 항목을 점검한다.

1. 자막 전체를 검토하여 슬라이드에 없는 설명, 주의사항, 역사적 맥락이 반영되었는지 확인한다.
2. 슬라이드의 모든 수식이 LaTeX로 재작성되었는지 확인한다.
3. 강의자가 강조한 주의사항은 `> **주의**:` 블록으로 명시한다.
4. 자막에서 언급된 역사적 배경, 수치 예시, 참고문헌이 반영되었는지 확인한다.
5. 그래프가 등장하는 모든 섹션에 플레이스홀더가 삽입되었는지 확인한다.
6. Overview 및 Contents 섹션이 제목 아래에 작성되었는지 확인한다.
7. Summary는 불릿 리스트, Review Questions는 번호 리스트 (8~10개)로 작성한다.

---

## 상세 원칙 참조

더 상세한 원칙은 `tasks/guide.md`를 참조한다.
강의 제목 및 URL은 `./LECTURE_LIST.yml`을 참조한다.

---

## 프로젝트 환경

### Python 인터프리터

- 경로: `C:\winpython\WPy64-312101\python\python.exe`
- 배포판: WinPython 3.12

### Jupyter Book 빌드

`jupyter-book.exe`는 WinPython 환경에서 직접 실행이 안 되므로 아래 명령을 사용한다.
빌드 전 반드시 clean을 먼저 실행하고, 완료 후 브라우저로 자동 열기.

```powershell
# 1. Clean
& "C:\winpython\WPy64-312101\python\python.exe" -c "from jupyter_book.cli.main import main; import sys; sys.argv = ['jb', 'clean', 'd:/projects/nyx7zen/zeta_explained_notes/docs']; main()"

# 2. Build
& "C:\winpython\WPy64-312101\python\python.exe" -c "from jupyter_book.cli.main import main; import sys; sys.argv = ['jb', 'build', 'd:/projects/nyx7zen/zeta_explained_notes/docs']; main()"

# 3. Open browser
Start-Process "D:\projects\nyx7zen\zeta_explained_notes\docs\_build\html\index.html"
```

빌드 결과: `docs/_build/html/index.html`

### 프로젝트 구조

- 프로젝트 루트: `D:\projects\nyx7zen\zeta_explained_notes\`
- 문서 루트: `docs/`
- TOC: `docs/_toc.yml`
- 설정: `docs/_config.yml`
- GitHub Actions: `.github/workflows/deploy.yml` (main 브랜치 push 시 GitHub Pages 자동 배포)

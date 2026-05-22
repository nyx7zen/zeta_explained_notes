# 강의별 작업 절차 (lec-NNN)

각 단계는 독립적으로 실행 가능하다.
실행 전 `LECTURE_LIST.yml`에서 해당 강의의 URL을 확인한다.

---

## Stage 1. 자막 추출 및 정제

```bash
python src/pipeline/create_lecture_text.py
```

완료 확인:
```
local/lec-NNN/lec-NNN.en.raw.vtt    ← yt-dlp 원본 자막
local/lec-NNN/lec-NNN.en.vtt        ← 정제본
local/lec-NNN/lec-NNN.cleaned.txt   ← 문서 작성용 정제 텍스트
```

---

## Stage 2. 동영상 저장 및 슬라이드 PDF 생성

```bash
python src/pipeline/create_lecture_slides.py
```

완료 후 `lec-NNN_slides.pdf`에서 불필요한 페이지를 수동으로 삭제한다.

- 필기가 많이 겹친 슬라이드
- 동일 슬라이드 중복 페이지
- 강의 내용과 무관한 페이지

완료 확인:
```
local/lec-NNN/lec-NNN.mp4
local/lec-NNN/lec-NNN_slides.pdf    ← 불필요 페이지 삭제 완료
```

---

## Stage 3. 더보기(Description) 추출

```bash
python src/pipeline/create_lecture_desc.py
```

완료 확인:
```
local/lec-NNN/lec-NNN_desc.txt
```

---

## Stage 4. 강의 노트 작성

### Claude Code (VS Code Extension) 사용 시

프로젝트 루트에서 Claude Code를 열고 아래와 같이 요청한다.

```
NNN강 문서를 만들어 주세요.
```

Claude Code는 `CLAUDE.md`의 지침에 따라 아래 파일을 읽고 노트를 생성한다.

```
local/lec-NNN/lec-NNN.cleaned.txt
local/lec-NNN/lec-NNN_desc.txt
local/lec-NNN/lec-NNN_slides.pdf
```

출력:
```
docs/contents/lec-NNN/lec-NNN_notes.md
```

### 웹 기반 AI 대화창 사용 시 (Claude / Gemini)

`tasks/prompt.md` 전체 내용을 첫 메시지로 붙여넣은 후,
아래 4개 파일을 첨부하고 요청문을 입력한다.

```
local/lec-NNN/lec-NNN_slides.pdf
local/lec-NNN/lec-NNN.cleaned.txt
local/lec-NNN/lec-NNN_desc.txt
LECTURE_LIST.yml
```

요청문:
```
위 원칙에 따라 첨부한 파일들을 바탕으로 lec-NNN_notes.md를 작성해 주세요.

강의 번호: NNN
강의 제목 및 URL은 첨부한 LECTURE_LIST.yml을 참조한다.
```

완료 후 검토하고 저장한다:
```
docs/contents/lec-NNN/lec-NNN_notes.md
```

---

## Stage 4 완료 후

`docs/_toc.yml`에 해당 강의를 추가한다.

```yaml
- file: contents/lec-NNN/lec-NNN_notes
  title: "N. 한국어 제목"
  sections:
    - file: contents/lec-NNN/lec-NNN_figures   ← figures 파일이 있을 때만
```

---

## Stage 5. 그래프 이미지 작업

`lec-NNN_notes.md`의 플레이스홀더를 확인하고,
`lec-NNN_slides.pdf`에서 해당 그래프를 크롭하여 저장한다.

```
docs/contents/lec-NNN/images/fig-NNN-001.png
docs/contents/lec-NNN/images/fig-NNN-002.png
...
```

이후 `lec-NNN_figures.ipynb`에서 그래프를 하나씩 작업한다.

완료 확인:
```
□ lec-NNN_notes.md 플레이스홀더 경로와 파일명 일치 확인
□ docs/contents/lec-NNN/images/ 폴더 내 fig-NNN-YYY.png 저장 완료
□ lec-NNN_figures.ipynb 작업 완료
```

## lec-002 작업 절차

### 사전 준비 (현재 대화창에서)

**1. lec-002 YouTube URL 확인**

재생목록에서 lec-002 영상의 URL을 확인합니다.
```
https://youtube.com/playlist?list=PLTcPERDxgHxm7TzJ9W92S-l5pGRuhZz10
```

**2. `lectures.py` 수정 (한 파일만 수정)**

```python
LECTURES = [
    # ("lec-001", "https://youtu.be/RMFt-9PzF54"),
    ("lec-002", "https://youtu.be/VIDEO_ID"),  # 주석 해제
]
```

---

### Stage 1 실행 (자막 생성)

```bash
python src/pipeline/create_lecture_text.py
```

완료 확인:
```
local/lec-002/lec-002.en.raw.vtt
local/lec-002/lec-002.en.vtt
local/lec-002/lec-002.cleaned.txt
```

---

### Stage 2 실행 (슬라이드 생성)

Stage 1과 동시에 진행 가능합니다.

```bash
python src/pipeline/create_lecture_slides.py
```

완료 후 `lec-002_slides.pdf`에서 불필요한 페이지를 삭제합니다.

---

### Stage 3 실행 (문서 작성) — 새 대화창

**1. 새 Claude 대화창 열기**

**2. 첫 메시지 작성**

`PROMPT.md` 파일 전체 내용을 복사하여 붙여넣은 후, 아래 요청문을 추가합니다.

```
이 PROMPT.md의 원칙에 따라 첨부한 자막 파일과 슬라이드 PDF를 바탕으로
lec-002_notes.md를 작성해 주세요.

강의 제목: Zeta in the Complex Plane
Source URL: https://youtu.be/VIDEO_ID
```

**3. 파일 첨부**

```
local/lec-002/lec-002.cleaned.txt   <- 첨부
local/lec-002/lec-002_slides.pdf    <- 첨부 (페이지 삭제 완료본)
```

**4. 검토 및 저장**

Claude가 생성한 초안을 검토한 후 저장합니다.

```
docs/contents/lec-002/lec-002_notes.md
```

**5. `docs/_toc.yml` 업데이트**

```yaml
- file: contents/lec-001/lec-001_notes
- file: contents/lec-002/lec-002_notes  <- 추가
```

---

### 참고

새 대화창에서 작성된 노트를 `lec-001_notes.md`와 비교하여 수준/스타일이 동일한지 확인합니다. 차이가 있으면 추가 수정을 요청합니다.
import re
import os
import sys


def clean_vtt(vtt_path, out_dir):
    """
    VTT 파일을 정제하여 다음 두 파일을 생성한다.
      - lec-NNN.en.vtt      : 오류 보정된 영어 자막 (동영상 플레이어용)
      - lec-NNN.cleaned.txt : 문서 작성용 정제 텍스트
    """
    # 파일명에서 lec_id 추출 (예: lec-001.en.raw.vtt → lec-001)
    basename = os.path.basename(vtt_path)          # lec-001.en.raw.vtt
    lec_id   = basename.split(".")[0]              # lec-001

    out_vtt  = os.path.join(out_dir, f"{lec_id}.en.vtt")
    out_txt  = os.path.join(out_dir, f"{lec_id}.cleaned.txt")

    with open(vtt_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. 헤더 제거
    text = re.sub(r"WEBVTT.*?\n\n", "", text, flags=re.DOTALL)

    # 2. 타임스탬프 줄 임시 보존 (vtt 재생성용)
    timestamp_pattern = re.compile(
        r"(\d{2}:\d{2}:\d{2}\.\d+\s-->\s\d{2}:\d{2}:\d{2}\.\d+[^\n]*)\n"
    )

    # 3. 단어별 타임스탬프 태그 제거
    text_clean = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d+>", "", text)
    text_clean = re.sub(r"<c>|</c>", "", text_clean)

    # 4. 기타 HTML 태그 제거
    text_clean = re.sub(r"<[^>]+>", "", text_clean)

    # 5. 타임스탬프 줄 제거
    text_clean = re.sub(
        r"\d{2}:\d{2}:\d{2}\.\d+\s-->\s\d{2}:\d{2}:\d{2}\.\d+[^\n]*\n", "", text_clean
    )

    # 6. 중복 줄 제거
    lines = text_clean.split("\n")
    seen, result = set(), []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line not in seen:
            seen.add(line)
            result.append(line)

    clean_text = " ".join(result)

    # 7. π 인식 실패 패턴 복원
    clean_text = re.sub(r"p(?:&lt;unk&gt;|<unk>)\^2", "π²", clean_text)
    clean_text = re.sub(r"(\d)(?:&lt;unk&gt;|<unk>)\^?\s*2", r"\1π²", clean_text)
    clean_text = re.sub(r"(?:&lt;unk&gt;|<unk>)", "π", clean_text)

    # 8. 수학/인명 오류 보정
    corrections = [
        # 인명
        (r"\bremon\b",               "Riemann"),
        (r"\bRemon\b",               "Riemann"),
        (r"\breman\b",               "Riemann"),
        (r"\briman\b",               "Riemann"),
        (r"\boiler\b",               "Euler"),
        (r"\bOiler\b",               "Euler"),
        (r"\bAlexander Ev\b",        "Alexander Ivić"),
        (r"\bMangoli\b",             "Mengoli"),
        # 수학 용어
        (r"\btailaylor\b",           "Taylor"),
        (r"\bMcLaren\b",             "Maclaurin"),
        (r"\bbuyer stress\b",        "Weierstrass"),
        (r"\bzater\b",               "zeta"),
        (r"\bzada\b",                "zeta"),
        (r"\bconverts\b",            "converges"),
        (r"\bcomplex plain\b",       "complex plane"),
        (r"\breel part\b",           "real part"),
        (r"\banalytic continues\b",  "analytic continuation"),
        (r"\bprimer number\b",       "prime number"),
        (r"\bzeta over two\b",       "zeta of two"),
        (r"\bthe some of the\b",     "the sum of the"),
        # 고유명사
        (r"\bbasel\b",               "Basel"),
        (r"\bNE1\b",                 "-1"),
        (r"\bnumber file\b",         "Numberphile"),
        (r"\bnum values\b",          "numerical values"),
        # 구어체 sum → some (수학적 sum 은 유지)
        (r"\bdo sum math\b",         "do some math"),
        (r"\bsum basics\b",          "some basics"),
        (r"\bsum reports\b",         "some reports"),
        (r"\bsum steps\b",           "some steps"),
        (r"\bsum sense\b",           "some sense"),
        (r"\bsum skips\b",           "some skips"),
        (r"\bhere are sum\b",        "here are some"),
        (r"\bknow sum\b",            "know some"),
    ]
    for pattern, replacement in corrections:
        clean_text = re.sub(pattern, replacement, clean_text)

    # --- 출력 1: 문서 작성용 txt ---
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(clean_text)

    # --- 출력 2: 동영상 플레이어용 cleaned vtt ---
    # 원본 vtt에서 타임스탬프 블록을 다시 읽어 텍스트만 교체
    with open(vtt_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # 단어별 태그 제거 후 vtt 구조 유지
    vtt_clean = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d+>", "", raw)
    vtt_clean = re.sub(r"<c>|</c>", "", vtt_clean)
    vtt_clean = re.sub(r"<[^>]+>", "", vtt_clean)

    for pattern, replacement in corrections:
        vtt_clean = re.sub(pattern, replacement, vtt_clean)

    vtt_clean = re.sub(r"p(?:&lt;unk&gt;|<unk>)\^2", "π²", vtt_clean)
    vtt_clean = re.sub(r"(\d)(?:&lt;unk&gt;|<unk>)\^?\s*2", r"\1π²", vtt_clean)
    vtt_clean = re.sub(r"(?:&lt;unk&gt;|<unk>)", "π", vtt_clean)

    with open(out_vtt, "w", encoding="utf-8") as f:
        f.write(vtt_clean)

    print(f"  저장: {os.path.basename(out_vtt)}")
    print(f"  저장: {os.path.basename(out_txt)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python clean_vtt.py <input.en.raw.vtt> <output_dir>")
        sys.exit(1)
    clean_vtt(sys.argv[1], sys.argv[2])
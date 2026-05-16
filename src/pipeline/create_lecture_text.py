import os
import subprocess
import sys
from LECTURE_URLS import LECTURES

# ============================================================
# 경로 설정
# ============================================================
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOCAL_DIR    = os.path.join(PROJECT_ROOT, "local")
CLEAN_VTT    = os.path.join(SCRIPT_DIR, "clean_vtt.py")


def download_subtitle(lec_id, url, out_dir):
    """yt-dlp 로 영어 자막 추출 → lec-NNN.en.raw.vtt"""
    print("  [download_subtitle] 자막 추출 중...")
    output_tmpl = os.path.join(out_dir, f"{lec_id}.%(ext)s")

    result = subprocess.run(
        [
            "yt-dlp",
            "--skip-download",
            "--write-auto-subs",
            "--sub-lang", "en",
            "--sub-format", "vtt",
            "--output", output_tmpl,
            url,
        ],
        capture_output=True,
        text=True,
    )

    # yt-dlp 가 생성하는 실제 파일명: lec-NNN.en.vtt
    generated = os.path.join(out_dir, f"{lec_id}.en.vtt")
    raw_vtt   = os.path.join(out_dir, f"{lec_id}.en.raw.vtt")

    if not os.path.exists(generated):
        print("  [오류] 자막 추출 실패")
        print(result.stderr[-300:])
        return False

    os.rename(generated, raw_vtt)
    print(f"  완료: {lec_id}.en.raw.vtt")
    return True


def clean_subtitle(lec_id, out_dir):
    """clean_vtt.py 실행 → lec-NNN.en.vtt + lec-NNN.cleaned.txt"""
    print("  [clean_subtitle] 자막 정제 중...")
    raw_vtt = os.path.join(out_dir, f"{lec_id}.en.raw.vtt")

    result = subprocess.run(
        ["python", CLEAN_VTT, raw_vtt, out_dir],
        capture_output=True,
        encoding="utf-8",
        text=True,
    )

    if result.returncode != 0:
        print("  [오류] 자막 정제 실패")
        print(result.stderr[-300:])
        return False

    print(f"  완료: {lec_id}.en.vtt")
    print(f"  완료: {lec_id}.cleaned.txt")
    return True


def check_stage1(lec_id, out_dir):
    """Stage 1 출력 파일 존재 여부 확인"""
    files = [
        f"{lec_id}.en.raw.vtt",
        f"{lec_id}.en.vtt",
        f"{lec_id}.cleaned.txt",
    ]
    print("\n  완료 체크:")
    all_ok = True
    for fname in files:
        exists = os.path.exists(os.path.join(out_dir, fname))
        print(f"    {'[OK]' if exists else '[--]'} {fname}")
        if not exists:
            all_ok = False
    return all_ok


def process_lecture(lec_id, url):
    """강의 1개에 대해 Stage 1 전체 실행"""
    out_dir = os.path.join(LOCAL_DIR, lec_id)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  {lec_id}  |  자막 생성")
    print(f"  {url}")
    print(f"{'='*55}")

    if not download_subtitle(lec_id, url, out_dir):
        print(f"\n  {lec_id}  실패")
        return False

    if not clean_subtitle(lec_id, out_dir):
        print(f"\n  {lec_id}  실패")
        return False

    ok = check_stage1(lec_id, out_dir)
    print(f"\n  {lec_id}  {'완료' if ok else '일부 실패'}")
    return ok


def main():
    if not LECTURES:
        print("[오류] LECTURES 리스트가 비어 있습니다.")
        print("       처리할 강의의 주석을 해제하세요.")
        sys.exit(1)

    print(f"자막 생성 시작: 총 {len(LECTURES)}개 강의")

    results = []
    for lec_id, url in LECTURES:
        ok = process_lecture(lec_id, url)
        results.append((lec_id, ok))

    print(f"\n{'='*55}")
    print("최종 결과:")
    for lec_id, ok in results:
        print(f"  {'[OK]' if ok else '[FAIL]'} {lec_id}")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
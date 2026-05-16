import os
import subprocess
import sys
from LECTURE_URLS import LECTURES

# ============================================================
# 경로 설정
# ============================================================
SCRIPT_DIR      = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT    = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOCAL_DIR       = os.path.join(PROJECT_ROOT, "local")
EXTRACT_FRAMES  = os.path.join(SCRIPT_DIR, "extract_frames.py")
IMAGES_TO_PDF   = os.path.join(SCRIPT_DIR, "images_to_pdf.py")
FRAME_THRESHOLD = 0.001


def download_video(lec_id, url, out_dir):
    """yt-dlp 로 동영상 다운로드 → lec-NNN.mp4"""
    print("  [download_video] 동영상 다운로드 중...")
    output_tmpl = os.path.join(out_dir, f"{lec_id}.%(ext)s")

    subprocess.run(
        [
            "yt-dlp",
            "--format", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "--output", output_tmpl,
            url,
        ],
    )

    mp4 = os.path.join(out_dir, f"{lec_id}.mp4")
    if not os.path.exists(mp4):
        print("  [오류] 동영상 다운로드 실패")
        return False

    print(f"  완료: {lec_id}.mp4")
    return True


def create_frames(lec_id, out_dir):
    """extract_frames.py 실행 → frames/*.png"""
    print("  [create_frames] 프레임 추출 중...")
    mp4        = os.path.join(out_dir, f"{lec_id}.mp4")
    frames_dir = os.path.join(out_dir, "frames")

    subprocess.run(
        [
            "python", EXTRACT_FRAMES,
            mp4,
            frames_dir,
            str(FRAME_THRESHOLD),
        ],
    )

    count = len([
        f for f in os.listdir(frames_dir)
        if f.lower().endswith(".png")
    ]) if os.path.exists(frames_dir) else 0

    if count == 0:
        print("  [오류] 프레임 추출 실패")
        return False

    print(f"  완료: {count}장 → frames/")
    return True


def create_pdf(lec_id, out_dir):
    """images_to_pdf.py 실행 → lec-NNN_slides.pdf"""
    print("  [create_pdf] PDF 생성 중...")
    frames_dir = os.path.join(out_dir, "frames")
    out_pdf    = os.path.join(out_dir, f"{lec_id}_slides.pdf")

    subprocess.run(
        ["python", IMAGES_TO_PDF, frames_dir, out_pdf],
    )

    if not os.path.exists(out_pdf):
        print("  [오류] PDF 생성 실패")
        return False

    print(f"  완료: {lec_id}_slides.pdf")
    return True


def check_stage2(lec_id, out_dir):
    """Stage 2 출력 파일 존재 여부 확인"""
    frames_dir  = os.path.join(out_dir, "frames")
    frame_count = len([
        f for f in os.listdir(frames_dir)
        if f.lower().endswith(".png")
    ]) if os.path.exists(frames_dir) else 0

    files = {
        f"{lec_id}.mp4"              : os.path.join(out_dir, f"{lec_id}.mp4"),
        f"frames/ ({frame_count}장)" : frames_dir,
        f"{lec_id}_slides.pdf"       : os.path.join(out_dir, f"{lec_id}_slides.pdf"),
    }
    print("\n  완료 체크:")
    all_ok = True
    for label, path in files.items():
        exists = os.path.exists(path)
        print(f"    {'[OK]' if exists else '[--]'} {label}")
        if not exists:
            all_ok = False
    return all_ok


def process_lecture(lec_id, url):
    """강의 1개에 대해 Stage 2 전체 실행"""
    out_dir = os.path.join(LOCAL_DIR, lec_id)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  {lec_id}  |  슬라이드 생성")
    print(f"  {url}")
    print(f"{'='*55}")

    if not download_video(lec_id, url, out_dir):
        print(f"\n  {lec_id}  실패")
        return False

    if not create_frames(lec_id, out_dir):
        print(f"\n  {lec_id}  실패")
        return False

    if not create_pdf(lec_id, out_dir):
        print(f"\n  {lec_id}  실패")
        return False

    ok = check_stage2(lec_id, out_dir)
    print(f"\n  {lec_id}  {'완료' if ok else '일부 실패'}")
    return ok


def main():
    if not LECTURES:
        print("[오류] LECTURES 리스트가 비어 있습니다.")
        print("       처리할 강의의 주석을 해제하세요.")
        sys.exit(1)

    print(f"슬라이드 생성 시작: 총 {len(LECTURES)}개 강의")

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
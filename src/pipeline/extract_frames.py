import os
import sys
import cv2


def extract_frames(video_path, out_dir, threshold=0.001):
    """
    동영상에서 장면 변화 감지 기반으로 프레임을 추출한다.
    threshold=0.001 권장 (Beamer 슬라이드 기준)
    """
    os.makedirs(out_dir, exist_ok=True)

    cap   = cv2.VideoCapture(video_path)
    fps   = cap.get(cv2.CAP_PROP_FPS)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"  동영상: {fps:.1f}fps, {total}프레임 ({total/fps/60:.1f}분)")

    prev_gray = None
    saved     = 0
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (320, 240))

        if prev_gray is not None:
            diff  = cv2.absdiff(gray, prev_gray)
            score = diff.mean() / 255.0

            if score > threshold:
                h, w   = frame.shape[:2]
                out    = cv2.resize(frame, (1280, int(1280 * h / w)))
                fname  = os.path.join(out_dir, f"frame_{saved+1:04d}.png")
                cv2.imwrite(fname, out)
                saved += 1
                ts = frame_idx / fps
                print(f"  [{saved:04d}] t={ts:.1f}s  score={score:.4f}")

        prev_gray  = gray
        frame_idx += 1

        if total > 0 and frame_idx % (total // 10 or 1) == 0:
            print(f"  진행: {frame_idx/total*100:.0f}%")

    cap.release()
    print(f"  추출 완료: {saved}장 → {out_dir}")
    return saved


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("사용법: python extract_frames.py <video.mp4> <out_dir> [threshold]")
        sys.exit(1)
    video     = sys.argv[1]
    out_dir   = sys.argv[2]
    threshold = float(sys.argv[3]) if len(sys.argv) > 3 else 0.001
    extract_frames(video, out_dir, threshold)
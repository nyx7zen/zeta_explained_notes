import os
import sys
from PIL import Image


def images_to_pdf(img_dir, out_pdf):
    """
    frames/ 폴더의 PNG 이미지를 하나의 PDF로 합친다.
    """
    images = sorted([
        os.path.join(img_dir, f)
        for f in os.listdir(img_dir)
        if f.lower().endswith(".png")
    ])

    if not images:
        print(f"  [오류] 이미지 없음: {img_dir}")
        return False

    print(f"  이미지 {len(images)}장 → PDF 생성 중...")

    imgs = []
    for path in images:
        img = Image.open(path).convert("RGB")
        imgs.append(img)

    imgs[0].save(
        out_pdf,
        save_all=True,
        append_images=imgs[1:]
    )
    print(f"  저장: {os.path.basename(out_pdf)}")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python images_to_pdf.py <img_dir> <out.pdf>")
        sys.exit(1)
    images_to_pdf(sys.argv[1], sys.argv[2])
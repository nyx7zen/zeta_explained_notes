import os
import sys
import yt_dlp
from LECTURE_URLS import LECTURES

# ============================================================
# Path Configuration
# ============================================================
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOCAL_DIR    = os.path.join(PROJECT_ROOT, "local")


def download_description(lec_id, url, out_dir):
    """Extract YouTube video description using yt-dlp and save to a text file."""
    print(f"  [download_description] Extracting description...")
    
    # Configure yt-dlp options (extract metadata only without downloading the video)
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'remote_components': ['ejs:github'],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video metadata
            info = ydl.extract_info(url, download=False)
            description = info.get('description', '')
            
            if not description:
                print("  [Warning] Video description is empty.")
            
            # Set target file path: lec-xxx_desc.txt
            desc_file_path = os.path.join(out_dir, f"{lec_id}_desc.txt")
            
            # Write content to file using UTF-8 encoding
            with open(desc_file_path, "w", encoding="utf-8") as f:
                f.write(description)
                
            print(f"  Completed: {lec_id}_desc.txt")
            return True
            
    except Exception as e:
        print(f"  [Error] Failed to extract description: {e}")
        return False


def process_lecture_desc(lec_id, url):
    """Create directory and process description extraction for a single lecture."""
    out_dir = os.path.join(LOCAL_DIR, lec_id)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n{'='*55}")
    print(f"  {lec_id}  |  Extracting Description")
    print(f"  {url}")
    print(f"{'='*55}")

    ok = download_description(lec_id, url, out_dir)
    print(f"\n  {lec_id}  {'SUCCESS' if ok else 'FAILED'}")
    return ok


def main():
    if not LECTURES:
        print("[Error] LECTURES list is empty.")
        print("        Please uncomment the lectures you want to process.")
        sys.exit(1)

    print(f"Starting description collection: Total {len(LECTURES)} lectures")

    results = []
    for lec_id, url in LECTURES:
        ok = process_lecture_desc(lec_id, url)
        results.append((lec_id, ok))

    print(f"\n{'='*55}")
    print("Final Results:")
    for lec_id, ok in results:
        print(f"  {'[OK]' if ok else '[FAIL]'} {lec_id}")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
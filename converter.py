import os
import subprocess

# 👇 change this to your movies root folder
MOVIES_DIR = r"G:/Project Netflix/static/movies"

def convert_to_mp4(input_path, output_path):
    """
    Convert MKV to MP4 using ffmpeg (container copy, no re-encode).
    """
    try:
        # ffmpeg command: just change container (-c copy keeps streams)
        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-c", "copy",
            output_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Converted: {input_path} → {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting {input_path}: {e}")

def scan_and_convert_movies():
    for root, dirs, files in os.walk(MOVIES_DIR):
        for file in files:
            if file.lower().endswith(".mkv"):
                mkv_path = os.path.join(root, file)
                mp4_path = os.path.splitext(mkv_path)[0] + ".mp4"

                # Skip if mp4 already exists
                if os.path.exists(mp4_path):
                    print(f"⏩ Skipping (already exists): {mp4_path}")
                    continue

                convert_to_mp4(mkv_path, mp4_path)

if __name__ == "__main__":
    scan_and_convert_movies()
    print("🎬 Conversion complete!")

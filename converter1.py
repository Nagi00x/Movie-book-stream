import os
import subprocess

# Path to your movies folder
movies_dir = "static/movies"

# Walk through all folders & subfolders
for root, dirs, files in os.walk(movies_dir):
    for filename in files:
        if filename.lower().endswith(".mp4") and not filename.lower().endswith(".browser.mp4"):
            input_path = os.path.join(root, filename)
            output_path = os.path.splitext(input_path)[0] + ".browser.mp4"

            # Skip if already converted
            if os.path.exists(output_path):
                print(f"✅ Skipping (already exists): {output_path}")
                continue

            # ffmpeg command (H.264 + AAC, browser-compatible)
            command = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "23",
                "-c:a", "aac",
                "-b:a", "128k",
                "-movflags", "+faststart",
                output_path
            ]

            print(f"🎬 Converting: {input_path} → {output_path}")
            subprocess.run(command, check=True)

print("✅ All videos processed!")


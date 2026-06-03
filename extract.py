import cv2
import os

# 📍 PATHS
VIDEO_PATH = "isl_videos/isl_video2.mp4"
DATA_DIR = "data"

# 🎯 SELECT ONLY FEW WORDS (IMPORTANT)
segments = {
    "hello": (91, 95),
    "thank_you": (295, 299),
    "sorry": (338, 342),
    "please": (320, 324),
    "welcome": (308, 312),
    "i": (182, 186)
}

# -------- PROCESS --------
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("❌ Video not found or cannot open")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

for word, (start, end) in segments.items():
    print(f"Processing: {word}")

    save_dir = os.path.join(DATA_DIR, word)
    os.makedirs(save_dir, exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, int(start * fps))

    frame_id = 0
    saved = 0

    while cap.get(cv2.CAP_PROP_POS_FRAMES) < end * fps:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔥 SAVE EVERY 5th FRAME
        if frame_id % 5 == 0:
            filename = os.path.join(save_dir, f"{word}_{saved}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

        frame_id += 1

    print(f"✅ {word} → {saved} frames")

cap.release()
print("🔥 DONE EXTRACTING")
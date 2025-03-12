import cv2
import os

video_path = "fish_video.mp4"  # 你的影片檔案
output_dir = "datasets/images/train"  # 儲存影像的資料夾
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_rate = 5  # 每 5 幀擷取一張影像
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frame_rate == 0:
        frame_name = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_name, frame)
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
print(f"擷取 {frame_count // frame_rate} 張影像完成！")
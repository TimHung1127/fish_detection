```
/your_project/
│── dataset/
│   │── images/            # 存放所有影像
│   │   │── train/         # 訓練集影像
│   │   │   ├── frame_0.jpg
│   │   │   ├── frame_5.jpg
│   │   │   ├── ...
│   │   │── val/           # 驗證集影像
│   │   │   ├── frame_100.jpg
│   │   │   ├── frame_105.jpg
│   │   │   ├── ...
│   │   │── test/          # 測試集影像
│   │   │   ├── frame_200.jpg
│   │   │   ├── frame_205.jpg
│   │   │   ├── ...
│   │── labels/            # 標註資料
│   │   │── train/         # 訓練集標註
│   │   │   ├── frame_0.txt
│   │   │   ├── frame_5.txt
│   │   │   ├── ...
│   │   │── val/           # 驗證集標註
│   │   │   ├── frame_100.txt
│   │   │   ├── frame_105.txt
│   │   │   ├── ...
│   │   │── test/          # 測試集標註
│   │   │   ├── frame_200.txt
│   │   │   ├── frame_205.txt
│   │   │   ├── ...
│   │── dataset.yaml       # YOLO 設定檔
│
│── videos/                # 影片存放位置
│   │── raw/               # 原始影片
│   │   ├── fish_video_1.mp4
│   │   ├── fish_video_2.mp4
│   │── processed/         # 轉換後的影片（帶標註）
│   │   ├── fish_video_1_annotated.mp4
│   │   ├── fish_video_2_annotated.mp4
│
│── runs/                  # YOLO 訓練和推論結果
│   │── detect/            # 物件偵測結果
│   │   │── train/        # 訓練過程
│   │   │   ├── weights/
│   │   │   │   ├── best.pt   # 訓練最佳模型
│   │   │   │   ├── last.pt   # 最後一輪模型
│   │   │   ├── results.png   # 訓練結果圖表
│   │── track/             # 追蹤結果
│   │   │── predict/       # 追蹤輸出
│   │   │   ├── tracked_video.mp4  # 追蹤後影片
│
│── scripts/               # Python 腳本
│   │── extract_frames.py
│   │── train_yolo.py
│   │── track_fish.py
│
│── requirements.txt
│── README.md
```

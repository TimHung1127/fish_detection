from ultralytics import YOLO

# 1. 載入 YOLOv8 預訓練模型
model = YOLO("yolov8n.pt")  # 可改為 yolov8s.pt, yolov8m.pt 等

# 2. 訓練模型
model.train(
    data="dataset/dataset.yaml",  # 你的 YOLO 設定檔 (指定類別、影像路徑)
    epochs=50,                    # 訓練 50 輪，可調整
    batch=8,                       # 批次大小
    imgsz=640,                     # 影像尺寸 (YOLO 預設 640x640)
    device="cuda",                  # 使用 GPU 訓練，若無 GPU 則改為 "cpu"
    workers=4,                      # 資料讀取線程數
    project="runs/detect",          # 訓練結果存放路徑
    name="train",                   # 訓練名稱 (結果存於 runs/detect/train/)
    save=True,                      # 是否儲存最終模型
    save_period=5,                  # 每 5 輪儲存一次模型
    exist_ok=True                   # 若資料夾已存在則覆蓋
)

# 3. 儲存最佳模型 (模型會自動儲存為 best.pt)
print("✅ 訓練完成，模型儲存於 runs/detect/train/weights/best.pt")

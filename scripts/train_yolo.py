from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset/dataset.yaml",
    epochs=50,
    batch=8,
    imgsz=640,  #default size is 640*640, need to change after finish the images labels
    device="cuda",
    workers=4,
    project="runs/detect",
    name="train",
    save=True,
    save_period=5,
    exist_ok=True
)

print("save in runs/detect/train/weights/best.pt")

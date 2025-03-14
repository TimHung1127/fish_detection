from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    model.train(
        data=r"C:\Users\Timhu\Desktop\topic\roboflow_data\data.yaml",
        epochs=50,
        batch=8,
        imgsz=640,  #default size is 640*640, need to change after finish the images labels
        device=0,
        workers=4,
        project=r"C:\Users\Timhu\Desktop\topic\runs\detect",
        name="train",
        save=True,
        save_period=5,
        exist_ok=True
    )
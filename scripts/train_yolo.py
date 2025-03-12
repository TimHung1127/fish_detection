from ultralytics import YOLO
from ultralytics.utils import DEFAULT_CFG

if __name__ == "__main__":
    # 更改預設儲存路徑
    DEFAULT_CFG.save_dir = r"\model_save"
    model = YOLO.load('yolo_model/yolov8x.pt')
    data = r"ML\Lib\site-packages\ultralytics\cfg\datasets\coco8.yaml"
    result = model.train(data = data, epochs=10, batch=1, save=True)
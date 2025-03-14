from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r"C:\Users\Timhu\Desktop\topic\runs\detect\train\weights\best.pt")
    results = model.predict(source=r"C:\Users\Timhu\Desktop\topic\videos\raw\IMG_2765.MOV", save=True, project=r"C:\Users\Timhu\Desktop\topic\runs\track")
    
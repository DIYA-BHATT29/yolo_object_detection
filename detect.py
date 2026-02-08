from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(
    source="https://ultralytics.com/images/bus.jpg",
    save=True
)

print("Detection completed")

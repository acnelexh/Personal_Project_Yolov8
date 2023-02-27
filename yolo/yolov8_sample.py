from ultralytics import YOLO

import os


# Load a model
#model = YOLO("yolov8n.pt")  # load an official detection model
model = YOLO("yolov8n-seg.pt")  # load an official segmentation model
#model = YOLO("~/Personal_Project_Yolov8/runs/detect/test_run_1_epochs/weights/best.pt")  # load a custom model

# Track with the model
results = model.predict(source="https://youtu.be/Zgi9g1ksQHc", show=True) 
results = model.predict(source="https://youtu.be/Zgi9g1ksQHc", show=True, tracker="bytetrack.yaml") 


from ultralytics import YOLO
from pathlib import Path
import os

# Train YOLOv8 on kitti for 10 epochs

batch_size = 16
epochs = 50
learning_rate = 1E-3
img_size = 640
data_path = os.path.normpath('/home/chenzyu/datasets/kitti_yolo')
weight_path = os.path.normpath('/home/chenzyu/Personal_Project_Yolov8/yolo/yolov8l.pt')

model = YOLO(weight_path)

model.train(
    data=os.path.join(data_path, 'kitti.yaml'),
    epochs=epochs,
    batch=batch_size,
    imgsz=img_size,
    save=True,
    pretrained=True,
    project='kitti_50_epochs',
    lr0=learning_rate,
    cos_lr=True)

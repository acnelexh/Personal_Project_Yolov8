## Individual Project of Practical Computer Vision

# Yolo v8
This project uses the Yolo v8 implementation from [Ultralytic](https://docs.ultralytics.com/)
## Setup
```
pip install ultralytics
```
## Training

I also written a training script, with all the training parameters is configurable in the .py file

```
cd yolo
python train_yolo.py
```
Yolo model can also be used for training and inference using CLI, the API can be found [here](https://docs.ultralytics.com/)

For the Yolo v8 training and evaluation, I am using the ultranalytics code base.
The pretrained Yolo v8 on image net can be found at 

## Model weights

Pretrained model can be found here

- Yolov8n small [model weight](./yolo/yolov8n.pt)

- Yolov8l large [model weight](./yolo/yolov8l.pt)

The trained model on kitti can be found at

- Yolov8n small 10 epochs [model weight](./yolo/kitti_10_small/train/weights/best.pt) and [results](./yolo/kitti_10_small/train)

- Yolov8n small 24 epochs [model weight](./yolo/kitti_24_small/train2/weights/best.pt) and [results](./yolo/kitti_24_small/train)

- Yolov8l large 24 epochs [model weight](./yolo/kitti_24_large/train/weights/best.pt) and [results](./yolo/kitti_24_large/train)

- Yolov8l large 50 epochs [model weight](./yolo/kitti_50_large/train/weights/best.pt) and [results](./yolo/kitti_50_large/train)

## Inference

For inference on a new image
```
yolo detect predict model=[model path] source=[image path]
```

# Faster-RCNN

For the Faster-RCNN training and evalution, I am using the mmdetection code base.

The configuration file I used for training the mode can be found [here](./mmdetection/configs/project/faster_rcnn.py)

The here is the [training result directory](/home/chenzyu/Personal_Project_Yolov8/mmdetection/work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs)

# Dataset

For this project, I am using the [Kitti autonomous driving dataset](https://www.cvlibs.net/datasets/kitti/). 
Specicially, the [2D object detection left color images](https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_image_2.zip) 

It consist of the following label

1. Car
2. Van
3. Truck
4. Pedestrian
5. Person_sitting
6. Cyclist
7. Tram
8. Misc
9. DontCare

I used [fiftyone](https://github.com/voxel51/fiftyone) to convert the Kitti dataset to COCO format, and [kitti_for_yolo](https://github.com/oberger4711/kitti_for_yolo) to convert Kitti dataset to YOLO format.



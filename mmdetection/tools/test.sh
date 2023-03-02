#!/usr/bin/env bash

python \
    tools/test.py \
    work_dirs/faster_rcnn/faster_rcnn.py \
    /home/chenzyu/Personal_Project_Yolov8/mmdetection/work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs/epoch_23.pth \
    --eval bbox
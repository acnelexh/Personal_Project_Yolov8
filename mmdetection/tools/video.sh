#!/usr/bin/env bash

VIDEO_FILE="/home/chenzyu/Personal_Project_Yolov8/data/demo/out.mp4"
CONFIG_FILE="/home/chenzyu/Personal_Project_Yolov8/mmdetection/work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs/faster_rcnn.py"
CHECKPOINT_FILE="/home/chenzyu/Personal_Project_Yolov8/mmdetection/work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs/epoch_23.pth"
OUT_FILE="faster_rcnn_demo.mp4"
SCORE_THR=0.5


python demo/video_demo.py \
    ${VIDEO_FILE} \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    [--score-thr ${SCORE_THR}] \
    [--out ${OUT_FILE}] 
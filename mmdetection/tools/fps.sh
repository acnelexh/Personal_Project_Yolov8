#!/usr/bin/env bash

python -m torch.distributed.launch --nproc_per_node=1 --master_port=29500 tools/analysis_tools/benchmark.py \
    work_dirs/faster_rcnn/faster_rcnn.py  \
    /home/chenzyu/Personal_Project_Yolov8/mmdetection/work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs/epoch_23.pth \
    --launcher pytorch
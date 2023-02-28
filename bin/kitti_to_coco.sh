#!/bin/bash

INPUT_DIR=/home/chenzyu/fiftyone/kitti/train
OUTPUT_DIR=~/fiftyone/kitti/train_coco

fiftyone convert \
    --input-dir ${INPUT_DIR} --input-type fiftyone.types.KITTIDetectionDataset \
    --output-dir ${OUTPUT_DIR} --output-type fiftyone.types.COCODetectionDataset
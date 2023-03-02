# The new config inherits a base config to highlight the necessary modification
_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_2x.py',
    '../_base_/default_runtime.py'
]

model = dict(
    backbone=dict(
        depth=50),
    roi_head=dict(
        bbox_head=dict(num_classes=9))
    )

# Modify dataset related settings
dataset_type = 'CocoDataset'
classes = ("Pedestrian", "Cyclist", "Car", "Van", "Truck", "Person_sitting", "Tram", "Misc", "DontCare")

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        img_prefix='/home/chenzyu/datasets/kitti_yolo/train/images/',
        classes=classes,
        ann_file='/home/chenzyu/datasets/kitti_coco/train_coco.json'),
    val=dict(
        type=dataset_type,
        img_prefix='/home/chenzyu/datasets/kitti_yolo/valid/images/',
        classes=classes,
        ann_file='/home/chenzyu/datasets/kitti_coco/valid_coco.json'),
    test=dict(
        type=dataset_type,
        img_prefix='/home/chenzyu/datasets/kitti_yolo/test/images',
        classes=classes,
        ann_file='/home/chenzyu/datasets/kitti_coco/test_coco.json'))


log_config = dict(interval=50)
work_dir = 'work_dir/faster_rcnn_r50_fpn_2x_coco_kitti_24_epochs'

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '/home/chenzyu/Personal_Project_Yolov8/mmdetection/pretrained_models/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth'
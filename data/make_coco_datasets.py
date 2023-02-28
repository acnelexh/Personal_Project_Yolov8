import json
from pathlib import Path
import shutil
import pprint

printer = pprint.PrettyPrinter(indent=4)

coco_json = json.load(open('/home/chenzyu/fiftyone/kitti/train_coco/labels.json', 'r'))

yolo_path = Path('/home/chenzyu/datasets/kitti_yolo/')

output_path = Path('/home/chenzyu/datasets/kitti_coco')

for partition in ['train', 'valid', 'test']:
    #divide the coco_json into train, valid, test
    #based on the image_id
    new_json = {}
    file_stems = set([f.stem for f in (yolo_path/partition/'labels').glob('*.txt')])
    printer.pprint(coco_json.keys())
    new_json['info'] = coco_json['info']
    new_json['licenses'] = coco_json['licenses']
    new_json['categories'] = coco_json['categories']
    new_json['images'] = []
    new_json['annotations'] = []
    images = coco_json['images']
    annotations = coco_json['annotations']
    for image in images:
        #print(image['file_name'])
        #assert(0 == 1)
        if image['file_name'].split('.')[0] in file_stems:
            new_json['images'].append(image)
    for annotation in annotations:
        #assert(0 == 1)
        if annotation['image_id'] in [image['id'] for image in new_json['images']]:
            new_json['annotations'].append(annotation)
    json.dump(new_json, open(output_path/f'{partition}_coco.json', 'w'))
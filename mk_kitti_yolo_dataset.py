from pathlib import Path
import random
import shutil

random.seed(69)

# this script partitions the KITTI dataset into train, validation, and test sets

IMG_PATH = Path('./data/kitti/training/image_2')
LABEL_PATH = Path('./data/kitti_yolo/labels')
OUTPUT_PATH = Path('./data/kitti_yolo')

labels = [f for f in LABEL_PATH.glob('*.txt')]

random.shuffle(labels)

train_set = labels[:int(0.6*len(labels))]
val_set = labels[int(0.6*len(labels)):int(0.8*len(labels))]
test_set = labels[int(0.8*len(labels)):]

(OUTPUT_PATH/'train'/'labels').mkdir(exist_ok=True, parents=True)
(OUTPUT_PATH/'train'/'images').mkdir(exist_ok=True, parents=True)

(OUTPUT_PATH/'valid'/'labels').mkdir(exist_ok=True, parents=True)
(OUTPUT_PATH/'valid'/'images').mkdir(exist_ok=True, parents=True)

(OUTPUT_PATH/'test'/'labels').mkdir(exist_ok=True, parents=True)
(OUTPUT_PATH/'test'/'images').mkdir(exist_ok=True, parents=True)

def mk_dataset(set_type, dataset):
    for label_txt in dataset:
        img = IMG_PATH / label_txt.name.replace('.txt', '.png')
        shutil.copy(img, OUTPUT_PATH/set_type/'images')
        shutil.copy(label_txt, OUTPUT_PATH/set_type/'labels')
    
mk_dataset('train', train_set)
mk_dataset('valid', val_set)
mk_dataset('test', test_set)
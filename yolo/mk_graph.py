from matplotlib import pyplot as plt
from pathlib import Path
import pandas as pd

csv_path = Path('/home/chenzyu/Personal_Project_Yolov8/yolo/kitti_24_large/train/results.csv')

df = pd.read_csv(csv_path)

print(df.keys())

epochs = df['                  epoch'].values

box_loss = df['           val/box_loss'].values

cls_loss = df['           val/cls_loss'].values


plt.plot(box_loss, label='box_loss')
plt.plot(cls_loss, label='cls_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.title('loss_kitti_24_large')
plt.legend()
plt.savefig('loss.png')
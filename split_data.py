import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

base_dir = ''

label_dir = os.path.join(base_dir, 'data.csv')
image_dir = os.path.join(base_dir, 'data')
train_dir = os.path.join(base_dir, 'drive_dataset', 'train')
val_dir = os.path.join(base_dir, 'drive_dataset', 'validation')

label_data = []

with open(label_dir, 'r') as f:
  label_data = f.readlines()

label_data = [row.replace('\n', '').split(',')[1] for row in label_data]
file_names = sorted([os.path.join(image_dir, file_name) for file_name in os.listdir(image_dir)])
train_files, test_files, train_labels, test_labels = train_test_split(file_names, label_data,
                                                                     test_size = 0.2,
                                                                     stratify=label_data) 
if os.path.exists(train_dir):
  shutil.rmtree(train_dir)

if os.path.exists(val_dir):
  shutil.rmtree(val_dir)

os.makedirs(train_dir, exist_ok=True)

for file_path, label in zip(train_files, train_labels):
  label_dir = os.path.join(train_dir, label)

  if not os.path.exists(label_dir):
    os.makedirs(label_dir)

  file_name = Path(file_path).name
  shutil.move(file_path, os.path.join(label_dir, file_name))

os.makedirs(val_dir, exist_ok=True)

for file_path, label in zip(test_files, test_labels):
  label_dir = os.path.join(val_dir, label)

  if not os.path.exists(label_dir):
    os.makedirs(label_dir)

  file_name = Path(file_path).name
  shutil.move(file_path, os.path.join(label_dir, file_name))

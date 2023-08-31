import os
import shutil

# Set source and destination directories
label_src_dir = "H:/My Drive/robocar/dataset/original/label/training/label_yolo"  # directory where original label files are stored
lablel_dest_dir = "H:/My Drive/robocar/dataset/kitti/test/labels"  # directory to which label files will be copied

# Get list of image filenames without the extension
image_files = os.listdir("H:/My Drive/robocar/dataset/kitti/test/images") # images whose lables are missing
image_basenames = [os.path.splitext(filename)[0] for filename in image_files]

# For each image file, find the corresponding label file and copy it
for image_basename in image_basenames:
    label_filename = image_basename + ".txt"  # assuming labels are in .txt format
    src_path = os.path.join(label_src_dir, label_filename)
    dest_path = os.path.join(lablel_dest_dir, label_filename)

    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(dest_path)
    else:
        print(f"Label file for {image_basename} does not exist in source directory.")

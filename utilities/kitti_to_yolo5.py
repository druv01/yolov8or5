import os
import cv2

kitti_path = '/mnt/h//My Drive/robocar/dataset/training/image_2/'
yolo_path = '/mnt/h/My Drive/robocar/yolov5/datasets/kitti/labels/'

# Mapping your class labels to integers
class_dict = {'Car': 0, 'Van': 1, 'Truck': 2, 'Pedestrian': 3, 'Cyclist': 4}

for filename in os.listdir(kitti_path):
    if filename.endswith('.txt'):
        kitti_file_path = os.path.join(kitti_path, filename)
        yolo_file_path = os.path.join(yolo_path, filename)

        if os.path.exists(yolo_file_path):
            continue

        #print(kitti_file_path)
        with open(kitti_file_path, 'r') as kitti_file, open(yolo_file_path, 'w') as yolo_file:
            for line in kitti_file:
                data = line.split()
                class_str = data[0]
                if class_str in class_dict:
                    class_idx = class_dict[class_str]

                    # KITTI bounding box coordinates are absolute values in pixels
                    xmin, ymin, xmax, ymax = map(float, [data[4], data[5], data[6], data[7]])

                    # Calculate YOLO-style center, width, and height
                    img = cv2.imread(kitti_file_path.replace('.txt', '.png'))  # replace with your image file extension

                    img_height, img_width = img.shape[:2]
                    
                    x_center = (xmin + xmax) / 2 / img_width
                    y_center = (ymin + ymax) / 2 / img_height
                    width = (xmax - xmin) / img_width
                    height = (ymax - ymin) / img_height

                    yolo_file.write(f'{class_idx} {x_center} {y_center} {width} {height}\n')

import os
import cv2
import concurrent.futures

img_path   = '/mnt/h//My Drive/robocar/dataset/original/training/training/image_2'
yolo_path  = '/mnt/h/My Drive/robocar/dataset/original/label/training/label_kitti'
label_path = '/mnt/h/My Drive/robocar/dataset/original/label/training/label_2'

class_dict = {'Car': 0, 'Van': 1, 'Truck': 2, 'Pedestrian': 3, 'Cyclist': 4, 'Tram': 5, 'Misc' : 6}

count = 0

def process_file(filename):
    #global count

    if filename.endswith('.png'):
        kitti_img_path = os.path.join(img_path, filename)
        yolo_file_path = os.path.join(yolo_path, filename).replace('.png', '.txt')

        if os.path.exists(yolo_file_path):
            return
        
        kitti_label_path = os.path.join(label_path, filename).replace('.png', '.txt').replace('.png', '.txt')


        with open(kitti_label_path, 'r') as kitti_file, open(yolo_file_path, 'w') as yolo_file:
            for line in kitti_file:
                #print(line)
                data = line.split()
                class_str = data[0]
                if class_str in class_dict:
                    class_idx = class_dict[class_str]
                    xmin, ymin, xmax, ymax = map(float, [data[4], data[5], data[6], data[7]])
                    img = cv2.imread(kitti_img_path)
                    img_height, img_width = img.shape[:2]
                    x_center = (xmin + xmax) / 2 / img_width
                    y_center = (ymin + ymax) / 2 / img_height
                    width = (xmax - xmin) / img_width
                    height = (ymax - ymin) / img_height
                    yolo_file.write(f'{class_idx} {x_center} {y_center} {width} {height}\n')

       # count += 1

# Create a pool of workers to execute processes
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    list(executor.map(process_file, os.listdir(img_path)))
#print(f"Count = {count}")
print("Done")


import matplotlib.pyplot as plt

model_versions = ['Nano', 'Small', 'Medium', 'Large']
yolov5_map = [71.9, 77, 80.3, 81.0]
yolov8_map = [77.9, 81.9, 83.1, 82.9]

yolov5_latency = [9.37, 9.3, 11.6, 13.93]
yolov8_latency = [15.37, 15.1, 17.3, 19.1]

plt.figure(figsize=(10, 5))
plt.ylim(70, 85)
plt.xlim(8, 20)

plt.plot(yolov5_latency, yolov5_map, marker='o', label='YOLOv5')
plt.plot(yolov8_latency, yolov8_map, marker='o', label='YOLOv8')

# Adding labels for each point - YOLOv5
for index, version in enumerate(model_versions):
    plt.annotate(f'v5{version}', (yolov5_latency[index], yolov5_map[index]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding labels for each point - YOLOv8
for index, version in enumerate(model_versions):
    plt.annotate(f'v8{version}', (yolov8_latency[index], yolov8_map[index]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('Latency in (ms) A100')
plt.ylabel('mAP50-90 KITTI')
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt

model_versions = ['Nano', 'Small', 'Medium', 'Large']

yolov8_map = [77.9, 81.9, 83.1, 82.9]
yolov8_latency = [15.37, 15.1, 17.3, 19.1]

plt.figure(figsize=(8, 4))
plt.ylim(10, 104)

plt.plot(model_versions, yolov8_map, marker='o', label='mAP50-95')
plt.plot(model_versions, yolov8_latency, marker='o', label='Latency')

# Annotate data points with values
for index, txt in enumerate(yolov8_map):
    plt.annotate(f"{txt:.1f}", (model_versions[index], yolov8_map[index]), textcoords="offset points", xytext=(0,10), ha='center')

for index, txt in enumerate(yolov8_latency):
    plt.annotate(f"{txt:.2f}", (model_versions[index], yolov8_latency[index]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend(loc='upper left')
plt.grid()
plt.show()

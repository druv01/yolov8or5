import matplotlib.pyplot as plt

model_versions = ['Nano', 'Small', 'Medium', 'Large']

yolov5_map = [71.9, 77, 80.3, 81.0]
yolov5_latency = [9.37, 9.3, 11.6, 13.93]

plt.figure(figsize=(8, 4))
plt.ylim(0, 100)

plt.plot(model_versions, yolov5_map, marker='o', label='mAP50-95')
plt.plot(model_versions, yolov5_latency, marker='o', label='Latency')

# Annotate data points with values
for index, txt in enumerate(yolov5_map):
    plt.annotate(f"{txt:.1f}", (model_versions[index], yolov5_map[index]), textcoords="offset points", xytext=(0,10), ha='center')

for index, txt in enumerate(yolov5_latency):
    plt.annotate(f"{txt:.2f}", (model_versions[index], yolov5_latency[index]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend(loc='upper left')
plt.grid()
plt.show()

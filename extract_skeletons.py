import os
from ultralytics import YOLO
import pandas as pd

labels = ["nose", "left_eye", "right_eye", "left_ear", "right_ear", "left_shoulder",
          "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist",
          "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle"]

# Функция, которую будет выполнять каждый поток
def process(video_path):
    # Загружаем модель
    model = YOLO('yolov8n-pose.pt')
    df = pd.DataFrame()
    # Запускаем распознавание для указанного видео
    results = model(source=video_path, show=False, conf=0.3, save=False)
    for r in results:
        if len(r) <= 0: # no one on the frame
            continue
        d = {}
        keypoints = r[0].keypoints # first person on video
        for label, xy in zip(labels, keypoints.xy[0]):
            x, y = int(xy[0].item()), int(xy[1].item())  # Accessing x and y coordinates correctly
            d[label+'_x'] = x
            d[label+'_y'] = y
        df = pd.concat([df, pd.DataFrame([d.copy()])], ignore_index=True)
    return df

for video in os.listdir('zmExport_710990'):
    df = pd.DataFrame(process(f'zmExport_710990\\{video}'))
    df.to_csv(f'keypoints-nano\\{video.split(".")[0]}.csv')
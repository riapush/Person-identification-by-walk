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
    results = model(source=video_path, show=False, conf=0.3, save=True)

process(f'zmExport_710990\\250-video.mp4')
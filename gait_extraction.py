import pandas as pd
import tsfel
import os
from sklearn.model_selection import train_test_split

# data = []
# for i in range(264):
#     with open(f'keypoints\\{i}.txt', 'r') as file:
#         lines = file.readlines()
#         line = lines[0].strip().split()  # Get the 1 line and split it
#         data.append(line)

# df = pd.DataFrame(data)

# # Retrieves a pre-defined feature configuration file to extract all available features
# cfg = tsfel.get_features_by_domain()

# # Extract features
# X = tsfel.time_series_features_extractor(cfg, df)

# X.to_csv('other.csv', header=False, index=False)
# print(X.shape)


labels = ["nose", "left_eye", "right_eye", "left_ear", "right_ear", "left_shoulder",
          "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist",
          "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle"]

def process_keypoints(path):
    df = pd.read_csv(path)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df['body_center_x'] = (df['left_shoulder_x'] + df['right_shoulder_x'] + df['left_hip_x'] + df['right_hip_x']) / 4
    df['body_center_y'] = (df['left_shoulder_y'] + df['right_shoulder_y'] + df['left_hip_y'] + df['right_hip_y']) / 4
    df['body_center_x'] = df['body_center_x'].astype(int)
    df['body_center_y'] = df['body_center_y'].astype(int)
    for label in labels:
        df[label+'_x'] = df[label+'_x'] - df['body_center_x']
        df[label+'_y'] = df[label+'_y'] - df['body_center_y']
    df.drop(['body_center_x', 'body_center_y'], axis=1, inplace=True)
    return df

# NORMILIZE RELATIVE TO BODY CENTER
for video in os.listdir('keypoints'):
    df = process_keypoints(f'keypoints\\{video}')
    df.to_csv(f'features\\{video.split(".")[0]}.csv')


# SEPARATE INTO TRAIN & TEST, EXTRACT FEATURES
for video in os.listdir('features'):
    df = pd.read_csv(f'features\\{video}')
    X_train, X_test = train_test_split(df, test_size=0.5, random_state=42)
    cfg = tsfel.get_features_by_domain("statistical")
    # Extract features
    X_train = tsfel.time_series_features_extractor(cfg, X_train)
    X_test = tsfel.time_series_features_extractor(cfg, X_test)
    X_train.to_csv(f'train\\{video.split(".")[0].split("-")[0]}.csv', header=False, index=False)
    X_test.to_csv(f'test\\{video.split(".")[0].split("-")[0]}.csv', header=False, index=False)


    


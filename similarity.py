from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os

train_data = {}
for video in os.listdir('train'):
    x_train = pd.Series(pd.read_csv(f'train\\{video}', header=None).iloc[0])
    x_train.fillna(x_train.mean(), inplace=True)
    train_data[video.split('.')[0]] = x_train.tolist().copy()

correct = 0
for video in os.listdir('test'):
    max_value = 0
    person = -1
    x_test = pd.Series(pd.read_csv(f'test\\{video}', header=None).iloc[0])
    x_test.fillna(x_test.mean(), inplace=True)
    x_test = x_test.tolist()
    for key, value in train_data.items():
        cos_sim = cosine_similarity([value], [x_test])
        if cos_sim > max_value:
            max_value = cos_sim
            person = key
    print(f'MAX COSINE SIMILARITY FOR PERSON {video.split(".")[0]} IS PERSON {person} ({max_value}). own value = {cosine_similarity([train_data[video.split(".")[0]]], [x_test])}')
    if video.split(".")[0] == person:
        correct += 1
    else:
        print('the one above is wrong!!')
print(correct)


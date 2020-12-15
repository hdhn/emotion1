import jieba,csv
import numpy as np
import pandas as pd
import emotion_analysis1 as ea

def ReadCSV(filename):
    datas = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        # header = next(csv_reader)        # 读取第一行每一列的标题
        for rows in csv_reader:
            if rows[2].isdigit():
                datas.append(rows[2])
        return datas
datas = ReadCSV('获取店铺评论.csv')
shop = np.mat(datas).reshape(len(datas),1)
datas1 = ea.ReadCSV('获取店铺评论.csv')
datas2 = []
for data in datas1:
    g,h = ea.EmotionByScore(data)
    emotion4 = ea.JudgingEmotionByScore(g,h)
    datas2.append(emotion4)
shop = np.insert(shop,1,values=datas2,axis=1)
print(shop)

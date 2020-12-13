import jieba,csv
import numpy as np
import pandas as pd

def ReadCSV(filename):
    datas = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        # header = next(csv_reader)        # 读取第一行每一列的标题
        for rows in csv_reader:
            datas.append(rows[6])
        return datas

import numpy as np
import csv
import pandas as pd
pos=[]
Efield = {}
with open('./Yelp_poi_categories.txt','r',encoding='utf-8') as reader:
    while True:
        lines = reader.readline()  # 整行读取数据
        if not lines:
            break
            pass
        p_tmp, E_tmp = [i for i in lines.split()]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        pos.append(p_tmp)  # 添加新读取的数据
        Efield[p_tmp]=E_tmp
    print(pos)
    
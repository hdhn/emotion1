import numpy as np
import json
import pandas as pd
Efield = {}
Efield1 = {}
pos = []
with open('./Yelp_poi_categories.txt','r',encoding='utf-8') as reader:
    while True:
        lines = reader.readline()  # 整行读取数据
        if not lines:
            break
        p_tmp, E_tmp = [i for i in lines.split()]# 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        pos.append(p_tmp)
        Efield[p_tmp]=E_tmp  # 添加新读取的数据
    print(Efield)
with open('./Yelp_train.txt','r',encoding='utf-8') as reader:
    while True:
        lines = reader.readline()  # 整行读取数据
        if not lines:
            break
        p_tmp, E_tmp,T_tmp = [i for i in lines.split()] #p_tmp,E_tmp,T_tmp分别代表第一，二，三列数据
        Efield1[p_tmp] = T_tmp     #存到字典中
    print(Efield1)
Efield2 = {}
#下面是用来储存到txt文件中
fileObject = open('jsonFile.txt', 'a',encoding='utf-8')
for items in Efield.keys():
    fileObject.write(Efield1[items])
    fileObject.write('\n')
fileObject.close()



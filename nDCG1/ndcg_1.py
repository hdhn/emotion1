import pandas as pd
import numpy as np

#读取Recommendation_itemId.csv数据，存放到Recommendation_itemId矩阵中,然后两个0,1矩阵相乘
Recommendation_itemId = np.loadtxt(open("recommendation_itemId.csv","rb"),delimiter=",",skiprows=0)
#读取测试集的数据，进行匹配，将Recommendation_itemId.csv矩阵转化为一个user-item的0，1矩阵
#numpy和pandas矩阵元素索引，numpy先行后列，pandas先列后行
z = np.zeros((600, 456),np.uint16)#构造元素全为0的矩阵
d = pd.DataFrame(z)
l = 10 #推荐列表长度
for i in range(0,Recommendation_itemId.shape [0]):
    for j in range(0,Recommendation_itemId.shape[1]):
      d[Recommendation_itemId[i][j]-1][i] = 1
      #print (Recommendation_itemId[i][j])
d.to_csv("recommendation_data.csv",index=False,header=False)
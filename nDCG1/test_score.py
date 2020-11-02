import numpy as np
import pandas as pd
import math


data = pd.read_csv('./meituan_data.csv', sep=",")
# pd.set_option('display.float_format',lambda x : '%.2f' % x) # 禁用科学计数表示
print(data)
data = np.array(data.groupby(['user']))
print(data)

user_poi_score_matrix = np.zeros((600, 456), np.float)
# print(user_poi_matrix)
user_poi_score_matrix = pd.DataFrame(user_poi_score_matrix)

test_data = pd.read_csv('./test_usual.csv', sep=",")
# pd.set_option('display.float_format',lambda x : '%.2f' % x) # 禁用科学计数表示
print(test_data)


for i in data:
    for j in i[1].values:
        print(i[0])
        print(j[3])
        print(j[8])
        user_poi_score_matrix [j[3]][i[0]] = j[8]
print(user_poi_score_matrix )



user_poi_test_score_matrix = np.zeros((600, 456), np.float)
user_poi_test_score_matrix = pd.DataFrame(user_poi_test_score_matrix)

for k in test_data.values:
    print(k[1])
    print(k[0])
    user_poi_test_score_matrix[k[1]][k[0]] = user_poi_score_matrix[k[1]][k[0]]
    print(user_poi_test_score_matrix)
print(user_poi_test_score_matrix)


user_poi_test_score_matrix .to_csv("test_data_score.csv", index=False, header=False)
import numpy as np
import pandas as pd
import math
from math import exp

coordinate_train = pd.read_csv('./coordinate_train1.csv', sep=",")
#print(coordinate_train)

data = np.array(coordinate_train.groupby(['user']),dtype=object)
# print(data)


geographic_data = pd.read_csv('Yelp_poi_coos.txt', sep="\t",header=None)
# print(data[1])
geographic_data.columns = ["pois","lat","lon"]
# print(geographic_data)



poi_coordinate_list = []
for t in geographic_data.values:
    lat =  float(t[1])
    lon = float(t[2])
    coordinate = [lat, lon]
    poi_coordinate_list.append(coordinate)
poi_coordinate_matrix = np.mat(poi_coordinate_list)
number1 = int(len(poi_coordinate_matrix))
# print(poi_coordinate_list)
# print(number1)

user_poi_geographic_score_matrix = np.zeros((1000, number1), np.float16)  # 构造已知用户数和商品数的元素全为0的矩阵
# user_poi_geographic_score_matrix = pd.DataFrame(user_poi_geographic_score_matrix)

# def function_A(x):
#     return (math.exp(-(1/(2*t**2)) * x))

def geographic_score(t):
    for i in data:
        user_geographic_coordinates_list = []
        for j in i[1].values:
            m = int(j[1])  # 用户i[0]访问过的兴趣点
            # print(m)
            # poi_list.append(m)
            a = float(j[3])
            b = float(j[4])
            geographic_coordinates = [a, b]  # 用户i[0]访问过的兴趣点的坐标
            print(geographic_coordinates)
            user_geographic_coordinates_list.append(geographic_coordinates)
            # print(user_geographic_coordinates_list)   # 用户i[0]访问过的兴趣点的坐标的列表

        user_geographic_coordinates_matrix = np.mat(user_geographic_coordinates_list)
        # print(user_geographic_coordinates_matrix)
        number = int(len(user_geographic_coordinates_matrix))
        # print(number)
        # right = 0
        coors_dot_matrix_score_sum = np.zeros((1,number1), np.float16)
        # print(coors_dot_matrix_score_sum)
        for k in range(number):
            coors_cha = poi_coordinate_matrix - np.tile(user_geographic_coordinates_matrix[k],(number1,1))
            # print(coors_cha)
            coors_dot = np.dot(coors_cha,coors_cha.T)
            coors_dot_matrix = np.mat(np.diagonal(coors_dot))
            # print(type(coors_dot_matrix))
            coors_dot_matrix_score = np.exp(-(1/(2*t**2))*coors_dot_matrix)
            print(coors_dot_matrix_score)

            coors_dot_matrix_score_sum += coors_dot_matrix_score
        # print(coors_dot_matrix_score_sum)
        score = 1 / (2 * math.pi * number * t) * coors_dot_matrix_score_sum
        # print(score)
        user_poi_geographic_score_matrix[i[0]] = score
        print(i[1].value)
        print(user_poi_geographic_score_matrix)

    # user_poi_geographic_score_matrix.to_csv("user_poi_geographic_probability_matrix.csv", index=False, header=False)
    np.savetxt('user_poi_geographic_probability_matrix.csv', user_poi_geographic_score_matrix, fmt="%.08f")

geographic_score(0.5)

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


#读取数据
recommendation_matrix_result = np.loadtxt(open("recommendation_data.csv","rb"),delimiter=",",skiprows=0)
recommendation_matrix_test = np.loadtxt(open("test_data_times.csv","rb"),delimiter=",",skiprows=0)
#print (np.sum(recommendation_matrix_result))


#将recommendation_matrix_result和test.data转化的0,1矩阵相乘，得到新的矩阵，每行累加，就可以得到命中的item个数。
recommendation_hit_count = recommendation_matrix_result*recommendation_matrix_test
#print (recommendation_hit_count)



# def get_dcg(y_pred, y_true, k):
#     # 注意y_pred与y_true必须是一一对应的，并且y_pred越大越接近label=1(用相关性的说法就是，与label=1越相关)
#     df = pd.DataFrame({"y_pred": y_pred, "y_true": y_true})
#     df = df.sort_values(by="y_pred", ascending=False)  # 对y_pred进行降序排列，越排在前面的，越接近label=1
#     df = df.iloc[0:k, :]  # 取前K个
#     dcg = (2 ** df["y_true"] - 1) / np.log2(np.arange(1, df["y_true"].count() + 1) + 1)  # 位置从1开始计数
#     dcg = np.sum(dcg)


Selected_recommendation_list = []
for i in recommendation_hit_count:
    i_Selected_recommendation_list = []
    # print(type(i))
    i_list = i.tolist()
    print(i_list)
    # poi_n = i_list.index('1.0')
    # print(poi_n)
    for j in i_list:
        if j == 1:
            poi_n = i_list.index(j)
            print(poi_n)
        # i_Selected_reco/mmendation_list.append(poi_n)
    # print(i_Selected_recommendation_list)


# def get_ndcg(df, k):
#     # df包含y_pred和y_true
#     dcg = get_dcg(df["y_pred"], df["y_true"], k)
#     idcg = get_dcg(df["y_true"], df["y_true"], k)
#     ndcg = dcg / idcg
#     return ndcg


# import sys, math
#
# topK = int(sys.argv[1])
#
#
# def DCG(label_list):
#     dcgsum = 0
#     for i in range(len(label_list)):
#         dcg = (2 ** label_list[i] - 1) / math.log(i + 2, 2)
#         dcgsum += dcg
#     return dcgsum
#
#
# def NDCG(label_list):
#     global topK
#     dcg = DCG(label_list[0:topK])
#     ideal_list = sorted(label_list, reverse=True)
#     ideal_dcg = DCG(ideal_list[0:topK])
#     if ideal_dcg == 0:
#         return 0
#     return dcg / ideal_dcg
#
#
# def queryNDCG(label_qid_score):
#     tmp = sorted(label_qid_score, key=lambda x: -x[2])
#     label_list = []
#     for label, q, s in tmp:
#         label_list.append(label)
#     return NDCG(label_list)
#
#
# last_qid = ""
# l_q_s = []
#
# ndcg = 0
# cnt = 0
#
# for line in sys.stdin:
#     label, qid, score = line.rstrip().split(" ")
#     if last_qid != "" and qid != last_qid:
#         ndcg += queryNDCG(l_q_s)
#         cnt += 1
#         l_q_s = []
#     last_qid = qid
#     l_q_s.append([int(label), qid, float(score)])
#
# if last_qid != "":
#     ndcg += queryNDCG(l_q_s)
#     cnt += 1
#
# # print cnt
# print(ndcg/cnt)

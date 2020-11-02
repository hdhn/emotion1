import pandas as pd
import numpy as np


Recommendation_itemId = np.loadtxt(open("recommendation_itemId.csv","rb"),delimiter=",",skiprows=0)

print(Recommendation_itemId)

test_data_score_matrix = np.loadtxt(open("test_data_score.csv","rb"),delimiter=",",skiprows=0)
test_data_score_matrix = np.matrix(test_data_score_matrix)
print(type(test_data_score_matrix))


dcg_matrix = np.zeros((600, 1), np.float)
dcg_matrix = pd.DataFrame(dcg_matrix)


for i in range(599):
    n = 1
    dcg_k = 0
    print(Recommendation_itemId[i])
    recommendation_list = Recommendation_itemId[i]
    print(type(recommendation_list))
    for j in range(9):
        item = int(recommendation_list[j])
        print(item)
        reli = test_data_score_matrix[i,item]
        # print(reli)

        dcg = (2**reli-1)/(np.log2(n+1))
        dcg_k = dcg_k + dcg
        print(dcg_k)

        print(dcg_matrix)
        n += 1
        print(n)
    dcg_matrix[0][i] = dcg_k

dcg_matrix.to_csv("dcg_data.csv",index=False,header=False)



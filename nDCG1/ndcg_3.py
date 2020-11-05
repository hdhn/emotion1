import pandas as pd
import numpy as np


Recommendation_itemId = np.loadtxt(open("recommendation_itemId.csv","rb"),delimiter=",",skiprows=0)

print(Recommendation_itemId)

test_data_score_matrix = np.loadtxt(open("test_data_score.csv","rb"),delimiter=",",skiprows=0)
test_data_score_matrix = np.matrix(test_data_score_matrix)
print(type(test_data_score_matrix))


idcg_matrix = np.zeros((600, 1), np.float)
idcg_matrix = pd.DataFrame(idcg_matrix)


for i in range(599):
    recommendation_score_dict = {}
    # print(i)
    recommendation_list = Recommendation_itemId[i]
    n = 1
    idcg_k = 0
    for j in range(9):
        item = int(recommendation_list[j])
        # print(item)
        score = test_data_score_matrix[i,item]
        recommendation_score_dict[item] = score
    print(recommendation_score_dict)
    recommendation_score_sorted = sorted(recommendation_score_dict.items(), key=lambda item: item[1], reverse=True)
    print(recommendation_score_sorted)
    for k in recommendation_score_sorted:
        print(type(k))
        reli = k[1]
        print(reli)
        idcg = (2**reli-1)/(np.log2(n+1))
        idcg_k = idcg_k + idcg
        print(idcg_k)
        n += 1
        print(n)

    idcg_matrix[0][i] = idcg_k
    print(idcg_matrix)

idcg_matrix.to_csv("idcg_data.csv",index=False,header=False)



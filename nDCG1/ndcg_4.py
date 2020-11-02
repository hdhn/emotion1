import pandas as pd
import numpy as np

dcg_data = np.loadtxt(open("dcg_data.csv","rb"),delimiter=",",skiprows=0)
idcg_data = np.loadtxt(open("idcg_data.csv","rb"),delimiter=",",skiprows=0)

print(dcg_data)
print(idcg_data)


ndcg_matrix = np.zeros((600, 1), np.float)
ndcg_matrix = pd.DataFrame(ndcg_matrix)

for i in range(599):
    dcg = dcg_data[i]
    idcg = idcg_data[i]
    if idcg == 0:
        idcg = 1
    ndcg = dcg / idcg
    print(ndcg)
    ndcg_matrix[0][i] = ndcg
    print(ndcg_matrix)
ndcg_k = np.mean(ndcg_matrix)
print(ndcg_k)
ndcg_matrix.to_csv("ndcg_data.csv", index=False, header=False)
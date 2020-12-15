import time

from sklearn.cluster import KMeans
from skimage import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def disEclud(arrA, arrB):
    d = arrA - arrB
    dist = np.sum(np.power(d, 2), axis=1)
    return dist


def randCent(dataSet, k):
    n = dataSet.shape[1]
    data_min = dataSet.iloc[:, :n - 1].min()
    data_max = dataSet.iloc[:, :n - 1].max()
    data_cent = np.random.uniform(data_min, data_max, (k, n - 1))
    return data_cent


def kmeans(dataSet, k, distMeas=disEclud, creatCent=randCent):
    m, n = dataSet.shape
    centroids = creatCent(dataSet, k)
    clusterAssment = np.zeros((m, 3))
    clusterAssment[:, 0] = np.inf
    clusterAssment[:, 1:3] = -1
    result_set = pd.concat([dataSet, pd.DataFrame(clusterAssment)], axis=1, ignore_index=True)
    clusterChange = True
    count1 = 0
    while clusterChange and count1 <= 10:
        start = time.time()
        clusterChange = False
        count1 += 1
        for i in range(m):
            dist = distMeas(dataSet.iloc[i, :n - 1].values, centroids)
            print(time.time() - start)
            result_set.iloc[i, n] = dist.min()
            result_set.iloc[i, n + 1] = np.where(dist == dist.min())[0]
        clusterChange = not (result_set.iloc[:, -1] == result_set.iloc[:, -2]).all()

        if clusterChange:
            cent_df = result_set.groupby(n + 1).mean()
            centroids = cent_df.iloc[:, :n - 1].values
            result_set.iloc[:, -1] = result_set.iloc[:, -2]
        print(time.time() - start)
    return centroids, result_set


image = io.imread('./2.jpg')
print(image)
io.imshow(image)
io.show()
rows = image.shape[0]
cols = image.shape[1]
print(rows, cols)
# image[0,0,:]：表示在第一个像素点的位置上的rgb取值，位置（0,0），reshape之后呢，位置变成（0）
image = image.reshape(rows * cols, 3)
print(image)
image = pd.DataFrame(image)
# n_init:每一次算法运行时开始的centroid seeds是随机生成的,
# 这样得到的结果也可能有好有坏. 所以要运行算法n_init次, 取其中最好的（时间最短的）.
# print(image)
# kmeans = KMeans(n_clusters=128,n_init=10,max_iter=200)
# kmeans.fit(image)

# clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8)
# labels = np.asarray(kmeans.labels_,dtype=np.uint8)
# labels = labels.reshape(rows,cols)
# print(clusters.shape)
# #np.save('codebook_test.npy',clusters)
# io.imsave('compressed_test1.jpg',labels)
# image = io.imread('compressed_test1.jpg')
# io.imshow(image)
# io.show()
ze = pd.DataFrame(np.zeros(image.shape[0]).reshape(-1, 1))
test_set = pd.concat([image, ze], axis=1, ignore_index=True)
test_cent, test_cluster = kmeans(test_set, 3)
test_cluster.iloc[:, 0:3] = test_cent[test_cluster.astype(int).iloc[:, 6], 0:3]
print(test_cent, test_cluster)
image1 = test_cluster.astype(int).iloc[:, 0:3]
print(image1)
image1 = np.array(image1).reshape(rows, cols, 3)
print(image1)
io.imshow(image1.astype(np.uint8))
io.show()

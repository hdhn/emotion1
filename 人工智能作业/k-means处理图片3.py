import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin
from skimage import io
# 计算欧氏距离
def calcDis(dataSet, centroids, k):
    clalist = []
    for data in dataSet:
        diff = np.tile(data, (k,
                              1)) - centroids  # 相减   (np.tile(a,(2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。 再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
        squaredDiff = diff ** 2  # 平方
        squaredDist = np.sum(squaredDiff, axis=1)  # 和  (axis=1表示行)
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)
    clalist = np.array(clalist)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    return clalist


# 计算质心
def classify(dataSet, centroids, k):
    # 计算样本到质心的距离
    clalist = calcDis(dataSet, centroids, k)
    # 分组并计算新的质心
    minDistIndices = np.argmin(clalist, axis=1)  # axis=1 表示求出每行的最小值的下标
    newCentroids = pd.DataFrame(dataSet).groupby(
        minDistIndices).mean()  # DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值
    newCentroids = newCentroids.values

    # 计算变化量
    changed = newCentroids - centroids

    return changed, newCentroids


# 使用k-means分类
def kmeans(dataSet, k):
    # 随机取质心
    centroids = random.sample(dataSet, k)
    flag = []
    # 更新质心 直到变化量全为0
    changed, newCentroids = classify(dataSet, centroids, k)
    while np.any(changed != 0):
        changed, newCentroids = classify(dataSet, newCentroids, k)

    centroids = sorted(newCentroids.tolist())  # tolist()将矩阵转换成列表 sorted()排序

    # 根据质心计算每个集群
    cluster = []
    clalist = calcDis(dataSet, centroids, k)  # 调用欧拉距离
    minDistIndices = np.argmin(clalist, axis=1)
    for i in range(k):
        cluster.append([])
    for i, j in enumerate(minDistIndices):  # enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])
        flag.append(j)


    return centroids, cluster,flag


# 创建数据集
def createDataSet():
    data = np.random.uniform(1,50,(100,2))
    return data#[[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]


def find_clusters(x, n_clusters, rseed=2):
    #1.随机选择簇中心点
    rng = np.random.RandomState(rseed)
    i = rng.permutation(x.shape[0])[:n_clusters]
    centers = x[i]

    while True:
        # 2a.给于最近的中心执行标签
        labels = pairwise_distances_argmin(x, centers)
        #2b.根据点的平均值找到新的中心
        new_centers =np.array([x[labels==i].mean(0)
                               for i in range(n_clusters)])
        #2c.确认收敛
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels
if __name__ == '__main__':
    image = io.imread('./1.jpg')
    #print(image)
    io.imshow(image)
    io.show()
    rows = image.shape[0]
    cols = image.shape[1]
    print(rows, cols)
    # image[0,0,:]：表示在第一个像素点的位置上的rgb取值，位置（0,0），reshape之后呢，位置变成（0）
    image = image.reshape(rows * cols, 3)
    print(image)

    #以上为处理图片添加的代码

    dataset =image
    centroids, cluster,flag = kmeans(list(dataset), 3)
    #flag = pd.DataFrame(flag)
    print('质心为：%s' % centroids)
    print('集群为：%s' % cluster)
    flag = np.array(flag)
    image =  pd.DataFrame(image)
    cluster = pd.DataFrame(cluster)
    ze = pd.DataFrame(flag.reshape(-1, 1))
    cluster = pd.concat([image, ze], axis=1, ignore_index=True)
    centroids=np.array(centroids)
    print(cluster)
    cluster.iloc[:, 0:3] = centroids[cluster.astype(int).iloc[:, -1], 0:3]
    image1 = cluster.astype(int).iloc[:, 0:3]
    #print(image1)
    image1 = np.array(image1).reshape(rows, cols, 3)
    #print(image1)
    io.imshow(image1.astype(np.uint8))
    io.show()
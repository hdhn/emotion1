import numpy as np
import matplotlib.pyplot as plt

#加载数据
def LoadData(fname):
    data = np.loadtxt(fname, delimiter='\t')
    return data


# 欧氏距离计算
def distOU(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


# 为给定数据集构建一个包含K个随机质心的集合
def randomCent(dataSet, k):
    m, n = dataSet.shape#m行n列数据
    centroids = np.zeros((k, n))#初始化质心，
    for i in range(k):
        index = int(np.random.uniform(0, m))  #从0到m随机采样，即随机选择质心的横坐标
        centroids[i, :] = dataSet[index, :]#确定质心的位置
    return centroids


# k均值聚类
def KMeans(dataSet, k):
    m = np.shape(dataSet)[0]
    # 第一列存样本属于哪一簇
    # 第二列存样本的到簇的中心点的误差
    clusterA = np.mat(np.zeros((m, 2)))#创建一个m*2的零矩阵
    clusterC = True

    # 第1步 初始化centroids
    centroids = randomCent(dataSet, k)
    while clusterC:
        clusterC = False

        # 遍历所有的样本（行数）
        for i in range(m):
            minDist = 100000.0
            minIndex = -1

            # 遍历所有的质心
            # 第2步 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distance = distOU(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
            # 第 3 步：更新每一行样本所属的簇
            if clusterA[i, 0] != minIndex:
                clusterC = True
                clusterA[i, :] = minIndex, minDist ** 2
        # 第 4 步：更新质心
        for j in range(k):
            ZCluster = dataSet[np.nonzero(clusterA[:, 0].A == j)[0]]  # 获取簇类所有的点
            centroids[j, :] = np.mean(ZCluster, axis=0)  # 对矩阵的行求均值

    return centroids, clusterA


def showCluster(dataSet, k, centroids, clusterA):
    m, n = dataSet.shape
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    # 绘制所有的样本
    for i in range(m):
        markIndex = int(clusterA[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # 绘制质心
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i])
    plt.show()
dataSet = LoadData("test.txt")
print(type(dataSet))
k = 4
centroids, clusterA = KMeans(dataSet, k)
showCluster(dataSet, k, centroids, clusterA)
import numpy as np
import pandas as pd
from skimage import io
import matplotlib.pyplot as plt


def disEclud(arrA,arrB):#计算欧式距离
    d = arrA - arrB
    dist = np.sum(np.power(d,2),axis=1)
    return dist
#初始化聚类中心：通过在区间范围随机产生的值作为新的中心点
def randCent(dataSet,k):
    n = dataSet.shape[1]#获取特征维度
    data_min = dataSet.iloc[:,:n-1].min()#获取数据集的最小值
    data_max = dataSet.iloc[:,:n-1].max()#数据集的最大值
    data_cent = np.random.uniform(data_min,data_max,(k,n-1))#随机出一个(k,n-1)的矩阵
    return data_cent

def kmeans(dataSet,k,distMeas = disEclud,creatCent = randCent):
    m,n = dataSet.shape
    centroids = creatCent(dataSet,k) #初始化聚类中心
    clusterAssment = np.zeros((m,3))    #创建(m,3)的全0矩阵
    clusterAssment[:,0] = np.inf    #第一列初始化为无限大
    clusterAssment[:,1:3] = -1      #第2-4列初始化为-1
    result_set = pd.concat([dataSet,pd.DataFrame(clusterAssment)],axis=1,ignore_index=True)
    #链接数据集与clusterAssment
    clusterChange = True
    while clusterChange :
        clusterChange = False
        for i in range(m):
            dist = distMeas(dataSet.iloc[i,:n-1].values,centroids) #计算欧氏距离
            result_set.iloc[i,n] = dist.min() #欧式距离的最小值储存在第n+1列
            result_set.iloc[i,n+1] = np.where(dist == dist.min())[0]#第n+2列储存质心编号
        clusterChange = not (result_set.iloc[:,-1]==result_set.iloc[:,-2]).all()
        if clusterChange:#判断质心是否发生变化
            cent_df = result_set.groupby(n+1).mean()
            centroids = cent_df.iloc[:,:n-1].values
            result_set.iloc[:,-1] = result_set.iloc[:,-2]
    return centroids,result_set

def createDataSet():
    data = np.random.uniform(1,50,(100,2))
    # image = io.imread('./1.jpg')
    # rows = image.shape[0]
    # cols = image.shape[1]
    # image = image.reshape(rows*cols,3)
    # print(image)
    # data = pd.DataFrame(image)
    data = pd.DataFrame(data)
    print(data)
    return data#[[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]

if __name__ == '__main__':
    testSet = createDataSet()
    ze = pd.DataFrame(np.zeros(testSet.shape[0]).reshape(-1,1))
    test_set = pd.concat([testSet,ze],axis=1,ignore_index= True)
    test_cent,test_cluster = kmeans(test_set,4)
    #print(test_cluster,test_cent)
    plt.scatter(test_cluster.iloc[:,0],test_cluster.iloc[:,1],c = test_cluster.iloc[:,-1])

    plt.scatter(test_cent[:,0],test_cent[:,1],color='red',marker='x',s = 80)
    plt.show()
    #print(test_cluster.iloc[:,-1])

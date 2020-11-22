import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def disEclud(arrA,arrB):
    d = arrA - arrB
    dist = np.sum(np.power(d,2),axis=1)
    return dist

def randCent(dataSet,k):
    n = dataSet.shape[1]
    data_min = dataSet.iloc[:,:n-1].min()
    data_max = dataSet.iloc[:,:n-1].max()
    data_cent = np.random.uniform(data_min,data_max,(k,n-1))
    return data_cent

def kmeans(dataSet,k,distMeas = disEclud,creatCent = randCent):
    m,n = dataSet.shape
    centroids = creatCent(dataSet,k)
    clusterAssment = np.zeros((m,3))
    clusterAssment[:,0] = np.inf
    clusterAssment[:,1:3] = -1
    result_set = pd.concat([dataSet,pd.DataFrame(clusterAssment)],axis=1,ignore_index=True)
    clusterChange = True
    while clusterChange:
        clusterChange = False
        for i in range(m):
            dist = distMeas(dataSet.iloc[i,:n-1].values,centroids)
            result_set.iloc[i,n] = dist.min()
            result_set.iloc[i,n+1] = np.where(dist == dist.min())[0]
        clusterChange = not (result_set.iloc[:,-1]==result_set.iloc[:,-2]).all()
        if clusterChange:
            cent_df = result_set.groupby(n+1).mean()
            centroids = cent_df.iloc[:,:n-1].values
            result_set.iloc[:,-1] = result_set.iloc[:,-2]
    return centroids,result_set

def createDataSet():
    data = np.random.uniform(1,50,(100,2))
    data = pd.DataFrame(data)
    print(data)
    return data#[[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]

if __name__ == '__main__':
    testSet = createDataSet()
    ze = pd.DataFrame(np.zeros(testSet.shape[0]).reshape(-1,1))
    test_set = pd.concat([testSet,ze],axis=1,ignore_index= True)
    test_cent,test_cluster = kmeans(test_set,4)
    plt.scatter(test_cluster.iloc[:,0],test_cluster.iloc[:,1],c = test_cluster.iloc[:,-1])

    plt.scatter(test_cent[:,0],test_cent[:,1],color='red',marker='x',s = 80)
    plt.show()
    print(test_cluster.iloc[:,-1])

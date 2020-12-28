# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage import io

def kmeans(data, n, m, k, plt):
    # 获取4个随机数
    rarray = np.random.random(size=k)
    # 乘以数据集大小——>数据集中随机的4个点
    rarray = np.floor(rarray*n)
    # 转为int
    rarray = rarray.astype(int)
    print('数据集中随机索引', rarray)
    # 随机取数据集中的4个点作为初始中心点
    center = data[rarray]
    # 测试比较偏、比较集中的点，效果依然完美，测试需要删除以上代码
    # center = np.array([[4.6,-2.5],[4.4,-1.7],[4.3,-0.7],[4.8,-1.1]])
    # 1行80列的0数组，标记每个样本所属的类(k[i])
    cls = np.zeros([n], np.int)
    print('初始center=\n', center)
    run = True
    time = 0
    while run:
        time = time + 1
        for i in range(n):
            # 求差
            tmp = data[i] - center
            # 求平方
            tmp = np.square(tmp)
            # axis=1表示按行求和
            tmp = np.sum(tmp, axis=1)
            # 取最小（最近）的给该点“染色”（标记每个样本所属的类(k[i])）
            cls[i] = np.argmin(tmp)
        # 如果没有修改各分类中心点，就结束循环
        run = False
        # 计算更新每个类的中心点
        for i in range(k):
            # 找到属于该类的所有样本
            club = data[cls==i]
            # axis=0表示按列求平均值，计算出新的中心点
            if len(club) != 0:
                newcenter = np.mean(club, axis=0)
            # 如果新旧center的差距很小，看做他们相等，否则更新之。run置true，再来一次循环
            ss = np.abs(center[i]-newcenter)
            if np.sum(ss, axis=0) > 1e-4:
                center[i] = newcenter
                run = True
        print('new center=\n', center)
    print('程序结束，迭代次数：', time)
    # 按类打印图表，因为每打印一次，颜色都不一样，所以可区分出来
    for i in range(k):
        club = data[cls == i]
        showtable(club, plt)
    # 打印最后的中心点
    showtable(center, plt)
    return center,cls




def showtable(data, plt):
    x = data.T[0]
    y = data.T[1]
    plt.scatter(x, y)


if __name__ == "__main__":
    # csv = pd.DataFrame(np.random.uniform(1,50,(80,2)))
    # # 打印原始数据
    # # showtable(csv.values, plt)
    # cent,flag = kmeans(csv.values, 80, 2, 4, plt)#数据量80，数据维度2，建议簇3-4
    # print(cent,flag)
    #plt.show()
    image = io.imread('./2.jpg')
    io.imshow(image)
    io.show()
    rows = image.shape[0]
    cols = image.shape[1]
    print(rows,cols)
    image = image.reshape(rows *cols,3)
    print(image)
    centroids,flag = kmeans(image,rows*cols,2,4,plt)
    print(centroids,flag)
    flag = np.array(flag)
    image =  pd.DataFrame(image)
    #cluster = pd.DataFrame(cluster)
    ze = pd.DataFrame(flag.reshape(-1, 1))
    test_cluster = pd.concat([image, ze], axis=1, ignore_index=True)
    centroids=np.array(centroids)
    #print(cluster)
    test_cluster.iloc[:, 0:3] = centroids[test_cluster.astype(int).iloc[:, -1], 0:3]
    image1 = test_cluster.astype(int).iloc[:, 0:3]
    #print(image1)
    image1 = np.array(image1).reshape(rows, cols, 3)
    #print(image1)
    io.imshow(image1.astype(np.uint8))
    io.show()

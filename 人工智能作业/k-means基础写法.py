import numpy as np
import matplotlib.pyplot as plt
import math
from skimage import io

image = io.imread('./timg.jpg')
io.imshow(image)
io.show()
rows = image.shape[0]
cols = image.shape[1]
image1 =image.reshape(rows*cols,3)
k=8
centriods = []
length = int(len(image1)/k)
for centerindex in range(k):
    centriods.append(image[centerindex*length])
def disEclud(arrA,arrB):
    distance = math.sqrt(math.pow(arrA[0]-arrB[0],2)+math.pow(arrA[1]-arrB[1],2)+math.pow(arrA[2]-arrB[2],2))
    return distance

def getminindex(minlist):#记录传入列表中的值的最小
    minindex = 0
    for i in range(len(minlist)):
        if minlist[i]<minlist[minindex]:
            minindex = i
    return minindex
def calc_distance(centroids,datasets):#计算距离
    global k
    distances = []
    indexs = []
    for i in range(k):
        distance = []
        index = []
        distances.append(distance)
        indexs.append(index)
    for index,dataset in enumerate(datasets):
        min_list = []
        for centroid in range(k):
            min_list.append(disEclud(dataset,centroids[centroid]))
        min_index = getminindex(min_list)
        distances[min_index].append(dataset)
        indexs[min_index].append(index)
    return distances,indexs
def calxyzavg(xyzs):
    l = []
    for i in range(len(xyzs)):

        x_sum = 0
        y_sum = 0
        z_sum = 0
        for j in xyzs[i]:
            x_sum = x_sum + j[0]
            y_sum = y_sum + j[1]
            z_sum = z_sum + j[2]
        x_sum = x_sum/len(xyzs[i])
        y_sum = y_sum/len(xyzs[i])
        z_sum = z_sum/len(xyzs[i])
        l.append((x_sum,y_sum,z_sum))
    return l


row_size = 10
col_size = 5

iterate_index = 1
flag = True
temp_index = 1
while flag:
    cd,indexs = calc_distance(centriods,image1)
    cxa = calxyzavg(cd)
    correct_num =0
    print(temp_index)
    temp_index = temp_index + 1
    for i in range(len(centriods)):
        if disEclud(centriods[i],cxa[i])<1:
            correct_num = correct_num +1
    if correct_num == len(centriods):
        flag = False
    else:
        centriods = cxa
group = cd
group_indexs = indexs
print("succeed")
for index,centriod in enumerate(np.array(centriods,dtype=int)):
    for i in indexs[index]:
        image1[i] = centriod

orignimage = image1.reshape(rows,cols,3)
io.imshow()
io.show()


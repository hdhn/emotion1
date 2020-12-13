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
def creatCent(image,k):
    centroids = []
    length = int(len(image)/k)
    for center in range(k):
        centroids.append(image[center*length])

def disEclud(arrA,arrB):
    distance = math.sqrt(math.pow(arrA[0],arrB[0],2)+math.pow(arrA[1]-arrB[1],2)+math.pow(arrA[2]-arrB[2],2))
    return distance

def getmin(minlist):
    minindex = 0
    for i in range(len(minlist)):
        if minlist[i]<minlist[minindex]:
            minindex = i
    return minindex
def
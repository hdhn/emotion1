from sklearn.cluster import KMeans
from skimage import io
import numpy as np

image = io.imread('./smile.jpg')
io.imshow(image)
io.show()
rows = image.shape[0]
cols = image.shape[1]
# image[0,0,:]：表示在第一个像素点的位置上的rgb取值，位置（0,0），reshape之后呢，位置变成（0）
image = image.reshape(rows*cols,3)
# n_init:每一次算法运行时开始的centroid seeds是随机生成的,
# 这样得到的结果也可能有好有坏. 所以要运行算法n_init次, 取其中最好的（时间最短的）.
print(image)
kmeans = KMeans(n_clusters=128,n_init=10,max_iter=200)
kmeans.fit(image)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8)
labels = np.asarray(kmeans.labels_,dtype=np.uint8)
labels = labels.reshape(rows,cols)
print(clusters.shape)
#np.save('codebook_test.npy',clusters)
io.imsave('compressed_test.jpg',labels)
image = io.imread('compressed_test.jpg')
io.imshow(image)
io.show()
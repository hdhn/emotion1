from skimage import io
import matplotlib.pyplot as mp
import sklearn.cluster as sc
from sklearn.cluster import KMeans


img = io.imread('./smile.jpg',True)
x = img.reshape(-1,1)
print(x)
model = sc.KMeans(n_clusters=4)
# 训练模型
model.fit(x)
label = model.labels_   # 每个样本的标签
# 获取聚类中心，并将其铺平
centers = model.cluster_centers_.ravel()
print(centers) # 查看centers的结构
# 生成新图片，将每个样本标签按每个聚类中心赋值，并转换成与img同维度
newimg = centers[label].reshape(img.shape)
#绘制图形
mp.figure('Quant',facecolor='lightgray')
mp.subplot(121)
mp.axis('off')# 关闭坐标系
mp.imshow(img,cmap='gray')
mp.subplot(122)
mp.axis('off')# 关闭坐标系
mp.imshow(newimg,cmap='gray')

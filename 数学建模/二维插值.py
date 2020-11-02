#样例3:某二维图像表达式为(x+y)e^(-5*(x^2+y^2)),完成图像的二维插值使其变清晰

import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
def func(x,y):
    return (x+y)*np.exp(-5.0*(x**2+y**2))

#X-Y轴分为15*15的网络
y,x = np.mgrid[-1:1:15j,-1:1:15j]
#计算每个网格点上函数值
fvals = func(x,y)
#三次样条二维插值
newfunc  =interpolate.interp2d(x,y,fvals,kind='cubic')
#计算100*100网格上插值
xnew = np.linspace(-1,1,100)
ynew = np.linspace(-1,1,100)
fnew = newfunc(xnew,ynew)
#可视化
#让imshow的参数interpolat设置为'nearest'方便比较插值处理
pl.subplot(121)
iml = pl.imshow(fvals,extent = [-1,1,-1,1],
                cmap=mpl.cm.hot,interpolation='nearest',origin="lower")
pl.colorbar(iml)
pl.subplot(122)
im2 = pl.imshow(fnew,extent=[-1,1,-1,1],
                cmap=mpl.cm.hot,interpolation='nearest',origin="lower")
pl.colorbar(im2)
pl.show()

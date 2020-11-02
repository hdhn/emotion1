#样例4:某图像表达式为(x+y)e**(-5*(x**2+y**2)),完成三维图像的二维插值可视化

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


def func(x,y):
    return (x+y)*np.exp(-5.0*(x**2+y**2))
#X-Y轴分为20*20的网格
x = np.linspace(-1,1,20)
y = np.linspace(-1,1,20)
x,y = np.meshgrid(x,y)
fvals = func(x,y)
#画分图1
fig = plt.figure(figsize=(9,6))
ax = plt.subplot(1,2,1,projection = '3d')
surf = ax.plot_surface(x,y,fvals,rstride=2,cstride=2,
                       cmap = cm.coolwarm,linewidth = 0.5,antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlabel('f(x,y)')
plt.colorbar(surf,shrink = 0.5,aspect = 5)#添加颜色条标注

#二维插值
newfunc = interpolate.interp2d(x,y,fvals,kind = 'cubic')
#计算100*100网格上插值
xnew = np.linspace(-1,1,100)
ynew = np.linspace(-1,1,100)
fnew = newfunc(xnew,ynew)
xnew,ynew = np.meshgrid(xnew,ynew)
ax2 = plt.subplot(1,2,2,projection = '3d')
surf2 = ax.plot_surface(xnew,ynew,fnew,rstride = 2,
                        cstride = 2,cmap = cm.coolwarm,linewidth = 0.5,antialiased = True)
ax2.set_xlabel('xnew')
ax2.set_ylabel('ynew')
ax2.set_zlabel('fnew(x,y')
plt.colorbar(surf2,shrink = 0.5,aspect = 5)#标注
plt.show()
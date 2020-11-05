#样例2:某电学元件的电压数据记录在0~10A范围与电流关系满足正弦函数，分别用0-5
#阶样条插值方法给出经过数据点的数值逼近函数曲线
#创建数据点集
import numpy as np
import pylab as pl
x = np.linspace(0,10,11)
y = np.sin(x)
#回执数据点集
pl.figure(figsize=(12,9))
pl.plot(x,y,'ro')
#根据kind创建interpld对象f、计算插值结果
xnew = np.linspace(0,10,101)
from scipy import interpolate
for kind in ['nearest','zero','linear','quadratic']:
    f = interpolate.interp1d(x,y,kind = kind)
    ynew = f(xnew)
    pl.plot(xnew,ynew,label = str(kind))
    pl.xticks(fontsize = 20)
    pl.xticks(fontsize = 20)
    pl.legend(loc = 'lower right')
    pl.show()


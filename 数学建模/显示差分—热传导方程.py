#1D热传导方程
#ut-kuxx = 0,0<=x<=1
#u(x,0) = 4x(1-x),0<=x<=1
#u(0,t)=0,t>=0
#u(1,t)=0,t>=0
#其中，k称为热传导系数，第2式是方程的初值条件，第3、4式是方程的边值条件

from  matplotlib import pylab
import  seaborn as sns
import  numpy as np
from CAL import PyCAL
PyCAL.font.set_size(20)
def initialCondition(x):
    return 4.0*(1.0-x)*x
xArray = np.linspace(0,1.0,50)
yArray = map(initialCondition,xArray)
pylab.figure(figsize=(12,6))
pylab.xlabel('$x$',fontsize = 15)
pylab.ylabel('$f(x)$',fontsize = 15)
pylab.title(u'一维热传导方程初值条件',fontproperties = font)

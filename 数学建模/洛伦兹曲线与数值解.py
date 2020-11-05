#以下方程组代表曲线在xyz三个方向上的速度。给定一个初始点，可以画出相应的洛伦兹曲线：
#dx/dt=p(y-x)
#dy/dt = x(r-z)
#dz/dt = xy-bz
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def dmove(Point,_,sets):
    p,r,b = sets
    x,y,z = Point
    return np.array([p*(y-x),x*(r-z),x*y-b*z])

t = np.arange(0,30,0.001)
P1 = odeint(dmove,(0.,1.,0.),t,args=([10.,28.,3.],))
P2 = odeint(dmove,(0.,1.01,0.),t,args=([10.,28.,3.],))

fig = plt.figure()
ax = Axes3D(fig)
#ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot(P1[:,0],P1[:,1],P1[:,2])
ax.plot(P2[:,0],P2[:,1],P2[:,2])

plt.show()

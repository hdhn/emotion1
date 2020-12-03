import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

x = np.linspace(0, 32, 1000)
y = 1-0.56*(x*24)**0.06
plt.plot(x, y,label = '时间-记忆保留比率')
plt.xlabel(u'时间(天)')
plt.ylabel(u'记忆保留比率')
plt.annotate("20分钟-58.2%", (0.014,0.582), xycoords='data',xytext=(5,0.7),arrowprops=dict(arrowstyle='->'))
plt.annotate("1小时-44.2%", (0.1,0.442), xycoords='data',xytext=(5,0.6),arrowprops=dict(arrowstyle='->'))
plt.annotate("9小时-36.8%", (0.3,0.368), xycoords='data',xytext=(7,0.5),arrowprops=dict(arrowstyle='->'))
plt.annotate("1天-33.7%", (1,0.337), xycoords='data',xytext=(10,0.4),arrowprops=dict(arrowstyle='->'))
plt.annotate("2天-23.8%", (2,0.278), xycoords='data',xytext=(0,0.2),arrowprops=dict(arrowstyle='->'))
plt.annotate("6天-26.4%", (6,0.264), xycoords='data',xytext=(10,0.3),arrowprops=dict(arrowstyle='->'))
plt.annotate("31天-21.1%", (31,0.211), xycoords='data',xytext=(25,0.4),arrowprops=dict(arrowstyle='->'))
plt.show()
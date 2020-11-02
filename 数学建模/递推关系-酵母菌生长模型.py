#查分方程建模的关键在于如何得到第n组数据与第n+1组数据之间的关系
import  matplotlib.pyplot as plt
time = [i for i in range(0,19)]
number = [9.6,18.3,29,47.2,71.1,119.1,174.6,257.3,\
          350.7,441.0,513.3,559.7,594.8,629.4,640.8,\
          651.1,665.9,659.6,661.8]
plt.title('Relationship between time and number')#创建标题
plt.xlabel('time')#X轴标签
plt.ylabel('number')
plt.plot(time,number)
plt.show()

import numpy as np
pn = [9.6,18.3,29,47.2,71.1,119.1,174.6,\
      257.3,350.7,441.0,513.3,559.7,594.8,629.4,\
      640.8,651.1,655.9,659.6]
deltap = [8.7,10.7,18.2,23.9,48,55.5,\
          82.7,93.4,90.3,72.3,46.4,35.1,\
          34.6,11.4,10.3,4.8,3.7,2.2]
pn = np.array(pn)
factor = pn*(665-pn)
f = np.polyfit(factor,deltap,1)
print(f)


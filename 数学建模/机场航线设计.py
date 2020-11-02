#数据集来自航空业，有一些关于航线的基本信息。有关某段旅程的起
# 始点和目的地。还有一些列表示每段旅程的到达和起飞时间。这个
# 数据集非常适合作为图进行分析。想象一下通过航线（边）连接的
# 几个城市（节点）。如果你是航空公司，你可以问如下几个问题：
#1、从A到B的最短路径是什么？分别从距离和时间角度考虑。
#2、有没有办法从C到D？
#3、哪些集成的交通最繁忙？
#4、那个机场位于大多数其他机场“之间”？这样它就可以变成当地的一个中转站。

import  numpy as np
import pandas as pd
data = pd.read_csv('data/Airlines.csv')
data.shape
data.dtypes

#将sched_dep_time转换为‘std’-预定的出发时间
data['std'] = data.sched_dep_time.astype(str).str.replace('(\d{2}')
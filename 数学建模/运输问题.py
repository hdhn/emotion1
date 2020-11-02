import pulp
import numpy as np
from pprint import pprint
#运输问题
#某商品有m个产地、n个销地，各产地的产量分别为a1,……，am,各销地的需求量分别为b1,……,bn。若该商品由i地运到j销地的单位运价为cij
#问应该如何调运才能使总运费最省？
#引入变量Xij，其取值为由i产地yunwangj销地的该商品数量，模型为：
#min∑i=1~m∑j=1~n cijxij
#∑j=1~n xij = ai
#∑i=1~m xij = bj
# xij>=0


def transportation_problem(costs,x_max,y_max):
    row = len(costs)
    col = len(costs[0])
    prob = pulp.LpProblem('Transportation_Problem',sense=pulp.LpMaximize)
    var = [[pulp.LpVariable(f'x{i}{j}',lowBound=0,cat=pulp.LpInteger) for j in range(col)] for i in range(row)]
    flatten = lambda x : [y for l in x for y in flatten(l)] if type(x) is list else [x]
    prob += pulp.lpDot(flatten(var),costs.flatten())
    for i in range(row):
        prob +=(pulp.lpSum(var[i]) <= x_max[i])
    for j in range(col):
        prob +=(pulp.lpSum([var[i][j] for i in range(row)]) <=y_max[j])
    prob.solve()
    return {'objective':pulp.value(prob.objective),'var':[[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}

if __name__ == '__main__':
    costs = np.array([[500,550,630,100,800,700],
                      [800,700,600,950,900,930],
                      [1000,960,840,650,600,700],
                      [1200,1040,980,860,880,780]])
    max_plant = [76,88,96,40]
    max_cultibation = [42,56,44,39,60,59]
    res = transportation_problem(costs,max_plant,max_cultibation)
    print(f'最大值为{res["objective"]}')
    print('各变量的取值为：')
    pprint((res['var']))
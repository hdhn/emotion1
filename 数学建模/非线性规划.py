import scipy
#scipy.optimize.minimize(fun,x0,args=(),method=None,jac=None,hess=None,hessp=None,bounds=None,constaints=(),tol=None,callback=None,options=None)
#fun:求最小值的目标函数 args:常数值
#method:求极值方法，一般默认。  constraints:约束条件
#x0:变量的初始猜测值，注意minimiz是局部最优

#样例3：计算1/x+x的最小值
from scipy.optimize import minimize
import numpy as np
def fun(args):
    a=args
    v=lambda x:a/x[0] + x[0]
    return v


if __name__ =="__main__":
    args = (1)  #a
    x0 = np.asarray((2))  #初始猜测值
    res = minimize(fun(args),x0,method='SLSQP')
    print(res.fun)
    print(res.success)
    print(res.x)

#样例4:计算(2+x1)/(1+x2) - 3x1 +4x3的最小值,其中x1、x2、x3范围在0.1到0.9之间
from scipy.optimize import minimize
import numpy as np
#计算(2+x1)/(1+x2) - 3*x1+4*x3 的最小值 x1,x2,x3的范围都在0.1到0.9之间
def fun(args):
    a,b,c,d = args
    v = lambda  x: (a+x[0])/(b+x[1]) - c*x[0]+d*x[2]
    return v
def con(args):
    # 约束条件 分为eq 和ineq
    #eq表示  函数结果等于0; ineq 表示  表达式 大于等于0
    x1min,x1max,x2min,x2max,x3min,x3max = args
    cons = ({'type':'ineq','fun':lambda  x:x[0]-x1min},\
            {'type':'ineq','fun':lambda  x:-x[0]+x1max},\
            {'type':'ineq','fun':lambda  x:x[1]-x2min},\
            {'type':'ineq','fun':lambda  x:-x[1]+x2max},\
            {'type':'ineq','fun':lambda  x:x[2]-x3min},\
            {'type':'ineq','fun':lambda  x:-x[2]+x3max})
    return cons

if __name__ =="__main__":
    #定义常量值
    args =(2,1,3,4) #a,b,c,d
    #设置参数范围/约束条件
    args1 =(0.1,0.9,0.1,0.9,0.1,0.9) #x1min.x1,ax,m2min,x2max
    cons = con(args1)
    #设置初始猜测值
    x0=np.asarray((0.5,0.5,0.5))
    res = minimize(fun(args),x0,method='SLSQP',constraints=cons)
    print(res.fun)
    print(res.success)
    print(res.x)


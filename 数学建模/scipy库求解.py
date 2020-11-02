from scipy import optimize
import numpy as np
#目标函数和约束条件，求解前应该转化为标准形式：
#min cTx
#{Ax<=b
# Aeq*x=beq
# lb<=x<=ub
#maxz = 2x1+3x2-5x3
#x1+x2+x3=7
#2x1-5x2+x3>=10
#x1+3x2+x3<=12
#x1,x2,x3>=0

c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])
B = np.array([-10,12])
Aeq = np.array([[1,1,1]])
Beq = np.array([7])

res = optimize.linprog(-c,A,B,Aeq,Beq)
print(res)

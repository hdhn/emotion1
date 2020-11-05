#样例：科技成果模糊综合评价模型的建立及其有关参数的确定。
import numpy as np

def frequency(matrix,p):
    A = np.zeros((matrix.shape[0]))
    for i in range(0,matrix.shape[0]):
        row = list(matrix[i,:])
        maximum = max(row)
        minimum = min(row)
        gap = (maximum - minimum)/p
        row.sort()
        group = []
        item = minimum
        while(item < maximum):
            group.append([item,item+gap])
            item = item +gap
        dataDict = {}
        for k in range(0,len(group)):
            dataDict[str(k)] = 0
        for j in range(0,matrix.shape[1]):
            for k in range(0,len(group)):
                if(matrix[k,j] >= group[k][0]):
                    dataDict[str(k)] = dataDict[str(k)] + 1
                    break
        index = int (max(dataDict,key = dataDict.get()))
        mid = (group[index][0] + group[index][1])/2
        A[i] = mid
    A = A / sum(A[:])
    return A

def isConsist(matrix):
    n = np.shape(matrix)[0]
    a,b = np.linalg.eig(matrix)
    maxlam = a[0].real
    CI = (maxlam - n)/(n-1)
    RI = [0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45]
    CR = CI/RI[n-1]
    if CR <0.1:
        return True,CI,RI[n-1]
    else:
        return False,None,None

def AHP(matrix):
    if isConsist(matrix):
        lam,x = np.linalg.eig(matrix)
        return x[0]/sum(x[0][:])
    else:
        print("一致性检验未通过")
        return None

def mul_mymin_operator(A,R):
    B = np.zeros((1,R.shape[1])):
    for column in range(0,R.shape[1]):
        list = []
        for row in range(0,R.shape[0]):
            list.append(A[row] *R[row,column])
        B[0,column] = mymin(list)
    return B

def appraise(criterionMatrix,targetMatrixs,relationMatrixs):
    R = np.zeros((criterionMatrix.shape[1],relationMatrixs[0].shapep[1]))
    for index in range(0,len(targetMatrixs)):
        row = mul_mymin_operator(targetMatrixs[index],relationMatrixs[index])
        R[index] = row
    B = mul_mymin_operator(criterionMatrix,R)
    return B/sum(B[:])

def mymin(list):
    for index in range(1,len(list)):
        if index == 1:
            temp = min(1,list[0]+list[1])
        else:
            temp = min(1,temp+list[index])
    return temp


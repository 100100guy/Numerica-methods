import numpy as np

def GaussianElimination (A, B, pivot = True, showall = True):
    def MaxRow (A, k):
        n = len(A)
        p = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[p][k]):
                p = i
        return p

    def RowSwap (A, B, p, q):
        n = len(A)
        for i in range(n):
            A[p][i], A[q][i] = A[q][i], A[p][i]
        B[p][0], B[q][0] = B[q][0], B[p][0]

    n = len(A)
    x = [0.0] * n
    for i in range(n-1):
        if pivot:
            RowSwap (A, B, i, MaxRow(A, i))
        for j in range(i+1, n):
            R = A[j][i] / A[i][i]
            for k in range (n):
                A[j][k] = A[j][k] - R * A[i][k]
            B[j][0] = B[j][0] - R * B[i][0]

    x[n-1] = B[n-1][0] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = B[i][0]
        for j in range(i+1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x


def polynomReg(m,x,y):
    X = []
    A=[[]]*(m+1)
    B=[[]]*(m+1)
    for i in range(m+1):
        A[i]=list()
        for j in range(m+1):
            A[i].append(powSum(x,i+j))
        B[i]=list()
        B[i].append(prodSum(x,y,i))
    X=GaussianElimination(A,B)
    return X

def powSum(x,m):
    sum=0
    for i in range(len(x)):
        sum+=x[i]**m
    return sum

def prodSum(x,y,m=1,eX=[]):
    sum=0
    if not eX:
        for i in range(len(x)):
            sum+=x[i]**m * y[i]
    else:
        for i in range(len(x)):
            sum+=x[i]**m * y[i] * eX[i]
    return sum

x=np.array([80,40,-40,-120,-200,-280,-340],dtype=float)
y=np.array([6.47e-6,6.24e-6,5.72e-6,5.09e-6,4.30e-6,3.33e-6,2.45e-6],dtype=float)
Answer=[]
Answer=polynomReg(2,x,y)
print(Answer)
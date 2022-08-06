import numpy as np

np.set_printoptions(formatter={'float':'{:0.8f}'.format})

def GaussianElimination(A,B,pivot=True,showall=True):

    n=len(B)
    t=np.zeros(n,float)
    m1=0
    k1=0
    if showall==True:
        print("The A matrix is: ")
        print(A)
        print("The B matrix is: ")
        print(B)

    #Forward elimination
    for k in range(n-1):
        if pivot==True:
            if A[k,k]==0:
                max=A[k,k]
                for m in range(k+1,n):
                    if abs(A[m,k])>max:
                        max=A[m,k]
                        m1=m
                        k1=k
                A[[k,m1]]=A[[m1,k]]
                B[[k, m1]] = B[[m1, k]]

        elif pivot==False:
            if A[k,k]==0:
                print("Invalid,since pivoting is disabled division by zero happens")
                exit()

        for i in range (k+1,n):
            if A[i,k]==0:
                continue
            factor=A[k,k]/A[i,k]
            for j in range(k,n):
                A[i,j]=A[k,j]-factor*A[i,j]

            B[i]=B[k]-factor*B[i]

            if(showall==True):
                print("The A matrix is: ")
                print(A)
                print("The B matrix is: ")
                print(B)

    #A[n-1,n-2]=0.000000000e+00

    #Back substitution

    t[n-1]=B[n-1]/A[n-1,n-1]

    for i in range(n-2,-1,-1):
        sum=0
        for j in range(i+1,n):
            sum=sum+A[i,j]*t[j]
        t[i]=(B[i]-sum)/A[i,i]

    for i in t:
        print("%.8f" % i)
    #print(t)

n=int(input())
X=np.zeros((n,n),dtype=float)

Y=np.zeros((n,1),dtype=float)

for i in range(n):
    x = input()
    y = x.split(" ")
    j = 0
    for k in y:
        # print(float(i))
        X[i][j] = float(k)
        j = j + 1

for i in range(n):
    x = input()
    y = x.split(" ")
    j = 0
    for k in y:
        Y[i][j] = float(k)
        j = j + 1

GaussianElimination(X,Y)
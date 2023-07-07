x=[0.698132,0.959931,1.134464,1.570796,1.919862]
y=[0.188224,0.209138,0.230052,0.250965,0.313707]

def powSum(x,m):
    sum=0
    for i in range(len(x)):
        sum+=x[i]**m
    return sum

def xyprodSum(x,y):
    sum=0
    mean=1
    for i in range(len(x)):
        sum+=x[i]*y[i]
    return sum

def linearRegression(x,y):
    a_1=(len(x)*xyprodSum(x,y)-powSum(x,1)*powSum(y,1))/(len(x)*powSum(x,2)-powSum(x,1)**2)
    a_0 = powSum(y,1)/len(y) - a_1 * powSum(x,1)/len(x)
    print(a_0)
    print(a_1)
linearRegression(x,y)

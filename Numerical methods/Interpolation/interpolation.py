import numpy as np
import math

def interpolate(a,b,x,n,s): #newton interpolate
    c=np.empty([n,n]);
    for i in range(0,n):
        c[0][i]=b[i+s];
    for i in range(1,n):
        for j in range(0,n-i):
            c[i][j]=(c[i-1][j]-c[i-1][j+1])/(a[j+s]-a[j+i+s])
            # print("%.2f" % (c[i][j]), end=' ')
        # print('')
    var=1.0
    ans=0
    for i in range (0,n):
        ans+=c[i][0]*var
        var*=(x-a[i+s])
    return ans

def linterpolate(a,b,x,n,s): #lagrange interpolate
    ans=0
    for i in range(0,n):
        g=b[i+s]
        for j in range(0,n):
            if j is not i:
                g*=(x-a[j+s])/(a[i+s]-a[j+s])
        ans+=g
    return ans

def error_cnt(x_1, x_2):
    return 100.0*(abs(x_1-x_2)/x_2)



f = open("gene.txt", "r")
h = [0,0]
a = []
b = []
for x in f:
    # print(x)
    h = x.split()
    # print(h)
    a.append(float(h[0]))
    b.append(float(h[1]))
print(a)
print(b)

print(f"taking 2 points: {interpolate(a,b,17,2,4)}")
print(f"taking 3 points: {interpolate(a,b,17,3,4)}")
print(f"taking 4 points: {interpolate(a,b,17,4,4)}")
print(f"taking 5 points: {interpolate(a,b,17,5,4)}")
print(f"error_2: {error_cnt(interpolate(a,b,17,2,4),interpolate(a,b,17,3,4))}")
print(f"error_3: {error_cnt(interpolate(a,b,17,3,4),interpolate(a,b,17,4,4))}")
print(f"error_4: {error_cnt(interpolate(a,b,17,4,4),interpolate(a,b,17,5,4))}")
print(f"taking 2 points: {interpolate(a,b,17,2,4)}")
print(f"taking 3 points: {interpolate(a,b,17,3,4)}")
print(f"taking 4 points: {interpolate(a,b,17,4,4)}")
print(f"taking 5 points: {interpolate(a,b,17,5,4)}")
print(f"error_2: {error_cnt(interpolate(a,b,17,2,4),interpolate(a,b,17,3,4))}")
print(f"error_3: {error_cnt(interpolate(a,b,17,3,4),interpolate(a,b,17,4,4))}")
print(f"error_4: {error_cnt(interpolate(a,b,17,4,4),interpolate(a,b,17,5,4))}")
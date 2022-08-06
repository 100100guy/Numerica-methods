def sums(a,b,py,px,pe,xx):
    n=len(a)
    sum=0
    for i in range(0,n):
        sum+=pow(b[i],py)*pow(a[i],px)*pow(2.71828,pe*xx*a[i])
    return sum

def bfunc(a,b,xx):
    return sums(a,b,1,1,1,xx)-(sums(a,b,1,0,1,xx)*sums(a,b,0,1,2,xx)/sums(a,b,0,0,2,xx))

def bijection(a,b):
    l=1000
    r=-1000
    while l-r>0.00000001:
        f1=bfunc(a.b,l)
        f2=bfunc(a,b,(l+r)/2)
        f3=bfunc(a,b,r)
        if f1*f2>0:
            l=(l+r)/2
        else:
            r=(l+r)/2

    return (l+r)/2
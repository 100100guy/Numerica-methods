def func(x):
    return 5*(x**3)-90*(x**2)+2376

def derivFunc(x):
    return 15*(x**2)-180*x


def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        print("The value of the root is : ",
          "%.5f" % x)


newtonRaphson(4)
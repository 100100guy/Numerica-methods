import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.21])
y = np.array([1,1.03,1.06,1.38,2.09,3.54,6.41,12.6,22.1,39.05,65.32,99.78])

plt.scatter(x, y)

# From the graph we can see that the graph has an exponential trend.so y = a(e^(bx)) or exponential model best fits the graph.
# and after transformation we get, lny = lna + bx, {a_0 = lna or a = e^a_0} , {a_1 = b}, {z=lny}


def x_i(power):  # sum of x_i**power
    sum = 0
    for i in range(x.size):
        sum = sum + x[i]**power
    return sum


def z_i():  # sum of z_i
    sum = 0
    for i in range(y.size):
        sum = sum + np.log(y[i])
    return sum


def x_i_z_i():  # sum of x_i_z_i
    sum = 0
    for i in range(x.size):
        sum = sum + x[i]*np.log(y[i])
    return sum


n = int(x_i(0))

a_1 = (n*x_i_z_i()-(x_i(1)*z_i()))/(n*x_i(2)-(x_i(1)**2))
a_0 = (z_i()/n)-(a_1*(x_i(1)/n))

print(f'a_0={a_0} and a_1={a_1}')
print(f'\n*1. So the equation is: {format(np.exp(a_0),"0.4f")}e^({format(a_1,"0.4f")}x)\n')

x_new = np.arange(0.0,0.25,0.01)
y_new = np.array(np.exp(a_0+(a_1)*x_new))

plt.plot(x_new, y_new, color = "green")
plt.xlabel('BAC')
plt.ylabel('Relative Risk of Crashing')

# 2nd Question
print(f'*2. For BAC of about 0.16 Relative Risk of Crashing: {format(np.exp(a_0 + a_1 * 0.16), "0.2f")}')

plt.show()
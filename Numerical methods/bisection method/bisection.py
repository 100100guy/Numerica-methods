import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return 5*(x**3)-90*(x**2)+2376

#Bisection method
def bisection(lower_bound, upper_bound, appx_err, max_iter):

    if (func(lower_bound) * func(upper_bound) >= 0):
        print("You have not assumed right lower bound and upper bound\n")
        return
    iter=1;

    mid = lower_bound
    while True:

        # Find middle point
        mid = (lower_bound + upper_bound) / 2
        new=mid
        if(iter!=1):

            epsilon=abs(((new-old))/new)*100
            if(epsilon<appx_err):
                break

        if(iter>max_iter):
            break
        # Check if middle point is root
        if (func(mid) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(mid) * func(upper_bound) < 0):

            lower_bound = mid
        else:
            upper_bound = mid

        old=mid
        iter+=1

    print("The value of root is : ", "%.5f" % mid," cm")

bisection(6, 7, 0.5, 100)


#Error printing
print("--------------------------------------------------")
print("Sl no.                Error ")
def bisection2(lower_bound, upper_bound):

    if (func(lower_bound) * func(upper_bound) >= 0):
        print("You have not assumed right a and b\n")
        return

    iter=0;
    mid = lower_bound

    while True:

        # Find middle point
        mid = (lower_bound + upper_bound) / 2
        new=mid

        if (iter == 0):
            print(iter,"                    No error in first iteration")

        if(iter!=0):
            epsilon=abs(((new-old))/new)*100
            if(iter>=10):
                print(iter,"                  ","%.5f"% epsilon)
            else:
                print(iter,"                   ","%.5f"% epsilon)

        if(iter>=20):
            break

        # Check if middle point is root
        if (func(mid) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(mid) * func(upper_bound) < 0):
            lower_bound = mid
        else:
            upper_bound = mid

        old=mid
        iter+=1

bisection2(6, 7)

#graph plotting
x = np.linspace(0,12,50)
y = 5*(x**3)-90*(x**2)+2376

# plot the function
plt.axhline(y=0,color='black')
plt.plot(x,y, 'r')

# show the plot
plt.show()


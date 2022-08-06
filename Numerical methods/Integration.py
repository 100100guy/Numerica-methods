import matplotlib.pyplot as plt

def T(x):
    return -(6.73*x+6.725e-8+7.26e-4*5e-4)/(3.62e-12*x+3.908e-8*x*5e-4)

def trapezoidal(a, b, n):

    h = (b - a) / n

    result = T(b) + T(a)

    for i in range(1, n):
        k = a + i * h
        result = result + 2 * T(k)

    result = result * h / 2

    return result


def simpson(a, b, n):
    n=2*n

    h = (b - a) / n

    result = T(a) + T(b)

    for i in range(1, n):
        k = a + i * h

        if i % 2 == 0:
            result = result + 2 * T(k)
        else:
            result = result + 4 * T(k)

    result = result * h / 3

    return result

def error_cnt(x_1, x_2):
    return 100.0*(abs(x_1-x_2)/x_2)

initial=1.22e-4
final=0.5*initial
print("Trapezoidal result: ")
print(f"taking 1 division:  {trapezoidal(initial,final,1)} , Error: Not Applicable ")
print(f"taking 2 divisions: {trapezoidal(initial,final,2)}  , Error:{error_cnt(trapezoidal(initial,final,1),trapezoidal(initial,final,2))}%")
print(f"taking 3 divisions: {trapezoidal(initial,final,3)} , Error:{error_cnt(trapezoidal(initial,final,2),trapezoidal(initial,final,3))}%")
print(f"taking 4 divisions: {trapezoidal(initial,final,4)} , Error:{error_cnt(trapezoidal(initial,final,3),trapezoidal(initial,final,4))}%")
print(f"taking 5 divisions: {trapezoidal(initial,final,5)} , Error:{error_cnt(trapezoidal(initial,final,4),trapezoidal(initial,final,5))}%")

print()

print("Simpson result: ")
print(f"taking 1 division:  {simpson(initial,final,1)} , Error: Not Applicable ")
print(f"taking 2 divisions: {simpson(initial,final,2)}  , Error:{error_cnt(simpson(initial,final,1),simpson(initial,final,2))}%")
print(f"taking 3 divisions: {simpson(initial,final,3)} , Error:{error_cnt(simpson(initial,final,2),simpson(initial,final,3))}%")
print(f"taking 4 divisions: {simpson(initial,final,4)} , Error:{error_cnt(simpson(initial,final,3),simpson(initial,final,4))}%")
print(f"taking 5 divisions: {simpson(initial,final,5)} , Error:{error_cnt(simpson(initial,final,4),simpson(initial,final,5))}%")

x=[0.000122, 0.00012, 0.0001, 0.00008, 0.00006, 0.00004, 0.00002]
y=[]
for i in x:
    y.append(simpson(initial,i,10))
plt.plot(x,y,marker='o',color='g')
plt.axhline(y=0,color='black')
plt.xlabel("Oxygen concentration, x (mol/cm^3)")
plt.ylabel("Time required, T(x) (seconds) ")
plt.grid()
plt.show()


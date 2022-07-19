# reference: page no: 253 & example no: 10.13

import matplotlib.pyplot as plt
import tabulate


def function(x, y):
    return x+y**2


def runge_kutta(x0, y0, xn, n):
    yn = 0
    h = (xn-x0)/n
    print(f"h=({xn}-{x0})/{n}  ={h}")
    x_val.append(x0)
    y_val.append(y0)
    for i in range(n):
        print(f"step {i+1}")
        print(f"x0= {round(x0, 4)}, y0= {round(y0, 4)}")
        k1 = h*(function(x0, y0))
        print(f"k1= {h} f({round(x0, 4)},{round(y0, 4)}) = {round(k1, 4)}")
        k2_d1 = (x0+h/2)
        k2_d2 = (y0+k1/2)
        k2 = h*(function(round(k2_d1, 5), round(k2_d2, 5)))
        print(f"k2= {h} f({round(k2_d1, 5)},{round(k2_d2, 5)}) = {h} f({k2_d1}+{k2_d2}) = {k2}")
        k3_d1 = (x0+h/2)
        k3_d2 = (y0+k2/2)
        k3 = h*(function(k3_d1, k3_d2))
        print(f"k2= {h} f({k3_d1},{k3_d2}) = {h} f({k3_d1}+{k3_d2}) = {k3}")
        k4_d1 = (x0+h)
        k4_d2 = (y0+k3)
        k4 = h*(function(k4_d1, k4_d2))
        print(f"k2= {h} f({k4_d1},{k4_d2}) = {h} f({k4_d1}+{k4_d2}) = {k4}")

        k = (k1+(2*k2)+(2*k3)+k4)/6
        print(f"k= ({k1}+2*{k2}+2*{k3}+k4) = {k}")
        yn = y0+k
        print(f"y{i+1}= ({y0} + {k}) = {yn}")
        y0 = yn
        x0 = x0+h

        print("\n\n")
        x_val.append(x0)
        y_val.append(y0)
    Data.append(x_val)
    Data.append(y_val)
    print(tabulate.tabulate(Data, tablefmt='fancy_grid'))
    print("x= %.4f, y= %.4f" % (xn, yn))


x_val = []
y_val = []
yn_val = []
Data = []
print("Initial Condition: ")
x0 = float(input("x0: "))
y0 = float(input("y0: "))
print("Calculation point: ")
xn = float(input("xn: "))
print("Interval number: ")
n = int(input("interval: "))
runge_kutta(x0, y0, xn, n)
plt.style.use('ggplot')
plt.title('Runge Kutta Method')
plt.plot(x_val, y_val, color='green', marker='o',
         linewidth=1, markersize=4, label='y value')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()

"""
    x0: 0
    y0: 1
    xN: 0.2
    interval: 4
"""

# repolish this one!

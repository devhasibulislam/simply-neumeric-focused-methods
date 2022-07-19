# reference: page no: 253 & example no: 10.13

import numpy, tabulate as tbl

def runge_kutta_order1(y, h, fxy):
    return round((y + (h * fxy)), 4)

# def f_xy(y):
def f_xy(x, y):
    # return round((1 - y), 4)
    return round((x + (y**2)), 4)

def findXvalue(x, i, h):
    return round((x + (i * h)), 4)

def findHvalue(xN, x0, n):
    return round(((xN - x0) / n), 4)

x0 = float(input("Enter value for x0: "))
y0 = float(input("Enter value for y0: "))
xN = float(input("Enter value for xN: "))
n = int(input("Intervals: "))
x = numpy.zeros(n + 1)
y = numpy.zeros(n + 1)
h = findHvalue(xN, x0, n)
x[0] = x0
y[0] = y0

print()

# value of x:
for i in range(1, n + 1, 1):
    x[i] = findXvalue(x[0], i, h)
    print(f"x[{i}] = {x[0]} + ({i} * {h}) = {x[i]}")

print()

# value of y:
for i in range(1, n + 1, 1):
    # y[i] = euler_method(y[i - 1], h, f_xy(y[i - 1]))
    y[i] = runge_kutta_order1(y[i - 1], h, f_xy(x[i - 1], y[i - 1]))
    print(f"y{i} = y(x{i}) = {round(y[i - 1], 4)} + ({h} * (-{x[i - 1]} * {round(y[i - 1], 4)}^2)) = {round(y[i], 4)}")

# keep x & y in a table
print()
data = [x, y]
print(tbl.tabulate(data,tablefmt="fancy_grid"))

print(f"y({xN}): {round(y[n], 4)}")

"""
    x0: 0
    y0: 1
    xN: 0.2
    n: 4
"""

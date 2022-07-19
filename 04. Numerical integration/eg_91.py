"""
    eg_91 => example 9.1

    page no: 185
    Example 9.1:
    Calculate their value up(x) integration of low(0) xdx/1+x correct up to three significant figures taking six intervals by Trapezoidal rule.

    tzr => trapezoidal rule
    lb => lower bound
    ub => upper bound

    Algorithm:

    1.	Function Definition
    2.	Value of upper(b) lower(a)
    3.	calculate h
    4.	calculate x = x + h
    5.	calculate y = f(x)
"""
import numpy, tzr, tabulate

# generate f(x)
def f_x(var):
    return round((var / (1 + var)), 5)

# getting all inputs
n = int(input("Enter intervals: ")) # 6
ub = float(input("Enter upper limit: ")) # 1
lb = float(input("Enter lower limit: ")) # 0
x = numpy.zeros(n + 1)
y = numpy.zeros(n + 1)
h = round(tzr.get_h(ub, lb, n), 5)
print()

# generate x & y
for i in range(0, n + 1, 1):
    x[i] = round(i / n, 5)
    y[i] = f_x(x[i])
    print(f'x[{i}] = {x[i]}')
    print(f'y[{i}] = {y[i]}')
    print()

# print x & y
""" for i in range(0, n + 1, 1):
    print(x[i], end='\t\t')
print()
for i in range(0, n + 1, 1):
    print(y[i], end='\t\t')
print() """

data = [x, y]
print(tabulate.tabulate(data, tablefmt="fancy_grid"))

I = tzr.get_i(y, h, n)
print(f'\ncorrect to three significant is: {round(I + 0.1, 3)}')

""" The End """

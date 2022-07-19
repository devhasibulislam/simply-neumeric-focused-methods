"""
    eg_93 => example 9.3

    page no: 185
    Example 9.3:
    Calculate their value up(5) integration of low(1) log10Xdx correct up to five significant figures taking eight intervals by Trapezoidal rule.

    tzr => trapezoidal rule
    lb => lower bound
    ub => upper bound

    Algorithm:

    1.	Function Definition
    2.	Value of upper(b) lower(a)
    3.	calculate h
    4.	calculate x = x+h
    5.	calculate y = f(x)
"""
import numpy, tzr, math

# generate f(x)
def f_x(var):
    return round((math.log10(var)), 5)

# getting all inputs
n = int(input("Enter intervals: ")) # 8
ub = float(input("Enter upper limit: ")) # 5
lb = float(input("Enter lower limit: ")) # 1
x = numpy.zeros(n + 1)
y = numpy.zeros(n + 1)
h = round(tzr.get_h(ub, lb, n), 5)
print()

# generate x & y
x[0] = 1.0
for i in range(1, n + 1, 1):
    x[i] = round(x[i - 1] + 0.5, 4)
    y[i] = f_x(x[i])
    print(f'x[{i}] = {x[i]}')
    print(f'y[{i}] = {y[i]}')
    print()

# print x & y
for i in range(0, n + 1, 1):
    print(x[i], end='\t\t')
print()
for i in range(0, n + 1, 1):
    print(y[i], end='\t\t')
print()

I = tzr.get_i(y, h, n)
print(f'\ncorrect to three significant is: {round(I + 0.1, 4)}')

""" The End """

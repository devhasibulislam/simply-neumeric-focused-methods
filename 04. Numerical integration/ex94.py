""" 
example 9.4, page no: 203
simpson's one-third rule
"""
import numpy, math, tabulate
import simpson13rule, get_h

def f_x(var):
    return round((math.exp(var)), 5)

n = int(input("interval is: "))
ub = float(input("upper bound is: "))
lb = float(input("lower bound is: "))
h = get_h.value_of_h(ub, lb, n)
x = numpy.zeros(n + 1)
y = numpy.zeros(n + 1)

x[0] = 0.0
y[0] = f_x(x[0])
for i in range(1, n + 1, 1):
    x[i] = x[i - 1] + h
    y[i] = f_x(x[i])

data = [x, y]
print(tabulate.tabulate(data, tablefmt='fancy_grid'))
print(f"I = {simpson13rule.value_of_i(y, n, h)}")

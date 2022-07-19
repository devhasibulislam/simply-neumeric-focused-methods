""" 
example 9.7, page no: 205
simpson's thiree-eight rule
"""
import numpy, tabulate
import simpson38rule, get_h

def f_x(var):
    return round((1 / (1 + var**2)), 5)

n = int(input("interval is: "))
ub = float(input("upper bound is: "))
lb = float(input("lower bound is: "))
h = get_h.value_of_h(ub, lb, n)
x = numpy.zeros(n)
y = numpy.zeros(n)

# x[0] = 0.0
# y[0] = f_x(x[0])
for i in range(0, n, 1):
    x[i] = i / 6
    y[i] = f_x(x[i])

data = [x, y]
print(tabulate.tabulate(data, tablefmt='fancy_grid'))
print(f"I = {simpson38rule.value_of_i(y, n, h)}")

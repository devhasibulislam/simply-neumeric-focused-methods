# reference: page no: 253 & example no: 10.13

import numpy as np

def f_xy(x, y):
    return round(((3 * x) + (y**2)), 4)

x0 = float(input("Enter value for x0: "))
y0 = float(input("Enter value for y0: "))
xN = float(input("Enter value for xN: "))
h = float(input("Enter value for h: "))
# h = 1 - xN
n = int(input("Intervals: "))
# n = 1
x = np.zeros(n + 1)
y = np.zeros(n + 1)
x[0] = x0
y[0] = y0

k1 = k2 = 0
k1 = round(h * f_xy(x[0], y[0]), 5)
k2 = round(h * f_xy(x[0] + h, y[0] + k1), 5)
y[1] = y[0] + (1/2) * (k1 + k2)

print(f"\nk1: {h} * f({x[0]}),({y[0]})")
print(f"k2: {h} * f({x[0]} + )")
print(f"runge kutta order 2: {y[0]} + 1/2 * ({k1} + {k2}) = {y[1]}")
print(f"\ny({xN}): {y[1]}")

"""
    x0: 1
    y0: 1.2
    xN: 1.1
    h: 0.1 (1 - xN) -> 1 or xN greater stay first.
    interval: 1
"""

# reference: page no:253 & example no: 10.13

import numpy as np

def dydx(x, y):
    return round((y**2 - x**2) / (y**2 + x**2), 4)

x0 = float(input("Enter value for x0: "))
y0 = float(input("Enter value for y0: "))
xN = float(input("Enter value for xN: "))
h = float(input("Enter value for h: "))
n = int(input("interval: "))
x = np.zeros(n + 1)
y = np.zeros(n + 1)
x[0] = x0
y[0] = y0
k1 = k2 = k3 = k4 = 0
print()

# value of x:
for i in range(1, n + 1, 1):
    x[i] = x[i - 1] + h
    print(f"x[{i}] = {x[i - 1]} + {h} = {x[i]}")
    y[i] = x[i]
print()

# value of k:
for i in range(1, n + 1, 1):
    print(f"iteration {i}:")
    k1 = round(h * dydx(x[i - 1], y[i - 1]), 4)
    print(f"k1 = {h} * f({x[i - 1]}, {y[i - 1]}) = {k1}")

    k2 = round(h * dydx(x[i - 1] + (h / 2), y[i - 1] + (k1 / 2)), 4)
    print(f"k2 = {h} * f({x[i - 1]} + {h / 2}, {y[i - 1]} + {k1 / 2}) = {k2}")

    k3 = round(h * dydx(x[i - 1] + (h / 2), y[i - 1] + (k2 / 2)), 4)
    print(f"k3 = {h} * f({x[i - 1]} + {h / 2}, {y[i - 1]} + {k2 / 2}) = {k3}")

    k4 = round(h * dydx(x[i - 1] + h, y[i - 1] + k3), 4)
    print(f"k4 = {h} * f({x[i - 1]} + {h}, {y[i - 1]} + {k3}) = {k4}")
    
    y[i] = round(y[i - 1] + ((1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)), 4)
    print()
print()

# dy = round(((1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)), 4)
# print(f"{round(1 / 6, 4)} * [{k1} + {2 * k2} + {2 * k3} + {k4}] = {dy}")
dy = y[n]
print(f"y({xN}): {dy}")

"""
    x0: 0
    y0: 1
    xN: 0.4
    h: 0.2 (changeable to 0.1)
    n: 2
"""

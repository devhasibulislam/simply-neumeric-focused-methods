# ode => ordinary differenctial equation
# page no: 231
# ode10_2 => example: 10.2

import numpy as np
from scipy.integrate import odeint
import tabulate as tbl

func = lambda y, x: 1 + (x * y)

y0 = 1
x = np.arange(0, 0.2, 0.1)  # parameter: start, stop, interval
y = odeint(func, y0, x)
data = [x, y]
# print(x, '\n', y)
print(tbl.tabulate(data, tablefmt="fancy_grid"))

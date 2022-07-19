# ode => ordinary differenctial equation
# page no: 230
# ode10_1 => example: 10.1

import numpy as np
from scipy.integrate import odeint
import tabulate as tbl

func = lambda y, x: x + y

y0 = 0
x = np.arange(1, 1.2, 0.1)  # parameter: start, stop, interval
y = odeint(func, y0, x)
data = [x, y]
# print(x, '\n', y)
print(tbl.tabulate(data, tablefmt="fancy_grid"))

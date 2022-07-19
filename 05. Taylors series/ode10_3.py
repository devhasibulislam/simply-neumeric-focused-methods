# ode => ordinary differenctial equation
# page no: 233
# ode10_3 => example: 10.3

import numpy as np
from scipy.integrate import odeint
import tabulate as tbl

func = lambda y, x: (x * y)**(1 / 3)

y0 = 1
x = np.arange(1, 1.3, 0.1)  # parameter: start, stop, interval
y = odeint(func, y0, x)
data = [x, y]
# print(x, '\n', y)
print(tbl.tabulate(data, tablefmt="fancy_grid"))

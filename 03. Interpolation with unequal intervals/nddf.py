""" nddf => newton's divided difference formula """

import ddt

var = float(input("\nInput evaluative number: "))

summation = 0
multiplication = 1
array_multiplication = 1

# creating rule type of this:
# f(X0) + (X - X0) * f(X0, X1) + (X - X0) * (X - X1) * f(X0, X1, X2) + ...
for i in range(0, 5, 1):
    if i != 0:
        multiplication *= (var - ddt.x[i - 1])
        array_multiplication = multiplication * ddt.y[0][i]
        summation += array_multiplication

    else: summation += ddt.y[0][i]

print(f"f({var}): {summation}")

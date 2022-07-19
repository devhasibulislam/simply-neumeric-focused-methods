""" lif => Lagrange's interpolation formula """
""" example: 5.6 & page no: 125 """

import numpy

n = int(input("Enter range: "))
var = float(input("Corresponding value is: "))
x = numpy.zeros(n)
y = numpy.zeros(n)
numerator = 1
denominator = 1
f_x = 0

# enter values for x:
for i in range(0, n, 1):
    x[i] = float(input(f'x[{i}]: '))

print()

# enter values for y:
for i in range(0, n, 1):
    y[i] = float(input(f'y[{i}]: '))

print()

# generating Lagrange's interpolation formula
for i in range(0, n, 1):
    print(f"iteration {i}:")
    for j in range(0, n, 1):
        if j == i:
            continue
        elif j != i:
            numerator *= (var - x[j])
            denominator *= (x[i] - x[j])
    f_x += ((numerator / denominator) * y[i])
    print(f"{numerator} / {denominator} * {y[i]} = {round(f_x, 2)}")
    numerator = 1
    denominator = 1

# the result is:
print(f"f({var}) is: {round(f_x, 2)}")
print()

"""
    case 1: 
        first input:4
        second input: 10

        x[0] = 5
        x[1] = 6
        x[2] = 9
        x[3] = 11

        y[0] = 12
        y[1] = 13
        y[2] = 14
        y[3] = 16
    output: 14.67
"""

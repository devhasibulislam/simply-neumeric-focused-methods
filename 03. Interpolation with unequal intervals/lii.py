""" lii => Lagrange's inverse interpolation """
""" example: 5.7, 5.8, 5.9 & page no: 127 """

import numpy

n = int(input("Enter range: "))
var = float(input("Corresponding value is: "))
x = numpy.zeros(n)
y = numpy.zeros(n)
numerator = 1
denominator = 1
f_y = 0

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
    for j in range(0, n, 1):
        if j == i:
            continue
        elif j != i:
            numerator *= (var - y[j])
            denominator *= (y[i] - y[j])
    f_y += ((numerator / denominator) * x[i])
    numerator = 1
    denominator = 1

# the result is:
print(f"f({var}) is: {round(f_y, 2)}")
print()

"""
    case 1:
        first input: 3
        second input: 0.3887

        x[0] = 21
        x[1] = 23
        x[2] = 25

        y[0] = 0.3706
        y[1] = 0.4068
        y[2] = 0.4433
    output: 22

    case 2:
        first input: 3
        second input: 0.3

        x[0]: 0.4
        x[1]: 0.6
        x[2]: 0.8

        y[0]: 0.3683
        y[1]: 0.3332
        y[2]: 0.2897
    output: 0.76
"""

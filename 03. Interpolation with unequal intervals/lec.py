# lec => lagrange error count
# (f^(n + 1) (estimation(x)) * (x - x0) * (x - x1) * (x - x2) * ... * (x - x(N - 1))) / (n + 1)!
# https://www.youtube.com/watch?v=RG5mTXLB9iA&t=86s

import numpy, math

def error(var, x, n):
    subMul = 1 # subtract multiplication
    for i in range(0, n, 1):
        subMul *= (var - x[i])
    
    subMul *= n + 1
    subMul /= (math.factorial(n + 1))

    print(abs(subMul))


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
    for j in range(0, n, 1):
        if j == i:
            continue
        elif j != i:
            numerator *= (var - x[j])
            denominator *= (x[i] - x[j])
    f_x += ((numerator / denominator) * y[i])
    numerator = 1
    denominator = 1

# the result is:
print(f"f({var}) is: {round(f_x, 2)}")
print()

# error at
error(var, x, n)

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
    output: 14.67 & 0.8333333333333334
"""

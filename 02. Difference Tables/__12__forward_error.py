import math
import numpy


def f_y(var):
    return round(math.sin(math.radians(var)), 4)

def forward_error(y, i, j):
    y[j][i] = round(y[j + 1][i - 1] - y[j][i - 1], 4)

def newtons__formula(y, u, size):
    temp = 0
    var = 0
    for i in range(size):
        if i == 0:
            temp += y[0][i]
        elif i == 1:
            var = (u * y[0][i])
            temp += var
            var = 0
        else:
            for j in range(1, i):
                var *= u - j
            var *= u
            var /= fact(i)
            var *= y[i][0]
            temp += var
            var = 0
    return round(temp, 7)

def fact(var):
    temp = 1
    for i in range(1, var + 1):
        temp *= i
    return temp

def forward__error(u, index, y):
    var = 1
    for i in range(1, index + 1):
        var *= (u - i)
    var *= u
    var /= fact(index + 1)
    var *= y
    return var

size = int(input("enter size: "))
x = numpy.zeros(size)
y = numpy.zeros((size, size))

for i in range(size):
    x[i] = float(input(f"x[{i}]: "))
    y[i][0] = f_y(x[i])
    print(f"y[{i}][0]: {format(y[i][0], '.4f')}")

# generate the forward difference table
for i in range(1, size):
    for j in range(0, size - i):
        forward_error(y, i, j)
print()

# print the forward difference table
for i in range(0, size):
    print(x[i], end='\t')
    for j in range(0, size - i):
        print(y[i][j], end='\t')
    print()
print()

# Newton's formula
x1 = float(input("X1: "))
# index = float(input("index: "))
index = 0
for i in range(0, size):
    if x1 < x[i]:
        index = i
        break
print(f"Index is: {index}")
u = (x1 - x[0]) / 5

print(f"Result for sin{x1} degree is: {newtons__formula(y, u, size)}")
temp = f"{forward__error(u, int(index), y[0][3]):.7f}"
print(f"By taking {index} for {x1} degrees position and getting off the error is: {temp}")

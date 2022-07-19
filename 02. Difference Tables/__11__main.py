import numpy
import math

# Evaluate y = e^2x for x = 0.05 using the following table:
# x = 0.00 -> y = 1.00
# x = 0.10 -> y = 1.2214
# x = 0.20 -> y = 1.4918
# x = 0.30 -> y = 1.8221
# x = 0.40 -> y = 2.255

# user defined function is here:
# function that take value of x and give value for y
def f_y(x):
    return round(float(math.exp(2 * x)), 4)

def forward_difference(y, i, j):
    y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

def backward_difference(y, i, j):
    y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

# main function starts here:
size = int(input("Enter size of your array: "))

x = numpy.zeros(size)
y = numpy.zeros((size, size))

# array inputs from user:
for i in range(size):
    x[i] = float(input(f"x[{i}]: "))
    y[i][0] = f_y(x[i])
    print(f"y[{i}][0]: {y[i][0]}")

# backward difference table
for i in range(1, size):
    k = i - 2
    for j in range(size - 1, k, -1):
        if j == i - 1:
            continue
        backward_difference(y, i, j)

# print it
print("Backward difference table is: ")
print("x\t\ty=e^2x\t\td_y\t\t\td^2_y\t\td^3_y\t\td^4_y")
print("---\t\t------\t\t------\t\t------\t\t------\t\t------")
for i in range(0, size):
    print(f"{x[i]}", end='\t\t')
    for j in range(0, i + 1):
        print(f"{format(round(y[j][i], 4), '.4f')}", end='\t\t')
    print()

# print()

# forward difference table:
# for i in range(1, size):
#     for j in range(0, size - i):
#         forward_difference(y, i, j)

# print it
# print("Forward difference table is: ")
# print("x\t\ty=e^2x\t\td_y\t\t\td^2_y\t\td^3_y\t\td^4_y")
# print("---\t\t------\t\t------\t\t------\t\t------\t\t------")
# for i in range(0, size):
#     print(f"{x[i]}", end='\t\t')
#     for j in range(0, size - i):
#         print(f"{format(round(y[i][j], 4), '.4f')}", end='\t\t')
#     print()

# print()

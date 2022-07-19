import numpy


def backward_error(y, i, j):
    y[j][i] = f"{(y[j][i - 1] - y[j - 1][i - 1]):.5f}"


size = int(input("enter size: "))
x = numpy.zeros(size)
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = numpy.zeros((size, size))

for i in range(size):
    x[i] = float(input(f"x[{i}]: "))
    y[i][0] = float(input(f"y[{i}][0]: "))

# generate the backward difference table
for i in range(1, size):
    k = i - 2
    for j in range(size - 1, k, -1):
        if j == i - 1:
            continue
        backward_error(y, i, j)

# print the backward difference table
print("\nBackward difference table: ")
for i in range(0, size):
    print(x[i], end='\t')
    for j in range(0, i + 1):
        print(y[i][j], end='\t')
    print()
print()

# input: 0.15
var = float(input("Function value is: "))

s = round((var - x[size - 1]) / x[0], 2)
# print(s)

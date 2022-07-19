""" fshm1 => for sabbir hassan mithu 1st file """

import numpy

n = int(input("Enter index: "))
print()

x = numpy.zeros(n)
y = numpy.zeros((n, n))

# user input for value: x
for i in range(0, n):
    x[i] = float(input(f"x[{i}]: "))

print()

# user input for value: y
for i in range(0, n):
    y[i][0] = float(input(f"y[{i}][0]: "))

# generate difference table
k = 0
for i in range(1, n):
    k = i
    for j in range(0, n - i):
        y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[k]))
        k += 1
        if y[j][i] == -0.0:
            y[j][i] = 0.0

print()

# print table
for i in range(0, n):
    print(f"{round(x[i], 4)}", end='\t\t')
    for j in range(0, n - i):
        print(f"{round(y[i][j], 4)}", end='\t\t')
    print()

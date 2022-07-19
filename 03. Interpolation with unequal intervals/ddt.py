""" ddt => divided difference table """
""" Example: 5.2, 5.3 & 5.4 & Page no: 117, 121 & 122 """

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
# dummy variable to reach control for x
k = 0
for i in range(1, n):
    k = i
    for j in range(0, n - i):
        y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[k]))
        k += 1
        # while output got negative zero
        if y[j][i] == -0.0:
            y[j][i] = 0.0

print()

# print table
for i in range(0, n):
    print(f"{round(x[i], 4)}", end='\t\t')
    for j in range(0, n - i):
        print(f"{round(y[i][j], 4)}", end='\t\t')
    print()

""" 
    case 1: 5
    x: 1 3 4 6 10
    y: 0 18 58 190 920

    case 2: 5
    5 7 11 13 21
    150 392 1452 2366 9702

    evaluate: 6
    output: 252

    case 3: 4
    0 1 2 5
    2 3 12 147

    case 4: 6
    x: 4 5 7 10 11 12
    y: 48 100 294 900 1210 2028

    evaluate: 8
    output: 448
"""

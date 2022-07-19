import numpy


# function that take value of x and give value for y
# def f_y(var):
#     return round(float(math.exp(2 * var)), 4)


# size for my array:
# size = int(input('Enter number of data points: '))
size = 5

x = numpy.zeros(size)
y = numpy.zeros((size, size))

# x = [100, 150, 200, 250, 300, 350, 400]
x = [19.5, 39.5, 59.5, 79.5, 99.5]
y[0][0] = 41.0
y[1][0] = 103.0
y[2][0] = 168.0
y[3][0] = 218.0
y[4][0] = 235.0

# input portion:
# print('Enter data for x and y: ')
# for i in range(size):
    # x[i] = float(input(f'x[{i}]: '))
    # y[i][0] = float(input('y[' + str(i) + ']: '))
    # y[i][0] = f_y(x[i])
    # print(f"y[{i}][0]: {y[i][0]}")

# Forward difference table portion:
for i in range(1, size):
    for j in range(0, size - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Forward difference table printing:
print('\nFORWARD DIFFERENCE TABLE\n')

for i in range(0, size):
    print(round(x[i], 4), end='')
    for j in range(0, size - i):
        print('\t\t   %0.4f' % (y[i][j]), end='')
    print()

# Backward difference table portion:
for i in range(1, size):
    for j in range(size - 1, i - 2, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

# Backward difference table printing:
print('\nBACKWARD DIFFERENCE TABLE\n')

for i in range(0, size):
    print(round(x[i], 4), end='')
    for j in range(0, i + 1):
        print('\t\t   %0.4f' % (y[i][j]), end='')
    print()

"""
x[0]: 19.5
y[0][0]:41
x[1]: 39.5
y[1][0]:103 
x[2]: 59.5
y[2][0]:168
x[3]: 79.5
y[3][0]:218
x[4]: 99.5
y[4][0]:235
"""

import __11__main

def f_u(u, size):
    temp = u
    for i in range(1, size):
        temp *= (u - i)
    return temp

def factorial(var):
    temp = 1
    for i in range(1, var + 1):
        temp *= i
    return temp

def newton_forward_difference(y, size, u):
    sum = y[0][0]
    for i in range(1, size):
        sum += ((f_u(u, i)) * y[0][i]) / factorial(i)
    return sum

def newton_backward_difference(y, size, u):
    sum = y[0][0]
    for i in range(1, size):
        sum += ((f_u(u, i)) * y[size - 1][i]) / factorial(i)
    return sum

x = float(input("Enter given value for X: "))
u = (x - __11__main.x[0]) / (__11__main.x[1] - __11__main.x[0])


# newton backward difference
print("Result for newton backward difference interpolation: ", end='')
print(round(newton_backward_difference(__11__main.y, __11__main.size, u), 6))

# newton forward difference
# print("Result for newton forward difference interpolation: ", end='')
# print(round(newton_forward_difference(main.y, main.size, u), 6))

# print()

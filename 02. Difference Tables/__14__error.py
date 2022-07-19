import __13__backward_error


def s_addition(s, var):
    temp = 1
    for i in range(1, var):
        temp *= (s + i)
    return temp * s


def fact(var):
    temp = 1
    for i in range(1, var + 1):
        temp *= i
    return temp


def error_approximation(s, size):
    var = 1
    for i in range(1, size):
        var *= (s + i)
    var *= s
    var /= fact(size)
    return var


# last values from array
temp = 0
for i in range(0, __13__backward_error.size):
    var = 1
    if i == 0:
        temp += __13__backward_error.y[__13__backward_error.size - 1][i]
    elif i == 1:
        temp += ((__13__backward_error.y[__13__backward_error.size - 1][i]) * __13__backward_error.s)
    else:
        var *= ((s_addition(__13__backward_error.s, i)) / fact(i))
        var *= __13__backward_error.y[__13__backward_error.size - 1][i]
        temp += var
        var = 1
print(round(temp, 5))

print(round(error_approximation(__13__backward_error.s, __13__backward_error.size), 7))

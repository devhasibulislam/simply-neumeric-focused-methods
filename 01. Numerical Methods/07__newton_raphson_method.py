# let's solve: x^3 - x - 1 = 0 with newton raphson method
# essential hints are:
# f(x) = x^3 - x - 1
# f'(x) = 3x^2 - 1
# ==> input: a = 1, b = 2
# but we give the precise input => 2
# formula --> Xn+1 = (Xn - f(Xn)) / f'(Xn)
# formula that been created from above heading => Xn+1 = (((2 * (Xn**3) + 1)) / ((3 * (Xn**2) - 1)))

def newton_raphson_method(var):
    return round((((2 * (var**3) + 1) / (3 * (var**2) - 1))), 3)

var = float(input("Enter value for var: "))
x_n1 = x_n = var
iteration = 1

while True:
    print(f"{iteration}. f(x) is: {x_n} and", end=' ')

    x_n = x_n1
    x_n1 = newton_raphson_method(x_n)

    print(f"f'(x) is: {x_n1}")

    if x_n == x_n1:
        print("\n")
        print(f"Positive root of x^3 - x - 1 is: {x_n}")
        break

    iteration += 1

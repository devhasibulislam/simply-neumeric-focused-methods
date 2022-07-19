def f_u(x_0, x, h):
    return (x - x_0) / h

x_0 = float(input("Enter evaluated value for X0: "))
x = float(input("Enter given value for X: "))
h = float(input("Enter difference for each occurence, h: "))
u = f_u(x_0, x, h)
print(u)

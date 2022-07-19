# page no: 231
# ie10_2 => example: 10.2

def f(x,y):
    return (1 + (x * y))

def euler(x0, y, n):
    for i in range(n):
        y = y+h*f(x0,y)
        x0 = x0+h
    print(y)

        


x0 = float(input("the value of x0: "))
y0 = float(input("the value of y0: "))
# xn = float(input("the value of xn: "))
h = float(input("the value of h: "))
n = int(input("number of steps: "))

euler(x0, y0, n)

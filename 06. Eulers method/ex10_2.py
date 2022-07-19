# page no: 231
# ex10_1 => example: 10.2

def func(x, y):
    return (1 + (x * y))

def euler_method(x0, y0, xN, n):
    h = 1
    h = (xN - x0) / h
    yN = 0
    for i in range(n):
        s = func(x0, y0)
        yN = y0 + h * s
        print(f"{round(x0, 3)}\t{round(y0, 3)}\t{round(s, 3)}\t{round(yN, 3)}")
        y0 = yN
        x0 = x0 + h
    print(f"\nAt x: {round(xN, 3)} & y: {round(yN, 3)}")

print("Initial condition:")
x0 = float(input("x0: "))
y0 = float(input("y0: "))
print("Calculation point, ", end='')
xN = float(input("xN: "))
n = int(input("interval: "))
print("\nSteps:")
euler_method(x0, y0, xN, n)

""" 
0
1
0.1
1
"""

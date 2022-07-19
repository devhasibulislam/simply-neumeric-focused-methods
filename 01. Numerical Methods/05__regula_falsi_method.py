# Solve the equation x^3-9x+1=0 for the root lying between 2 and 3, correct to three significant figures
# =======================================================================================================>

# function segment:
# ----------------->
def function_of_var(var):
    return ((var**3) - (9 * var) + 1)

def regula_falsi_formula(a, b, f_a, f_b):
    return (a - (((f_a) / (f_b - f_a)) * (b - a)))

# main code segment:
# ------------------>
# ===> enter as input 2 & 3
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

c = f_c = root = 0

f_a = function_of_var(a)
f_b = function_of_var(b)

print(f"Function of f(a): {round(f_a, 4)} & f(b): {round(f_b, 4)} ")

while True:
    c = round(regula_falsi_formula(a, b, f_a, f_b), 4)
    print(f"Value for instance root: {c} ")

    f_c = round(function_of_var(c), 4)
    print(f"Function of root is f(root): {f_c} ")

    if root == c:
        print(f"Finally root is: {root} ")
        break

    if f_c < 0:
        a = c
        f_a = f_c
        root = c

    if f_c > 0:
        b = c
        f_b = f_c
        root = c

    print("\n")

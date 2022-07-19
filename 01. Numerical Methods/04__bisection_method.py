# Solve the equation x^3 + x^2 - 1 = 0 for the root lying between 0 and 1, correct to three significant figures
# ============================================================================================================>

# user defined function segment
# ----------------------------->
def intro():
    print("\n")
    print("Name: Hasibul Islam")
    print("ID: 1935202062")
    print("\n")

def function_of_var(var):
    return ((var**3) + (var**2) - 1)


def function_of_C(a, b):
    return ((a + b) / 2)


# main executive segment
# ---------------------->
intro()

# === |> enter as input 0 & 1
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

print(f"a: {a} ")
print(f"b: {b} ")

f_a = round(function_of_var(a), 5)
f_b = round(function_of_var(b), 5)

c = f_c = root = 0

print(f"f(a): {f_a} ")
print(f"f(b): {f_b} ")

while True:
    c = round(function_of_C(a, b), 5)
    print(f"c: {c} ")

    f_c = round(function_of_var(c), 5)
    print(f"f(c): {f_c} ")

    if root == c:
        print("\n")
        print(f"The root of (x^3+x^2-1=0) is: {round(root, 5)} ")
        break

    # now check f(c) is negative of not
    # condition: if negative then replace with a else b
    if f_c < 0:
        a = c
        f_a = f_c
        print(f"a: {a} ")
        print(f"f(a): {f_a} ")
        print(f"b: {b} ")
        print(f"f(b): {f_b} ")
        root = c

    elif f_c > 0:
        b = c
        f_b = f_c
        print(f"a: {a} ")
        print(f"f(a): {f_a} ")
        print(f"b: {b} ")
        print(f"f(b): {f_b} ")
        root = c

    print("\n")

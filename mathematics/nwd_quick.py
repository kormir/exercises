"""
Program find greatest common divisor of two numbers a and b
"""
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
print(f"Obliczam NWD({a} ,{b})...")


def nwd(x: int, y: int) -> int:
    c = 0
    while y != 0:
        c = x % y
        x = y
        y = c
    return x


print(f"NWD({a}, {b}) = {nwd(x=a, y=b)}")

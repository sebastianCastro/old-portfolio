import math
print("下面开始解方程:")
print()
print("ax²+bx+c=0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
discriminant = (pow(b, 2) - (4*(a*c)))
if discriminant > 0:
    print("这个方程有两个解:")
    quadraticFormulaX1 = b.__neg__() + math.sqrt(discriminant)
    x1 = quadraticFormulaX1 / (2*a)
    quadraticFormulaX2 = b.__neg__() - math.sqrt(discriminant)
    x2 = quadraticFormulaX2 / (2*a)
    print(f"{x1} & {x2}")
elif discriminant == 0:
    print("这个方程有一个解:")
    x3 = b.__neg__() / (2*a)
    print(x3)
else:
    print("这个方程没有解")

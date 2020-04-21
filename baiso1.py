"""Bài 1. Lập chương trình thực hiện công việc sau:
    Nhập ba số a, b, c bất kì từ bàn phím
    Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Kể cả trường hợp a=0)
"""

import math

print("enter a,b,c for quadratic equation: ax^2 +bx +c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("This is not quadratic equations!!")
    print('The quadratic equations has solution is: x={}'.format(-c/b))
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        print("Frist solution is: x1 = ",((-b + sqrt(delta))/ 2*a) )
        print("Secon solution is: x2 = ", ((-b - sqrt(delta))/ 2*a))
    elif delta == 0:
        print("The quadratic equation has 01 solution is: x = ", -b/2*a)
    else:
        print("Equations not solution!!!!")

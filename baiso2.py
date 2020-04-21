"""Bài 2. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    S_3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
    Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím
"""

import math
n = int(input("Exponent n =  "))
x = float(input("enter x = "))

s1 = 0
s2 = 0
s3 = 0

if n > 0:
    for i in range(0, n + 1):
        s1 += x**i
        s2 -= x**i
        s3 += x**i / math.factorial(i)
else:
     print("Please enter n > 0!!!")

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)


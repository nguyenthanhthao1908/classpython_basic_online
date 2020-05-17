"""Bài 11: Cho dãy số Fibonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
    + Hàm Đệ quy
    + Hàm Không đệ quy
"""
def fibonacci_DQ(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    elif n > 3:
        return fibonacci_DQ(n-1) + fibonacci_DQ(n-2) + fibonacci_DQ(n-3)
def fibonacci_KDQ(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    else:
        F1 = 1
        F2 = 1
        F3 = 2
        Fn = 0
        while n > 3:
            Fn = F1 + F2 + F3
            F1 = F2
            F2 = F3
            F3 = Fn
            n -= 1
        return Fn
print(fibonacci_DQ(10))
print(fibonacci_KDQ(10))
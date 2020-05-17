"""Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
"""
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True
    return False
print(is_prime(7))


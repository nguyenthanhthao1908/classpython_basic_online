"""Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào"""

def find_min_max(*numbers):
    print("Min numbers:", min(*numbers))
    print("Max numbers:", max(*numbers))
print(find_min_max(56, 78, 8, 10, 200, -56, 1))
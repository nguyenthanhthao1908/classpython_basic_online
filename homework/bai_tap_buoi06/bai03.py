"""Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
"""
D1 = {1: 30, 2: 20, 3: 8, 4: 30, 5: 55, 6: 8}
D2 = {}

for key, value in D1.items():       #key, value trong danh sách tuple key, value
    if value not in D2.values():    #nếu value không có trong danh sach ptu của D2 thì:
        D2[key] = value             #key của D2 = (value) lấy từ D1
print(D2)
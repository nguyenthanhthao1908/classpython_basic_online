"""
Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
"""
D1 = {23: 19, 4: 99, 5: 5, 7: 8, 56: 200, 9: 5, 0: 85.5}
D2 = list(D1.values())
D2.sort(reverse=True)
print(D2[:3])

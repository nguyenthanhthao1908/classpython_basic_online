"""Bài 04:
 Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
"""

D1 = {23: 19, 4: 99, 5: 5, 7: 8, 56: 200, 9: 5, 0: 85.5}
D2 = list(D1.keys())
D2.sort(reverse=True)
print(D2[:3])

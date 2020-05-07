"""
Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
"""
D1 = {'e': 30, 1: 20, 'i': 45, 't': 66, 9: 99}
D2 = {1: 20, 5: 55, 'm': 66, 9: 99, 2: 20}
D3 = []
for i in D1.items():
    if i in D2.items():
        D3.append(i)
print('key_value duplicate:', dict(D3))
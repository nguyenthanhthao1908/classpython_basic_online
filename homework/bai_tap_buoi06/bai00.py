"""Bài 00: Viết chương trình tính tích các phần tử trong một dict"""
D = {'t': 19, 'a': 99, 5: 5, 7: 8}
P = 1
for i in D:
    P *= D[i]
print("Result =", P)
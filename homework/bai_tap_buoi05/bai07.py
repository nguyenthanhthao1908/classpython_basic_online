"""Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không."""
T1 = ('Nguyen', 56, 7.34, "thanh", 99, 'y', 'ha', 8)
T2 = ('Thanh', 99, 19, 'y', 'Thao', 56)
T3 = ("tha")

for i in T1:
    for j in T2:
        if i == j:
            print('phan tu chung la:', j)
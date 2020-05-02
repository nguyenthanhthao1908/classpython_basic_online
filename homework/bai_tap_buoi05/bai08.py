"""Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không."""
T1 = ('Nguyen', 'thanh', 7.34, "thanh", 99, 'y', 8, 99)
for i in T1:
    if T1.count(i) >= 2:
        print("duplicate element:",i)

